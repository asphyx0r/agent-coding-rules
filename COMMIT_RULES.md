# COMMIT_RULES.md

## Purpose

This file defines commit message rules for commits created by an AI coding
agent.

## Scope

Apply these rules before creating any commit.

## Privacy Guard

- Do not create the commit until every file included in the commit has passed
  this privacy review.
- Never commit a `.env` file containing real environment values, secrets,
  credentials, private URLs, tokens, passwords, or API keys.
- Commit only `.env` templates that contain placeholders or documented example
  values.
- Before committing, review each file included in the commit in its entirety
  for sensitive data, including passwords, API keys, tokens, private keys,
  credentials, private URLs, and real environment-specific values.
- Never commit a file that contains sensitive data.
- The presence of sensitive data must block the commit.
- Notify the user when sensitive data is found.
- When in doubt about whether data is sensitive, ask the user to decide.
- When in doubt about whether data is sensitive, never decide alone that the
  commit is valid.
- A file containing sensitive data must be modified to remove or replace that
  data before it can be committed.

## Commit Message Rules

- Use `.gitmessage` as the commit message template or style reference if it
  exists in the repository.
- Write all commit message content in English.
- Keep the commit subject line at 50 characters or fewer.
- Separate the subject from the body with a blank line.
- Wrap all commit body lines at 72 characters or fewer.
- In the body, briefly describe which files or areas changed and why.
