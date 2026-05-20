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

### Naming

- Use lowercase variable names for local script variables, such as `file_path` and `retry_count`.
- Reserve uppercase variable names for environment variables, constants, and exported configuration.
- Use `local` for function-scoped variables to avoid leaking temporary state into the global scope.
- Name Bash functions after the command action or question they implement, such as `build_archive` or `is_valid_tag`.

### Formatting

- Start Bash scripts with an explicit Bash shebang. Use the project standard when one exists; otherwise prefer `#!/usr/bin/env bash` for user-space portability or `#!/bin/bash` for controlled system environments.
- Do not use Bash-only syntax under `#!/bin/sh`; arrays, `[[ ... ]]`, `local`, and `${BASH_SOURCE[@]}` require a Bash shebang.
- Match the existing Bash style when editing existing scripts, and do not reformat unrelated code.
- For new Bash files without a project style, use readable shell indentation, short lines, and consistent command layout.
- For user-facing Bash scripts, keep usage or help text in one reusable block when that avoids duplicated output for `-h`, `--help`, and invalid options.
- Add a function header comment only when a Bash function's purpose, globals, arguments, output, or return behavior is not obvious from the code.

### Errors

- Check command failures explicitly when continuing after an error is valid.
- Do not rely on strict mode alone; handle expected failures with explicit control flow such as `if ! command; then ... fi`, a documented fallback, or a justified `|| true`.
- Send diagnostics, warnings, and errors to STDERR; reserve STDOUT for normal script output.
- For recurring operational Bash scripts, route diagnostics through a small logging function when that improves consistency or troubleshooting; keep one-off scripts simple.
- For Bash diagnostics or logging, use `printf` or a logging helper instead of bare `echo` when message formatting, timestamps, or STDERR routing matter.
- Preserve command substitution status when it matters by separating `local` declaration from assignment, for example `local value` followed by `value="$(command)"`.
- Fail early with clear error messages when required arguments, files, directories, commands, or environment variables are missing or invalid.

### Safety

- Use Bash only when Bash is the declared target; treat Bash and POSIX shell as distinct languages.
- Respect the target Bash version; avoid Bash 4+ features such as `readarray`, `mapfile`, or associative arrays unless the target runtime supports them.
- Keep Bash scripts limited to small utilities, glue code, wrappers, automation, and command orchestration; recommend a higher-level language when logic, data processing, or long-term maintenance becomes complex.
- For new non-trivial Bash scripts, use `set -euo pipefail` after checking that the script behaves correctly under those modes. When editing existing scripts, preserve existing strict-mode behavior unless the change requires it and representative checks pass.
- Document any omitted or intentionally disabled strict-mode option.
- Quote variable expansions by default, preferably as `"${var}"`, unless word splitting or glob expansion is deliberately required and justified.
- Validate shell-facing inputs before they affect commands, paths, or destructive operations, including parsed options, positional arguments, environment variables, filenames, command output, and data read from standard input.
- When a Bash script needs runtime configuration, read configurable values from parsed options, environment variables, or config files with explicit defaults and validation; do not add configurability that the task or script contract does not require.
- Make rerunnable Bash jobs idempotent when they are intended for cron, CI retries, deployment, or maintenance; avoid adding state tracking only for speculative reuse.
- Use file locking for Bash scripts that must not run concurrently, and release locks through the script cleanup path.
- Use arrays for dynamic command argument lists, then expand them with `"${array[@]}"`; do not store multiple command arguments in a single string.
- Do not generate `eval` unless the user explicitly requests it and every evaluated input is strictly controlled; prefer arrays, case statements, direct invocation, or explicit parsing.
- Never parse `ls` output to process files; use globs, `find`, Bash tests, or null-delimited processing.
- Do not iterate over command output with `for var in $(...)` unless the output is explicitly controlled and whitespace-safe; prefer `while IFS= read -r`, `readarray` when supported by the target Bash version, or null-delimited `find -print0` processing.
- Use `trap` for cleanup when scripts create temporary files, locks, or reversible state changes.
- Create temporary files and directories with `mktemp`; do not use predictable names based on process IDs, timestamps, or hardcoded paths.
- Prefer explicit path prefixes such as `./*` for globs in the current directory, especially before passing filenames to destructive commands.
- Configure glob behavior intentionally when it affects correctness, such as enabling `nullglob` for empty matches or documenting any use of `set -f`.
- Do not generate SUID or SGID shell scripts; recommend `sudo` or a safer privileged wrapper when elevated privileges are required.
- Enable debug tracing only behind an explicit opt-in flag or environment variable; never enable `set -x` unconditionally in production scripts.

### Tests

- Run `bash -n` before accepting generated Bash code.
- Run ShellCheck when available, and fix or explicitly justify every warning that remains.
- Test failure paths as well as successful execution paths when changing Bash behavior.
- Verify scripts that use strict mode, traps, globs, temporary files, or argument forwarding with representative inputs before presenting them as final.

### Idioms

