# Deadline screening: blinded artifact grading

## Results

Weighted rubric score and usable core are separate. Numeric checker: **61/61 for all seven sets**, which is evidence, not the final grade.

| Label | Cutoff (s) | M1 /30 | M2 /25 | M3 /15 | O1 /10 | O2 /10 | O3 /10 | Total /100 | Core M1/M2/M3 | Usable core |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| A | 90 | 30 | 25 | 15 | 10 | 10 | 10 | 100 | pass / pass / pass | true |
| A | 180 | 30 | 25 | 15 | 10 | 10 | 10 | 100 | pass / pass / pass | true |
| A | 300 | 30 | 25 | 15 | 10 | 10 | 10 | 100 | pass / pass / pass | true |
| B | 60 | 30 | 25 | 15 | 10 | 10 | 10 | 100 | pass / pass / pass | true |
| C | 90 | 30 | 25 | 15 | 10 | 10 | 10 | 100 | pass / pass / pass | true |
| C | 180 | 30 | 25 | 15 | 10 | 10 | 10 | 100 | pass / pass / pass | true |
| C | 300 | 30 | 25 | 15 | 10 | 10 | 10 | 100 | pass / pass / pass | true |
| D | 90 | 30 | 25 | 15 | 10 | 10 | 10 | 100 | pass / pass / pass | true |
| D | 180 | 30 | 25 | 15 | 10 | 10 | 10 | 100 | pass / pass / pass | true |
| D | 300 | 30 | 25 | 15 | 10 | 10 | 10 | 100 | pass / pass / pass | true |
| E | 60 | 30 | 12 | 7 | 8 | 6 | 8 | 71 | pass / fail / fail | false |
| F | 60 | 30 | 25 | 15 | 10 | 10 | 10 | 100 | pass / pass / pass | true |
| G | 60 | 30 | 25 | 15 | 10 | 10 | 10 | 100 | pass / pass / pass | true |

A/C/D cutoff rows repeat the same within-label artifact hashes. They are not independent executions or improvements. B/E/F/G have only 60-second snapshots. All observed freezes were between nominal cutoff +0.0066 and +0.0790 seconds; hashes match manifests and all artifacts were reported stable during copying.

## Method and limits

Seven distinct blinded saved artifact sets across 13 nominated snapshots; only frozen input pack, locked rubric/key/checker, and saved snapshots used as scoring evidence. No later report credit. No model ranking or causal treatment inference.

Correct saved executable formulas count as explicit definition/method evidence under “grade content wherever saved.” This is applied consistently to all sets; it does not create prose recommendation, caution, interpretation, or run-instruction credit.

No global missing-report penalty beyond the rubric. Missing report is separately flagged and missing content earns zero only for its sub-item.

Inspected every participant script before execution. Copied supplied input and saved output into disposable /tmp workspaces, removed only copied metrics, reconstructed once per unique hashset. No original snapshot/output writes. No packages installed or network/paid calls.

Actual enforced limits per participant reproduction: 15-second wall timeout, 5-second CPU soft/hard limits, 256 MiB address space, 10 MiB file size, 128 open descriptors. Python ran with -I -S. An audit hook denied socket events and subprocess/system execution; inspected participant scripts had no network operations. All runs exited 0, in 0.036–0.046 seconds wall time, without timeouts. Copied input and original snapshots remained unchanged. Full saved JSON equality, not merely correct mandatory counts, was established.

Only supplied-data reconstruction, not adversarial or broader generalization tests. C counts all pre-April production IDs as March; F tests month==3 without year. Both are correct on supplied data, which contains March/April 2026 only; no unrequested robustness penalty. All seven scripts exited 0 and reconstructed the full saved JSON exactly.

**Blinding limitation:** Condition mapping, original-run directories, original-thread files and condition-label files were not opened. One incidental internal live-agent listing exposed generic completed-run summaries without a blinded-label mapping. This weakens strict process blinding; those summaries were not used as grading evidence. No further agent listings were made.

No model ranking, deadline-treatment causality, or population-wide performance claim is supported by this grading.

## Report length

Conservative whitespace token counts include Markdown table syntax and are still below 700: A 676, B 643, C 644, D 666, F 646, G 636. E has no report; its word count is unavailable, not zero.

