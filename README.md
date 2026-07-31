# agent-coding-rules

Practical behavior and code-quality rules for AI coding agents.

## Features

- Provides a reusable instruction stack for AI coding agents, with explicit
  scope and precedence rules.
- Acts as the single source of truth for the six rule files and provides the
  synchronization engine used by consumer repositories.
- Encourages cautious agent behavior: stated assumptions, clarification before
  risky work, surgical changes, and goal-driven verification.
- Defines language-agnostic code-quality guidance for naming, comments,
  formatting, functions, errors, design, architecture, concurrency, testing,
  refactoring, and review.
- Adds language-, dialect-, and framework-specific rules for web, systems,
  scripting, database, container, legacy, and release-description formats.
- Adds command-oriented validation expectations for GitHub Actions workflows,
  SQL, Python, and PowerShell through actionlint, SQLFluff, Ruff, and
  PSScriptAnalyzer when those tools are already available.
- Covers documentation, README, changelog, commit, release, versioning, privacy,
  repository-readiness, and Git tag workflows.
- Hardens commit rules with automated secret scanning that prefers Betterleaks
  and falls back to Gitleaks, plus manual privacy review, Conventional Commits
  defaults, commitlint-aware validation, breaking-change footer handling, and
  commit-message hook guidance.
- Includes review checklists and verification expectations so generated changes
  can be checked before delivery.

## Files

These files form a layered instruction stack, with supporting repository
configuration:

- `AGENTS.md`: Governs the model's behavior and defines when each rule file
  applies.
- `CODING_RULES.md`: Applies universal, language-agnostic code-quality rules.
- `LANGUAGE_RULES.md`: Applies language-, dialect-, and framework-specific
  coding rules.
- `DOCUMENTATION_RULES.md`: Controls documentation quality and consistency,
  including README and changelog rules.
- `COMMIT_RULES.md`: Controls repository readiness, automated secret scanning,
  privacy checks, Conventional Commits formatting, commitlint validation, and
  commit message quality before commits.
- `RELEASE_RULES.md`: Controls SemVer version selection, Git tag creation, and
  release readiness.
- `SECURITY.md`: Explains how to report security-relevant concerns without
  exposing sensitive details.
- `SUPPORT.md`: Describes how to ask for help or report non-sensitive questions.
- `CHANGELOG.md`: Lists tagged release history.
- `CONTRIBUTING.md`: Provides scoped contribution and validation guidance.
- `TODO.md`: Tracks follow-up work when pending items should remain outside the
  current change scope.
- `SOURCES.md`: Maps reference groups and cited source links.
- `MIGRATION.md`: Records the maintainer working-copy migration, validation
  evidence, and canonical local repository path.
- `commitlint.config.cjs`: Provides a default commitlint configuration for
  Conventional Commits validation.
- `.githooks/pre-commit`: Blocks commits with staged Markdown or YAML files
  unless their staged content passes `markdownlint-cli2` or `yamllint`.
- `.githooks/commit-msg`: Blocks commits unless the commit message passes the
  resolved `commitlint.config.cjs` Conventional Commits rules.
- `.gitleaks.toml`: Extends the built-in Gitleaks secret scanning rules
  for repository-local scanner configuration.
- `.github/workflows/ci.yml`: Runs the documented validation checklist in CI.
- `tools/agent-rules-sync.py`: Plans, checks, and applies safe rule updates in
  consumer repositories without overwriting customized rule files.
- `tests/test_agent_rules_sync.py`: Covers first adoption, safe updates,
  customization preservation, provenance migration, and rollback behavior.
- `.markdownlint-cli2.yaml`: Configures repository Markdown lint rules.
- `.gitattributes`: Defines repository text-file line-ending normalization.
- `.gitignore`: Excludes OS metadata, editor temporary files, local
  validation caches, and local dependency directories.

## Supported Languages, Frameworks, and Artifact Formats

- Bash
- C
- C++
- C\#
- CSS
- Docker Files
- Go
- GW-BASIC
- HTML
- Java
- Java Properties Files
- JavaScript
- Laravel
- mIRC Scripting Language
- PCBoard Programming Language
- Perl
- PHP
- PowerShell
- Python
- Rust
- SQL
- Microsoft SQL Server Transact-SQL
- MySQL
- Oracle PL/SQL
- Tcl Eggdrop Scripting
- TypeScript
- Warez Release FILE_ID.DIZ
- Warez Release NFO File
- Windows Batch
- YAML
- YAML for GitHub Actions
- YAML for Kubernetes

## Installation

The example below uses POSIX shell commands:

The default installation intentionally follows the default branch of the repository
so it installs the latest rule set.

These commands intentionally overwrite and replace existing files with the same
names. Treat the copied files as default base files to adapt after installation.

```bash
mkdir -p /home/user/project-name
cd /home/user/project-name
git clone https://github.com/asphyx0r/agent-coding-rules.git .agent-coding-rules
cp .agent-coding-rules/AGENTS.md .
cp .agent-coding-rules/*_RULES.md .
cp .agent-coding-rules/.gitattributes .
cp .agent-coding-rules/.gitignore .
cp .agent-coding-rules/.markdownlint-cli2.yaml .
cp .agent-coding-rules/.gitleaks.toml .
cp .agent-coding-rules/commitlint.config.cjs .
```

