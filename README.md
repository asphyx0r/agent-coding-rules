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
- Covers documentation, README, changelog, commit, release, versioning, privacy,
  repository-readiness, and Git tag workflows.
- Includes review checklists and verification expectations so generated changes
  can be checked before delivery.

## Files

These files form a layered instruction stack:

- `AGENTS.md`: Governs the model's behavior and defines when each rule file
  applies.
- `CODING_RULES.md`: Applies universal, language-agnostic code-quality rules.
- `LANGUAGE_RULES.md`: Applies language-, dialect-, and framework-specific
  coding rules.
- `DOCUMENTATION_RULES.md`: Controls documentation quality and consistency,
  including README and changelog rules.
- `COMMIT_RULES.md`: Controls repository readiness, privacy checks, and commit
  message quality before commits.
- `RELEASE_RULES.md`: Controls SemVer version selection, Git tag creation, and
  release readiness.
- `CHANGELOG.md`: Lists tagged release history.

## Supported Languages and Frameworks

- Bash
- C
- C++
- C#
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
- Warez Release FILE_ID.DIZ
- Warez Release NFO File
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

- [Karpathy agent rules](https://github.com/multica-ai/andrej-karpathy-skills)
- Robert C. Martin, "Clean Code: A Handbook of Agile Software Craftsmanship" (978-0132350884)
- Martin Paul Eve, "Warez: The Infrastructure and Aesthetics of Piracy" (978-1-68571-036-1)
- The PPL Development Kit: The PCBoard Programming Language Reference Manual
  (1993, Clark Development Co., Inc.)
- Microsoft GW-BASIC Interpreter User's Guide and User's Reference (1986)
- [Preslav Rachev, The 10 Go Error Handling Commandments](https://preslav.me/2026/05/19/10-golang-error-handling-commandments)
- [Semantic Versioning 2.0.0](https://semver.org/)
- [RFC 2119 - Key words for use in RFCs to Indicate Requirement Levels](https://www.rfc-editor.org/rfc/rfc2119)
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
- [Microsoft Learn - Common C# code conventions](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions)
- [Microsoft Learn - Names of Classes, Structs, and Interfaces](https://learn.microsoft.com/en-us/dotnet/standard/design-guidelines/names-of-classes-structs-and-interfaces)
- [Microsoft Learn - Asynchronous programming scenarios](https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/async-scenarios)
- [Microsoft Learn - Built-in types and literals](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/built-in-types)
- [Laravel Documentation](https://laravel.com/docs)
- [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/)
- [The Cargo Book](https://doc.rust-lang.org/cargo/)
- [The Rust Reference](https://doc.rust-lang.org/reference/)
- [The Rust Programming Language](https://doc.rust-lang.org/stable/book/)
- [Rust By Example](https://doc.rust-lang.org/rust-by-example/)
- [Rust Compiler Development Guide](https://rustc-dev-guide.rust-lang.org/)
- [Microsoft Pragmatic Rust Guidelines](https://microsoft.github.io/rust-guidelines/guidelines/index.html)
- [Apollo Rust Best Practices](https://github.com/apollographql/rust-best-practices)
- [Good Practices for Writing Rust Libraries](https://pascalhertleif.de/artikel/good-practices-for-writing-rust-libraries/)
- [Docker Documentation](https://docs.docker.com/)
- [Google TypeScript Style Guide](https://google.github.io/styleguide/tsguide.html)
- [FILE_ID.DIZ Frequently Asked Questions](https://www.roysac.com/file_iddesc.html)

## License

[MIT](LICENSE.txt)
