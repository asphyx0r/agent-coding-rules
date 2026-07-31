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
bash -n .githooks/pre-commit
bash -n .githooks/commit-msg
shellcheck .githooks/pre-commit .githooks/commit-msg
shfmt -d -i 2 .githooks/pre-commit .githooks/commit-msg
actionlint
ruff check tools/agent-rules-sync.py tests/test_agent_rules_sync.py
python -B -m unittest discover -s tests -p 'test_agent_rules_sync.py' -v
betterleaks git --no-banner --redact
```

Enable the versioned local hooks in each checkout that should use them:

```bash
git config core.hooksPath .githooks
```

Git does not activate versioned hooks automatically after cloning. The local
`pre-commit` hook blocks commits with staged Markdown or YAML files unless their
staged content passes `markdownlint-cli2` or `yamllint`. The local `commit-msg`
hook blocks commits unless the message passes `commitlint` with the repository
configuration. These hooks complement CI and do not replace the full validation
checklist.

Validate GitHub Actions changes with:

```bash
actionlint
```

Before commits, also scan staged content:

```bash
betterleaks git --staged --redact --no-banner
```
