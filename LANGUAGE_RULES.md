# LANGUAGE_RULES.md

## Purpose

This file defines language-specific coding rules for code generated or modified by an AI coding agent.

Use this file together with `AGENTS.md` and `CODING_RULES.md`:
- `AGENTS.md` governs agent behavior.
- `CODING_RULES.md` governs language-agnostic code quality.
- `LANGUAGE_RULES.md` governs restrictions, conventions, and exceptions specific to each target language.

## Scope

Apply only the section or sections that match the language of the files being
created, edited, reviewed, or refactored.

When a language or dialect section explicitly says it applies in addition to a
more general section, apply both sections. If those sections overlap, prefer
the more specific language or dialect rule.

If the target language has no section in this file, apply only `CODING_RULES.md` plus repository conventions; do not invent language-specific rules.

If a repository has stronger local conventions, follow the repository conventions first.

If a language-specific rule conflicts with a general rule from `CODING_RULES.md`, the language-specific rule takes precedence.

Use the operational definitions in `CODING_RULES.md` for qualitative phrases such as `small`, `when practical`, `when possible`, and `when appropriate`.

## HTML

### Naming

- Use semantic `class` and `id` names that describe the content, role, or domain concept instead of visual appearance alone.
- Prefer kebab-case for multi-word `class` and `id` values unless the repository already defines a stricter naming convention.
- Give links, buttons, form controls, headings, and page titles meaningful text that remains understandable outside its visual context.

### Formatting

- Start every standalone HTML document with `<!doctype html>` to trigger standards or no-quirks rendering mode.
- Do not use legacy HTML doctypes or XML declarations for normal HTML documents.
- Add a valid `lang` attribute to the root `<html>` element, using the shortest accurate language value for the page content.
- Include a meaningful `<title>` element in every standalone HTML document; the title must describe the page purpose, not only the project or application name.
- Keep metadata, page title, linked resources, and document-level configuration inside `<head>`, and keep visible content inside `<body>`.
- Use lowercase for doctype declarations, element names, attribute names, and case-insensitive attribute values.
- Quote attribute values consistently, and never omit quotes when the value contains spaces or could be parsed as multiple attributes.
- For boolean attributes, write only the attribute name when the value is true.
- Escape reserved characters such as `&`, `<`, `>`, `"`, and `'` when they would otherwise be parsed as markup or attribute syntax.
- Keep attribute lists readable and consistent; avoid arbitrary spacing, mixed quotation styles, and mixed casing within the same document or project.
- Structure text with headings, paragraphs, lists, and other content elements instead of using line breaks or visual styling to simulate document structure.
- Use heading levels to represent the document outline, not merely to control visual size.

### Errors

- Treat missing required document structure, such as `<!doctype html>`, `<html lang>`, `<head>`, `<title>`, or `<body>` in standalone documents, as a defect to fix before finalizing generated HTML.
- Treat unlabeled interactive controls, missing form instructions, unclear error messages, and inaccessible validation feedback as defects.
- When automatically detected input errors can occur, identify the invalid input and describe the error in text.
- Treat malformed attribute syntax, unescaped reserved characters, invalid nesting, and duplicate IDs as defects to fix before presenting HTML as final.

### Safety

- Prefer native HTML semantics over redundant ARIA; do not add roles that duplicate implicit semantics unless there is a specific compatibility reason.
- Use native interactive elements such as `<button>`, `<a>`, `<input>`, `<select>`, and `<textarea>` instead of custom clickable `<div>` or `<span>` elements whenever they match the required behavior.
- Ensure interactive functionality is keyboard-operable unless the function inherently depends on pointer movement.
- Add useful `alt` text to informative images, and use empty `alt` text only for decorative images that should be ignored by assistive technologies.
- For data tables, use `<th>` for headers and add `scope` when it is needed to associate headers with rows or columns.
- Add `<caption>` to data tables when a concise summary helps users understand the table.
- Provide labels or instructions for form controls that require user input.
- Use HTML attributes that expose input purpose when collecting user information and when the expected meaning can be programmatically determined.
- Do not use color as the only way to convey information, indicate an action, request a response, or distinguish an element.
- Warn users when a link opens a new window, opens a new tab, or points to a non-HTML resource, using visible text or an accessible equivalent.
- Provide a skip link near the start of `<body>` when pages contain repeated navigation before the main content.
- Do not convert accessible native HTML into custom markup unless the user explicitly requests a custom component and the accessibility behavior is reimplemented.

### Tests

- Before finalizing generated HTML, verify that every element has a clear structural or semantic purpose.
- Before finalizing generated HTML, verify that generated interactive controls are keyboard-accessible, labeled, and understandable without visual context.
- Validate standalone HTML for document structure, malformed markup, duplicate IDs, invalid nesting, and unescaped reserved characters when a validator or equivalent project check is available.
- Review images, tables, forms, headings, links, buttons, source order, and repeated navigation for accessibility regressions.
- When modifying existing HTML, verify that the change preserves the project's established formatting and naming conventions unless they conflict with accessibility, validity, or explicit user requirements.

### Idioms

- Use the correct HTML element for the intended meaning before considering generic `<div>` or `<span>` markup.
- Use semantic layout elements such as `<header>`, `<nav>`, `<main>`, `<article>`, `<aside>`, and `<footer>` when their meaning matches the content.
- Preserve a logical source order; do not rely on CSS layout to compensate for an HTML order that becomes confusing when read by assistive technologies.
- Generate the simplest valid HTML that satisfies the requested structure.
- Do not add speculative components, styling hooks, ARIA roles, scripts, or metadata that the user did not request.

### Other

- Avoid using `data-*` attributes when a standard semantic element or attribute already represents the same information.
- Use `data-*` only for application-specific metadata that has no suitable native HTML representation.
- Avoid `<base>` unless the project explicitly requires it; prefer explicit, stable paths for links and resources to reduce maintenance surprises.
- Add resource `type` metadata when it clarifies non-obvious linked resources, such as alternate feeds or downloadable documents.
- In HTML templating environments, separate HTML, CSS, and JavaScript into maintainable units when the platform supports includes or equivalent composition.
- Treat HTML templating organization as a project organization concern, not as a universal HTML syntax requirement.

## CSS

### Naming

- Use the project's existing CSS naming convention before introducing a new one.
- If no project convention exists, use lowercase kebab-case for class names, custom properties, animation names, and other custom identifiers.
- Use semantic class names that describe the component, role, state, or domain concept instead of visual appearance alone.
- Avoid styling against generated, random, or framework-internal class names; use stable project-owned classes, attributes, or framework-supported hooks when a selector must outlive a render cycle.
- Use CSS custom properties for repeated declaration values such as colors, spacing, font sizes, shadows, durations, z-indexes, and component-local measurements when reuse, theming, or safer maintenance is needed. Do not use `var()` in media or container query conditions unless the project's build tooling explicitly supports that pattern.

### Formatting

- Match the existing project formatting, ordering, import structure, and organization before applying any generic CSS convention.
- Use the project-configured formatter or linter when one exists, and do not introduce new CSS tooling unless the task explicitly allows tooling changes.
- Organize styles into clear logical sections such as base styles, typography, layout, components, utilities, and overrides when the file size or project style justifies it.
- Add section comments only when they help navigation; do not comment obvious declarations.
- Keep related declarations together inside a rule, such as layout, box model, typography, color, and effects.
- Put custom properties near the top of a declaration block when they are local to that rule.
- Use shorthand properties only when every constituent value is intentional and the shorthand improves readability.
- Do not mix shorthand and longhand properties for the same concern when that creates hidden overrides.
- Preserve a predictable CSS import order when cascade order affects behavior; do not auto-sort CSS imports blindly.
- Keep CSS code blocks syntactically valid and parseable; do not place pseudo-syntax, informal grammar, or invalid placeholders inside `css` fenced blocks.

### Errors

- Treat invalid CSS syntax, malformed selectors, unmatched braces, empty declaration blocks, and non-functional declarations as defects to fix before finalizing CSS.
- Treat accidental duplicate declarations, repeated selectors, contradictory rules, and dead CSS as defects when they are introduced or exposed by the current change.
- Do not use `!important` to escape ordinary specificity or cascade problems; first refactor selector specificity, cascade order, or component structure.
- Use `!important` only when there is a documented and unavoidable reason, such as overriding a third-party rule that cannot be changed.
- Do not use arbitrary hard-coded values only because they visually work; replace them with named tokens, relative units, or layout mechanisms when practical.
- Add a short comment for unusual values when the reason cannot be expressed through naming, tokens, or structure.

### Safety

- Prefer class selectors for styling because they are reusable and keep specificity manageable.
- Avoid ID selectors for styling unless a specific, documented constraint requires them.
- Keep selectors as simple as possible while still targeting the intended elements.
- Avoid deeply nested, overly broad, or unnecessarily qualified selectors when a clear class selector is sufficient.
- Use standard modern CSS only when it is supported by the project's declared browser baseline.
- Avoid deprecated, obsolete, non-standard, or unnecessary vendor-prefixed features unless a compatibility fallback is explicitly required.
- Do not place reusable styling in HTML `style` attributes; use CSS files, scoped CSS, components, or existing utility classes instead.
- Use inline styles only for dynamic runtime values that cannot be represented cleanly elsewhere, and make that exception explicit.
- Do not introduce Sass, Less, BEM, SMACSS, utility-first CSS, CSS Modules, or another methodology unless the project already uses it or the user explicitly requests it.
- When a framework supports scoped component styles, use scoped styles for component-specific CSS and reserve global CSS for true global concerns.

### Tests

- Before finalizing CSS, verify that generated or modified styles follow the existing project convention.
- Verify that selectors are no more specific than necessary and that no unnecessary `!important` declaration was added.
- Verify that no dead, duplicated, empty, or contradictory CSS remains in the touched scope.
- Verify that CSS import order has not been changed in a way that unintentionally affects cascade behavior.
- Verify responsive behavior for the affected layout ranges when CSS changes media queries, container queries, layout, sizing, or visibility.
- Run the project's CSS formatter, linter, build, visual regression checks, or browser checks when they are available and relevant to the change.
- When framework-specific CSS rules are applied, verify that the target framework or styling system is actually in use.

### Idioms

- Use the simplest CSS layout model that fits the requirement.
- Prefer Flexbox and CSS Grid for modern layout instead of float-based or table-based layout hacks.
- Write responsive CSS intentionally, using the project's established approach such as mobile-first styling when applicable.
- Keep media queries and container queries scoped to real layout changes instead of arbitrary visual patching.
- Plan broad or complex CSS before writing it by identifying base styles, layout styles, component styles, overrides, and reusable patterns.
- Avoid CSS that repeatedly overrides or cancels earlier declarations.
- If the project uses Tailwind or another utility-first system, prefer existing utilities before writing ad-hoc CSS.
- Do not mix utility-first styling and custom CSS in a way that duplicates the same styling responsibility.

### Other

- Prefer project-specific CSS standards first.
- If the project has no CSS convention, apply the smallest consistent rule set needed to keep stylesheets readable, testable, and maintainable.
- Prefer official, maintained, and directly applicable CSS documentation over generic blog posts, forums, social media discussions, or video content.
- Apply framework-specific CSS guidance only when the project context confirms that the framework is in use.
- When modifying existing CSS, change only the rules required by the requested behavior and avoid unrelated selector, naming, or file-organization refactors.

## SQL

### Naming

- Use descriptive and stable names for tables, columns, CTEs, views, and aliases.
- Prefer identifiers that describe the business meaning of the data rather than implementation details.
- Avoid vague names, unexplained abbreviations, Hungarian prefixes such as `tbl_`, and identifiers that collide with reserved SQL keywords.
- When a query references multiple tables, assign meaningful aliases and qualify selected columns with those aliases.
- Do not rely on unqualified column names in joins, because they can become ambiguous or break when schemas evolve.

### Formatting

- Write SQL so that another engineer can understand the intent without reconstructing hidden assumptions.
- Prefer explicit, readable SQL over clever or overly compact SQL.
- Use one formatting convention consistently across the repository.
- If no repository convention exists, use uppercase SQL keywords, lowercase `snake_case` identifiers, consistent indentation, and one logical expression per line for complex queries.
- Do not mix casing, alias styles, indentation styles, or comma conventions inside the same file.
- Use explicit `JOIN ... ON` clauses instead of implicit joins in the `WHERE` clause.
- Keep join predicates in `ON` clauses and filtering predicates in `WHERE` clauses, unless a specific outer-join semantic requires otherwise.
- Do not use `SELECT *` in production SQL that returns a result set; explicitly list the columns required by the caller, report, migration, or validation step.
- Use `SELECT *` only for exploration, and only with an explicit row limit.
- Inside `EXISTS`, prefer a constant projection such as `SELECT 1` unless the project or target database has a documented convention.
- Add comments when they explain business rules, non-obvious filters, data-quality workarounds, performance tradeoffs, or intentional deviations from normal conventions.
- Do not comment syntax that the SQL already expresses plainly.
- Keep SQL comments current when query logic changes.

