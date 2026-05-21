# RELEASE_RULES.md

## Purpose

This file defines Git tag creation rules for tags created by an AI coding
agent.

## Scope

Apply these rules before creating any Git tag.

## Repository Readiness and Integrity

- Do not create the tag until the repository readiness checks in this section
  have passed or any skipped check has been reported to the user with the
  reason it was skipped.
- Inspect the local repository state immediately before creating the tag with
  `git status --short --branch` or an equivalent Git status command.
- Do not create the tag while Git reports unresolved merges, unmerged paths,
  rebases, cherry-picks, bisects, or any other in-progress operation that could
  make the tag target ambiguous.
- Do not create the tag while the working tree contains uncommitted changes or
  untracked files, unless the user explicitly approves creating the tag despite
  those reported files.
- Run `git fsck --full` before creating the tag to verify local repository
  object integrity.
- Do not create the tag if any repository integrity check fails.
- Identify the exact commit SHA that the tag will point to before creating the
  tag.
- If commit status checks, CI results, branch protection, or hosted review
  checks are required for the tag target, inspect them before creating the tag.
- Do not claim that commit status checks, CI results, branch protection, or
  hosted review checks are valid unless they were actually inspected.
- If required remote or hosted checks cannot be inspected from the current
  environment, report that limitation to the user before creating the tag.

## Version Rules

- Use strict SemVer for version numbers.
- Use the `MAJOR.MINOR.PATCH` version format unless a valid SemVer pre-release
  or build metadata identifier is explicitly required.

## Bump Rules

- Given a version number `MAJOR.MINOR.PATCH`, increment `MAJOR` when making
  incompatible API changes.
- Given a version number `MAJOR.MINOR.PATCH`, increment `MINOR` when adding
  functionality in a backward-compatible manner.
- Given a version number `MAJOR.MINOR.PATCH`, increment `PATCH` when making
  backward-compatible bug fixes.
- Use pre-release labels and build metadata only as valid SemVer extensions to
  the `MAJOR.MINOR.PATCH` format, and only when they are explicitly required.
- Before creating any tag, validate the selected version number with this exact
  regular expression. Validate the version number without the leading lowercase
  `v` tag prefix:

  ```regex
  ^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$
  ```

- Do not create the tag if the selected version number fails the regular
  expression validation.

## Remote Tag Rules

- When a tag will be pushed to a remote repository, inspect the remote tags
  before selecting the version and again immediately before pushing the tag.
- Do not push the tag if the same tag already exists in the remote repository.
- If remote SemVer tags exist, include them when identifying the highest
  existing SemVer version for the requested bump type.
- Stop and ask before creating or pushing the tag if the selected local version
  is lower than the highest matching remote SemVer version, equal to an
  existing remote version, or otherwise conflicts with the version required by
  the requested bump type.

## Tag Rules

Before creating a tag:

- Inspect existing Git tags.
- Consider only tags matching a lowercase `v` prefix followed by a strict
  SemVer version, such as `v1.0.1`.
- If no matching tags exist, ask for the initial strict SemVer version before
  creating a tag, then use that version as the tag version.
- If matching tags exist, identify the highest existing SemVer version and
  increment it using the requested SemVer bump type: major, minor, or patch.
- If matching tags exist and no bump type is specified, ask before creating the
  tag.
- Create the tag using a lowercase `v` prefix followed by the selected strict
  SemVer version.