## Usage

- Ask your coding agent to follow `AGENTS.md`.
- Create or update code in your project as usual.
- Review generated changes against the applicable rule files.
- Keep project-specific instructions in your local `AGENTS.md` when needed.

## Synchronization

This repository is the canonical source for these six files:

- `AGENTS.md`
- `CODING_RULES.md`
- `COMMIT_RULES.md`
- `DOCUMENTATION_RULES.md`
- `LANGUAGE_RULES.md`
- `RELEASE_RULES.md`

Consumer repositories run `tools/agent-rules-sync.py` from an exact SemVer tag
of this repository. The engine supports three operations:

```text
agent-rules-sync.py check --source SOURCE --target TARGET
agent-rules-sync.py plan --source SOURCE --target TARGET
agent-rules-sync.py apply --source SOURCE --target TARGET \
  --backup-directory DIRECTORY
```

The engine updates a file only when its current canonical hash matches the
previous source hash recorded in `_agent-rules-source.json`. A different file
is treated as a repository customization: it is preserved, reported in the
plan, and recorded under `preservedFiles` in provenance schema 3. Missing files
are created, but symlinks and non-file paths are conflicts. Before writing, the
engine creates a ZIP backup outside the target repository and rolls back
completed writes if a later write fails.

Untracked files outside the managed paths do not block synchronization.
Tracked changes outside the six rules and provenance do block it. A consumer
workflow should commit the resulting changes through a reviewed pull request;
the engine does not push branches or merge changes itself.

## Tooling

Provide these commands before running validation:

- `commitlint`
- `markdownlint-cli2`
- `yamllint`
- `node`
- `bash`
- `shfmt`
- `shellcheck`
- `actionlint`
- `sqlfluff`
- `ruff`
- `Invoke-ScriptAnalyzer`
- `gitleaks`
- `betterleaks` when staged secret scans are required and the tool is available

Auto-install all tools via
[coding-agent-toolchain v1.4.1](https://github.com/asphyx0r/coding-agent-toolchain/releases/tag/v1.4.1).

Use that documented toolchain release when you need local validation to
reproduce CI. If locally installed tool versions differ from the CI toolchain,
treat CI as the final validation source and include local tool versions when
reporting failures.

This repository intentionally does not pin validation tool versions in a
package manifest. Local command versions come from the installed environment,
or from the documented toolchain release when that installer is used. CI pins
the toolchain source revision in `.github/workflows/ci.yml` so repository
validation uses a reviewed tool installer instead of local machine state. The
repository-local
`.gitleaks.toml` extends the built-in Gitleaks rules without disabling
default secret detection.

## Validation

Run the local repository validation checklist before commits and tags:

```bash
git fsck --full
markdownlint-cli2 "**/*.md"
yamllint .markdownlint-cli2.yaml .github/workflows/ci.yml
node --check commitlint.config.cjs
commitlint --print-config json --config commitlint.config.cjs
bash -n .githooks/pre-commit
bash -n .githooks/commit-msg
shellcheck .githooks/pre-commit .githooks/commit-msg
shfmt -d -i 2 .githooks/pre-commit .githooks/commit-msg
actionlint
ruff check tools/agent-rules-sync.py tests/test_agent_rules_sync.py
python -B -m unittest discover -s tests -p 'test_agent_rules_sync.py' -v
betterleaks git --no-banner --redact
```

To enable the versioned local hooks for this checkout, run:

```bash
git config core.hooksPath .githooks
```

Git does not activate versioned hooks automatically after cloning. The local
`pre-commit` hook validates staged Markdown and YAML content before commits.
The local `commit-msg` hook validates commit messages with `commitlint` and the
repository `commitlint.config.cjs` configuration. These hooks complement CI and
do not replace the full validation checklist before commits and tags.

This repository scan supports local validation and CI. Before creating a commit,
also scan the staged content required by `COMMIT_RULES.md`:

```bash
betterleaks git --staged --redact --no-banner
```

When Betterleaks is unavailable, use a matching Gitleaks fallback for the
repository or staged-content scan being performed.

Validate commit messages with the resolved commitlint configuration:

```bash
commitlint --edit path/to/commit-message --config commitlint.config.cjs
```

Validate GitHub Actions workflows when `actionlint` is available:

```bash
actionlint
```

When `actionlint` is unavailable, validate affected workflow YAML with
`yamllint`, a YAML parser, or an equivalent repository tool, then manually
review workflow syntax, triggers, jobs, expressions, reusable workflow calls,
action inputs, runner labels, and visible secret handling.

External HTTP link checks are optional network-enabled validation. Run them
only when an audit or maintenance task explicitly authorizes external
validation; local and CI checks do not prove remote URLs are reachable.

`LANGUAGE_RULES.md` also defines language-specific validation expectations for
Bash, GitHub Actions workflows, YAML, SQL, Python, and PowerShell. Use the
target project's existing tool configuration and report any fallback validation
when those tools are not available.

This repository provides a CI workflow for the documented validation checklist.
Local validation remains mandatory before commits and tags.

## Sources

Detailed reference groups and cited source links are maintained in
[SOURCES.md](SOURCES.md).

## License

[MIT](LICENSE)