### Errors

- Handle `NULL` explicitly with `IS NULL`, `IS NOT NULL`, and `COALESCE` where appropriate.
- Do not compare nullable values as if `NULL` were an ordinary value.
- Keep nullable logic visible instead of hiding it inside unclear expressions.
- In grouped queries, include every non-aggregated selected column in the `GROUP BY` clause unless the target database provides a documented and intentional functional-dependency rule.
- Do not rely on permissive database behavior that returns arbitrary non-grouped values.
- Do not add `DISTINCT` merely to remove unexpected duplicates.
- Investigate and fix the join condition, grouping level, or source data issue when duplicates are unexpected.

### Safety

- Use query parameters for user-controlled values.
- Do not construct SQL by concatenating raw user input.
- Use primary keys, foreign keys, unique constraints, `NOT NULL`, and `CHECK` constraints when they express durable data integrity rules.
- Do not leave critical integrity rules only in application code when the database can enforce them reliably.
- Choose SQL data types that match the domain.
- Avoid floating-point types for exact financial values; use exact numeric types such as `NUMERIC` or `DECIMAL` when precision matters.
- Wrap related changes in a transaction when they must succeed or fail together.
- Keep transactions as short as possible.
- Do not wait for user interaction while a transaction is open.

### Tests

- For slow, expensive, business-critical, or production-impacting SQL, inspect the execution plan instead of guessing.
- Verify whether performance-sensitive queries scan too much data, use expected indexes, sort unnecessarily, or perform expensive joins.
- When result order matters to a caller, report, export, pagination workflow, or deterministic test, make that order explicit with `ORDER BY`.
- Do not add `ORDER BY` when result order is irrelevant.
- Validate schema changes against the intended primary keys, foreign keys, uniqueness, nullability, check constraints, data types, indexes, and transaction behavior.

### Idioms

- Apply selective filters as early as possible when doing so preserves query semantics, especially before aggregation, joins, CTE reuse, or subquery processing.
- Do not move filters across outer joins, aggregations, or window calculations unless the result set remains intentionally unchanged.
- Use `WHERE` for row-level filters and reserve `HAVING` for aggregate filters.
- Keep predicates index-friendly by avoiding functions, arithmetic, concatenation, or `CASE` expressions around indexed columns in `WHERE` predicates when an equivalent direct predicate is possible.
- Prefer range predicates and explicit Boolean logic that allow the optimizer to use indexes.
- Use `=` for exact matches and reserve `LIKE` for pattern matching.
- Avoid leading wildcards such as `LIKE '%term'` or `LIKE '%term%'` unless the performance cost is acceptable and documented.
- Use `EXISTS` instead of `COUNT(*)` when the requirement is only to check whether at least one matching row exists.
- Use `UNION ALL` when duplicates are acceptable or already impossible.
- Use `UNION` only when deduplication is required and the cost is justified.
- Use CTEs when they make a query easier to read, test, or reuse.
- Do not introduce CTEs for trivial single-use logic if they make the query longer without clarifying intent.
- Add indexes only for known access patterns, filter predicates, joins, ordering needs, or uniqueness constraints.
- Do not add indexes without considering write cost, storage cost, and workload tradeoffs.

### Other

- Prefer standard SQL when portability matters.
- Use vendor-specific functions, hints, syntax, or extensions only when they are required, documented, and isolated enough to be changed later.
- Treat SQL as code and store DDL, DML, migrations, seed scripts, and repeatable maintenance scripts in version control.
- Do not rely on undocumented manual production changes.

## MySQL

Apply this section to MySQL code in addition to the generic `SQL` section. When
both sections address the same topic, prefer the more specific MySQL rule.

### Naming

- Use clear, stable, and project-consistent names for MySQL databases, tables,
  columns, indexes, constraints, routines, triggers, and aliases.
- Define an explicit primary key for every table, using a stable natural key only
  when it is obvious and using an auto-incrementing surrogate key when no
  natural key is clear.
- Match foreign key column data types and MySQL-required attributes with the
  referenced columns: fixed-precision size and sign must match, and nonbinary
  string columns must use the same character set and collation.
- Name foreign key columns consistently with the referenced domain concept so
  join intent remains easy to review.
- Do not encode multiple logical values in a single column when those values
  need to be queried, indexed, constrained, or updated independently.
- Document the purpose of non-obvious indexes, especially composite, prefix,
  covering, or workload-specific indexes.

### Formatting

- Keep MySQL DDL, DML, migration scripts, and maintenance SQL readable enough
  that storage engine choices, transaction boundaries, locking behavior, and
  operational assumptions are visible to a reviewer.
- Prefer explicit column lists in production MySQL queries and return only the
  rows and columns required by the caller, report, migration, or validation
  step.
- Use deterministic `ORDER BY` clauses for pagination and for any query where
  result order matters.
- Keep predicates sargable by avoiding unnecessary functions, casts, arithmetic,
  implicit conversions, or incompatible type comparisons on indexed columns.
- Keep related transaction statements close together and make `START
  TRANSACTION`, `COMMIT`, and `ROLLBACK` boundaries explicit.

### Errors

- Handle MySQL deadlocks and lock wait timeouts at the application boundary with
  bounded retries only when the operation is idempotent or safely repeatable.
- Define rollback behavior before adding multi-step writes, production
  migrations, or destructive schema changes.

### Safety

- Use `InnoDB` as the default storage engine for transactional application data
  unless a documented requirement justifies another engine.
- Require `NO_ENGINE_SUBSTITUTION` in controlled environments where accidental
  storage engine substitution would create operational risk.
- Use MySQL foreign keys when the application domain requires referential
  integrity to be enforced by the database.
- Add or change indexes only when justified by an observed query pattern, an
  `EXPLAIN` plan, or a documented performance reason.
- Design composite indexes according to MySQL's leftmost-prefix rule.
- Avoid redundant indexes that serve the same prefix and access pattern as an
  existing index.
- Consider storage cost and write overhead before adding indexes to high-write
  MySQL tables.
- Analyze non-trivial `SELECT`, `UPDATE`, `DELETE`, `INSERT ... SELECT`, and
  `REPLACE` statements with `EXPLAIN` before optimizing or approving them.
- Avoid unbounded reads in application endpoints and batch large reads or writes
  when practical.
- Keep MySQL transactions short, explicit, and limited to one business
  operation.
- Do not mix unrelated business operations in the same MySQL transaction.
- Do not use `LOCK TABLES` for normal InnoDB application workflows.
- Use row-level locking patterns such as `SELECT ... FOR UPDATE` only when
  exclusive access to specific rows is required.
- Do not create long-running transactions for batch jobs without chunking,
  progress tracking, and rollback strategy.
- Use dedicated MySQL users per application, service, or job.
- Do not use `root` or broad administrative accounts for application runtime
  access.
- Grant the minimum required privileges at the narrowest practical scope:
  database, table, column, or routine.
- Require prepared statements or parameterized query APIs for
  application-provided values.
- Require TLS for sensitive database connections and avoid plaintext credentials
  or data in transit.
- Avoid exposing MySQL directly to the public internet unless an explicit,
  reviewed operational requirement exists.
- Prefer private networking for MySQL access when possible.
- Never allow unrestricted `0.0.0.0/0` database access without an explicitly
  documented temporary exception.
- Treat `SECURITY DEFINER`, stored routines, dynamic SQL, triggers, and elevated
  privileges as high-risk areas requiring explicit review.
- Do not store MySQL credentials in source code, committed configuration files,
  or logs.
- Avoid destructive schema changes without an explicit backup, rollback, or data
  recovery strategy.

### Deployment and Operations

Apply this section only when creating, editing, reviewing, or refactoring MySQL
deployment, runtime configuration, migrations, backups, or maintenance scripts.
For ordinary query, schema, or application SQL changes, do not expand the task
into operational changes unless the current change directly affects them.

- Configure database connection timeouts explicitly instead of relying on
  unknown client, driver, or server defaults.
- Use exponential backoff for transient connection failures, maintenance events,
  and failover recovery.
- Split large schema or data migrations into ordered, observable, and restartable
  steps.
- Ensure failed migrations, interrupted batch jobs, and partially applied data
  changes have a documented recovery path.
- Do not treat a backup, export, or point-in-time recovery setup as valid until
  restore behavior has been tested.
- Rotate credentials and remove unused MySQL users during regular maintenance
  reviews.
- Verify that production backups, retention, binary log retention, recovery
  point objective, and recovery time objective match project recovery
  requirements.
- Protect MySQL backups from accidental deletion and unauthorized access.
- Monitor CPU, memory, disk, connections, slow queries, replication, and
  failover health for production MySQL systems.
- Add alerting for disk space thresholds and avoid running near full storage.
- Tune MySQL server parameters only with a documented hypothesis, before-and-
  after measurements, and a rollback plan.
- Test major MySQL upgrades in a representative environment before production.
- Run MySQL upgrade checks and fix incompatibilities before the production
  upgrade.
- Verify that a full backup exists and is restorable before upgrading
  production.
- Benchmark critical queries before and after MySQL upgrades because optimizer,
  authentication, encryption, storage engine, index, and memory changes can
  introduce regressions.
- Test application behavior during MySQL maintenance and failover events because
  existing connections can be dropped.
- Use slow query logs, query insights, or equivalent tooling to identify real
  bottlenecks before changing schema, indexes, or server configuration.
- Review slow queries periodically and prioritize fixes by frequency, latency,
  and business impact.
- Use connection pooling for applications that open many short-lived MySQL
  connections.
- Set a clear upper bound for connection pools per application instance and
  account for horizontal scaling.
- Close or return MySQL connections to the pool promptly after each unit of
  work.
- Use exports only as an additional protection mechanism when backup scope or
  retention does not cover the recovery scenario.

### Tests

- Use the same SQL mode for export and import migrations when moving data
  between MySQL environments.
- Test schema migrations in an environment that represents production data
  volume, indexes, constraints, storage engine, character sets, collations, and
  SQL mode.
- Capture baseline metrics before performance changes and compare them after the
  change.

### Idioms

- Use joins for relational access instead of repeated application-side lookups
  when related data can be retrieved in one controlled MySQL query.
- Use explicit `START TRANSACTION` and `COMMIT` blocks for related DML
  operations that must succeed or fail together.
- Prefer covering indexes only for hot read paths where selected columns are
  stable and the query benefit outweighs maintenance overhead.
- Prefer clear MySQL over clever MySQL unless the optimized form is measurably
  better and remains maintainable.

### Other

- Prefer official MySQL documentation and maintained managed-provider
  documentation when MySQL guidance conflicts.
- Do not generate MySQL-specific rules for another SQL dialect without explicit
  compatibility validation.
- Do not assume cloud-provider recommendations apply unchanged to self-managed
  MySQL.
- Do not assume self-managed MySQL settings apply unchanged to managed MySQL
  services.
- Keep MySQL rules separate from ORM-specific, framework-specific, and
  cloud-provider-specific rules unless the target context explicitly requires
  them.
- Document assumptions about MySQL version, deployment model, storage engine,
  SQL mode, character set, collation, and client driver when they affect a
  recommendation.
- Do not introduce a new index, transaction boundary, privilege, trigger, stored
  procedure, routine, server parameter, or migration behavior without explaining
  the operational impact.
- When modifying MySQL, always check regression risk in result cardinality,
  locking behavior, transaction scope, index usage, privilege requirements,
  migration compatibility, and deployment model compatibility.

## Oracle PL/SQL

Apply this section to Oracle PL/SQL code in addition to the generic `SQL`
section. When both sections address the same topic, prefer the more specific
Oracle PL/SQL rule.

### Naming

- Use project-defined naming conventions consistently for packages, procedures,
  functions, parameters, variables, constants, and exceptions.
- When a repository defines PL/SQL prefixes such as `p_`, `l_`, `g_`, `lc_`, or
  `gc_`, apply them consistently inside the touched PL/SQL scope.
