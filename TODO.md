# TODO

This file tracks follow-up work that should not be folded into the current
local-validation documentation changes.

## CI Validation Follow-Up

Reminder: implement a minimal CI workflow that runs the validations already
documented by this repository.

Correction recommandée :

- Créer `.github/workflows/ci.yml`.
- Déclencher sur `pull_request`, `push` vers `main`, et éventuellement
  `workflow_dispatch`.
- Mettre `permissions: contents: read`.
- Ajouter un job avec timeout.
- Installer les outils via la release `coding-agent-toolchain`.
- Exécuter seulement les contrôles déjà pertinents pour ce dépôt :
  - `markdownlint-cli2 "**/*.md"`
  - `yamllint .markdownlint-cli2.yaml`
  - `node --check commitlint.config.cjs`
  - `commitlint --print-config json --config commitlint.config.cjs`
  - un scan secret, par exemple
    `betterleaks git --no-banner --redact` ou équivalent adapté CI.

Before implementing the workflow, verify that `coding-agent-toolchain` can be
installed non-interactively in GitHub Actions. If it cannot, use explicit,
CI-compatible installers for each tool instead.
