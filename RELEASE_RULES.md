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