- Name functions after the value they return and procedures after the action
  they perform.
- Use `%TYPE` and `%ROWTYPE` for variables, records, rows, and cursor results
  that are tied to database columns or query results.
- Do not hard-code PL/SQL data types when the variable represents an existing
  table column, row, cursor row, or schema-owned type.
- Replace magic values with named constants, domain concepts, lookup functions,
  or package-level APIs when they represent statuses, thresholds, business
  rules, or domain values.

### Formatting

- Keep package specifications focused on the public API and keep implementation
  details in the package body.
- Do not change a package specification unless the public API must change.
- Prefer implementation changes in package bodies when the public contract does
  not need to change.
- Keep executable sections short enough that the main control flow remains easy
  to review.
- Extract named local procedures or functions when a PL/SQL block grows into
  multiple logical steps.
- Use `ELSIF` or `CASE` for mutually exclusive branches instead of independent
  `IF` blocks.
- Do not generate `GOTO` in PL/SQL code; use structured conditionals, loops,
  local subprograms, or explicit error handling instead.

### Errors

- Centralize reusable PL/SQL error handling in package APIs instead of
  duplicating exception logging logic in every handler.
- Catch specific exceptions before using `WHEN OTHERS`.
- Use `WHEN OTHERS` only at an outer boundary where the error can be logged,
  preserved, and deliberately re-raised or translated.
- Do not hide the root cause of an exception.
- Do not use exceptions as normal branching logic.
- Keep transaction control out of reusable PL/SQL components by default.
- Do not issue `COMMIT` or `ROLLBACK` inside reusable packages, procedures, or
  functions unless that component explicitly owns the transaction boundary.
- Use autonomous transactions only for isolated logging or audit records that
  must survive rollback of the main transaction.

### Safety

- Do not expose mutable package state in the package specification.
- Declare non-constant package-level data in the package body, and expose access
  through explicit getter or setter subprograms only when needed.
- Keep functions value-oriented and side-effect-light.
- Do not use `OUT` or `IN OUT` parameters in functions.
- Use procedures when logic performs DML, modifies state, or must return
  multiple outputs.
- Use `NOCOPY` only when large `OUT` or `IN OUT` parameters are necessary and
  safe after checking exception and aliasing risks.
- Use bind variables whenever runtime values are passed into SQL.
- Do not concatenate runtime values into SQL text when bind variables can be
  used.
- Prefer static SQL when dynamic SQL is not required.
- Validate identifiers, values, and allowed operations explicitly before using
  them in dynamic SQL.
- Choose invoker-rights or definer-rights deliberately for PL/SQL units.
- Do not rely on the default privilege model without checking the security
  impact.
- Apply least privilege to PL/SQL APIs and underlying schema objects.
- Prefer granting access through narrow package APIs instead of broad direct
  privileges on tables, views, or critical procedures.

### Tests

- Write regression tests before changing legacy PL/SQL behavior.
- Write unit tests for packages, procedures, and functions when their behavior
  must not regress.
- Keep each PL/SQL unit test focused on one behavior.
- Use an Arrange-Act-Assert structure for PL/SQL tests: set up inputs and
  database state, execute the PL/SQL unit, then assert the expected result.
- Design tests so that an incorrect implementation can actually fail the test.
- Rerun affected PL/SQL tests after code, data, package specification, package
  body, or schema changes.
- Use available PL/SQL checks and tools such as compiler warnings, PL/Scope,
  the PL/SQL hierarchical profiler, SQL Developer, Toad, or SonarQube when they
  are part of the project toolchain.

### Idioms

- Implement reusable PL/SQL logic inside packages by default.
- Avoid standalone procedures or functions unless the target environment or
  integration point explicitly requires them.
- Treat the package specification as the public API and the package body as the
  private implementation.
- Encapsulate business rules and repeated SQL behind package functions or
  procedures.
- Do not duplicate business logic, predicates, formulas, or SQL fragments across
  pages, triggers, procedures, or anonymous blocks.
- Prefer set-based SQL and bulk processing over row-by-row processing.
- Use `BULK COLLECT` and `FORALL` for high-volume operations when they reduce
  context switches and fit the available memory constraints.
- Minimize work inside loops by avoiding repeated calculations and unnecessary
  repeated passes over collections or result sets.
- Use cursor `FOR` loops only when every row must be processed.
- Do not use cursor `FOR` loops for single-row retrieval.
- When fetching from explicit cursors, fetch into records rather than unrelated
  individual variables.
- Do not declare the index variable of a numeric `FOR` loop; let PL/SQL define
  it implicitly.
- Use Oracle built-ins, SQL functions, PL/SQL built-ins, and Oracle-supplied
  packages before writing custom implementations.
- Use early `EXIT`, `EXIT WHEN`, or `RETURN` from `FOR` and `WHILE` loops only
  when the exit condition is intentional and clearer than carrying extra state
  or nesting conditionals.
- For searched `CASE` expressions with overlapping predicates, preserve
  semantic correctness before optimizing branch order.
- Reorder searched `CASE` branches for performance only when the predicates
  remain semantically equivalent.

### Other

- Document public package APIs in the package specification.
- Public package API documentation should explain the purpose, parameters, and
  return values of exposed procedures and functions.
- Avoid documenting obvious implementation details that are already clear from
  the PL/SQL code itself.

## Microsoft SQL Server Transact-SQL

Apply this section to Microsoft SQL Server Transact-SQL code in addition to the generic `SQL` section when the target language or database dialect is T-SQL. When both sections address the same topic, prefer the more specific T-SQL rule.

### Naming

- Before generating T-SQL, identify the exact target platform: SQL Server, Azure SQL Database, Azure SQL Managed Instance, Azure Synapse Analytics, Fabric SQL, or another Microsoft SQL platform.
- Do not assume that every T-SQL feature is available on every Microsoft SQL platform.
- State the target SQL Server product, deployment model, and version when syntax, behavior, compatibility level, or feature availability matters.
- Use schema-qualified object names such as `dbo.customer` whenever possible.
- Do not rely on the caller's default schema for production database objects.
- Do not use the `sp_` prefix for user-defined stored procedures.
- Use stable, descriptive object, procedure, parameter, variable, temporary table, and alias names.
- Follow the repository convention for identifier casing; if no local convention exists, keep T-SQL keywords uppercase and identifiers consistently cased.
- Prefix Unicode string literals with `N`, such as `N'value'`, when the literal contains or may contain Unicode text.

### Formatting

- Terminate T-SQL statements with semicolons consistently.
- Always terminate `MERGE` statements with a semicolon.
- Write T-SQL so that the target platform, object names, filtering logic, ordering logic, and transaction boundaries are visible to a reviewer.
- Use explicit column lists in production `SELECT` statements instead of `SELECT *`.
- Return only the rows and columns required by the caller, report, export, validation, or data-change operation.
- Use `ORDER BY` whenever result order matters.
- Do not rely on storage order, clustered index order, insertion order, or execution-plan side effects for result ordering.
- Do not use ordinal positions such as `ORDER BY 1` or `ORDER BY 2`; use explicit column names or aliases.
- Use `TOP (...)` with parentheses.
- Pair `TOP (...)` with `ORDER BY` when deterministic row selection is required.
- Use `OFFSET` and `FETCH` for page-based retrieval when they are supported by the target platform and version.
- For stable paging, use a deterministic and preferably unique ordering key.
- Use named parameters when executing stored procedures, such as `EXEC dbo.MyProcedure @UserId = @user_id;`.
- Put `SET NOCOUNT ON;` at the start of stored procedures unless the caller intentionally depends on row-count messages.
- Declare procedure-sensitive `SET` options explicitly at the start of the procedure when the logic depends on them.
- Explicitly define `NULL` or `NOT NULL` for temporary table columns instead of relying on session defaults.
- Keep T-SQL hints, session options, transaction settings, and version-specific syntax local to the statement, procedure, or migration that requires them.

### Errors

- Use `TRY...CATCH` for transactional, procedural, or multi-step T-SQL logic that needs controlled error handling.
- Do not assume `TRY...CATCH` catches compile-level, connection-level, or every possible severity-level failure.
- In `CATCH` blocks, deliberately return, rethrow, or translate errors when caller visibility is required.
- Prefer `THROW` over `RAISERROR` in new T-SQL code when rethrowing or raising procedural errors.
- Use `XACT_STATE()` in `CATCH` blocks before deciding whether to commit or roll back a transaction.
- Roll back uncommittable transactions instead of attempting to commit them.
- Use `SET XACT_ABORT ON;` when a runtime error must terminate and roll back the full transaction.
- Keep transactions as short as possible to reduce locking, blocking, and deadlock risk.
- Do not wait for user interaction, external approval, or long-running non-database work while a transaction is open.
- When generated T-SQL can fail because of missing objects, permissions, invalid input, duplicate data, or unexpected cardinality, make the failure path explicit.

### Safety

- Never concatenate unvalidated user input into dynamic SQL.
- Validate input type, length, format, range, and allowed values before using external input in T-SQL.
- Parameterize dynamic SQL with `sp_executesql` whenever dynamic SQL is required and values can be parameterized.
- Review any generated use of `EXEC`, `EXECUTE`, or `sp_executesql` as a SQL injection risk boundary.
- Use `QUOTENAME()` for dynamic identifiers when identifier generation is unavoidable and the input length is suitable.
- Use quote-doubling with `REPLACE()` for dynamic string literals when dynamic SQL cannot be avoided.
- Do not use dynamic SQL for static statements that can be written safely as ordinary parameterized T-SQL.
- Apply least privilege when generating grants, ownership chains, procedure execution patterns, or access-control examples.
- Do not generate SQL that broadens permissions beyond the minimum required by the requested behavior.
- Avoid exposing sensitive columns by default in generated queries, views, stored procedures, exports, and diagnostics.
- Prefer designs compatible with column-level protection, row-level security, auditing, and least-privilege access when sensitive data is involved.
- Use query hints, table hints, index hints, locking hints, and `OPTION (...)` only as a last resort for a documented optimizer, locking, or regression problem.
- Do not add `NOLOCK` or other isolation-affecting hints as a default performance shortcut.
- Document every required hint with the observed problem, target SQL Server version or platform, expected effect, and regression risk.
- Use explicit transactions for multi-step data changes that must succeed or fail together.
- Ask for clarification before generating destructive operations when object names, target environment, filter criteria, transaction scope, or permission impact are ambiguous.

### Tests

- For non-trivial generated T-SQL, state how correctness should be verified: expected row counts, deterministic ordering, affected rows, rollback behavior, permission boundaries, or error paths.
- For performance-sensitive T-SQL, inspect the execution plan instead of guessing.
- Verify that predicates can use expected indexes when performance depends on index usage.
- Verify that generated result sets are deterministic when used for reports, exports, tests, paging, or `TOP (...)` operations.
- Test stored procedures with named parameters, missing or invalid inputs, `NULL` inputs, and expected error paths when those paths are affected.
- Test transaction logic for success, failure, rollback, and uncommittable transaction behavior when generated code uses explicit transactions.
- Test dynamic SQL with safe values, invalid values, boundary lengths, and attempted injection strings when dynamic SQL is generated.
- Test `MERGE` behavior with matched rows, unmatched source rows, unmatched target rows, duplicates, and batching assumptions when `MERGE` is generated.
- When version-specific syntax or platform-specific behavior is used, verify it against the declared SQL Server product, version, and compatibility level.

### Idioms

- Prefer the smallest correct T-SQL solution that satisfies the requested behavior.
- Do not add stored procedures, dynamic SQL, temporary tables, hints, transactions, `MERGE`, or abstractions unless they are required by the task.
- Avoid wrapping indexed columns in functions, arithmetic, casts, concatenation, or `CASE` expressions inside `WHERE` or `JOIN` predicates when an equivalent sargable predicate is possible.
- Avoid scalar function calls over large result sets unless the design explicitly requires them and the performance cost is acceptable.
- Use `UNION ALL` unless duplicate elimination is required.
- Use `MERGE` only when it is simpler and safer than separate `INSERT`, `UPDATE`, and `DELETE` statements.
- Prefer explicit `INSERT`, `UPDATE`, or `DELETE` statements for simple source-to-target changes when they are clearer or safer than `MERGE`.
- Keep `MERGE ON` conditions strictly focused on target-source matching.
- Do not move target filtering logic into a `MERGE ON` clause to force performance behavior.
- Do not use `TOP` inside `MERGE` for deterministic batching unless successive batches are explicitly controlled and documented.
- Do not generalize SQL Server version-specific behavior to all Microsoft SQL platforms.
- Flag unsafe ambiguity instead of guessing when missing information affects data modification, security, permissions, object names, target SQL platform, transaction scope, or destructive operations.

