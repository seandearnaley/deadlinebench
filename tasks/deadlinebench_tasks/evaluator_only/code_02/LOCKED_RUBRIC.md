# Locked rubric: code_02, version 1

Evaluator-only. Do not disclose this folder or its contents to participants. All values are synthetic. This rubric is locked before trials and applies identically to every model, deadline condition, and saved snapshot.

Run `python checks.py /path/to/snapshot/output` in a separate process with the benchmark's execution limit. It imports only the submitted `stock_csv.py`, writes no snapshot files, and prints deterministic JSON category points and failure details. A missing/unloadable module earns zero. Maximum 100 points. Evaluate the same script at 90, 180, and 300 seconds; do not use a later snapshot to repair an earlier result. Any execution timeout is a failed evaluation, not a successful partial import.

| Category | Points | Full-credit behavior and expected answer |
| --- | ---: | --- |
| M1 CSV parsing | 30 | Use strict standard CSV parsing, remove only the leading BOM, skip all-blank rows, normalize a unique three-field header, trim data, enforce nonempty identity fields and signed ASCII integer syntax, return records in input order, and translate invalid inputs/CSV errors to ValueError. Header order/BOM/CRLF/quoted comma/quoted newline/blank/zero and invalid header/row/quantity/quote/type cases all pass. |
| M2 Reconciliation | 25 | Add quantities to each (sku, location) key instead of overwriting them; retain zero and negative totals. Repeated keys, distinct locations/SKUs, empty/generator, and non-mutation cases all pass. |
| M3 Availability | 15 | Sum max(per-location net, 0) only for the requested SKU; reconcile before clamping. Separate deficits, repeated adjustments, other SKUs, absent SKU, generator, and non-mutation cases all pass. |
| O1 Deficits | 10 | Reconcile, retain negative keys only, negate net quantity, and sort tuples by SKU then location. Repeated keys, cancelled deficits, empty/generator, and non-mutation cases all pass. |
| O2 Export | 10 | Use standard CSV quoting with a fixed header and line terminator \n, preserve row/field order, and include final terminator. Comma/quote/newline fields, zero/negative quantities, empty/generator, and non-mutation cases all pass. |
| O3 Transfer | 10 | Validate arguments and reconciled source availability; materialize and shallow-copy each input record, then append exactly the two signed adjustment rows. Exact-availability, repeated source rows, generator, independent returned dictionaries, insufficient stock, invalid quantity/identity/same-location, and non-mutation cases all pass. |

Each category's checks are all-or-nothing, with no subjective or unlisted bonuses and no cross-category cap. Functionality is scored from runnable saved output. Optional report notes, implementation style, strategy claims, and the original buggy source earn no points. File immutability and snapshot collection are handled by the outer benchmark protocol, not by an extra hidden quality criterion.

The hidden examples test only the participant prompt. The rubric is a concise description of correct repairs, not a prescribed implementation: any standard-library implementation meeting the public contracts is acceptable. Do not alter weights or checks after inspecting participant performance.
