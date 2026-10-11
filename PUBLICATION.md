# Publication notes

Published from the completed `DeadlineBench-live-pilot-and-task-suite.zip` research bundle on 11 October 2026.

Source archive SHA-256:

```text
e303c830f7189cd9d484271853c9a42bad12fcc35e32091ec9c31c69118b6095
```

Both the outer archive and nested six-task ZIP passed ZIP integrity checks before extraction. The task suite is available as browsable files and as its unchanged ZIP. All 64 file hashes in the suite manifest and all 38 file observations across 13 pilot snapshots were checked against the extracted bytes.

## Changes for public release

- Two historical grading utilities use repository-relative paths in place of absolute grading workspace paths.
- Nine grading JSON files replace the absolute Python interpreter path in recorded commands with `python3`. This is a path redaction, not a newly executed command. Arguments, output, exit status, timing, limits, scores, and evidence hashes are unchanged.
- Two passages in the market-validation report replace session-specific authorization/request language with public research-status wording. The lack of customer validation and commercial evidence remains explicit.
- The repository README, these notes, a change record, and a small `.gitignore` were added.

[publication_changes.json](publication_changes.json) lists each modified source file, the reason, and its original and published SHA-256. No task input, answer key, locked rubric, participant artifact, snapshot manifest, condition mapping, or timing-validation record was changed. The original outer ZIP is not republished because it contains the unsanitized paths.

Outgoing text, scripts, JSON, CSV, and the nested archive were reviewed for credentials, personal machine paths, internal thread identifiers, private request context, and hidden operational instructions. No credentials or internal thread identifiers were found. Task prompts and evaluator instructions remain part of the published research materials.

## Scope of this release

This is publication of existing research. No new agent trials, provider calls, customer outreach, hosted workflows, or deployments were performed. The saved independent-grader reproduction records are prior evidence; their executions were not repeated during publication.

The pilot has seven runs on one synthetic task. The 300-second assignment checkpoints are not independent shorter-budget trials. Neither a causal policy benefit nor a model ranking is established. Only frozen on-time artifacts receive credit; the missing short-budget brief remains excluded.