### Other

- Prefer official Microsoft Learn documentation as the primary source for Microsoft SQL Server Transact-SQL behavior.
- When T-SQL guidance conflicts, prioritize maintained official Microsoft documentation over blogs, forums, videos, PDFs, examples, or secondary summaries.
- Treat Microsoft SQL Server Transact-SQL as a SQL dialect with product-specific behavior, not as interchangeable generic SQL.
- Isolate vendor-specific syntax, hints, platform assumptions, and compatibility-level dependencies so they can be reviewed or changed later.
- State version or platform constraints explicitly for features that apply only to specific SQL Server versions, Azure SQL variants, Synapse, Fabric SQL, or compatibility levels.
- Do not claim that generated T-SQL is portable to other SQL databases unless portability was intentionally checked.

## Go

### Naming

- Use `mixedCaps` for unexported identifiers and `MixedCaps` for exported identifiers.
- Do not use `snake_case` for Go identifiers unless an external format or protocol requires it.
- Keep short names acceptable in very small scopes, especially conventional names such as `i`, `r`, `w`, and `ctx`.
- Keep package names short, lowercase, single-word, and descriptive.
- Do not use underscores, mixed caps, vague names, or redundant package prefixes in package names.
- Prefer singular package names when the package represents one cohesive concept.
- Avoid repeating package, receiver, parameter, or return type names in function and method names; use the call site as the readability test.
- Do not prefix ordinary getter methods with `Get`; prefer `Owner()` over `GetOwner()` and reserve `SetOwner()` for setters that mutate state.
- Name one-method interfaces after behavior using the conventional `-er` form when it matches established Go usage, such as `Reader`, `Writer`, or `Formatter`.

### Formatting

- Format Go code with `gofmt` or `go fmt` before presenting or committing it.
- Do not manually align code, comments, struct fields, imports, or whitespace against `gofmt`; let the standard formatter decide.
- Use Go modules as the default project unit, with one root module by default unless a clear architectural reason justifies multiple modules.
- Use `package main` only for executable commands; library code must use domain-specific package names.
- Organize Go packages by cohesive responsibility rather than by technical layer alone.
- Avoid catch-all packages such as `util`, `common`, or `helper` unless the package name is narrowly qualified and meaningful.

### Errors

- Return errors explicitly and handle them immediately instead of hiding failures.
- Return `error` values for expected failures; do not use `panic` for ordinary control flow or normal error cases.
- Prefer linear guard clauses and let the successful path continue down the page.
- Avoid unnecessary `else` blocks after `return`, `break`, `continue`, or `goto`.
- Do not ignore returned errors unless the reason is explicit, intentional, and local to the call site.
- At package boundaries, add caller-level context to foreign errors such as the operation, identifier, path, or dependency involved.
- Inside the same package, prefer returning the original error when the caller already has enough local context.
- When adding error context, describe the action being attempted with concise phrases such as `loading config`, `fetching user`, or `reserving stock`.
- Avoid noisy error prefixes such as `failed to`, `cannot`, or `error while` when a concise action phrase is clearer.
- Do not repeat details already present in the wrapped error; add higher-level intent instead.
- Do not make callers, dashboards, or alerts depend on exact error message strings.
- When code must branch on an error, expose a sentinel error checked with `errors.Is` or a typed error checked with `errors.As`.
- Wrap errors with `%w` only when callers should be able to inspect the underlying error with `errors.Is` or `errors.As`.
- Treat `%w` as part of the package API contract because it exposes the wrapped error to callers.
- When the underlying error should not become part of the public contract, return contextual errors without exposing implementation details.
- Use `%v` instead of `%w` when the human-readable message is useful but the underlying storage, driver, RPC, third-party, or dependency error must remain private.
- At system or dependency boundaries, translate implementation-specific errors into package-owned sentinel errors or custom error types.
- Make callers branch on the package domain error vocabulary, not on accidental details of the current storage, client, or dependency implementation.
- Use `errors.Is` and `errors.As` for wrapped error inspection; do not compare wrapped errors directly.
- Log an error or return it, but do not do both in the same layer.
- Return recoverable errors upward and let the terminal decision layer log an unhandled error once.
- At outer handlers, check `context.Canceled` and `context.DeadlineExceeded` before treating an error as an application failure.
- Use `panic` and `recover` sparingly; recover only inside deferred functions and only at deliberate failure-containment boundaries.

### Safety

- Pass `context.Context` explicitly as the first parameter when a function needs deadlines, cancellation, or request-scoped values.
- Do not store contexts inside structs, do not pass `nil` contexts, and use `context.TODO()` only when the correct context is genuinely unknown.
- Always call the cancellation function returned by `context.WithCancel`, `context.WithDeadline`, or `context.WithTimeout`; use `defer cancel()` when appropriate.
- Use `defer` immediately after successful resource acquisition when cleanup must happen regardless of the return path.
- Remember that `defer` is function-scoped, not block-scoped.
- Prefer channels when they make ownership and sequencing clearer; prefer mutexes when they are simpler for protecting shared state.
- Prevent goroutine leaks by defining a clear cancellation or completion path through context cancellation, channel closure, or another explicit signal.
- Do not start a goroutine that can fail without providing an observable error path.
- For concurrent work that can fail, use an explicit error collection mechanism such as `errgroup` or a buffered error channel.
- Log, signal, or deliberately escalate goroutine errors instead of allowing them to disappear silently.
- Be careful with loop variables captured by closures or goroutines, especially when targeting Go versions before 1.22.
- For Go 1.22 and later, do not apply pre-1.22 loop-variable workarounds blindly; check the project `go.mod` before applying version-dependent rules.

### Tests

- Write Go tests in files ending with `_test.go` using `TestXxx` functions.
- Use descriptive test names such as `TestFunctionName_Scenario` when the scenario improves failure diagnosis.
- Use `go test` as the default verification command for package behavior.
- Use table-driven tests for multiple input/output cases when they keep the test logic clearer.
- Use subtests with `t.Run` when cases need names, filtering, parallelism, or isolated setup.
- Keep tests deterministic unless nondeterminism is the behavior under test.
- Avoid hidden test dependencies on wall-clock timing, map iteration order, global mutable state, external services, or uncontrolled goroutine scheduling.
- Test failure paths that branch on sentinel errors, typed errors, wrapped errors, cancellation, or dependency-boundary translation.
- Do not assert exact error message strings unless the message text is the explicit behavior under test.
- Use `go vet` as a static-analysis safety check, not as proof of correctness.
- Run `go test -race` when tests exercise concurrent paths or when a change affects concurrency-sensitive code.
- After a Go code change, run the smallest meaningful verification set first, usually formatting only touched files or packages, `go test` for affected packages, `go vet` when useful, and `go test -race` when justified by the codebase and task.

### Idioms

- Prefer Go idioms over verbose names or non-Go naming conventions.
- Prefer concrete types until tests, package boundaries, or alternate implementations justify an interface.
- Keep interfaces small, behavior-focused, and defined near the consumer when practical.
- Document exported public API identifiers with Go doc comments, following repository lint rules.
- Use package comments as complete sentences and avoid duplicate package comments across multiple files.

## PHP

### Naming

- Use `$camelCase` for variables.
- Use `camelCase` for methods and functions.
- Use `PascalCase` for classes, interfaces, traits, and enums.
- Use `UPPER_SNAKE_CASE` for constants.

### Formatting

- Follow PSR-12 unless the repository defines another PHP coding standard.
- Enforce PHP formatting with tooling such as PHP_CodeSniffer or PHP-CS-Fixer when available.
- Apply PHP formatters only to touched PHP files unless a project PHP check requires a broader format pass.

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

### Formatting

- Encode Java source files in UTF-8 and do not introduce non-standard whitespace characters.
- Prefer one top-level Java type per source file, and make the `.java` file name match the case-sensitive public top-level type when one exists.
- Keep Java source files structurally ordered: license or copyright block, package declaration, imports, then the top-level type declaration.
- Do not use wildcard imports.
- Use explicit imports only, and keep static imports separated from non-static imports.
- Keep overloaded methods and constructors contiguous.
- Always use braces for `if`, `else`, `for`, `do`, and `while`, even for single-statement bodies.
- Use one executable statement per line.
- Keep line length under 100 characters unless the project style guide allows an explicit exception.
- Prefer clear line wrapping over dense one-line code or fragile horizontal alignment.
- Use blank lines to separate logical groups, not to create visual noise.

### Errors

- Keep checked and unchecked exception usage consistent with the project.
- Never ignore caught exceptions silently.
- Handle caught exceptions by logging, rethrowing, returning a meaningful fallback, or documenting why ignoring the exception is safe.
- Catch the most specific exception type that the code can handle meaningfully.
- Do not catch broad exceptions unless the handling is intentional and specific.
- Use `try-with-resources` for resources that implement `AutoCloseable`.
- Do not log and rethrow the same exception unless the catch block adds meaningful context.

### Safety

- Prefer immutable fields with `final` when practical.
- Favor immutable objects when state should not change after construction.
- Use constructor initialization and avoid setters where immutable behavior is intended.
- Keep fields private by default, and expose behavior through methods when appropriate.
- Do not expose instance or class fields publicly without a clear structural reason.
- Avoid returning `null` for collections; return an empty collection when appropriate.
- Avoid circular dependencies between Java packages or JPMS modules.
- Express domain-significant Java constants as `static final` constants, enums, or configuration values.
- Avoid embedded assignments when they reduce readability.
- Access static members through the class name, not through an instance.
- Do not override `Object.finalize`.
- When changing Java dependencies or build files, use the project's dependency audit tooling when available.

### Tests

- Use the project's Java test framework for behavior that must not regress.
- Prefer unit tests for local Java logic and integration tests for Java component boundaries.
- Use Java test method names or display names that communicate the behavior under test and the expected outcome.
- Run the smallest meaningful verification set after a Java change, covering compilation, tests, formatting, imports, exception handling, dependency impact, and behavior preservation.
- Use Maven, Gradle, or the project's Java dependency tooling when changing dependencies, and run tests before accepting dependency changes.

### Idioms

- Use `switch` expressions or statements when supported by the project's configured Java version and when they make multi-branch selection clearer than repeated `if else` chains.
- Do not replace simple conditions with `switch` unless it improves readability.
- Document intentional `switch` fall-through with a local comment at the fall-through point.
- Prefer collections over arrays when dynamic size, generics, or collection operations are needed.
- Use arrays when fixed-size, low-level, or interoperability constraints justify them.
- Use enhanced `for` loops when index management is unnecessary.
- Use streams when filtering, mapping, or aggregation is clearer than imperative iteration.
- Do not use streams when they obscure simple control flow.
- Use lambdas for functional interfaces when they reduce boilerplate and remain readable.
- Keep lambda bodies short; extract named methods when lambda bodies become complex.
- Use `@Override` whenever overriding or implementing a method.

### Other

- Write Javadoc for public APIs and behavior that external callers must understand.
- Begin each Javadoc block with a concise summary fragment.
- Keep Javadoc block tags meaningful and non-empty.
- Do not write empty `@param`, `@return`, `@throws`, or `@deprecated` descriptions.
- Add a Java interface or abstract class only when the current Java code has a concrete, repeated need for it.
- Do not generalize Spring, Maven, Gradle, Google Cloud, IDE-specific, or framework-specific guidance to all Java code.
- Apply framework-specific guidance only when the project context uses that framework or tool.
- When Java guidance conflicts, prefer maintained, official, or project-local standards over archived or vendor-blog guidance.

## Java Properties Files

### Naming

- Use `.properties` as the standard filename suffix for Java properties resources.
- Use stable, descriptive, dot-separated property keys that reflect the configuration domain.
- Avoid vague property keys such as `value`, `flag`, `url1`, or `temp`.
- Treat localization property keys as durable identifiers and do not rename them casually.
- Translate property values, not property keys, unless the project has an explicit key-localization mechanism.

### Formatting