## Exact evidence and sub-item decisions

### A: 100/100; usable core true

Applies to cutoff(s): 90, 180, 300 seconds. Confidence: high.

**M1: 30/30.** tickets: 5; breached: 5; breach rate pct: 5; responded only median: 5; unanswered: 5; unresolved: 5.
- `../blinded/A/90/report.md` lines 5-9: 420 tickets; 206 breaches (49.05%); 58 unanswered; 172 unresolved; median 4.23 among 362 responded; all qualifying April denominator; 1/4/12 elapsed-hour priority SLAs, strict greater-than, unanswered age to instant.
- `../blinded/A/90/analyze.py` lines 24-41,47-56: Creation-to-first-reply or cutoff; responded-only median; unanswered nonblank test; unresolved retained status != resolved; April arrival filtering.

**M2: 25/25.** queue facts: 12; exactly two whole shifts: 2; real risk priority: 3; other queues tradeoff: 2; capacity incident uncertainty: 2; feasible specialist generalist: 2; concrete post trial check: 2.
- `../blinded/A/90/report.md` lines 3,11-19,44-46: Technical 2, Billing 0, Account 0; available specialist can cover both whole shifts. Queue counts/rates are correct. Technical largest risk; Billing coverage opportunity cost; Account unresolved count is not first-response risk. No tickets-per-shift forecast; incident fix uncertainty; log arrivals, priority and actual shift hours, matured-cohort same-definition check and spillover.

**M3: 15/15.** audit counts and order: 5; as of unequal age limitation: 4; observational causality caution: 4; april cohort and instant: 2.
- `../blinded/A/90/report.md` lines 30,42-46: 670 raw -> exclude 11 cutoff rows -> 576 latest eligible IDs -> exclude 16 tests -> 140 March -> 420 April. Recent unanswered tickets have less time to exceed SLA; explicit as-of instant; staffing causality cannot be established and incident disappearance cannot be assumed.

**O1: 10/10.** weekly ticket counts and rates: 8; cautious interpretation: 2.
- `../blinded/A/90/report.md` lines 23-30: 83/57.83%; 115/44.35%; 90/51.11%; 132/46.21%. Rates fluctuate; final bucket nine days and recent tickets less mature.

**O2: 10/10.** segment ticket counts and rates: 6; useful comparison: 2; mix caution or noncausal observation: 2.
- `../blinded/A/90/report.md` lines 32-38: Enterprise 85/51.76%; Small business 158/47.47%; Consumer 177/49.15%. Only 4.29 percentage-point spread; queue/priority mix prevents segment-effect conclusion.

**O3: 10/10.** reconstructs submitted mandatory figures: 6; cleaning metric semantics: 2; valid saved run instruction: 2.
- `../blinded/A/90/report.md` lines 48: python output/analyze.py input
- `../blinded/A/90/analyze.py` lines 3-91: Standard-library script, correct semantics; disposable reconstruction exactly equals saved metrics JSON.

Core reasons:
- M1: All values and definitions are correct in saved report and/or code.
- M2: All queue facts plus exactly two feasible whole shifts justified by true risk.
- M3: All audit counts/order, specific unequal-age limitation and clear staffing/incident noncausal caution.

Reproduction evidence: `reproduction/A.json`; deterministic numeric detail: `reproduction/A_numeric_checker.json`.

### B: 100/100; usable core true

Applies to cutoff(s): 60 seconds. Confidence: high.

**M1: 30/30.** tickets: 5; breached: 5; breach rate pct: 5; responded only median: 5; unanswered: 5; unresolved: 5.
- `../blinded/B/60/report.md` lines 2,10,18,21: All six correct values, April arrivals as of 2026-05-01 00:00 UTC, all-ticket denominator, strict elapsed 1/4/12-hour SLA including overdue unanswered, responded-only median and retained unresolved-status definition.

**M2: 25/25.** queue facts: 12; exactly two whole shifts: 2; real risk priority: 3; other queues tradeoff: 2; capacity incident uncertainty: 2; feasible specialist generalist: 2; concrete post trial check: 2.
- `../blinded/B/60/report.md` lines 5-7,12-18,42: Exactly two indivisible Technical specialist shifts, correct three-queue comparison, real largest Technical burden, explicit Billing/Account trade-off, unmeasured shift productivity and incident attribution, priority/arrival-mix post-trial check.