- Use `[[ ... ]]` for Bash conditionals; use `[ ... ]` only when POSIX shell compatibility is required.
- Use `[[ -z "${var:-}" ]]` and `[[ -n "${var:-}" ]]` when the variable may be unset; use `"${var}"` only when the variable is guaranteed to be set.
- Use arithmetic contexts such as `(( count > 0 ))` for numeric comparisons and arithmetic expressions.
- Use `"$@"` when forwarding positional arguments; justify any use of `$*`.
- Prefer `$(...)` over backticks for command substitution.
- Use a `main` function for scripts that contain helper functions or meaningful control flow, and end non-library scripts with `main "$@"`.
- Prefer functions over aliases inside scripts.
- Prefer `printf` over `echo` for predictable output.

### Other

- User-facing Bash scripts that accept options should support `-h` or `--help`, print usage information, and reject unknown options with a clear error.

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

## PowerShell

### Naming

- Use approved PowerShell verbs from `Get-Verb` in `Verb-Noun` names for public commands, functions, and advanced functions.
- Prefer specific singular nouns over generic nouns such as `Item`, `Object`, or `Data` unless the generic noun accurately describes the resource.
- Use PascalCase for public functions, parameters, modules, classes, enums, attributes, public fields, and public properties.
- Use lowercase for PowerShell keywords and operators.
- Use full command names instead of aliases in maintained scripts.
- Use full parameter names instead of positional shorthand in maintained scripts.
- Prefer established parameter names such as `Path`, `LiteralPath`, `Name`, `InputObject`, `Credential`, `Force`, and `PassThru` when they match the command behavior.
- Use `Path` when wildcard expansion is intended and `LiteralPath` when the input must be interpreted exactly.

### Formatting

- Start maintained scripts and advanced functions with `[CmdletBinding()]` unless there is a clear reason not to.
- Structure advanced functions in execution order: `param`, `begin`, `process`, then `end`.
- Use four spaces per indentation level unless the existing project style requires otherwise.
- Keep lines under 115 characters when practical.
- Prefer splatting, arrays, hashtables, and natural continuation over backtick line continuation.
- Do not leave trailing whitespace.
- Do not use semicolons as routine line terminators.
- Keep formatting-only changes separate from functional changes.

### Errors

- Use `-ErrorAction Stop` for cmdlet calls inside `try` blocks when the failure must be caught.
- Set `$ErrorActionPreference = 'Stop'` only within a clear scope and restore the previous value afterward.
- Put the whole transactional operation inside `try` instead of using Boolean flags to infer success.
- Do not use `$?` as structured error handling.
- Capture the current error record immediately at the start of each `catch` block.
- Prefer explicit exceptions, captured error records, and actionable diagnostics over ambiguous status output.

### Safety

- Never hard-code credentials, tokens, passwords, or other secrets in scripts, repositories, logs, or command history.
- Accept credentials through a `[System.Management.Automation.PSCredential]` parameter when a reusable command needs credentials.
- Use `SecureString` only for sensitive values and avoid plaintext conversion except at the final required API boundary.
- Treat execution policies as operational controls, not security boundaries.
- Prefer signed scripts in controlled environments when organizational policy requires controlled script execution.
- Validate external input before using it in commands, paths, filters, or script blocks.
- Prefer paths based on `$PSScriptRoot`, `Join-Path`, or resolved absolute paths over unsafe relative paths.

### Tests

- Validate generated or modified PowerShell with PowerShell-aware tooling when available.
- Run or recommend `PSScriptAnalyzer`, formatting checks, and minimal execution tests when the environment allows it.
- Test pipeline input, validation attributes, error paths, and state-changing commands when they are affected by a change.
- Do not claim a PowerShell rule is functionally required when it is only stylistic or taste-based.

### Idioms

- Use `process {}` when accepting pipeline input.
- Output objects to the pipeline from reusable tools instead of formatted text.
- Do not use `return` as the normal output mechanism for reusable functions.
- Add `[OutputType()]` to reusable public functions when they return objects.
- Do not use `Write-Host` for reusable script output unless the command is intentionally display-only or host-interactive.
- Use `Write-Verbose`, `Write-Debug`, and `Write-Warning` for optional detail, diagnostics, and warnings.
- Keep each public command output stream coherent; do not interleave unrelated strings, status text, and objects.
- Support `-PassThru` for state-changing commands when returning the changed object should be optional.
- Use `SupportsShouldProcess` for public commands that change state when `-WhatIf` or `-Confirm` support is expected.
- Use strongly typed parameters when the accepted value has a clear type.
- Use `[switch]` for optional true/false command flags.
- Prefer parameter validation attributes over manual validation inside the function body.
- Provide comment-based help for public scripts and functions.
- Keep parameter documentation close to the `param` block when practical.
- Put reusable behavior in modules or function libraries instead of duplicating it across controller scripts.

### Other

- Generate the simplest PowerShell implementation that satisfies the request.
- Do not add module structure, logging frameworks, configuration systems, remoting support, or extra abstractions unless required by the user request or project context.
- Treat framework-specific guidance for PowerShell Universal, MSP/RMM tools, enterprise hardening, or hosting platforms as contextual unless the project explicitly uses those environments.
- Preserve the existing project style when editing existing PowerShell code.
- Do not reformat unrelated legacy code while making a functional change.
- Keep comments accurate and useful; update them whenever behavior changes.
- Explain intent, constraints, workarounds, or decisions instead of obvious syntax.
- Measure performance before optimizing PowerShell code.
- Prefer readability unless performance has been proven to matter.
- Stream large inputs instead of loading everything into memory when incremental processing is feasible.