- Represent Java `.properties` files as string-based key-value configuration resources.
- Convert property values to typed values explicitly in application code after loading and validation.
- Use one consistent assignment style in each generated file, preferably `key=value`.
- Do not mix `key=value`, `key = value`, `key:value`, and whitespace-separated forms in the same file.
- Use comments starting with `#` or `!` only to clarify purpose, units, accepted values, default behavior, or operational warnings.
- Do not use large blocks of commented-out alternatives as the primary configuration mechanism.
- Document non-obvious or mandatory properties close to the property they describe.
- Preserve intentional leading, trailing, and embedded whitespace in property values.
- Choose the file encoding deliberately and document non-default encoding expectations.
- For classic `java.util.Properties` compatibility, avoid raw characters outside ISO-8859-1 unless the loading code explicitly uses an encoding-aware path.
- Escape syntax-sensitive characters only when required by the properties format or the selected parser.
- Pay special attention to `#`, `!`, `=`, `:`, backslashes, leading spaces, tabs, logical newlines, and Unicode escape sequences.
- Use escaped `\n` for logical newlines inside values unless physical multiline continuation is explicitly intended.
- Use line continuation only when it improves readability and the target parser supports it.
- When using continuation lines, ensure the trailing backslash and continuation indentation do not change the expected value.
- Do not escape single or double quotes unless the consuming framework, message formatter, or localization tool requires it.

### Errors

- Treat missing mandatory properties as configuration errors instead of silently substituting unsafe defaults.
- Use `getProperty(key, defaultValue)` only when the default value is semantically valid and safe.
- Do not use Java default property lists to hide incomplete or invalid configuration.
- Validate and report invalid typed conversions for integers, booleans, durations, URLs, paths, enums, and similar typed values.
- Do not duplicate property keys unless the selected runtime explicitly documents duplicate-key or repeated-key behavior.
- For plain `java.util.Properties`, do not rely on duplicate keys as a list mechanism.

### Safety

- Do not store production secrets, credentials, tokens, passwords, private URLs, or API keys in properties files.
- Represent secrets as placeholders or runtime-injected values and document the expected secure source.
- Do not generalize Spring Boot behavior to plain Java properties files.
- Apply Spring Boot-specific rules only when the target project explicitly uses Spring or Spring Boot.
- Do not use Apache Commons Configuration features unless the target project explicitly uses Apache Commons Configuration.
- Treat `include`, `includeOptional`, delimiter-based lists, repeated keys as lists, and builder-based saving as parser-specific behavior.
- When using Apache Commons Configuration lists, configure delimiter handling explicitly instead of assuming comma-separated values are split automatically.

### Tests

- Validate generated or modified properties files for syntax, duplicate keys, encoding, missing mandatory values, and unintentionally unescaped syntax-sensitive characters.
- Test application-level conversion and validation for every property value that becomes a typed value.
- Test missing mandatory properties and invalid values on affected configuration paths.
- Test localization properties for missing keys, placeholder consistency, syntax, encoding, and unescaped characters.
- When parser-specific behavior is used, test the behavior with the actual parser used by the project.

### Idioms

- Use `getProperty()` for normal reads from `java.util.Properties`; do not use inherited `Hashtable.get()` for ordinary property lookup.
- Use `setProperty()` for normal writes to `java.util.Properties`; do not use inherited `put()` or `putAll()` for ordinary property updates.
- Use `store()` or `storeToXML()` when serializing a `Properties` object unless a custom layout must be preserved.
- Use XML properties only when XML format, XML tooling, or explicit XML encoding behavior is required.
- Load and save persisted properties from stable, well-known locations.
- Use Java default property lists only for real fallback layers that are intentionally overridden by application-specific values.
- Use the placeholder convention expected by the consuming formatter for localized values.
- Use numbered or ICU-style placeholders only when the consuming parser explicitly supports that convention.

### Other

- For Spring Boot projects, keep shared values in `application.properties` and environment-specific values in profile-specific files such as `application-dev.properties`, `application-test.properties`, and `application-prod.properties`.
- Keep one language or locale per localization properties file.
- Keep Spring Boot, Apache Commons Configuration, and localization rules conditional to avoid applying framework-specific behavior to plain Java properties files.


## TypeScript

### Naming

- Use `camelCase` for variables and functions.
- Use `PascalCase` for classes, interfaces, type aliases, and enums.
- Use `UPPER_CASE` for global compile-time constants only when the project
  already uses that convention.
- Keep TypeScript names descriptive and avoid encoding type information that the
  type system already exposes.
- Keep interfaces small, focused, and limited to one coherent consumer or
  responsibility.
- Avoid empty interfaces because they do not define a meaningful contract.

### Formatting

- Match the existing project formatting, module style, semicolon policy, and
  linting setup before applying a generic TypeScript convention.
- Use ES module syntax with `import` and `export` for normal module boundaries.
- Do not use `namespace` for ordinary code organization.
- Do not use TypeScript `require` import syntax unless legacy interoperability
  or third-party constraints require it.
- End statements with explicit semicolons when the project style allows or
  requires semicolons.
- Use TypeScript-aware ESLint and Prettier when they are already configured or
  explicitly introduced for the project.
- Do not rely on manual formatting or ad hoc review to enforce TypeScript style
  when automated checks are available.

### Errors

- Type callback return values as `void` when the caller intentionally ignores
  the returned value.
- Do not type ignored callback returns as `any`.
- Do not mark callback parameters optional unless the callback may actually be
  invoked without those arguments.
- When using overloads, order signatures from the most specific to the most
  general.
- Use overloads only when call shapes or return types genuinely differ.
- Do not write overloads that only add trailing parameters with the same return
  type; use optional parameters for that shape.
- Treat failed narrowing, invalid external data, and unsafe assertions as design
  errors to fix at the boundary where the value enters the typed code.

### Safety

- Enable strict type checking for new TypeScript projects; at minimum, keep
  `strict` enabled and do not hide implicit `any` errors.
- Avoid `any` in maintained code.
- Use explicit domain types when the value shape is known.
- Use `unknown` when a value is intentionally not known yet, then narrow it
  before reading properties, calling methods, or passing it into typed APIs.
- Use primitive type names such as `string`, `number`, `boolean`, and `symbol`.
- Do not use boxed primitive types such as `String`, `Number`, `Boolean`,
  `Symbol`, or `Object` as ordinary value types.
- Use `object` or a more precise object shape for non-primitive objects.
- Check optional properties for `undefined`, use optional chaining, or narrow the
  value before accessing nested members or calling methods.
- Prefer runtime narrowing with `typeof`, `instanceof`, property checks, or
  discriminants before using a value as a narrower type.
- Use `as` assertions only when a clear local invariant exists that TypeScript
  cannot infer, and document why the assertion is safe when the reason is not
  obvious.
- Treat JSON, API responses, user input, environment variables, and persisted
  data as untrusted until validated or narrowed at runtime.
- Use `readonly` for properties that must be assigned only during object
  creation or initialization.

### Tests

- Run the smallest relevant TypeScript verification set after a TypeScript
  change, including type checking, linting, formatting, and tests when the
  project provides them.
- Verify that generated or modified TypeScript compiles under the project's
  configured strictness level.
- Add or update tests when TypeScript behavior changes, especially for invalid
  inputs, boundary values, external-data validation, and narrowing-dependent
  branches.
- Test public API contracts when exported function signatures, return shapes,
  interfaces, type aliases, or generics change.
- Treat ESLint, Prettier, and `tsc` as quality gates when they are part of the
  project toolchain.

### Idioms

- Prefer TypeScript inference for clear local implementation details.
- Add explicit types where they clarify public APIs, document non-obvious
  intent, or protect contracts from accidental changes.
- Type exported functions, public methods, callbacks, and reusable library
  boundaries explicitly at their parameters.
- Add return types when the return shape is part of the public contract,
  complex, or likely to be accidentally changed.
- Model finite string or numeric values with literal unions instead of broad
  `string` or `number` types.
- Prefer union types over overloads when only one parameter varies by type.
- Use type aliases for unions, primitives, tuples, intersections, and
  composition that interfaces cannot express cleanly.
- Use interfaces for reusable object shapes and class contracts when extension
  or structural typing is the clearest expression.
- Use the simplest type construct that accurately expresses the contract.
- Avoid mapped types, conditional types, and complex generic abstractions unless
  they materially improve correctness or remove real duplication.
- Introduce generics only when a type parameter connects meaningful positions,
  such as input to output, key to object, or container to contained value.
- Use generic constraints such as `Key extends keyof Type` when they prevent
  invalid property access.
- Avoid return-type-only generics in new APIs.
- Use standard utility types such as `Partial`, `Required`, `Readonly`, `Pick`,
  and `Record` only when they make the transformation of an existing type
  clearer than an explicit type.

### Other

- Document exported APIs, top-level exports, public members, and non-obvious
  properties or methods with useful JSDoc when intent is not clear from the
  signature and name.
- Do not write comments that merely repeat TypeScript identifiers or restate
  obvious type information.
- Do not add TypeScript tooling, transpiler configuration, linter configuration,
  formatter configuration, or framework-specific rules unless the task or
  existing project context requires them.
- Prefer official TypeScript documentation, project-local conventions, and
  maintained style guides over generic examples when TypeScript guidance
  conflicts.

## JavaScript

### Naming

- Use clear variable, function, class, and module names that describe observable behavior or domain meaning.
- Avoid reusing one variable for different semantic meanings.
- Use function names that describe the action performed or the value returned.
- Avoid boolean flag parameters when they create multiple hidden code paths; split the behavior into separate functions instead.
- Keep callback and inline function names or parameters clear enough that the caller intent remains visible.

### Formatting

- Match the existing project style before introducing any JavaScript formatting convention.
- Use the repository formatter when one is already configured.
- Keep indentation, spacing, string quoting, semicolon policy, and module style consistent within the same repository.
- Prefer clear code over clever or overly compact expressions.
- Do not compress multiple operations into one expression when it hides intent.
- Keep comments focused on why a JavaScript decision exists, not on what the code plainly does.
- Remove stale comments when changing the behavior they describe.
- Use JSDoc only when it clarifies public API contracts, complex types, or non-obvious behavior.

### Errors

- Always handle rejected promises.
- Do not intentionally ignore a promise unless the reason is documented and safe.
- Use `try` / `catch` around awaited operations when the function can recover, add context, translate the error, or perform required cleanup.
- Do not swallow errors silently.
- Throw `Error` objects or project-standard error subclasses, not strings or arbitrary values.
- Preserve the original error context when wrapping errors.
- Add actionable context to errors close to the failure source.
- Do not catch an error unless the function can recover, enrich it, translate it, or perform required cleanup.
- Do not hide operational failures behind default fallback values unless the fallback is explicitly safe.
- Keep error messages specific enough to debug without exposing secrets.
- Validate function preconditions at public boundaries.

### Safety

- Treat all external input as untrusted.
- Validate input at application boundaries before using it in business logic.
- Normalize external input types at system boundaries before using them internally.
- Use explicit parsing for numbers, booleans, dates, and JSON-derived values.
- Use sink-specific escaping, encoding, validation, or parameterized APIs before sending data to HTML, URLs, SQL, shell commands, logs, or other sensitive sinks.
- Never build executable code from user-controlled strings.
- Avoid `eval`, `Function`, and string-based dynamic execution unless there is a documented, reviewed, and unavoidable reason.
- Validate JSON shape before trusting parsed content.
- Protect against prototype pollution when merging or deserializing untrusted objects.
- Avoid mutating function parameters unless mutation is the explicit purpose of the function.
- Do not expose mutable internal state directly from modules or classes.
- Do not use objects as dictionaries for untrusted keys without guarding against inherited properties and prototype pollution.
- Keep browser-only APIs such as `window`, `document`, `localStorage`, and DOM APIs out of Node.js code unless the runtime explicitly provides them.
- Keep Node.js APIs such as `fs`, `path`, `process`, and server-side modules out of browser code unless a bundler or polyfill strategy is explicitly defined.

### Tests

- Add or update tests when changing JavaScript behavior.
- For bug fixes, write a test that reproduces the bug before or alongside the fix.
- Test invalid inputs, boundary cases, and asynchronous failure paths.
- Keep test fixtures small and explicit.
- Avoid snapshot tests for logic-heavy code unless the snapshot is stable and easy to review.
- Do not mock standard JavaScript language behavior; mock external systems and unstable boundaries instead.
- After a JavaScript change, verify the affected runtime behavior, promise rejection handling, module loading, input coercion, and browser or Node.js boundary assumptions.

### Idioms