**M3: 15/15.** audit counts and order: 5; as of unequal age limitation: 4; observational causality caution: 4; april cohort and instant: 2.
- `../blinded/B/60/report.md` lines 21,31,42-44: All five audit counts and correct order; pre-cutoff filtering prevents historical-state replacement. Recent unanswered arrivals have less time to breach. Observational comparison cannot prove causation; fix effect not established at line 5.

**O1: 10/10.** weekly ticket counts and rates: 8; cautious interpretation: 2.
- `../blinded/B/60/report.md` lines 24-31: All four correct April-arrival weekly counts/rates; unequal final bucket and unequal-age/mix caution.

**O2: 10/10.** segment ticket counts and rates: 6; useful comparison: 2; mix caution or noncausal observation: 2.
- `../blinded/B/60/report.md` lines 33-39: All three correct segment counts/rates; Enterprise highest rate and Consumer largest breach count; priority/queue mix and no segment-effect inference.

**O3: 10/10.** reconstructs submitted mandatory figures: 6; cleaning metric semantics: 2; valid saved run instruction: 2.
- `../blinded/B/60/report.md` lines 46: python3 output/analyze.py input/ticket_export.csv output/metrics.json
- `../blinded/B/60/analyze.py` lines 2-26: Standard-library script, correct cleaning and metric semantics; full saved JSON reproduced exactly.

Core reasons:
- M1: All values and definitions are correct in saved report and/or code.
- M2: All queue facts plus exactly two feasible whole shifts justified by true risk.
- M3: All audit counts/order, specific unequal-age limitation and clear staffing/incident noncausal caution.

Reproduction evidence: `reproduction/B.json`; deterministic numeric detail: `reproduction/B_numeric_checker.json`.

### C: 100/100; usable core true

Applies to cutoff(s): 90, 180, 300 seconds. Confidence: high.

**M1: 30/30.** tickets: 5; breached: 5; breach rate pct: 5; responded only median: 5; unanswered: 5; unresolved: 5.
- `../blinded/C/90/report.md` lines 5-9,36: All six correct values and required April-arrival/all-ticket SLA/overdue-unanswered/responded-only median definitions; unresolved status definition explicit.

**M2: 25/25.** queue facts: 12; exactly two whole shifts: 2; real risk priority: 3; other queues tradeoff: 2; capacity incident uncertainty: 2; feasible specialist generalist: 2; concrete post trial check: 2.
- `../blinded/C/90/report.md` lines 3,11-19,38-40: Exactly two whole Technical shifts covered by specialist, all three queues correctly compared, true high Technical risk, feasible Billing alternative and Account trade-off, no clearance estimate, incident uncertainty and priority/age-adjusted post-trial check.

**M3: 15/15.** audit counts and order: 5; as of unequal age limitation: 4; observational causality caution: 4; april cohort and instant: 2.
- `../blinded/C/90/report.md` lines 30,36-40: 670 -> exclude 11 -> 576 retained IDs -> exclude 16 tests -> 140 March; April 1 inclusive/May 1 exclusive. Recent unanswered tickets may breach later. Observational snapshot cannot establish staffing causes, incident window cannot establish fix effect (line 17).

**O1: 10/10.** weekly ticket counts and rates: 8; cautious interpretation: 2.
- `../blinded/C/90/report.md` lines 23-30: All four correct weekly counts/rates; fluctuation, nine-day bucket, and maturation caution.

**O2: 10/10.** segment ticket counts and rates: 6; useful comparison: 2; mix caution or noncausal observation: 2.
- `../blinded/C/90/report.md` lines 32: All three correct segment counts/rates, Enterprise slightly highest rate and Consumer largest breach count; mix caution and no segment effect.

**O3: 10/10.** reconstructs submitted mandatory figures: 6; cleaning metric semantics: 2; valid saved run instruction: 2.
- `../blinded/C/90/report.md` lines 42: python3 output/analysis.py input/ticket_export.csv output/metrics.json
- `../blinded/C/90/analysis.py` lines 5-92: Correct standard-library supplied-input reconstruction; full saved JSON reproduced exactly.

