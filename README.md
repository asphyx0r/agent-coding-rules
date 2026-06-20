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
- Adds GitHub Actions workflow rules for trigger scope, job structure,
  permissions, cache and artifact handling, pinned third-party actions,
  untrusted input, privileged triggers, and runner selection.
- Clarifies that GitHub Actions workflow rules apply only to
  `.github/workflows/*.yml` and `.github/workflows/*.yaml`, in addition to the
  generic YAML rules, with the GitHub Actions-specific rule taking precedence
  when both sections overlap.
- Adds command-oriented validation expectations for GitHub Actions workflows,
  SQL, Python, and PowerShell through actionlint, SQLFluff, Ruff, and
  PSScriptAnalyzer when those tools are already available.
- Covers documentation, README, changelog, commit, release, versioning, privacy,
  repository-readiness, and Git tag workflows.
- Hardens commit rules with automated secret scanning that prefers Betterleaks
  and falls back to Gitleaks, plus manual privacy review, Conventional Commits
  defaults, commitlint-aware validation, breaking-change footer handling, and
  commit-message hook guidance.
- Includes review checklists and verification expectations so generated changes
  can be checked before delivery.

## Files

These files form a layered instruction stack, with supporting repository
configuration:

- `AGENTS.md`: Governs the model's behavior and defines when each rule file
  applies.
- `CODING_RULES.md`: Applies universal, language-agnostic code-quality rules.
- `LANGUAGE_RULES.md`: Applies language-, dialect-, and framework-specific
  coding rules.
- `DOCUMENTATION_RULES.md`: Controls documentation quality and consistency,
  including README and changelog rules.
- `COMMIT_RULES.md`: Controls repository readiness, automated secret scanning,
  privacy checks, Conventional Commits formatting, commitlint validation, and
  commit message quality before commits.
- `RELEASE_RULES.md`: Controls SemVer version selection, Git tag creation, and
  release readiness.
- `CHANGELOG.md`: Lists tagged release history.
- `commitlint.config.cjs`: Provides a default commitlint configuration for
  Conventional Commits validation.
- `.markdownlint-cli2.yaml`: Configures repository Markdown lint rules.
- `.gitattributes`: Defines repository text-file line-ending normalization.

## Supported Languages, Frameworks, and Artifact Formats

- Bash
- C
- C++
- C\#
- CSS
- Docker Files
- Go
- GW-BASIC
- HTML
- Java
- Java Properties Files
- JavaScript
- Laravel
- mIRC Scripting Language
- PCBoard Programming Language
- Perl
- PHP
- PowerShell
- Python
- Rust
- SQL
- Microsoft SQL Server Transact-SQL
- MySQL
- Oracle PL/SQL
- Tcl Eggdrop Scripting
- TypeScript
- Warez Release FILE_ID.DIZ
- Warez Release NFO File
- Windows Batch
- YAML
- YAML for GitHub Actions
- YAML for Kubernetes

## Installation

The example below uses POSIX shell commands:

```bash
mkdir -p /home/user/project-name
cd /home/user/project-name
git clone https://github.com/asphyx0r/agent-coding-rules.git .agent-coding-rules
cp .agent-coding-rules/AGENTS.md .
cp .agent-coding-rules/*_RULES.md .
cp .agent-coding-rules/.gitattributes .
cp .agent-coding-rules/.markdownlint-cli2.yaml .
cp .agent-coding-rules/commitlint.config.cjs .
cp .agent-coding-rules/LICENSE.txt .
```

Copying `LICENSE.txt` preserves the MIT license notice for reused files, and
copying `.gitattributes`, `.markdownlint-cli2.yaml`, and
`commitlint.config.cjs` preserves the repository's text normalization,
Markdown lint, and commit message lint configuration.

## Usage

- Ask your coding agent to follow `AGENTS.md`.
- Create or update code in your project as usual.
- Review generated changes against the applicable rule files.
- Keep project-specific instructions in your local `AGENTS.md` when needed.

## Tooling

Provide these commands before running validation:

- `commitlint`
- `markdownlint-cli2`
- `yamllint`
- `gitleaks`
- `betterleaks` when staged secret scans are required and the tool is available

## Validation

Validate the commitlint configuration and a commit message file:

```bash
commitlint --print-config json --config commitlint.config.cjs
commitlint --edit path/to/commit-message --config commitlint.config.cjs
```