- Use `const` by default for bindings that are not reassigned.
- Use `let` only when reassignment is required.
- Do not use `var` in new code.
- Declare variables in the narrowest practical scope.
- Initialize variables close to their first meaningful use.
- Avoid implicit globals; every variable must be explicitly declared.
- Use `===` and `!==` by default.
- Use `==` or `!=` only when type coercion is intentional, documented, and covered by tests.
- Do not rely on implicit type conversion for business logic.
- Do not compare complex objects by reference unless reference identity is the intended behavior.
- Prefer `async` / `await` for promise-based asynchronous flows when it improves readability.
- Avoid deeply nested promise chains; flatten the control flow or extract helper functions.
- Keep concurrent operations explicit with `Promise.all`, `Promise.allSettled`, or sequential `await`, depending on failure semantics.
- Organize reusable code into modules with explicit imports and exports.
- Avoid hidden global dependencies between files.
- Prefer named exports for shared utilities when multiple functions are exported from the same module.
- Use default exports only when the module clearly exposes one primary concept.
- Avoid circular dependencies; if they appear, extract shared logic into a lower-level module.
- Keep module boundaries aligned with responsibilities, not arbitrary file size.
- Prefer immutable data transformations when they make intent clearer.
- Use object destructuring only when it improves readability.
- Prefer `Map` or `Set` when key-value or uniqueness semantics are clearer than plain objects or arrays.
- Use classes only when state and behavior naturally belong together.
- Prefer simple functions and plain objects when no object lifecycle is needed.
- Keep constructors simple; avoid asynchronous work or heavy side effects in constructors.
- Use private fields or closure-based encapsulation for internal state when supported by the target runtime.
- Prefer composition over inheritance unless inheritance clearly models the domain.
- Do not create abstract base classes or inheritance hierarchies speculatively.

### Other

- Always identify the target JavaScript runtime before generating code: browser, Node.js, embedded platform, or mixed runtime.
- Prefer standard JavaScript features documented by MDN before introducing third-party dependencies.
- Do not generalize framework-specific practices to JavaScript as a language rule unless the target project explicitly uses that framework.
- Do not add a dependency for functionality that can be implemented clearly with standard JavaScript in a few lines.
- Do not add framework, bundler, transpiler, linter, formatter, or test-runner configuration unless explicitly requested or required by the existing project.
- Start with readable JavaScript, then optimize only when there is a measured bottleneck or a known runtime constraint.
- Avoid unnecessary work inside loops, render cycles, event handlers, and frequently called callbacks.
- Cache repeated expensive computations only when the cache lifecycle is clear.
- Avoid blocking the main thread in browser code with heavy synchronous work.
- Avoid synchronous file operations in server code paths that must remain responsive.
- Use lazy loading or dynamic imports only when they solve a real loading or dependency boundary problem.
- Do not introduce micro-optimizations that make code harder to maintain without measurable benefit.

## Bash

### Naming

- Use lowercase variable names for local script variables, such as `file_path` and `retry_count`.
- Reserve uppercase variable names for environment variables, constants, and exported configuration.
- Use `local` for function-scoped variables to avoid leaking temporary state into the global scope.
- Name Bash functions after the command action or question they implement, such as `build_archive` or `is_valid_tag`.

### Formatting

- Start Bash scripts with an explicit Bash shebang. Use the project standard when one exists; otherwise prefer `#!/usr/bin/env bash` for user-space portability or `#!/bin/bash` for controlled system environments.
- Do not use Bash-only syntax under `#!/bin/sh`; arrays, `[[ ... ]]`, `local`, and `${BASH_SOURCE[@]}` require a Bash shebang.
- Preserve the existing Bash dialect, shebang style, strict-mode usage, and function layout when editing existing scripts.
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
- Run ShellCheck when available, and fix or explicitly justify warnings introduced or exposed by the current change in the touched Bash scope.
- For Bash scripts, exercise nonzero exit paths and missing argument, missing file, or missing command cases when they are affected by a change.
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

- Use `snake_case` for variables, functions, methods, modules, and packages.
- Keep module and package names short, lowercase, and descriptive.
- Use `PascalCase` / `CapWords` for classes and exceptions.
- Add the `Error` suffix to exception classes when the exception represents an error.
- Use `UPPER_SNAKE_CASE` for constants.
- Define shared constants at module level when they represent fixed configuration or domain values.
- Avoid visually ambiguous single-character names such as `l`, `O`, and `I`.
- Use `self` for instance methods and `cls` for class methods.
- Use a trailing underscore when a name conflicts with a Python keyword, such as `class_`.

### Formatting

- Follow the repository's established Python style before applying generic Python style rules.
- Follow PEP 8 when the repository has no stronger local convention.
- Use 4 spaces per indentation level and never mix tabs and spaces for Python indentation.
- Keep line length consistent with the project; if no project rule exists, default to 79 characters for code and 72 characters for long comments or docstrings.
- Prefer implicit line continuation inside parentheses, brackets, and braces.
- Avoid backslash continuations unless compatibility constraints require them.
- Place imports at the top of the file after module comments and docstrings.
- Group imports in this order: standard library, third-party packages, then local application imports.
- Separate import groups with one blank line.
- Use one import per line for modules.
- Prefer absolute imports for clarity and safer resolution.
- Avoid wildcard imports.

### Errors

- Prefer explicit exceptions over silent failure or ambiguous return values.
- Use exception types that make the failure mode clear to callers.
- Keep expected failure handling explicit at the call site or at a deliberate boundary.
- Do not suppress Python exceptions without a local, documented reason.
- Do not expose debug tracebacks or internal exception details to end users in production behavior.

### Safety

- Avoid mutable default arguments.
- Use `None` as the default sentinel when a default value must be created per call.
- Use context managers for files, locks, network connections, transactions, and other managed resources when the object supports them.
- Validate and sanitize untrusted input before it reaches file paths, shell commands, database queries, deserialization, or sensitive business logic.
- Use prepared statements or parameterized queries for database access.
- Never build SQL queries by concatenating untrusted input.
- Never hardcode secrets such as passwords, API keys, tokens, private URLs, or credentials.
- Keep development and production behavior separate; debug output, verbose errors, and permissive settings must not leak into production runtime.
- Prefer the Python standard library before adding a third-party dependency.
- Justify every new Python dependency and keep dependency changes minimal.
- Use the project's isolated Python environment when installing or running dependencies, such as `venv`, Poetry, uv, Conda, Docker, or the repository's documented workflow.
- Check package names carefully before installation to reduce typo-squatting and dependency-confusion risk.
- Respect the Python versions and dependency constraints declared by the project.
- Do not upgrade Python or dependencies blindly when the project declares supported runtime targets.

### Tests

- Use the project's existing Python test framework and test layout before introducing any new testing convention.
- When available and configured, run the relevant Python formatter, linter, type checker, tests, and coverage checks.
- Use project-approved tools such as `pytest`, `unittest`, `ruff`, `black`, `mypy`, or `pyright` only when they are already part of the project or explicitly requested.
- If checks cannot be run, state exactly which Python checks were skipped and why.

### Idioms

- Prefer f-strings for string interpolation when supported by the project's Python version.
- Add type hints when they improve clarity or match project conventions.
- Compare singletons with identity operators, such as `is None` and `is not None`.
- Do not use `== None` or `!= None`.
- Do not rely on truthiness when `None` has a distinct meaning from valid false values such as `0`, `""`, or `[]`.
- Avoid implementation-specific assumptions when portable Python code is expected.
- Use `__all__` when a module deliberately exposes a public API.
- Do not rely on indirectly imported names as public API unless the re-export is explicitly documented.

### Other

- Use docstrings for modules, public classes, and public functions when they are part of the public API or when project conventions require them.
- Keep docstrings concise, accurate, and aligned with the implemented behavior.
- Treat undocumented interfaces as internal unless project documentation says otherwise.
- Use a single leading underscore for non-public names.
- Do not expose internal names as part of a public API by accident.
- Import public names from the module that actually defines them unless a documented re-export exists.
- Do not generalize framework-specific advice to all Python code.
- Apply framework, library, or runtime-version rules only when the project context confirms they are relevant.

## Perl

### Naming

- Use `snake_case` for local variables and subroutines unless the project uses another convention.
- Use mnemonic identifiers that reveal role and intent.
- Avoid single-letter names except for established Perl conventions such as `$a` and `$b` in sort blocks or very small local scopes.
- Prefer underscore-separated lexical variable names such as `$file_path` or `$retry_count` for longer local identifiers.
- Use normal Perl module names that start with a capital letter unless the module is intentionally pragma-like or the project already uses another convention.
- Use a leading underscore for private package variables or subroutines when it helps distinguish package internals from public API.

### Formatting

- Enforce one coherent Perl layout style for the project.
- Use `perltidy` when it is available and configured by the repository; do not reformat unrelated Perl files.
- Prefer four-space indentation, spaces instead of tabs, one statement per line, whitespace around binary operators, and trailing commas in multiline lists.
- Group related statements into readable paragraphs and separate unrelated code chunks with blank lines.
- Prefer the clearest Perl construct over the shortest construct.
- Avoid clever one-liners in maintained code when an expanded form is easier to read, test, debug, or maintain.
- Parenthesize expressions when precedence, argument binding, or context could be ambiguous to a maintainer.
- Use block `if` statements for non-trivial decisions; reserve postfix `if` for short, obvious, low-risk statements.
- Keep conditions simple, prefer positive phrasing when practical, and make control-flow variations visible.
- Use loop labels only when they clarify multi-level `last`, `next`, or `redo` control flow.

### Errors

- Check the return value of file, directory, process, and system operations.
- Handle failures from `open`, `opendir`, `chdir`, `mkdir`, `system`, `exec`, and similar operations explicitly.
- Include the failed operation, relevant argument, and system error in diagnostics when practical.
- Use lexical filehandles and explicit modes, such as `open(my $fh, '<', $path)`.
- Avoid bareword filehandles and ambiguous two-argument `open`.
- Use list-form `system` or `exec` when invoking external commands and shell interpolation is not required.
- Use `system` instead of backticks when the command output is not needed.
- Do not use backticks in void context.

### Safety

- Enable strictness and warnings in every maintained Perl source file with `use strict;` and `use warnings;`, unless legacy compatibility explicitly prevents it.
- Use `use v5.36;` or newer as a strictness substitute only when the project explicitly supports that minimum Perl version.
- Do not use `-w` or `$^W` as substitutes for lexical warnings because they can affect code outside the current file.
- Limit every `no strict` or `no warnings` relaxation to the smallest possible scope and document why it is required.
- Use `my` for lexical variables by default.
- Avoid symbolic references unless a well-contained metaprogramming pattern requires them.
- Prefer native Perl built-ins and modules over shelling out for ordinary file, text, or process operations.
- Treat external input as untrusted before using it in file paths, shell commands, database queries, HTML output, or security-sensitive contexts.
- Validate, normalize, and constrain untrusted input at the boundary where it enters the program.
- Use DBI placeholders for parameterized database queries.
- Do not interpolate untrusted values into SQL.
- Use allowlists for dynamic SQL identifiers when identifiers cannot be parameterized.
- Use taint-aware patterns for legacy CGI or exposed scripts when the deployment model benefits from taint mode and explicit untainting.

### Tests

- Provide tests for generated or modified Perl behavior.
- Prefer `Test::More` for comparing expected and actual values because it gives useful diagnostics.
- Declare an expected test plan when the number of tests is known.
- Use dynamic test planning only when the test count genuinely depends on runtime data.
- Use `Perl::Critic` and `Test::Perl::Critic` as configurable quality gates when the project uses them.
- Treat Perl::Critic policies as project rules, not universal truth; configure them to match the repository style before enforcing them.

### Idioms

- Prefer three-argument `open`.
- Do not use `grep` or `map` in void context; use `foreach` when the goal is iteration with side effects.
- Keep regular expressions readable with `/x` or `/xx`, whitespace, and comments when patterns become non-trivial.
- Split very complex matching logic into smaller named checks when that improves maintainability.
- Choose regular-expression delimiters that reduce escaping.
- Do not use `/.../` when another delimiter makes slash-heavy or backslash-heavy patterns clearer.
- Keep compact Perl idioms only when they remain easier to verify than the expanded form.

### Other

- Document public Perl modules, scripts, and interfaces with POD.
- Include purpose, synopsis or usage, public subroutines or methods, diagnostics, configuration, dependencies, known limitations, author or contact, and license in POD when applicable.
- Write documentation for common usage before edge cases.
- Keep POD markup, terminology, structure, and tone consistent across the project.
- Prefer named command-line options over fragile positional arguments when a script accepts multiple inputs, outputs, or modes.
- Provide both short and long option forms for user-facing scripts when it improves usability.
- Support standard CLI conventions where relevant, including `-` for standard input or output and `--` as the end of options.


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
- Apply PowerShell formatting only to touched PowerShell files unless a project check requires a broader format pass.

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

