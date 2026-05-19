# LANGUAGE_RULES.md

## Purpose

This file defines language-specific coding rules for code generated or modified by an AI coding agent.

Use this file together with `AGENTS.md` and `CODING_RULES.md`:
- `AGENTS.md` governs agent behavior.
- `CODING_RULES.md` governs language-agnostic code quality.
- `LANGUAGE_RULES.md` governs restrictions, conventions, and exceptions specific to each target language.

## Scope

Apply only the section that matches the language of the files being created, edited, reviewed, or refactored.

If the target language has no section in this file, apply only `CODING_RULES.md` plus repository conventions; do not invent language-specific rules.

If a repository has stronger local conventions, follow the repository conventions first.

If a language-specific rule conflicts with a general rule from `CODING_RULES.md`, the language-specific rule takes precedence.

Use the operational definitions in `CODING_RULES.md` for qualitative phrases such as `small`, `when practical`, `when possible`, and `when appropriate`.

## Go

### Formatting

- Use `gofmt` formatting.

### Naming

- Use `camelCase` for local variables and unexported identifiers.
- Use `PascalCase` for exported identifiers.
- Keep short names acceptable in small scopes: `i`, `r`, `w`, `ctx`.
- Prefer Go idioms over verbose names.
- Keep package names short, lowercase, and singular.
- Do not use underscores in package names.

### Errors

- Return errors explicitly instead of hiding failures.
- Return `error` values; do not panic for normal failures.
- Wrap errors with useful context when propagating them.
- Do not ignore returned errors unless the reason is explicit and intentional.

### Idioms

- Keep interfaces small and define them near the consumer when practical.

### Tests

- Use table-driven tests when they improve clarity.
- Name tests like `TestFunctionName_Scenario`.

## PHP

### Naming

- Use `$camelCase` for variables.
- Use `camelCase` for methods and functions.
- Use `PascalCase` for classes, interfaces, traits, and enums.
- Use `UPPER_SNAKE_CASE` for constants.

### Formatting

- Follow PSR-12 unless the repository defines another PHP coding standard.
- Enforce PHP formatting with tooling such as PHP_CodeSniffer or PHP-CS-Fixer when available.
- Do not introduce formatting-only changes unless the task explicitly asks for them or the touched PHP code must be formatted to pass project checks.

### Runtime and Types

- Respect the minimum PHP version declared by `composer.json`, CI, runtime configuration, or project documentation.
- If the minimum PHP version is not discoverable and syntax compatibility matters, ask before using version-specific syntax or APIs.
- Declare `strict_types=1` when consistent with the project, and apply it consistently within the touched PHP scope.
- Use typed properties, parameters, and return types when supported by the target PHP version and consistent with the surrounding code.
- Use modern PHP features such as constructor property promotion, enums, `match`, and `readonly` only when they improve clarity and are supported by the project runtime.
- Use strict comparisons with `===` and `!==` unless loose comparison is required by the domain.

### Errors

- Prefer exceptions over ambiguous `false` or `null` error returns when consistent with the project.
- Use SPL or domain-specific exception types when they make error handling clearer than catching generic `Exception`.
- Do not suppress errors with the `@` error-control operator.

### Input, Output, and Security

- Treat request parameters, cookies, sessions, uploaded files, downloaded files, request bodies, and third-party responses as untrusted until validated.
- Validate external input at the boundary before using it in application logic; do not rely on client-side checks or previous workflow steps.
- Escape output for the target context, especially HTML, JavaScript, shell commands, SQL, XML, and similar executable contexts.
- Use the repository's database abstraction with parameter binding for SQL queries; when writing raw PDO, use prepared statements with bound parameters.
- Never concatenate untrusted input into SQL, and still validate writes against business rules.
- Use `password_hash()` and `password_verify()` for password storage; do not design custom password hashing schemes.
- Do not implement custom cryptography for production use; use reviewed libraries or platform APIs.
- Use `filter_var()` with `FILTER_VALIDATE_EMAIL` for ordinary email validation unless the project has a documented and tested alternative.
- Confirm email requirements before relying on `FILTER_VALIDATE_EMAIL` for internationalized domains or nonstandard but valid address forms.
- Do not sanitize HTML with regular expressions; use contextual escaping or a dedicated sanitizer such as HTML Purifier.
- Do not hardcode secrets in PHP source files or committed PHP configuration; load them through the project's secure configuration mechanism.

