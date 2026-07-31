import importlib.util
import io
import json
import os
import subprocess
import tempfile
import unittest
import zipfile
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest import mock


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1] / "tools" / "agent-rules-sync.py"
)
SPEC = importlib.util.spec_from_file_location("agent_rules_sync", SCRIPT_PATH)
SYNC = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(SYNC)


class AgentRulesSyncTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.source = self.root / "source"
        self.target = self.root / "target"
        self.backups = self.root / "backups"
        self.backup_index = 0
        self.init_repository(self.source)
        self.init_repository(self.target)
        for index, relative_path in enumerate(SYNC.RULE_PATHS):
            (self.source / relative_path).write_text(
                f"# Rule {index}\n\nCanonical content.\n",
                encoding="utf-8",
            )
        self.commit_all(self.source, "add source rules")
        self.run_git(self.source, "tag", "v1.2.3")

    def tearDown(self):
        self.temporary.cleanup()

    def run_git(self, root, *arguments):
        return subprocess.run(
            ("git", "-C", str(root), *arguments),
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()

    def init_repository(self, root):
        root.mkdir()
        self.run_git(root, "init")
        self.run_git(root, "config", "user.name", "Test User")
        self.run_git(root, "config", "user.email", "test@example.invalid")
        self.run_git(
            root,
            "remote",
            "add",
            "origin",
            "git@github.com:test/rules.git",
        )
        (root / ".gitkeep").write_text("", encoding="utf-8")
        self.commit_all(root, "initialize repository")

    def commit_all(self, root, message):
        self.run_git(root, "add", ".")
        self.run_git(root, "commit", "-m", message)

    def apply(self):
        self.backup_index += 1
        plan = SYNC.build_plan(self.source, self.target)
        backup_directory = self.backups / str(self.backup_index)
        return SYNC.apply_plan(self.target, backup_directory, plan)

    def actions(self, plan):
        return {item["path"]: item["action"] for item in plan["actions"]}

    def update_source(self, paths=None, tag="v1.2.4"):
        selected = paths or SYNC.RULE_PATHS
        for relative_path in selected:
            path = self.source / relative_path
            path.write_text(
                path.read_text(encoding="utf-8") + "Updated upstream.\n",
                encoding="utf-8",
            )
        self.commit_all(self.source, "update source rules")
        self.run_git(self.source, "tag", tag)

    def read_provenance(self):
        return json.loads(
            (self.target / SYNC.PROVENANCE_PATH).read_text(encoding="utf-8")
        )

    def test_first_adoption_preserves_existing_custom_rule(self):
        custom = self.target / SYNC.RULE_PATHS[0]
        custom.write_text("# Local policy\n", encoding="utf-8")
        self.commit_all(self.target, "add local policy")

        plan = SYNC.build_plan(self.source, self.target)

        actions = self.actions(plan)
        self.assertEqual(actions[SYNC.RULE_PATHS[0]], "preserve-customized")
        for relative_path in SYNC.RULE_PATHS[1:]:
            self.assertEqual(actions[relative_path], "create")
        self.assertEqual(plan["summary"]["preserved"], 1)

        backup = self.apply()

        self.assertIsNotNone(backup)
        self.assertEqual(custom.read_text(encoding="utf-8"), "# Local policy\n")
        provenance = self.read_provenance()
        self.assertEqual(provenance["schemaVersion"], 3)
        self.assertEqual(
            [item["path"] for item in provenance["preservedFiles"]],
            [SYNC.RULE_PATHS[0]],
        )
        settled = SYNC.build_plan(self.source, self.target)
        self.assertEqual(settled["summary"]["changed"], 0)
        self.assertEqual(
            self.actions(settled)[SYNC.RULE_PATHS[0]],
            "preserved",
        )

    def test_known_upstream_files_update_safely(self):
        self.apply()
        self.commit_all(self.target, "adopt source rules")
        self.update_source(paths=(SYNC.RULE_PATHS[0],))

        plan = SYNC.build_plan(self.source, self.target)

        self.assertEqual(self.actions(plan)[SYNC.RULE_PATHS[0]], "update")
        self.apply()
        self.assertEqual(
            SYNC.canonical_digest(
                (self.target / SYNC.RULE_PATHS[0]).read_bytes(),
                "target",
            ),
            SYNC.canonical_digest(
                (self.source / SYNC.RULE_PATHS[0]).read_bytes(),
                "source",
            ),
        )
        self.assertNotIn("preservedFiles", self.read_provenance())

    def test_partial_sync_updates_safe_files_and_preserves_custom_file(self):
        self.apply()
        self.commit_all(self.target, "adopt source rules")
        custom_path = self.target / SYNC.RULE_PATHS[0]
        custom_path.write_text("# Repository-specific policy\n", encoding="utf-8")
        self.commit_all(self.target, "customize local policy")
        self.update_source()

        plan = SYNC.build_plan(self.source, self.target)

        actions = self.actions(plan)
        self.assertEqual(actions[SYNC.RULE_PATHS[0]], "preserve-customized")
        for relative_path in SYNC.RULE_PATHS[1:]:
            self.assertEqual(actions[relative_path], "update")

        self.apply()

        self.assertEqual(
            custom_path.read_text(encoding="utf-8"),
            "# Repository-specific policy\n",
        )
        for relative_path in SYNC.RULE_PATHS[1:]:
            self.assertEqual(
                SYNC.canonical_digest(
                    (self.target / relative_path).read_bytes(),
                    relative_path,
                ),
                SYNC.canonical_digest(
                    (self.source / relative_path).read_bytes(),
                    relative_path,
                ),
            )

    def test_changed_custom_file_refreshes_provenance_only(self):
        custom_path = self.target / SYNC.RULE_PATHS[0]
        custom_path.write_text("# Local policy\n", encoding="utf-8")
        self.commit_all(self.target, "add local policy")
        self.apply()
        self.commit_all(self.target, "record local policy")
        custom_path.write_text("# Revised local policy\n", encoding="utf-8")
        self.commit_all(self.target, "revise local policy")

        plan = SYNC.build_plan(self.source, self.target)

        actions = self.actions(plan)
        self.assertEqual(actions[SYNC.RULE_PATHS[0]], "preserve-customized")
        self.assertEqual(actions[SYNC.PROVENANCE_PATH], "update")
        self.assertEqual(plan["summary"]["changed"], 1)
        self.apply()
        self.assertEqual(
            self.actions(SYNC.build_plan(self.source, self.target))[
                SYNC.RULE_PATHS[0]
            ],
            "preserved",
        )

    def test_custom_file_matching_source_removes_preservation_record(self):
        custom_path = self.target / SYNC.RULE_PATHS[0]
        custom_path.write_text("# Local policy\n", encoding="utf-8")
        self.commit_all(self.target, "add local policy")
        self.apply()
        self.commit_all(self.target, "record local policy")
        custom_path.write_bytes((self.source / SYNC.RULE_PATHS[0]).read_bytes())
        self.commit_all(self.target, "restore canonical policy")

        plan = SYNC.build_plan(self.source, self.target)

        self.assertEqual(self.actions(plan)[SYNC.RULE_PATHS[0]], "aligned")
        self.assertEqual(self.actions(plan)[SYNC.PROVENANCE_PATH], "update")
        self.apply()
        self.assertNotIn("preservedFiles", self.read_provenance())

    def test_schema_two_provenance_upgrades_without_rule_changes(self):
        source_metadata, source_files = SYNC.inspect_source(self.source)
        for relative_path, content in source_files.items():
            (self.target / relative_path).write_bytes(content)
        provenance = {
            "schemaVersion": 2,
            "repository": {"name": "target"},
            "starterKit": {"ref": "v2.2.1", "commit": "a" * 40},
            "agentRules": source_metadata,
        }
        (self.target / SYNC.PROVENANCE_PATH).write_text(
            json.dumps(provenance),
            encoding="utf-8",
        )
        self.commit_all(self.target, "add schema two provenance")

        plan = SYNC.build_plan(self.source, self.target)

        self.assertEqual(plan["summary"]["changed"], 1)
        self.apply()
        updated = self.read_provenance()
        self.assertEqual(updated["schemaVersion"], 3)
        self.assertEqual(updated["repository"], provenance["repository"])
        self.assertEqual(updated["starterKit"], provenance["starterKit"])

    def test_symlink_is_reported_as_conflict(self):
        target_path = self.target / SYNC.RULE_PATHS[0]
        try:
            os.symlink(self.target / ".gitkeep", target_path)
        except OSError as error:
            self.skipTest(f"symlink creation is unavailable: {error}")

        plan = SYNC.build_plan(self.source, self.target)

        self.assertEqual(
            self.actions(plan)[SYNC.RULE_PATHS[0]],
            "conflict-symlink",
        )
        self.assertFalse(plan["applicable"])

    def test_apply_rolls_back_when_an_atomic_write_fails(self):
        plan = SYNC.build_plan(self.source, self.target)
        original_atomic_write = SYNC.atomic_write
        failed = False

        def fail_on_provenance(path, content):
            nonlocal failed
            if path.name == SYNC.PROVENANCE_PATH and not failed:
                failed = True
                raise OSError("injected failure")
            original_atomic_write(path, content)

        with mock.patch.object(SYNC, "atomic_write", fail_on_provenance):
            with self.assertRaisesRegex(OSError, "injected failure"):
                SYNC.apply_plan(self.target, self.backups, plan)

        for relative_path in SYNC.RULE_PATHS:
            self.assertFalse((self.target / relative_path).exists())
        self.assertFalse((self.target / SYNC.PROVENANCE_PATH).exists())

    def test_unrelated_untracked_file_does_not_block_apply(self):
        unrelated = self.target / "local-notes.txt"
        unrelated.write_text("keep\n", encoding="utf-8")

        plan = SYNC.build_plan(self.source, self.target)

        self.assertTrue(plan["applicable"])
        self.apply()
        self.assertEqual(unrelated.read_text(encoding="utf-8"), "keep\n")

    def test_unrelated_tracked_change_blocks_apply(self):
        unrelated = self.target / "README.md"
        unrelated.write_text("base\n", encoding="utf-8")
        self.commit_all(self.target, "add readme")
        unrelated.write_text("dirty\n", encoding="utf-8")

        plan = SYNC.build_plan(self.source, self.target)

        self.assertEqual(plan["unmanagedDirty"], ["README.md"])
        self.assertFalse(plan["applicable"])
        with self.assertRaisesRegex(SYNC.SyncError, "not applicable"):
            SYNC.apply_plan(self.target, self.backups, plan)

    def test_line_endings_and_final_newline_are_ignored(self):
        for relative_path in SYNC.RULE_PATHS:
            source_text = (self.source / relative_path).read_text(encoding="utf-8")
            target_text = source_text.rstrip("\n").replace("\n", "\r\n")
            (self.target / relative_path).write_bytes(target_text.encode("utf-8"))
        source_metadata, _ = SYNC.inspect_source(self.source)
        provenance = SYNC.build_provenance({}, source_metadata, [])
        (self.target / SYNC.PROVENANCE_PATH).write_text(
            json.dumps(provenance),
            encoding="utf-8",
        )
        self.commit_all(self.target, "add normalized rules")

        plan = SYNC.build_plan(self.source, self.target)

        self.assertEqual(plan["summary"]["changed"], 0)

    def test_backup_contains_previous_files_and_metadata(self):
        custom = self.target / SYNC.RULE_PATHS[0]
        custom.write_text("custom\n", encoding="utf-8")
        self.commit_all(self.target, "add custom policy")

        backup = self.apply()

        self.assertIsNotNone(backup)
        with zipfile.ZipFile(backup) as archive:
            self.assertIn(SYNC.RULE_PATHS[0], archive.namelist())
            self.assertIn("_backup.json", archive.namelist())

    def test_source_rule_modification_is_rejected(self):
        (self.source / SYNC.RULE_PATHS[0]).write_text(
            "modified\n",
            encoding="utf-8",
        )

        with self.assertRaisesRegex(SYNC.SyncError, "must match"):
            SYNC.build_plan(self.source, self.target)

    def test_source_without_exact_semver_tag_is_rejected(self):
        self.run_git(self.source, "tag", "-d", "v1.2.3")

        with self.assertRaises(SYNC.SyncError):
            SYNC.build_plan(self.source, self.target)

    def test_dry_run_does_not_write_or_create_backup(self):
        stdout = io.StringIO()
        stderr = io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            exit_code = SYNC.main(
                [
                    "--dry-run",
                    "apply",
                    "--source",
                    str(self.source),
                    "--target",
                    str(self.target),
                    "--backup-directory",
                    str(self.backups),
                ]
            )

        self.assertEqual(exit_code, 0, stderr.getvalue())
        self.assertFalse((self.target / SYNC.PROVENANCE_PATH).exists())
        self.assertFalse(self.backups.exists())
        self.assertGreater(json.loads(stdout.getvalue())["summary"]["changed"], 0)

    def test_check_returns_one_for_drift_and_zero_after_apply(self):
        with redirect_stdout(io.StringIO()):
            self.assertEqual(
                SYNC.main(
                    [
                        "check",
                        "--source",
                        str(self.source),
                        "--target",
                        str(self.target),
                    ]
                ),
                1,
            )
        self.apply()
        self.commit_all(self.target, "synchronize rules")

        with redirect_stdout(io.StringIO()):
            self.assertEqual(
                SYNC.main(
                    [
                        "check",
                        "--source",
                        str(self.source),
                        "--target",
                        str(self.target),
                    ]
                ),
                0,
            )


if __name__ == "__main__":
    unittest.main()