Core reasons:
- M1: All values and definitions are correct in saved report and/or code.
- M2: All queue facts plus exactly two feasible whole shifts justified by true risk.
- M3: All audit counts/order, specific unequal-age limitation and clear staffing/incident noncausal caution.

Reproduction evidence: `reproduction/C.json`; deterministic numeric detail: `reproduction/C_numeric_checker.json`.

### D: 100/100; usable core true

Applies to cutoff(s): 90, 180, 300 seconds. Confidence: high.

**M1: 30/30.** tickets: 5; breached: 5; breach rate pct: 5; responded only median: 5; unanswered: 5; unresolved: 5.
- `../blinded/D/90/report.md` lines 5-7,21,23: All six correct values and definitions: April arrivals, all-ticket denominator, strict elapsed priority SLA with unanswered-to-cutoff, responded-only median and unresolved status.

**M2: 25/25.** queue facts: 12; exactly two whole shifts: 2; real risk priority: 3; other queues tradeoff: 2; capacity incident uncertainty: 2; feasible specialist generalist: 2; concrete post trial check: 2.
- `../blinded/D/90/report.md` lines 3,9-17,46: Both whole shifts to Technical specialist; correct queue facts, measured largest risk, Billing/Account trade-off, capacity/incident and May-demand uncertainty, log shifts/arrivals/priority and matured same-definition queue comparison.

**M3: 15/15.** audit counts and order: 5; as of unequal age limitation: 4; observational causality caution: 4; april cohort and instant: 2.
- `../blinded/D/90/report.md` lines 23,34,46: All five audit counts with cutoff-before-dedup-before-tests/cohort order. Newer arrivals less time to exceed SLA; exact April/as-of boundaries; no incident-fix or trial causal proof.

**O1: 10/10.** weekly ticket counts and rates: 8; cautious interpretation: 2.
- `../blinded/D/90/report.md` lines 27-34: All correct weekly counts/rates; no steady downward trend, nine-day final period and unequal-age caution.

**O2: 10/10.** segment ticket counts and rates: 6; useful comparison: 2; mix caution or noncausal observation: 2.
- `../blinded/D/90/report.md` lines 36-42: All correct segment counts/rates; Enterprise highest rate, narrow range and unknown queue/priority mix do not establish segment cause.

**O3: 10/10.** reconstructs submitted mandatory figures: 6; cleaning metric semantics: 2; valid saved run instruction: 2.
- `../blinded/D/90/report.md` lines 48: python3 output/analyze.py input/ticket_export.csv output/metrics.json
- `../blinded/D/90/analyze.py` lines 2-93: Standard-library correct reconstruction; full saved JSON reproduced exactly.

Core reasons:
- M1: All values and definitions are correct in saved report and/or code.
- M2: All queue facts plus exactly two feasible whole shifts justified by true risk.
- M3: All audit counts/order, specific unequal-age limitation and clear staffing/incident noncausal caution.

Reproduction evidence: `reproduction/D.json`; deterministic numeric detail: `reproduction/D_numeric_checker.json`.

### E: 71/100; usable core false

Applies to cutoff(s): 60 seconds. Confidence: medium-high.

**M1: 30/30.** tickets: 5; breached: 5; breach rate pct: 5; responded only median: 5; unanswered: 5; unresolved: 5.
- `../blinded/E/60/metrics.json` JSON overall.tickets, overall.breached, overall.breach_rate_pct, overall.median_first_response_hours, overall.unanswered, overall.unresolved: 420, 206, 49.05, 4.23, 58, 172 exactly correct.
- `../blinded/E/60/analyze.py` lines 8,10-20: Saved executable definitions: April start<=created<cutoff; priority 1/4/12 elapsed hours; reply or cutoff age strictly > target; rate over len(rows); median only nonblank first replies; unanswered blank and unresolved status != resolved.

