# Security Policy

This repository contains reusable AI coding-agent rules and validation
configuration. It does not ship a runtime service, but security reports can
still matter when they involve exposed secrets, unsafe automation guidance, or
workflows that could cause unintended repository changes.

## Reporting a Vulnerability

No dedicated private security contact is currently documented for this
repository.

Do not publish real secrets, credentials, private URLs, exploit details, or
sensitive reproduction data in public issues, pull requests, or comments. If the
repository's GitHub security advisory feature or another maintainer-approved
private channel is available, use that private channel first. If no private
channel is available, open a public issue with a high-level, non-sensitive
summary and ask maintainers where to send details.

## What to Include

- A short description of the security concern.
- The affected file, rule section, workflow, or validation command.
- Minimal non-sensitive reproduction steps.
- The expected behavior and the observed behavior.
- Any known risk to users, CI, release, secrets, or agent safety.

## Scope

Security-relevant reports include:

- Leaked credentials, private URLs, tokens, or keys.
- Unsafe CI/CD guidance or workflow configuration.
- Rule text likely to make agents expose secrets, run untrusted code, bypass
  validation, or modify files outside the requested scope.
- Dependency or toolchain guidance likely to pull untrusted code unexpectedly.

General style, wording, documentation, or maintainability issues belong in the
normal contribution workflow unless they create a concrete security risk.

## Supported Versions

Only the current `main` branch and the latest tagged release are considered for
security review unless maintainers state otherwise.
