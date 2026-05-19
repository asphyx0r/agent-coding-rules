# RELEASE_RULES.md

## Purpose

This file defines Git tag creation rules for tags created by an AI coding
agent.

## Scope

Apply these rules before creating any Git tag.

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
- When a tag will be pushed to a remote repository, inspect the remote tags
  before selecting the version and before pushing the tag.
- Do not push the tag if the same tag already exists in the remote repository.
- If remote SemVer tags exist, include them when identifying the highest
  existing SemVer version for the requested bump type.
- Stop and ask before pushing if the selected local version is lower than the
  highest matching remote SemVer version, equal to an existing remote version,
  or otherwise conflicts with the version that should result from the requested
  bump type.

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