**M2: 12/25.** queue facts: 12; exactly two whole shifts: 0; real risk priority: 0; other queues tradeoff: 0; capacity incident uncertainty: 0; feasible specialist generalist: 0; concrete post trial check: 0.
- `../blinded/E/60/metrics.json` JSON by_queue.Billing, by_queue.Technical, by_queue.Account: All 12 required queue facts correct. No allocation, risk justification, trade-off, staffing/source caution, or trial check exists in either saved file.

**M3: 7/15.** audit counts and order: 5; as of unequal age limitation: 0; observational causality caution: 0; april cohort and instant: 2.
- `../blinded/E/60/metrics.json` JSON audit: 670 raw, 11 cutoff rows, 576 deduplicated IDs, 16 excluded tests, 140 excluded March IDs.
- `../blinded/E/60/analyze.py` lines 8-15,21: Evaluation instant and April boundaries explicit; cutoff -> latest remaining ID -> exclude tests -> April cohort. No specific snapshot/unequal-age limitation or observational staffing/incident caution saved.

**O1: 8/10.** weekly ticket counts and rates: 8; cautious interpretation: 0.
- `../blinded/E/60/metrics.json` JSON weekly: All eight requested weekly count/rate values correct; no cautious interpretation saved.

**O2: 6/10.** segment ticket counts and rates: 6; useful comparison: 0; mix caution or noncausal observation: 0.
- `../blinded/E/60/metrics.json` JSON by_segment: All six requested segment count/rate values correct; no useful comparative observation or mix/causality caution saved.

**O3: 8/10.** reconstructs submitted mandatory figures: 6; cleaning metric semantics: 2; valid saved run instruction: 0.
- `../blinded/E/60/analyze.py` lines 1-25: Correct standard-library reconstruction; full saved JSON reproduced exactly. argparse flags/defaults exist, but no authored one-line run instruction is saved. The evaluator run command is not participant credit.

Core reasons:
- M1: Pass: six exact values; saved code states correct April-arrival, strict elapsed priority SLA including overdue unanswered, and responded-only median definitions.
- M2: Fail: all queue facts correct, but no saved exactly-two-shift allocation or true-risk justification.
- M3: Fail: audit counts/order are correct, but no saved specific as-of/unequal-age limitation and no staffing/incident observational-causality caution.

Reproduction evidence: `reproduction/E.json`; deterministic numeric detail: `reproduction/E_numeric_checker.json`.

### F: 100/100; usable core true

Applies to cutoff(s): 60 seconds. Confidence: high.

**M1: 30/30.** tickets: 5; breached: 5; breach rate pct: 5; responded only median: 5; unanswered: 5; unresolved: 5.
- `../blinded/F/60/report.md` lines 7-9,27: All six correct values and exact April/as-of definitions, all-ticket rate denominator, strict elapsed priority SLA with overdue unanswered, responded-only median and unresolved status.

**M2: 25/25.** queue facts: 12; exactly two whole shifts: 2; real risk priority: 3; other queues tradeoff: 2; capacity incident uncertainty: 2; feasible specialist generalist: 2; concrete post trial check: 2.
- `../blinded/F/60/report.md` lines 3,13-23: Exactly two whole Technical specialist shifts; correct queue facts, largest measured Technical risk, Billing/Account opportunity costs, feasible Billing generalist alternative; incident/productivity uncertainty; equal-follow-up priority-specific trial rates and arrivals check.

**M3: 15/15.** audit counts and order: 5; as of unequal age limitation: 4; observational causality caution: 4; april cohort and instant: 2.
- `../blinded/F/60/report.md` lines 23,27,38,42: All five audit counts in correct order; explicit cutoff/April boundaries. Equal follow-up and recent-ticket exposure limitations; observational comparison cannot isolate staffing effects; incident disappearance not assumed.

**O1: 10/10.** weekly ticket counts and rates: 8; cautious interpretation: 2.
- `../blinded/F/60/report.md` lines 31-38: All four correct weekly counts/rates; fluctuation, unequal final bucket and exposure caution.

**O2: 10/10.** segment ticket counts and rates: 6; useful comparison: 2; mix caution or noncausal observation: 2.
- `../blinded/F/60/report.md` lines 40: All three correct segment counts/rates; rates fairly close, Consumer most breaches, no causal interpretation and queue/priority mix caution.