- Add PowerShell module structure, logging frameworks, configuration systems, or remoting support only when required by the task or existing project context.
- Treat framework-specific guidance for PowerShell Universal, MSP/RMM tools, enterprise hardening, or hosting platforms as contextual unless the project explicitly uses those environments.
- Stream large inputs instead of loading everything into memory when incremental processing is feasible.

## Windows Batch

### Naming

- Prefer `.cmd` for new Windows NT-based command scripts unless the project convention requires `.bat`.
- Keep `.bat` only for compatibility, legacy behavior, or consistency with existing project files.
- Avoid spaces in Windows Batch script filenames.
- Avoid script names that collide with built-in commands, common executables, or commands expected to be found through `PATH`.
- Use `%~nx0` or `%~n0` when a script must print its own name in usage, help, or diagnostic messages.
- Use local variable names that cannot be confused with system, global, or dynamic environment variables.
- Do not overwrite system, global, or dynamic variables such as `%TEMP%`, `%TMP%`, `%DATE%`, `%TIME%`, `%RANDOM%`, `%ERRORLEVEL%`, `%CD%`, `%PATHEXT%`, or `%COMSPEC%`.
- Use clear constant-style variable names for documented exit codes.

### Formatting

- Start user-facing Windows Batch scripts with `@ECHO OFF`.
- Start non-trivial scripts with `SETLOCAL ENABLEEXTENSIONS` to limit environment side effects and enable command processor extensions.
- Enable delayed expansion only when runtime variable expansion inside loops or parenthesized blocks is required.
- Avoid delayed expansion when processing values that may contain exclamation marks unless the script deliberately handles them.
- Keep functional script code ASCII-only unless the script explicitly configures and documents code page or Unicode handling.
- Write one command per line by default.
- Avoid excessive `&` command chaining.
- Avoid caret line continuations unless they clearly improve readability.
- Indent parenthesized blocks consistently.
- Keep conditionals, loops, and subroutines visually separable with simple spacing.
- Use `REM` for comments that must be safe in all contexts.
- Use `::` only for simple top-level comments.
- Do not use `::` comments inside `FOR` loops or parenthesized blocks.
- Keep user-facing help or usage text concise and reusable when the script accepts options.

### Errors

- Return `0` on success and a non-zero exit code on failure.
- Treat exit codes as part of the script interface.
- Document non-zero exit codes near the top of non-trivial scripts.
- Check critical command failures explicitly.
- For fail-fast behavior, use `command || EXIT /B <code>` or an equivalent checked branch.
- Prefer `EXIT /B` inside scripts and subroutines.
- Do not use plain `EXIT` unless the intention is to close the command processor.
- When checking general failure, prefer explicit non-zero checks over assumptions that every failure code is greater than or equal to `1`.
- Use `IF ERRORLEVEL n` with descending thresholds when testing ranges; use `%ERRORLEVEL% NEQ 0` when an exact non-zero check is required.
- Write diagnostics and errors to STDERR when normal STDOUT may be consumed by another command.
- Fail clearly when required arguments, files, commands, directories, environment variables, or privileges are missing.
- Do not redirect errors to `NUL` when those errors affect control flow or troubleshooting.

### Safety

- Use `%~dp0` for paths relative to the script location.
- Do not use `%CD%` when the intended base path is the script directory.
- Quote paths, filenames, and variable expansions that may contain spaces or special characters.
- Use `SET "name=value"` for string assignments, especially when values may contain spaces or special characters.
- Do not add spaces around `=` in basic `SET` assignments.
- Avoid storing surrounding quote characters inside variable values unless the value semantically includes quotes.
- Quote variables at the point of use instead of storing surrounding quotes in the variable value.
- Validate command-line arguments before processing them.
- Handle missing arguments explicitly.
- Handle unexpected extra arguments explicitly when the script has a fixed interface.
- Handle empty user input explicitly.
- Validate numeric input before using it in `SET /A` expressions.
- Treat user input, environment variables, command output, and file paths as untrusted until validated.
- Sanitize or constrain paths before passing them to destructive commands such as `DEL`, `RD`, `RMDIR`, or `ROBOCOPY /MIR`.
- Do not store credentials, tokens, passwords, API keys, or other secrets in Windows Batch files.
- Do not make automation scripts depend on `PAUSE`.
- Reserve `PAUSE` for manual or demonstration scripts.
- Document required administrator privileges when a script needs elevation.
- Do not silently assume elevation.
- Avoid hidden side effects on the caller environment, current directory, global variables, or external files.

### Tests

- Run Windows Batch scripts from an existing Command Prompt during development so errors and output remain visible.
- For generated or modified scripts, provide a representative `cmd.exe` verification command when execution is practical.
- Exercise the supported help or usage option, such as `/?`, `/h`, `-h`, or `--help`, when that path is affected by a change.
- Exercise missing argument, invalid argument, missing file, and failure-path behavior when those paths are affected by a change.
- Verify scripts that use delayed expansion, parenthesized blocks, redirection, argument forwarding, destructive file operations, or subroutines with representative inputs.
- Verify that expected STDOUT, STDERR, log output, and exit codes match the script contract.
- For automation scripts, test execution without interactive prompts.
- For scripts that may need troubleshooting, verify that log files are initialized, overwritten, appended, or timestamped according to the intended retention behavior.
- Do not claim a Windows Batch script is production-ready unless quoting, argument validation, error handling, exit codes, and verification steps have been addressed.

### Idioms

- Use `%1` through `%9` for positional arguments.
- Use `%0` for the script invocation.
- Use `%*` when forwarding all original arguments.
- Use `SHIFT` when processing more than nine arguments.
- Use `%~1` to remove surrounding quotes from an argument.
- Use `%~f1`, `%~d1`, `%~p1`, `%~n1`, `%~x1`, or related modifiers when path components must be extracted from an argument.
- Use `IF NOT DEFINED var` when checking whether a variable is unset.
- Quote both sides of string comparisons when variables may be empty.
- Use direct quoted comparisons only when comparing actual string values.
- Use `IF /I` only when case-insensitive comparison is required.
- Keep comparisons case-sensitive by default.
- Use `IF EXIST` and `IF NOT EXIST` for filesystem checks.
- Use `FOR` for iterating files, directories, values, ranges, and command output.
- Inside batch files, use `%%I` loop variables, not `%I`.
- Use `FOR /F` deliberately when parsing command output or file lines, and document delimiter or token choices when they are not obvious.
- Use delayed expansion with `!VAR!` when variables must update at execution time inside parenthesized blocks.
- Use `SET /A` only for arithmetic or numeric assignments.
- Use labels plus `CALL :subroutine` only for reusable subroutines.
- Place subroutines after the main logic.
- Ensure the main logic exits before execution can fall through into subroutines.
- End every subroutine with `EXIT /B <code>`.
- Treat subroutine return values as status codes.
- Use STDOUT, files, or caller-provided variables for returned data.
- Do not use exit codes to return business values or parsed data.
- Redirect STDOUT and STDERR deliberately with `>`, `>>`, `2>`, and `2>&1`.
- Use `NUL` only to suppress expected noise.
- Prefer `ROBOCOPY` over `XCOPY` for robust directory copy operations when the target Windows environment supports it.
- When checking `ROBOCOPY`, treat documented success and partial-success exit codes separately from real failure codes.

### Other

- Use Windows Batch for simple Windows automation, command orchestration, file operations, scheduled task wrappers, and low-dependency tasks.
- Prefer PowerShell or another more suitable language for complex logic, typed data handling, object pipelines, REST APIs, or larger maintainability needs.
- Prefer simple, explicit Batch control flow over clever command processor tricks.
- Keep labels and `CALL :subroutine` blocks focused on one clear script responsibility.
- Keep user-facing messages concise, actionable, and consistent.
- Do not generalize rules from Azure Batch, Python integration, GUI automation, POSIX shell, Bash, WSL, or other non-Command-Prompt ecosystems unless they are directly applicable to Windows Batch scripting.

## PCBoard Programming Language

### Naming

- Use `.PPS` as the default extension for PPL source files.
- Do not use `.PPE` as a source extension; `.PPE` is the compiled executable format produced by PPLC.
- Declare variables before use with a documented PPL type: `BOOLEAN`, `DATE`, `INTEGER`, `MONEY`, `STRING`, or `TIME`.
- Start variable names with a letter, then use only letters, digits, and underscores.
- Do not use spaces, hyphens, punctuation, accented characters, or Unicode characters in identifiers.
- Do not rely on letter case to distinguish variables, labels, keywords, or identifiers.
- Use consistent casing only for readability, because case is significant only inside literal strings.
- Keep variable names meaningfully unique within their first 32 characters to avoid compiler-recognized name collisions.
- Name labels by intent and use them only for localized subroutines or exceptional exits.

### Formatting

- Write PPL source as plain ASCII-compatible text suitable for a DOS-era compiler.
- Avoid Unicode punctuation, smart quotes, non-ASCII operators, invisible characters, and editor-specific formatting.
- Keep physical lines short and readable even though PPL source lines may allow much longer text.
- Prefer one clear statement per line over dense one-line code.
- Use explicit `LET variable = expression` assignments when generating code.
- Use parentheses in non-trivial arithmetic, string, or boolean expressions to make precedence explicit.
- Keep generated examples minimal, complete, and compilable.
- Do not place pseudo-code inside PPL code blocks unless it is clearly marked as pseudo-code.
- Document the intended PCBoard and PPLC versions when generated code depends on version-sensitive syntax, functions, or behavior.

### Errors

- Treat PPLC compiler errors as blocking; do not deliver or install a PPE when compilation fails.
- Treat PPLC compiler warnings as defects unless a warning is intentionally accepted and documented.
- When compiling through automation, check PPLC exit status and diagnostics, and distinguish clean success, warnings, missing inputs, missing files, and fatal failures when the compiler exposes enough information.
- After file operations such as `FOPEN`, `FCREATE`, `FAPPEND`, `FGET`, or `FPUT`, check `FERR(channel)` when failure could affect correctness.
- Close every opened file channel explicitly with `FCLOSE` before returning from the routine that opened it.
- Keep file channel usage within the documented `0` through `7` range.
- Avoid complex channel reuse; a routine that opens a channel should normally close the same channel before returning.
- Do not rely on implicit type conversion for correctness-sensitive business logic.
- Make conversions explicit when mixed expression types could change behavior or readability.

### Safety

- Treat user input, file contents, modem input, display text, and PCBoard environment data as untrusted until validated.
- Use typed input statements, explicit input lengths, valid character masks, and appropriate flags when collecting user input.
- Do not accept unrestricted strings when a narrower input format is known.
- Hide passwords and confidential values with `ECHODOTS` or an equivalent supported input flag.
- Do not echo secrets in clear text to the remote or local display.
- Strip PCBoard display or color control sequences, such as `@X` codes, before writing user-facing strings to plain logs when those codes are not meaningful.
- Use `STRIPATX()` when PCBoard color/control code removal is required.
- Do not pass user-controlled text into execution paths, PPE launch paths, or display-control contexts that can interpret PCBoard control sequences.
- Enforce the required PCBoard command security level at installation time through `CMD.LST` or the conference-specific command list.
- Check runtime authorization before executing privileged actions when authorization affects correctness or security.
- For long output, use `STARTDISP` with the appropriate mode and periodically check `ABORT()`.
- When output is aborted, stop printing and call `RESETDISP` before continuing with later display logic.

### Tests

- For any non-trivial PPL change, follow the full lifecycle: write `.PPS`, compile with PPLC, install the generated `.PPE`, then test it in the intended PCBoard context.
- Do not treat successful compilation alone as sufficient validation.
- Test the PPE at the exact intended integration point, such as command, script questionnaire, `PCBTEXT` prompt, display file, or menu replacement.
- Test file-operation success and failure paths when the PPE opens, creates, appends, reads, or writes files.
- Test user abort behavior for long displays that use `STARTDISP`, `ABORT()`, and `RESETDISP`.
- Test input validation, length limits, masks, and confidential-input behavior when the PPE accepts user input.
- Test command security level and runtime authorization behavior when the PPE performs privileged actions.
- Test generated code against the declared target PCBoard and PPLC versions when compatibility matters.

### Idioms

