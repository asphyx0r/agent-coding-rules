# Contributing

This repository contains reusable coding-agent rule files and repository
validation configuration. Use this guide when preparing repository changes.

## Change Scope

- Keep each change focused on one rule, documentation, validation, or release concern.
- Follow `AGENTS.md` before editing files and apply the rule files that match the task.
- Avoid unrelated formatting or cleanup.

## Validation

For reproducible local validation, install the tools through the
coding-agent-toolchain release documented in README.md. If local tool
versions differ from CI, treat CI as the final validation source and include
local tool versions when reporting validation failures.

Run the repository validation checklist before requesting review:

```bash
git fsck --full
markdownlint-cli2 "**/*.md"
yamllint .markdownlint-cli2.yaml .github/workflows/ci.yml
node --check commitlint.config.cjs
commitlint --print-config json --config commitlint.config.cjs
actionlint
betterleaks git --no-banner --redact
```

Validate GitHub Actions changes with:

```bash
actionlint
```

Before commits, also scan staged content:

```bash
betterleaks git --staged --redact --no-banner
```
