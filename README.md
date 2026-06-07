# agent-coding-rules

Practical behavior and code-quality rules for AI coding agents.

## Features

- Provides reusable behavioral rules for AI coding agents.
- Defines language-agnostic, language-specific, framework-specific,
  documentation, commit, and release rules.
- Includes C-specific rules for standard selection, C89/C90/C95 through C23
  compatibility, headers, allocation checks, macros, buffers, and verification.
- Includes C++-specific rules for standard selection, RAII, ownership,
  parameter passing, smart pointers, headers, templates, error handling,
  concurrency assumptions, and verification.
- Includes Dockerfile and `.dockerignore` rules for image build logic,
  layering, build context, image safety, and publication checks.
- Includes Rust-specific rules for ownership, error handling, unsafe code,
  rustdoc examples, Cargo features, and Cargo-based verification.
- Keeps agent instructions separate from human-facing project documentation.

## Files

- `AGENTS.md`: Defines the model behavior rules.
- `CHANGELOG.md`: Lists tagged release history.
- `CODING_RULES.md`: Defines the code-quality rules for code produced by the model.
- `COMMIT_RULES.md`: Defines commit readiness, privacy, and message rules.
- `DOCUMENTATION_RULES.md`: Defines documentation rules, including README and
  changelog rules.
- `LANGUAGE_RULES.md`: Defines language- and framework-specific coding rules.
- `RELEASE_RULES.md`: Defines release version and Git tag rules.

## Supported Languages and Frameworks

- Bash
- C
- C++
- CSS
- Docker Files
- Go
- GW-BASIC
- HTML
- Java
- Java (Properties Files)
- JavaScript
- Laravel (PHP Framework)
- mIRC Scripting Language
- PCBoard Programming Language
- Perl
- PHP
- PowerShell
- Python
- Rust
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
- [ISO/IEC JTC1/SC22/WG14 - C](https://www.open-std.org/jtc1/sc22/wg14/)
- [ISO/IEC 9899:1990 - Programming languages - C](https://www.iso.org/standard/17782.html)
- [ISO/IEC 9899:1990/Amd 1:1995 - Programming languages - C - Amendment 1: C Integrity](https://www.iso.org/standard/23909.html)
- [ISO/IEC 9899:1999 - Programming languages - C](https://www.iso.org/standard/29237.html)
- [ISO/IEC 9899:2011 - Information technology - Programming languages - C](https://www.iso.org/standard/57853.html)
- [ISO/IEC 9899:2018 - Information technology - Programming languages - C](https://www.iso.org/standard/74528.html)
- [ISO/IEC 9899:2024 - Information technology - Programming languages - C](https://www.iso.org/standard/82075.html)
- [Standard C++ - The Standard](https://isocpp.org/std/the-standard)
- [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines)
- [cppreference - C++ language reference](https://en.cppreference.com/cpp/language)
- The PPL Development Kit: The PCBoard Programming Language Reference Manual (1993, Clark Development)
- Microsoft GW-BASIC Interpreter User's Guide and User's Reference (1986)
- [Laravel Documentation](https://laravel.com/docs)
- [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/)
- [The Cargo Book](https://doc.rust-lang.org/cargo/)
- [The Rust Reference](https://doc.rust-lang.org/reference/)
- [Docker Documentation](https://docs.docker.com/)

## License

[MIT](LICENSE.txt)
