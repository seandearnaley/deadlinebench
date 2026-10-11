# DeadlineBench: six offline screening tasks

A small synthetic screening set for testing useful work under a deadline. Two evidence-synthesis briefs, two CSV decision reports, and two small Python repairs. All people, organizations, figures, and operational records are invented. No network, paid APIs, packages, external writes, or user-machine access is needed.

Every task states exactly three mandatory requirements (30/25/15 points) and three useful optional items (10 each). Each cutoff is scored independently from files that already exist in output/. A short correct partial artifact earns its specified points. Research and decision tasks have no hidden preferred recommendation. The code cases explicitly use category-level contract pass/fail scoring. These categories are screening diagnostics, not a calibrated leaderboard or a claim that different task types have equal difficulty.

## Cases
- research_01: Choose a multilingual support-search pilot from conflicting proposals, handling trials, independent answer audits, costs and implementation constraints.
- research_02: Choose a parcel mis-sort intervention from an operational trial, pooled-versus-route evidence, audits, implementation costs and labor constraints.
- data_01: Allocate two additional support shifts from an overlapping 670-row snapshot export; calculate SLA results, queue risk, cleaning audit and cautious alternatives.
- data_02: Review promotional contribution from orders, partial refund events and marketing spend; compare channels and assign a constrained hypothetical $2,000 test budget.
- code_01: Repair a 62-line daily service-window helper: parsing, merging and duration; optional membership, gaps and formatting.
- code_02: Repair a 61-line warehouse CSV helper: parsing, reconciliation and usable stock; optional shortages, export and transfers.

## Separation and freezing
participant_inputs/ contains only instructions and source inputs. evaluator_only/ contains answer keys, fixed rubrics, test cases and validation evidence. Give the participant a fresh copy of one task's participant directory. Do not expose evaluator_only/, the manifest's evaluator hashes, other tasks, or prior answers in its task workspace. Separation by directory is not a security boundary; enforce restricted task workspaces when benchmark integrity requires it. The participant writes only output/ and leaves inputs unchanged.

MANIFEST.json lists prompts, output contracts and SHA-256 digests. Digests lock the files as delivered. data_01 participant inputs and its weighted rubric were frozen before the initial instrumentation pilot. USABLE_CORE_LOCKED.txt adds a separate preregistered flag with unchanged weights. Do not modify inputs, rubrics or flags after viewing participant outputs; changes require a new version and fresh trials.

## Deadline/snapshot use
Nominal cutoffs are 90, 180 and 300 seconds. Keep the actual deadline instruction consistent with the experimental condition. A 300-second task with 90/180/300 snapshots measures trajectories under a long deadline; it is not equivalent to three independently assigned deadline budgets. Compare matched conditions using the same task, input version, model, tool access and delivery protocol.

Start an independent monotonic observer clock when the task is actually delivered to an admitted participant; record queued/admission delay separately. Snapshot output/ at each cutoff, record timestamps and file hashes, and grade each immutable snapshot. Do not use later files or unsaved chat answers to improve an earlier score. If the participant finishes before a cutoff, its last saved artifact remains the artifact at that cutoff. Use atomic replacement when saving to avoid partially written JSON/modules. Do not inspect outputs before criteria are frozen.

Report six category scores, total, mandatory-category completion and highest-value missing work. For data_01 additionally report the locked usable-core flag's three booleans and their AND. Weighted score and usable-core status serve different purposes. Record missing outputs, invalid JSON/import failures and evaluator timeouts honestly. No optional work is required for usable core.

## Minimal evaluation
Python 3.10+ standard library suffices. From this package:

    python evaluator_only/evaluate.py data_01 /absolute/path/to/snapshot/output

Use any of the six IDs. Research dispatch only reports whether a saved report exists and points to its human rubric; synthesis is not reliably machine-scoreable. Data checks report exact numeric evidence (61 or 64 possible numeric points), not the whole 100-point human judgment; recover correct numbers from prose when the JSON is missing. Code checks return a deterministic six-category total. Checks use only behavior explicitly described in the participant prompt. The dispatcher adds a 15-second limit, so hung candidate code is an inconclusive/error result to review, never an invented success.

Run participant scripts or repair modules only in a disposable, offline, restricted participant/evaluation environment with no secrets. The supplied Python checks are evaluators, not a security sandbox. Use the human rubrics for methods, decisions, limitations, evidence traceability and reproducibility. Data validation used independent SQLite/integer-cent core aggregates plus numeric positive controls. Code VALIDATION.json files record buggy=0, mandatory-only=70, complete=100, and missing/syntax=0 controls. Research validation records verify packet arithmetic and source references.

No observer, agent orchestrator, web app or repository implementation is included. This package is the task set and a small checking aid.
