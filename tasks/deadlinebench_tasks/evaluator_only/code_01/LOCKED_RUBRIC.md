# Locked rubric: code_01, version 1

Evaluator-only. Do not disclose this folder or its contents to participants. All values are synthetic. This rubric is locked before trials and applies identically to every model, deadline condition, and saved snapshot.

Run `python checks.py /path/to/snapshot/output` in a separate process with the benchmark's execution limit. It imports only the submitted `service_windows.py`, writes no snapshot files, and prints deterministic JSON category points and failure details. A missing/unloadable module earns zero. Maximum 100 points. Evaluate the same script at 90, 180, and 300 seconds; do not use a later snapshot to repair an earlier result. Any execution timeout is a failed evaluation, not a successful partial import.

| Category | Points | Full-credit behavior and expected answer |
| --- | ---: | --- |
| M1 Clock parsing | 30 | Enforce an exact five-character ASCII HH:MM representation, reject out-of-range fields and nonstrings with ValueError, then compute 60 × hour + minute. Successful boundary and interior examples and invalid format/range/type cases all pass. |
| M2 Window merging | 25 | Validate shape, integer types excluding bool, and day bounds. Copy and sort windows, then merge when the next start is no greater than the current end, using the greater end. Nested, touching, repeated, generator, empty, and non-mutation cases all pass. |
| M3 Coverage duration | 15 | Measure the validated union rather than summing raw intervals. Empty/generator/nested coverage, invalid intervals, and non-mutation cases all pass. |
| O1 Membership | 10 | Validate minute and all windows; return actual bool using start <= minute < end. Empty, boundary, generator, invalid type/range, and invalid later interval cases all pass. |
| O2 Gaps | 10 | Validate bounds and windows, merge/clip covered intervals, and emit every positive-length hole, including leading/trailing holes. Empty, equal-bounds, outside-coverage, generator, and invalid bounds/windows cases all pass. |
| O3 Formatting | 10 | Validate non-bool integer in 0..1440 and format both fields with two digits; 1440 yields 24:00. Boundary/interior and invalid type/range cases all pass. |

Each category's checks are all-or-nothing, with no subjective or unlisted bonuses and no cross-category cap. Functionality is scored from runnable saved output. Optional report notes, implementation style, strategy claims, and the original buggy source earn no points. File immutability and snapshot collection are handled by the outer benchmark protocol, not by an extra hidden quality criterion.

The hidden examples test only the participant prompt. The rubric is a concise description of correct repairs, not a prescribed implementation: any standard-library implementation meeting the public contracts is acceptable. Do not alter weights or checks after inspecting participant performance.