### Dependencies and Autoloading

- Use Composer for PHP dependency management and autoloading when the project uses Composer.
- Keep namespaces consistent with the project's Composer autoloading configuration.
- Avoid adding new manual `require` or `include` chains for class loading when Composer autoloading is available.
- For applications, preserve or update `composer.lock` when changing Composer dependencies.
- Do not run broad dependency updates unless the task asks for them; prefer the smallest Composer change that satisfies the request.

### Text and Dates

- Use UTF-8 consistently across PHP, the database, and the browser; use `utf8mb4` for MySQL connections and schema configuration.
- Use `mb_*` functions when character boundaries matter in Unicode strings.
- Use `DateTimeImmutable` or `DateTime` for date and time logic that requires comparison, timezone conversion, or mutation.

### Tests and Checks

- When changing PHP behavior, add or update tests in the existing PHP test framework when practical.
- Run the relevant PHP verification command when available, such as `php -l`, PHPUnit, Pest, PHPStan, Psalm, PHP_CodeSniffer, PHP-CS-Fixer, or a project script.

### Idioms

- Namespace project classes unless the surrounding PHP code intentionally uses another convention.
- Avoid adding new global state; use the project's existing class, configuration, or function structure.
- In template-oriented PHP, avoid adding new database queries directly to view templates; use the existing controller, model, repository, or service layer.

## Java

### Naming

- Use `camelCase` for variables, fields, and methods.
- Use `PascalCase` for classes, interfaces, records, and enums.
- Use `UPPER_SNAKE_CASE` for constants.
- Keep package names lowercase.

### Errors

- Keep checked and unchecked exception usage consistent with the project.
- Do not catch broad exceptions unless the handling is intentional and specific.

### Safety

- Prefer immutable fields with `final` when practical.
- Avoid returning `null` for collections; return an empty collection when appropriate.

### Formatting

- Do not use wildcard imports.

## Bash

### Safety

- Use `local` inside functions for function-local variables.
- Quote variable expansions unless word splitting or glob expansion is explicitly intended.
- Use `set -euo pipefail` only when the script behavior has been checked for those modes.
- Check required arguments at the start of the script.

### Idioms

- Use `[[ ... ]]` for conditional expressions in Bash scripts.
- Use `"$@"` when forwarding all arguments.
- Prefer `$(...)` over backticks for command substitution.

### Errors

- Check command failures explicitly when continuing after an error is valid.

### Naming

- Use lowercase variables for local script variables: `file_path`, `retry_count`.
- Reserve uppercase variable names for environment variables, constants and exported configuration.

## Python

### Naming

- Use `snake_case` for variables, functions, and methods.
- Use `PascalCase` for classes.
- Use `UPPER_SNAKE_CASE` for constants.

### Formatting

- Follow PEP 8 unless the repository has a different established convention.

### Errors

- Prefer explicit exceptions over silent failure or ambiguous return values.

### Safety

- Avoid mutable default arguments.
- Use context managers for files, locks, and managed resources.

### Idioms

- Prefer f-strings for string interpolation when supported.
- Add type hints when they improve clarity or match project conventions.

## Perl

### Safety

- Use `strict` and `warnings` unless the file is constrained by legacy compatibility.
- Use `my` for lexical variables.

### Naming

- Use `snake_case` for local variables and subroutines unless the project uses another convention.

### Errors

- Check return values from file, process, and system operations.

### Idioms

- Prefer three-argument `open`.
- Avoid symbolic references unless required by a well-contained metaprogramming pattern.
- Keep regular expressions readable with names, whitespace, or comments when they become complex.
