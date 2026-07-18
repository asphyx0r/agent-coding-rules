# Repository Migration

This document records the migration of the maintainer's canonical working copy
from a Google Drive synchronized directory to a local NTFS directory.

## Reason

The repository was moved to avoid Windows access-control failures and
`helper_unknown_error` launcher failures observed when Git and Codex operated
through the synchronized Google Drive directory. The migration changes only the
maintainer's storage location. The GitHub repository, history, branches, tags,
and project contents remain unchanged.

## Locations

| Role | Path | Status |
| --- | --- | --- |
| Previous working directory | `G:\Mon Drive\Code\Docs\agent-coding-rules` | No longer used under this name |
| Retained safety source | `G:\Mon Drive\Code\Docs\DEPRECATED-agent-coding-rules` | Retained for recovery |
| Canonical working directory | `C:\codex\agent-coding-rules` | Active reference |
| Migration evidence | `C:\codex\_migration-logs\agent-coding-rules-20260718-202049-081-0656b9a3` | Retained for audit |

## Actions Performed

1. Verified the source repository topology, worktree state, refs, index, object
   database, branches, tags, remote configuration, and unsupported Git
   features before copying.
2. Copied the complete repository through a staging directory with Robocopy,
   including the `.git` directory and all working-tree files.
3. Generated content manifests before and after the copy and compared every
   entry by relative path, type, size, timestamp, and SHA-256.
4. Ran `git fsck --full --strict` against the source, staging, and destination
   repositories.
5. Validated the staged copy before renaming the original directory and
   promoting the local destination.
6. Recalculated the retained source manifest after the rename and confirmed it
   still matched the final migration manifest.
7. Compared `HEAD`, the index, local and remote branches, and all local and
   remote tags between the retained source and the local destination.
8. Activated the versioned local hooks with
   `git config core.hooksPath .githooks`.
9. Removed confirmed orphaned read-only Git processes after verifying that
   they had no parent process and held no Git lock.
10. Installed PowerShell 7.6.3 in the maintainer profile while retaining
    Windows PowerShell 5.1 as a validated fallback for the migration script.
11. Corrected the external migration script so Robocopy exit codes are logged
    as integers and future migrations validate the source again after the
    final rename.

## Validation Evidence

- Nine migration manifests contained 754 entries and shared the SHA-256
  `386DAE088E2B8DAAA68B39AB8CBA6EBC0B971CF9999CD21FE734B3133A0F5E3E`.
- Robocopy transferred 552 directories, 202 files, and 883,883 bytes without
  failures, mismatches, or unexpected extra entries.
- Source, staging, and destination integrity checks completed successfully.
- The retained source and local destination had identical `HEAD` trees and
  indexes.
- The local branch, its remote-tracking branch, and the GitHub branch resolved
  to commit `7c9f279d7e2bd23568f3cf1c1476e9cccfe66424` at migration validation time.
- All 77 local tags matched their remote counterparts, including peeled
  annotated tag objects.
- The repository was neither shallow nor bare and used no alternate object
  store, graft, replace ref, nested repository, reparse point, or Git LFS
  storage.
- The reported dangling trees and blobs are unreferenced historical objects,
  not repository corruption.

## Operating Decision

`C:\codex\agent-coding-rules` is the canonical maintainer working directory for
future changes, commits, tags, and pushes. The retained Google Drive source and
migration logs should remain available until the maintainer explicitly removes
them after a successful post-migration push and remote verification.

Do not run `git gc` or `git prune` on the retained source while maximum recovery
coverage is required.
