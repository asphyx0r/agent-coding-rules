# agent-coding-rules

Practical behavior and code-quality rules for AI coding agents.

## Features

- Provides a reusable instruction stack for AI coding agents, with explicit
  scope and precedence rules.
- Encourages cautious agent behavior: stated assumptions, clarification before
  risky work, surgical changes, and goal-driven verification.
- Defines language-agnostic code-quality guidance for naming, comments,
  formatting, functions, errors, design, architecture, concurrency, testing,
  refactoring, and review.
- Adds language-, dialect-, and framework-specific rules for web, systems,
  scripting, database, container, legacy, and release-description formats.
- Adds GitHub Actions workflow rules for trigger scope, job structure,
  permissions, cache and artifact handling, pinned third-party actions,
  untrusted input, privileged triggers, and runner selection.
- Clarifies that GitHub Actions workflow rules apply only to
  `.github/workflows/*.yml` and `.github/workflows/*.yaml`, in addition to the
  generic YAML rules, with the GitHub Actions-specific rule taking precedence
  when both sections overlap.
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
- `CHANGELOG.md`: Lists tagged release history.
- `TODO.md`: Tracks follow-up work when pending items should remain outside the
  current change scope.
- `commitlint.config.cjs`: Provides a default commitlint configuration for
  Conventional Commits validation.
- `.markdownlint-cli2.yaml`: Configures repository Markdown lint rules.
- `.gitattributes`: Defines repository text-file line-ending normalization.
- `.gitignore`: Excludes OS metadata and editor temporary files.

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
cp .agent-coding-rules/commitlint.config.cjs .
cp .agent-coding-rules/LICENSE.txt .
```

Copying `LICENSE.txt` preserves the MIT license notice for reused files, and
copying `.gitattributes`, `.gitignore`, `.markdownlint-cli2.yaml`, and
`commitlint.config.cjs` preserves the repository's text normalization,
ignored-file patterns, Markdown lint, and commit message lint configuration.

## Usage

- Ask your coding agent to follow `AGENTS.md`.
- Create or update code in your project as usual.
- Review generated changes against the applicable rule files.
- Keep project-specific instructions in your local `AGENTS.md` when needed.

## Tooling

Provide these commands before running validation:

- `commitlint`
- `markdownlint-cli2`
- `yamllint`
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

This repository does not pin validation tool versions in a package manifest.
Local command versions come from the installed environment, or from the
documented toolchain release when that installer is used.

## Validation

Run the local repository validation checklist before commits and tags:

```bash
markdownlint-cli2 "**/*.md"
yamllint .markdownlint-cli2.yaml
node --check commitlint.config.cjs
commitlint --print-config json --config commitlint.config.cjs
betterleaks git --no-banner --redact
```

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

[MIT](LICENSE.txt)