- Treat PCBoard Programming Language as a PCBoard-specific compiled scripting language, not as generic BASIC, batch, or Pascal.
- Prefer PCBoard-native PPEs that customize one clear PCBoard integration point.
- Keep PPEs small, focused, and tied to their intended PCBoard runtime context.
- Match the PPE design to its installation context instead of mixing command, questionnaire, prompt, display-file, and menu responsibilities.
- Prefer structured control flow with `IF`/`ELSEIF`/`ELSE`/`ENDIF`, `WHILE`/`ENDWHILE`, and `FOR`/`NEXT`.
- Reserve `GOTO` for exceptional exits, such as leaving deeply nested logic after a critical error.
- Use `GOSUB` and `RETURN` for repeated logic, and ensure every `GOSUB` path reaches a matching `RETURN`.
- Prefer broadly supported PPL primitives for compatibility-oriented code.
- Avoid version-specific functions unless the target PCBoard and PPLC versions are known to support them.

### Other

- State the operational assumptions for every generated PPL/PPE deliverable.
- Include the assumed PCBoard version, PPLC version if known, installation point, expected file paths, required security level, file channels used, and ANSI/color-code expectations.
- Do not introduce modern abstractions, dependency managers, package layouts, unit-test frameworks, or security models that are not supported by the DOS/PCBoard/PPL environment.
- Explain modern safety concerns separately instead of pretending the original runtime supports modern controls.
- Use secondary sources only for historical or ecosystem context, not as the basis for unsupported technical rules.

## Tcl Eggdrop Scripting

### Naming

- Apply these rules only to Tcl scripts written for Eggdrop bots; do not apply
  them blindly to generic Tcl applications, Eggdrop C modules, or unrelated IRC
  bot frameworks.
- Use a Tcl namespace for non-trivial Eggdrop scripts to avoid collisions with
  Eggdrop globals and with other loaded scripts.
- When a namespace is not practical, prefix script-specific procedures and
  variables with a short, unique script identifier.
- Use clear variable and procedure names that reveal Eggdrop intent, such as the
  bind type, IRC target, configured channel, timer purpose, or permission model.
- Do not rely on naming conventions alone to distinguish strings, lists, arrays,
  dictionaries, or integers; make parsing and data conversion explicit where the
  type affects correctness.
- Avoid generic global procedure or variable names such as `init`, `config`,
  `data`, `user`, or `message` in scripts that may be loaded with other scripts.

### Formatting

- Structure maintained Eggdrop Tcl scripts into clear sections: header, user
  configuration, procedure definitions, bind declarations, and load
  confirmation.
- Include the script name, version, purpose, target Eggdrop version, target Tcl
  version when relevant, and basic usage in the header.
- Keep user-editable settings in one dedicated configuration section near the
  top of classic Tcl scripts.
- For Eggdrop 1.10+ Autoscripts, expose normal user configuration through
  `manifest.json` instead of requiring manual edits to active Tcl code.
- Keep operational code separate from configuration; do not duplicate the same
  configurable value across unrelated code paths.
- Group `bind` declarations so the script behavior can be audited quickly.
- For simple scripts, grouping binds near the top is acceptable when it improves
  readability.
- For larger or riskier scripts, define procedures before registering binds so
  load-time errors are less likely to leave partially active behavior.
- End maintained scripts with a clear `putlog` load message that includes the
  script name and version.

### Errors

- Ensure every `bind` references an existing procedure.
- Ensure every bound procedure uses the exact argument list required by the
  documented Eggdrop bind type.
- Do not invent Eggdrop commands, Tcl commands, bind types, or module-specific
  commands that are not available in the declared target runtime.
- Declare module requirements before using module-specific Eggdrop commands.
- State the minimum Eggdrop and Tcl versions when using version-sensitive
  commands, Autoscript packaging, or behavior that may differ across Eggdrop
  versions.
- Treat load-time failures as operational defects; do not design scripts that
  can silently load with missing procedures, broken binds, or incomplete
  configuration.
- Do not rely on public channel messages for diagnostics; use Eggdrop logging
  commands for runtime visibility.

### Safety

- Prefer the most specific bind that solves the requested behavior.
- Do not use broad message listeners such as `PUBM *` when an exact public
  command bind is sufficient.
- Use Eggdrop bind flags to restrict who may trigger commands whenever the
  access requirement can be expressed with Eggdrop's flag model.
- Do not replace Eggdrop's global, channel, bot, `|`, or `&` flag-mask behavior
  with ad hoc privilege checks unless bind flags cannot express the required
  condition.
- Treat IRC nicknames, idents, hosts, channel names, public messages, private
  messages, topic text, and file contents as untrusted input.
- Do not treat raw IRC text as a Tcl list unless the script intentionally parsed
  it into a Tcl list.
- Use Tcl string commands for raw strings and Tcl list commands only for actual
  Tcl lists.
- Use `putserv` for direct server commands.
- Use `puthelp` for normal channel or user messages.
- Use `putquick` only when faster queued output is justified.
- Avoid `putnow` unless immediate unqueued output is explicitly required,
  because bypassing queues can flood the bot off the IRC server.
- Use `putlog` or `putloglev` for operational diagnostics instead of sending
  debug output to public channels.
- Use `.tcl source script/file.tcl` only in controlled development scenarios
  where `.tcl` is enabled only for trusted users.
- Do not develop or test new scripts directly on important or busy channels.
- When a script creates binds, timers, or persistent state, provide a cleanup
  strategy using `unbind`, `killtimer`, or `killutimer` as appropriate.
- Store timer identifiers returned by `timer` or `utimer` when the timer may
  need to be cancelled later.
- Do not create infinite repeating timers with count `0` unless their lifecycle
  is explicitly managed.

### Tests

- Test new or modified Eggdrop Tcl scripts on a non-critical bot before
  deploying them to active channels.
- Reload classic scripts through the Eggdrop configuration and `.rehash`, or
  restart the bot when the change requires it.
- For controlled development only, verify manual reloads with `.tcl source`
  under restricted access.
- Before presenting generated Eggdrop Tcl code as final, verify that every bind
  has a matching procedure and the correct procedure signature.
- Verify that generated output uses the intended Eggdrop queue: `putserv`,
  `puthelp`, `putquick`, or `putnow`.
- Verify that configurable values are defined once and read consistently.
- Verify that non-trivial scripts use a namespace or a unique script prefix.
- Verify that repeating timers have a defined cancellation or lifecycle
  strategy.
- Verify that the script logs a clear load message with its name and version.
- For Eggdrop 1.10+ Autoscripts, verify that the package contains the Tcl script
  and `manifest.json`, and that the script name, manifest name, and directory
  name are consistent.

### Idioms

- Implement Eggdrop behavior as Tcl procedures triggered by Eggdrop binds.
- Keep bind-specific logic thin; move non-trivial parsing, validation, and
  behavior into named procedures.
- Use `timer` for minute-level scheduling and `utimer` for second-level
  scheduling.
- Use `global` only for variables that are intentionally shared in classic Tcl
  scripts.
- For Autoscripts and namespace-based scripts, prefer Tcl's `variable` command
  over unnecessary `global` statements.
- Keep classic script conventions and Autoscript conventions separate unless
  the target deployment model explicitly requires both.
- Prefer Eggdrop-native commands and documented bind behavior over patterns
  copied from unrelated Tcl or IRC bot frameworks.

### Other

- Prefer official Eggheads or Eggdrop documentation for Eggdrop command and bind
  behavior.
- Use Eggdrop.fr wiki or forum guidance only when it is consistent with
  official Eggdrop documentation.
- Treat existing script repositories, script catalogs, Stack Overflow, Reddit,
  Hacker News, and generic hosting knowledgebase pages as examples or secondary
  context, not as normative sources.
- Do not generalize a rule from one example Eggdrop script into a universal
  coding rule.
- When generating Autoscript packages, include at least the Tcl script and a
  `manifest.json` file.
- Keep script, manifest, and directory names consistent for Autoscript packages.
- Do not require users to edit active code paths for normal configuration.
- Write comments that explain intent, configuration, assumptions, permission
  requirements, queue choices, timer lifecycle, or non-obvious Eggdrop behavior.
- Do not generate comments that merely restate the next Tcl command.

## mIRC scripting language

### Naming

- Use clear alias names that describe the command shortcut, reusable routine, or
  custom identifier behavior.
- Define implementation-only aliases with `alias -l` so they remain local to the
  current script file and are not exposed as public commands.
- Use `/var` for routine-local state and reserve variables created with `/set`
  for state that must intentionally survive beyond the current alias, event, or
  script execution.
- Use clear socket names when raw socket handling is required, so each socket's
  lifecycle and event handlers remain easy to audit.

### Formatting

- Keep aliases small, explicit, and focused on one command shortcut, reusable
  routine, or simple custom identifier behavior.
- Do not generate aliases that call themselves recursively.
- Inside script files, omit leading `/` command prefixes unless they improve
  clarity in an example or are required by the surrounding context.
- Use `//` only when command-line identifier evaluation is intentionally
  required, `.` only when a quiet command is intended, and `!` only when alias
  processing must be bypassed.
- Use `;` for line comments and `/* ... */` for block comments.
- Comment non-obvious event triggers, risky commands, identifier evaluation,
  file access, socket handling, and intentional use of `halt`, `goto`, or global
  state.

### Errors

- Validate required alias parameters before using them, using required-parameter
  forms such as `$$1` or explicit guards before commands that depend on user
  input.
- Use positional parameters such as `$1`, `$2`, and `$2-` deliberately and only
  where their meaning is clear at the call site.
- Treat identifiers as runtime expressions that may return `$null`; check for
  `$null` before branching, formatting output, or passing identifier results to
  commands.
- For non-trivial scripts that need recovery or cleanup, define an `:error`
  label, read `$error`, handle the failure, and call `/reseterror` before
  continuing or returning.
- When using file commands, check file access errors with
  `$fopen(<handle>).err`, `$ferr`, or the relevant mIRC file-error identifier
  because file access failures do not necessarily halt execution.
- When using sockets, check `$sockerr` after socket commands and before
  processing socket events.

### Safety

- Keep remote events narrow by using precise levels, match text, and locations.
- Avoid broad catch-all private or channel message handlers unless the behavior
  is intentionally global and documented.
- Do not generate opaque, obfuscated, or unexplained remote scripts; generated
  mIRC scripts must remain readable and reviewable before loading.
- Avoid generating file server or DCC exposure unless explicitly requested.
- If file server behavior is required, restrict the exposed home directory,
  document the risk, and avoid exposing private or confidential files.
- Use raw sockets only for scripts that genuinely need raw network connections;
  do not generate socket code for ordinary IRC automation.
- Close files after use with `/fclose`, and close sockets after use when the
  socket lifecycle is complete.
- Avoid unintended double evaluation when assigning literal expression-like
  content; use non-evaluating forms such as `/set -n` or `/var -n` when the
  value must remain literal.

### Tests

- Verify generated mIRC scripts against the official mIRC Help behavior for the
  commands, identifiers, events, file handling, hash tables, sockets, and script
  features used.
- Test aliases with missing, empty, and multi-word parameters when positional
  parameters, required parameters, or `$2-` are used.
- Test `$null` results from identifiers before approving branches or output that
  depends on identifier values.
- Test file access success and failure paths, including cleanup paths that must
  call `/fclose`.
- Test socket success and failure paths when socket code is generated, including
  `$sockerr` handling and socket closure.
- Verify that remote event handlers match only the intended levels, text, and
  locations.
- Verify that generated hash-table logic does not depend on item storage, save,
  or load order.

### Idioms

- Prefer structured control flow with `if`, `elseif`, `else`, `while`, `break`,
  and `continue` for normal logic.
- Avoid `goto` except for simple, clearly bounded labels where structured flow
  would be less clear; document every intentional `goto` use.
- Use `/return [value]` when an alias or custom identifier must return a value
  to its caller through `$result`.
- Use `/halt` only when the intended behavior is to stop the current script and
  prevent further processing.
- Use hash tables for large keyed data that needs efficient storage and lookup,
  but never rely on hash table item order.
- Use `$calc()` for intentionally complex calculations.
- Enable big-float calculations only for scripts that require very large numeric
  calculations, because big-float calculations are slower than normal
  calculations.

### Other

- Treat official mIRC Help semantics as the primary source of truth for mIRC
  scripting behavior.
- Do not treat editor completion files, autocomplete snippets, historical
  articles, forums, or examples as authoritative language specifications.
- Use autocomplete data only as editor-support context for discovering possible
  command names or parameters, never as a replacement for official mIRC
  documentation.