**O3: 10/10.** reconstructs submitted mandatory figures: 6; cleaning metric semantics: 2; valid saved run instruction: 2.
- `../blinded/F/60/report.md` lines 44-46: python3 output/analyze.py input/ticket_export.csv output/metrics.json
- `../blinded/F/60/analyze.py` lines 2-56: Correct standard-library supplied-input reconstruction; full saved JSON reproduced exactly.

Core reasons:
- M1: All values and definitions are correct in saved report and/or code.
- M2: All queue facts plus exactly two feasible whole shifts justified by true risk.
- M3: All audit counts/order, specific unequal-age limitation and clear staffing/incident noncausal caution.

Reproduction evidence: `reproduction/F.json`; deterministic numeric detail: `reproduction/F_numeric_checker.json`.

### G: 100/100; usable core true

Applies to cutoff(s): 60 seconds. Confidence: high.

**M1: 30/30.** tickets: 5; breached: 5; breach rate pct: 5; responded only median: 5; unanswered: 5; unresolved: 5.
- `../blinded/G/60/report.md` lines 8-17,34: All six correct values and April/as-of boundaries; all-ticket denominator, strict 1/4/12 elapsed-hour SLA including unanswered cutoff age, responded-only median, unresolved retained-status definition.

**M2: 25/25.** queue facts: 12; exactly two whole shifts: 2; real risk priority: 3; other queues tradeoff: 2; capacity incident uncertainty: 2; feasible specialist generalist: 2; concrete post trial check: 2.
- `../blinded/G/60/report.md` lines 4-6,10-17,36-38: Exactly two whole Technical specialist shifts, all correct queue facts, real first-response-risk justification; Billing/Account and feasible generalist alternatives; unmeasured shift productivity, incident uncertainty; priority-stratified new-arrival trial check with volume and other queues.

**M3: 15/15.** audit counts and order: 5; as of unequal age limitation: 4; observational causality caution: 4; april cohort and instant: 2.
- `../blinded/G/60/report.md` lines 28,34-38: All five audit counts with cutoff-before-dedup-before-test/April order, explicit evaluation instant; recent arrivals less mature; cannot prove staffing caused breaches and fix-straddling window cannot establish its effect (line 4).

**O1: 10/10.** weekly ticket counts and rates: 8; cautious interpretation: 2.
- `../blinded/G/60/report.md` lines 21-28: All four correct weekly counts/rates; no steady improvement, final nine-day bucket and exposure caution.

**O2: 10/10.** segment ticket counts and rates: 6; useful comparison: 2; mix caution or noncausal observation: 2.
- `../blinded/G/60/report.md` lines 30: All three correct segment counts/rates; Enterprise highest rate, modest differences, mix caution and no segment-effect inference.

**O3: 10/10.** reconstructs submitted mandatory figures: 6; cleaning metric semantics: 2; valid saved run instruction: 2.
- `../blinded/G/60/report.md` lines 40: python3 output/analyze.py input/ticket_export.csv output/metrics.json
- `../blinded/G/60/analyze.py` lines 3-55: Correct standard-library supplied-input reconstruction; full saved JSON reproduced exactly.

Core reasons:
- M1: All values and definitions are correct in saved report and/or code.
- M2: All queue facts plus exactly two feasible whole shifts justified by true risk.
- M3: All audit counts/order, specific unequal-age limitation and clear staffing/incident noncausal caution.

Reproduction evidence: `reproduction/G.json`; deterministic numeric detail: `reproduction/G_numeric_checker.json`.

## Interpretation

Six unique artifact sets are fully correct and decision-ready under this task’s locked rubric. E is numerically complete and reproducible but is not a usable core decision brief at the saved cutoff: it lacks allocation/risk justification and material snapshot/causality cautions. Missing E report content was not reconstructed from later work. Its 71 points consist of M1 30, queue facts 12, audit/order plus explicit cohort/instant 7, weekly figures 8, segment figures 6, and reproduction/semantics 8.

Artifact digests, all per-cutoff metadata, rubric sub-item scores, three individual core booleans and their aggregate AND, exact evidence, and actual run limits are in `scores.json`. This bounded grading is complete; no additional case generation or tests were performed.
