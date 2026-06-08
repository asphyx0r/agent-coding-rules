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
- Includes C#-specific rules for .NET naming, formatting, exception handling,
  async code, analyzers, LINQ, initialization idioms, and verification.
- Includes Dockerfile and `.dockerignore` rules for image build logic,
  layering, build context, image safety, and publication checks.
- Includes Rust-specific rules for ownership, error handling, unsafe code,
  rustdoc examples, Cargo features, and Cargo-based verification.
- Includes Warez Release NFO File rules for fixed-width `.nfo` artifacts,
  ASCII/CP437 rendering, safe scope, and piracy-risk boundaries.
- Includes Warez Release `FILE_ID.DIZ` rules for BBS-compatible archive
  descriptions, profile-specific width and height limits, disk markers, archive
  placement, and DIZ-specific validation.
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

- [Karpathy-Inspired Claude Code Guidelines](https://github.com/multica-ai/andrej-karpathy-skills)
- Robert C. Martin, "Clean Code: A Handbook of Agile Software Craftsmanship" (978-0132350884)
- Martin Paul Eve, "Warez: The Infrastructure and Aesthetics of Piracy" (978-1-68571-036-1)
- The PPL Development Kit: The PCBoard Programming Language Reference Manual (1993, Clark Development Co., Inc.)
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
