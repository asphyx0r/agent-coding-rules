# agent-coding-rules

Practical behavior and code-quality rules for AI coding agents.

## Features

- Provides reusable behavioral rules for AI coding agents.
- Defines language-agnostic, language-specific, documentation, commit, and
  release rules.
- Keeps agent instructions separate from human-facing project documentation.

## Files

- `AGENTS.md`: Defines the model behavior rules.
- `CHANGELOG.md`: Lists tagged release history.
- `CODING_RULES.md`: Defines the code-quality rules for code produced by the model.
- `COMMIT_RULES.md`: Defines commit readiness, privacy, and message rules.
- `DOCUMENTATION_RULES.md`: Defines documentation rules, including README and
  changelog rules.
- `LANGUAGE_RULES.md`: Defines language-specific coding rules.
- `RELEASE_RULES.md`: Defines release version and Git tag rules.

## Supported Languages

- Bash
- CSS
- Go
- GW-BASIC
- HTML
- Java
- Java (Properties Files)
- JavaScript
- mIRC Scripting Language
- PCBoard Programming Language
- Perl
- PHP
- PowerShell
- Python
- SQL (Generic)
- SQL (Microsoft SQL Server Transact-SQL)
- SQL (MySQL)
- SQL (Oracle PL/SQL)
- Tcl (Eggdrop Scripting)
- TypeScript
- Windows Batch

## Installation

The example below uses POSIX shell commands:

```bash
mkdir -p /home/user/project-name
cd /home/user/project-name
git clone https://github.com/asphyx0r/agent-coding-rules.git .agent-coding-rules
cp .agent-coding-rules/AGENTS.md .
cp .agent-coding-rules/*_RULES.md .
```

## Usage

- Create or update code in your project as usual.
- Ask your coding agent to follow `AGENTS.md`.
- Review generated changes against the applicable rule files.
- Keep project-specific instructions in your local `AGENTS.md` when needed.

## Sources

- [Karpathy-Inspired Claude Code Guidelines](https://github.com/multica-ai/andrej-karpathy-skills)
- Robert C. Martin, Clean Code: A Handbook of Agile Software Craftsmanship (978-0132350884)
- [Semantic Versioning 2.0.0](https://semver.org/)
- The PPL Development Kit: The PCBoard Programming Language Reference Manual (1993, Clark Development)
- Microsoft GW-BASIC Interpreter User's Guide and User's Reference (1986)

## License

[MIT](LICENSE.txt)
