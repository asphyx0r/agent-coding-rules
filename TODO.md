# TODO

This file tracks follow-up work that should not be folded into the current
local-validation documentation changes.

## CI Validation Follow-Up

Reminder: implement a minimal CI workflow that runs the validations already
documented by this repository.

Recommended correction:

- Create `.github/workflows/ci.yml`.
- Trigger it on `pull_request`, `push` to `main`, and optionally
  `workflow_dispatch`.
- Set `permissions: contents: read`.
- Add a job with a timeout.
- Install the tools through the `coding-agent-toolchain` release.
- Run only the checks already relevant to this repository:
  - `markdownlint-cli2 "**/*.md"`
  - `yamllint .markdownlint-cli2.yaml`
  - `node --check commitlint.config.cjs`
  - `commitlint --print-config json --config commitlint.config.cjs`
  - a secret scan, for example
    `betterleaks git --no-banner --redact` or a CI-compatible equivalent.

Before implementing the workflow, verify that `coding-agent-toolchain` can be
installed non-interactively in GitHub Actions. If it cannot, use explicit,
CI-compatible installers for each tool instead.