Validate GitHub Actions workflows when `actionlint` is available:

```bash
actionlint
```

When `actionlint` is unavailable, validate affected workflow YAML with
`yamllint`, a YAML parser, or an equivalent repository tool, then manually
review workflow syntax, triggers, jobs, expressions, reusable workflow calls,
action inputs, runner labels, and visible secret handling.

Run Markdown lint against all Markdown files:

```bash
markdownlint-cli2 "**/*.md"
```

If `yamllint` is available, validate the Markdown lint configuration:

```bash
yamllint .markdownlint-cli2.yaml
```

The Markdown lint command also parses `.markdownlint-cli2.yaml`; use
`yamllint` for YAML style checks when it is available.

`LANGUAGE_RULES.md` also defines language-specific validation expectations for
GitHub Actions workflows, SQL, Python, and PowerShell. Use the target project's
existing tool configuration and report any fallback validation when those tools
are not available.

## Sources

This list records cited references used while developing the rules; it is not
an exhaustive source map for every supported language or framework.

- [Karpathy agent rules](https://github.com/multica-ai/andrej-karpathy-skills)
- Robert C. Martin, "Clean Code: A Handbook of Agile Software Craftsmanship" (978-0132350884)
- Martin Paul Eve, "Warez: The Infrastructure and Aesthetics of Piracy" (978-1-68571-036-1)
- The PPL Development Kit: The PCBoard Programming Language Reference Manual
  (1993, Clark Development Co., Inc.)
- Microsoft GW-BASIC Interpreter User's Guide and User's Reference (1986)
- [Preslav Rachev, The 10 Go Error Handling Commandments](https://preslav.me/2026/05/19/10-golang-error-handling-commandments)
- [SQLFluff documentation](https://docs.sqlfluff.com/)
- [Ruff documentation](https://docs.astral.sh/ruff/)
- [Microsoft Learn - PSScriptAnalyzer module](https://learn.microsoft.com/powershell/utility-modules/psscriptanalyzer/overview)
- [Semantic Versioning 2.0.0](https://semver.org/)
- [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/)
- [commitlint documentation](https://commitlint.js.org/)
- [commitlint CLI reference](https://commitlint.js.org/reference/cli.html)
- [commitlint rules reference](https://commitlint.js.org/reference/rules.html)
- [commitlint configuration reference](https://commitlint.js.org/reference/configuration.html)
- [commitlint local setup guide](https://commitlint.js.org/guides/local-setup.html)
- [commitlint AI agents guide](https://commitlint.js.org/guides/ai-agents.html)
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
- [GitHub Actions workflows documentation](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflows)
- [GitHub Actions workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)
- [GitHub Actions secure use reference](https://docs.github.com/en/actions/reference/security/secure-use)
- [GitHub Actions GITHUB_TOKEN authentication](https://docs.github.com/en/actions/tutorials/authenticate-with-github_token)
- [GitHub Actions dependency caching](https://docs.github.com/en/actions/concepts/workflows-and-actions/dependency-caching)
- [GitHub Actions workflow artifacts](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts)
- [GitHub Actions using secrets](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets)
- [GitHub Actions OpenID Connect](https://docs.github.com/en/actions/concepts/security/openid-connect)
- [GitHub Actions self-hosted runners](https://docs.github.com/en/actions/concepts/runners/self-hosted-runners)
- [rhysd/actionlint](https://github.com/rhysd/actionlint)
- [FILE_ID.DIZ Frequently Asked Questions](https://www.roysac.com/file_iddesc.html)
- [YAML 1.2.2 Specification](https://yaml.org/spec/1.2.2/)
- [yamllint documentation](https://yamllint.readthedocs.io/en/stable/)
- [PyYAML security guidance](https://yaml.com/projects/pyyaml/)
- [Kubernetes Documentation - Objects In Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/)
- [Kubernetes Documentation - Recommended Labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/)
- [Kubernetes Documentation - Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/)
- [Kubernetes Documentation - Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)
- [Kubernetes Documentation - Configure a Security Context for a Pod or Container](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)
- [Kubernetes Documentation - Resource Management for Pods and Containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
- [Kubernetes Documentation - Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
- [Kubernetes Documentation - kubectl apply](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_apply/)

## License

[MIT](LICENSE.txt)
