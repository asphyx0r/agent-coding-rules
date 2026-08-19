"""Check, plan, and apply canonical agent-rule updates."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import subprocess
import sys
import tempfile
import zipfile
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

VERSION = "2.1.0"
PROVENANCE_PATH = "_agent-rules-source.json"
RULE_PATHS = (
    "AGENTS.md",
    "BRANCH_RULES.md",
    "CODING_RULES.md",
    "COMMIT_RULES.md",
    "DOCUMENTATION_RULES.md",
    "LANGUAGE_RULES.md",
    "RELEASE_RULES.md",
)
MANAGED_PATHS = frozenset((*RULE_PATHS, PROVENANCE_PATH))
SEMVER_TAG = re.compile(
    r"^v(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)"
    r"(?:-((?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*)"
    r"(?:\.(?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*))*))?"
    r"(?:\+([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?$"
)


class SyncError(Exception):
    """Raised when a synchronization safety condition is not met."""


def run_git(root: Path, *arguments: str) -> str:
    result = subprocess.run(
        ("git", "-C", str(root), *arguments),
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip()
        raise SyncError(f"git {' '.join(arguments)} failed: {detail}")
    return result.stdout.strip()


def require_git_root(root: Path, label: str) -> Path:
    resolved = root.resolve()
    if not resolved.is_dir():
        raise SyncError(f"{label} is not a directory: {resolved}")
    git_root = Path(run_git(resolved, "rev-parse", "--show-toplevel")).resolve()
    if git_root != resolved:
        raise SyncError(f"{label} must be the Git repository root: {resolved}")
    return resolved


def canonical_text(raw: bytes, label: str) -> bytes:
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as error:
        raise SyncError(f"{label} must be UTF-8 text.") from error
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    return (normalized.rstrip("\n") + "\n").encode("utf-8")


def canonical_digest(raw: bytes, label: str) -> str:
    return hashlib.sha256(canonical_text(raw, label)).hexdigest()


def canonical_json(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def normalize_repository_url(value: str) -> str:
    repository = value.strip()
    ssh_match = re.fullmatch(r"git@github\.com:(.+?)(?:\.git)?", repository)
    if ssh_match:
        return f"https://github.com/{ssh_match.group(1)}"
    if repository.endswith(".git"):
        return repository[:-4]
    return repository


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    if path.is_symlink() or not path.is_file():
        raise SyncError(f"JSON path must be a regular file: {path}")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise SyncError(f"Invalid JSON file: {path}") from error
    if not isinstance(value, dict):
        raise SyncError(f"JSON root must be an object: {path}")
    return value


def require_regular_file(path: Path, label: str) -> bytes:
    if path.is_symlink() or not path.is_file():
        raise SyncError(f"{label} must be a regular file: {path}")
    return path.read_bytes()


def inspect_source(source: Path) -> tuple[dict[str, Any], dict[str, bytes]]:
    source = require_git_root(source, "source")
    status = run_git(source, "status", "--porcelain", "--", *RULE_PATHS)
    if status:
        raise SyncError("Source rule files must match the checked-out Git commit.")

    source_ref = run_git(source, "describe", "--tags", "--exact-match", "HEAD")
    if not SEMVER_TAG.fullmatch(source_ref):
        raise SyncError("Source HEAD must have an exact SemVer tag prefixed with v.")

    source_commit = run_git(source, "rev-parse", "HEAD")
    repository = normalize_repository_url(
        run_git(source, "remote", "get-url", "origin")
    )
    files: dict[str, bytes] = {}
    digests: dict[str, str] = {}
    for relative_path in RULE_PATHS:
        raw = require_regular_file(
            source / relative_path,
            f"source rule {relative_path}",
        )
        canonical = canonical_text(raw, f"source rule {relative_path}")
        files[relative_path] = canonical
        digests[relative_path] = hashlib.sha256(canonical).hexdigest()

    metadata = {
        "repository": repository,
        "requestedRef": source_ref,
        "ref": source_ref,
        "commit": source_commit,
        "files": list(RULE_PATHS),
        "fileHashes": digests,
    }
    return metadata, files


def previous_file_hashes(provenance: dict[str, Any]) -> dict[str, str]:
    agent_rules = provenance.get("agentRules")
    if not isinstance(agent_rules, dict):
        return {}
    file_hashes = agent_rules.get("fileHashes")
    if not isinstance(file_hashes, dict):
        return {}
    return {
        path: digest
        for path, digest in file_hashes.items()
        if path in RULE_PATHS and isinstance(digest, str)
    }


def previous_preserved_files(
    provenance: dict[str, Any],
) -> dict[str, dict[str, str]]:
    preserved = provenance.get("preservedFiles")
    if not isinstance(preserved, list):
        return {}
    records: dict[str, dict[str, str]] = {}
    for value in preserved:
        if not isinstance(value, dict):
            continue
        path = value.get("path")
        digest = value.get("canonicalSha256")
        if path not in RULE_PATHS or not isinstance(digest, str):
            continue
        records[path] = {
            key: item
            for key, item in value.items()
            if isinstance(key, str) and isinstance(item, str)
        }
    return records


def build_provenance(
    existing: dict[str, Any],
    source_metadata: dict[str, Any],
    preserved_files: list[dict[str, str]],
) -> dict[str, Any]:
    provenance = dict(existing)
    provenance.pop("generatedAt", None)
    provenance["schemaVersion"] = 3
    provenance["agentRules"] = source_metadata
    if preserved_files:
        provenance["preservedFiles"] = sorted(
            preserved_files,
            key=lambda item: item["path"],
        )
    else:
        provenance.pop("preservedFiles", None)
    return provenance


def tracked_changes(target: Path) -> list[str]:
    paths: set[str] = set()
    for arguments in (
        ("diff", "--name-only", "--"),
        ("diff", "--cached", "--name-only", "--"),
    ):
        output = run_git(target, *arguments)
        paths.update(line for line in output.splitlines() if line)
    return sorted(paths)


def build_plan(source: Path, target: Path) -> dict[str, Any]:
    target = require_git_root(target, "target")
    source_metadata, source_files = inspect_source(source)
    provenance_path = target / PROVENANCE_PATH
    existing_provenance = load_json(provenance_path)
    previous_hashes = previous_file_hashes(existing_provenance)
    previous_preserved = previous_preserved_files(existing_provenance)
    tracked_dirty = tracked_changes(target)
    unmanaged_dirty = [path for path in tracked_dirty if path not in MANAGED_PATHS]
    actions: list[dict[str, str]] = []
    preserved_files: list[dict[str, str]] = []

    for relative_path in RULE_PATHS:
        target_path = target / relative_path
        expected = source_metadata["fileHashes"][relative_path]
        if target_path.is_symlink():
            action = "conflict-symlink"
        elif not target_path.exists():
            action = "create"
        elif not target_path.is_file():
            action = "conflict-non-file"
        else:
            current = canonical_digest(
                target_path.read_bytes(),
                f"target rule {relative_path}",
            )
            if current == expected:
                action = "aligned"
            elif previous_hashes.get(relative_path) == current:
                action = "update"
            else:
                previous = previous_preserved.get(relative_path, {})
                action = (
                    "preserved"
                    if previous.get("canonicalSha256") == current
                    else "preserve-customized"
                )
                preserved_files.append(
                    {
                        "path": relative_path,
                        "canonicalSha256": current,
                        "sourceCanonicalSha256": expected,
                        "status": "customized",
                    }
                )
        actions.append({"path": relative_path, "action": action})

    desired_provenance = build_provenance(
        existing_provenance,
        source_metadata,
        preserved_files,
    )
    provenance_action = (
        "aligned"
        if existing_provenance
        and canonical_json(existing_provenance)
        == canonical_json(desired_provenance)
        else ("create" if not provenance_path.exists() else "update")
    )
    actions.append({"path": PROVENANCE_PATH, "action": provenance_action})

    conflicts = [
        item for item in actions if item["action"].startswith("conflict-")
    ]
    writes = [
        item for item in actions if item["action"] in {"create", "update"}
    ]
    preserved = [
        item
        for item in actions
        if item["action"] in {"preserved", "preserve-customized"}
    ]
    return {
        "schemaVersion": 2,
        "source": {
            "repository": source_metadata["repository"],
            "ref": source_metadata["ref"],
            "commit": source_metadata["commit"],
        },
        "target": str(target),
        "targetHead": run_git(target, "rev-parse", "HEAD"),
        "clean": not bool(tracked_dirty),
        "unmanagedDirty": unmanaged_dirty,
        "applicable": not unmanaged_dirty and not conflicts,
        "actions": actions,
        "summary": {
            "aligned": sum(
                item["action"] == "aligned" for item in actions
            ),
            "changed": len(writes),
            "preserved": len(preserved),
            "conflicts": len(conflicts),
        },
        "_sourceFiles": source_files,
        "_desiredProvenance": desired_provenance,
    }


def public_plan(plan: dict[str, Any]) -> dict[str, Any]:
    return {
        key: value for key, value in plan.items() if not key.startswith("_")
    }


def is_within(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
    except ValueError:
        return False
    return True


def create_backup(
    target: Path,
    backup_directory: Path,
    plan: dict[str, Any],
) -> Path:
    resolved_backup = backup_directory.resolve()
    if is_within(resolved_backup, target) or resolved_backup == target:
        raise SyncError("Backup directory must be outside the target repository.")
    resolved_backup.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    source_ref = plan["source"]["ref"].replace("/", "-")
    backup_path = resolved_backup / f"agent-rules-{source_ref}-{timestamp}.zip"
    if backup_path.exists():
        raise SyncError(f"Backup archive already exists: {backup_path}")

    with zipfile.ZipFile(
        backup_path,
        mode="x",
        compression=zipfile.ZIP_DEFLATED,
    ) as archive:
        for relative_path in (*RULE_PATHS, PROVENANCE_PATH):
            path = target / relative_path
            if path.is_file() and not path.is_symlink():
                archive.write(path, arcname=relative_path)
        archive.writestr(
            "_backup.json",
            json.dumps(
                {
                    "schemaVersion": 1,
                    "targetHead": plan["targetHead"],
                    "source": plan["source"],
                },
                indent=2,
            )
            + "\n",
        )
    return backup_path


def atomic_write(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.",
        dir=path.parent,
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(content)
        mode = stat.S_IMODE(path.stat().st_mode) if path.exists() else 0o644
        os.chmod(temporary, mode)
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def apply_plan(
    target: Path,
    backup_directory: Path,
    plan: dict[str, Any],
) -> Path | None:
    if not plan["applicable"]:
        raise SyncError(
            "Plan is not applicable; resolve unmanaged changes and conflicts."
        )
    writable = [
        item
        for item in plan["actions"]
        if item["action"] in {"create", "update"}
    ]
    if not writable:
        return None

    backup_path = create_backup(target, backup_directory, plan)
    originals: dict[str, bytes | None] = {}
    written: list[str] = []
    try:
        for item in writable:
            relative_path = item["path"]
            path = target / relative_path
            originals[relative_path] = path.read_bytes() if path.is_file() else None
            if relative_path == PROVENANCE_PATH:
                content = (
                    json.dumps(
                        plan["_desiredProvenance"],
                        ensure_ascii=False,
                        indent=2,
                    )
                    + "\n"
                ).encode("utf-8")
            else:
                content = plan["_sourceFiles"][relative_path]
            atomic_write(path, content)
            written.append(relative_path)
    except Exception:
        for relative_path in reversed(written):
            path = target / relative_path
            content = originals[relative_path]
            if content is None:
                path.unlink(missing_ok=True)
            else:
                atomic_write(path, content)
        raise
    return backup_path


def print_json(value: dict[str, Any]) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-h", "--help", action="help", help="show help and exit")
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {VERSION}",
        help="show version and exit",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="validate and print the execution plan without writing",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="show additional diagnostics",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    for name, help_text in (
        ("check", "verify that a target matches or records the source rules"),
        ("plan", "inspect a target without writing"),
    ):
        command = subparsers.add_parser(name, help=help_text)
        command.add_argument("--source", type=Path, required=True)
        command.add_argument("--target", type=Path, required=True)
    apply_command = subparsers.add_parser(
        "apply",
        help="apply a safe synchronization plan",
    )
    apply_command.add_argument("--source", type=Path, required=True)
    apply_command.add_argument("--target", type=Path, required=True)
    apply_command.add_argument(
        "--backup-directory",
        type=Path,
        required=True,
    )
    return parser


def main(arguments: list[str] | None = None) -> int:
    parser = build_parser()
    options = parser.parse_args(arguments)
    try:
        plan = build_plan(options.source, options.target)
        if options.verbose:
            print(
                f"Source {plan['source']['ref']} at "
                f"{plan['source']['commit']}",
                file=sys.stderr,
            )
        if options.command == "check":
            print_json(public_plan(plan))
            return 0 if plan["summary"]["changed"] == 0 else 1
        if options.command == "plan" or options.dry_run:
            print_json(public_plan(plan))
            return 0
        backup_path = apply_plan(
            options.target.resolve(),
            options.backup_directory,
            plan,
        )
        result = public_plan(build_plan(options.source, options.target))
        result["backup"] = str(backup_path) if backup_path else None
        print_json(result)
        return 0
    except (OSError, SyncError, zipfile.BadZipFile) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
