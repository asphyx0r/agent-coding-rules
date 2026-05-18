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

### Safety

- Use strict comparisons with `===` and `!==` unless loose comparison is required by the domain.
- Declare strict types when consistent with the project.
- Use typed properties, parameters, and return types when supported by the target PHP version.
- Do not suppress errors with `@`.

### Errors

- Prefer exceptions over ambiguous false/null error returns when consistent with the project.

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
