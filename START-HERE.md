# DeadlineBench: first real-agent screening results
October 11, 2026 · exploratory prototype, not a validated benchmark

## What was completed

- Six offline tasks across research, data analysis and small code repairs, with separate answer keys, explicit mandatory/optional requirements and lightweight checks.
- Seven actual native-agent runs on one synthetic support-analysis task, using gpt-6.1-sol with xhigh reasoning.
- An independent monotonic-clock observer froze delivered files at the cutoffs. A separate grader assessed anonymized snapshots against a locked rubric.
- Primary-source customer research, an interview script and a draft pilot offer. No outreach occurred.

These were actual model-produced files, unlike the preceding synthetic scheduler simulation. No separately invoked paid provider API was used. Native-agent compute is not assumed to be economically free; its marginal cost was not measured.

## Results

| Assigned budget | Condition | Usable core at deadline | Weighted task score |
|---|---|---:|---:|
| 300 seconds | Ordinary deadline | 1/1 | 100/100 |
| 300 seconds | Clock affordance | 1/1 | 100/100 |
| 300 seconds | Clock + scope guidance | 1/1 | 100/100 |
| 60 seconds | Ordinary deadline, two runs | 1/2 | 71 and 100 |
| 60 seconds | Clock + scope guidance, two runs | 2/2 | 100 and 100 |

All three 300-second runs already had their final complete artifacts in the 90-second snapshot. The 90/180-second observations were checkpoints within a 300-second assignment, **not separate shorter-budget trials**.

The one short-budget miss had correct calculations and a working analysis script at the deadline but no saved decision brief. A report existed afterward, but was not counted. This is exactly the distinction between progress and delivered user value that the benchmark needs to preserve.

**This does not establish that scope guidance improves performance.** There are only two short runs per condition, one task, one model/effort setting, no randomized order, and shared infrastructure. The repetition reversed launch order but does not remove those limitations. Generous-budget performance was at ceiling. We have neither a meaningful model ranking nor evidence that training is needed.

## Measurement and grading checks

- Snapshot polling delay was below 80 milliseconds in the first wave; actual observation timing is retained per snapshot.
- All 38 graded file observations were stable during reading. A subsequent hash/mtime check found matching original bytes predated the nominal cutoff, supporting on-time presence despite polling delay.
- All seven saved scripts reproduced their submitted numeric output in isolated copies according to the independent grader; the full grading record describes execution limits.
- One initial scope-run admission failed because concurrency slots were occupied. It had no participant and was excluded as an infrastructure event; the replacement received a fresh full budget. The failed attempt is documented in the protocol.
- Inputs and the weighted rubric were frozen before output inspection. A separate core-validity definition was clarified after two launches but before output inspection; this is exploratory, not a preregistered confirmatory study.
- Grading used anonymized artifacts. The grader incidentally saw generic run-completion summaries from an agent listing, without label associations; this limits a claim of perfect blinding.
- Agents shared a filesystem and were instructed not to inspect other trials/keys; this was not an adversarially isolated benchmark. A proper external harness must enforce that boundary.

## What this changes

The first experiment supports building the measurement correctly, not building a company yet. It demonstrated that a late brief can be excluded even when the agent ultimately reports completion, while a partially finished calculation can retain diagnostic credit without counting as a usable deliverable.

Next technical step: use harder cases from the six-task suite, predeclare multiple genuine deadlines, randomize order, and repeat each condition enough to estimate variability. Compare against a strong fixed mandatory-first baseline. Add tool-delay/deadline-change stress only after the basic result is stable. Separate orchestration failure from model-policy failure.

Next commercial step: investigate one workflow where the deadline truly binds. Multi-tool technical-support agents are a candidate, not a verified buyer. Existing products already support timing, quality and mandatory gates, so our test must change a customer's configuration/release decision or expose a failure their current evaluation misses. Interview and pilot drafts are included; no customer interest or revenue is claimed.

## Bundle map

- tasks/deadlinebench_screening_v1.zip: six tasks, inputs, locked rubrics, checks and validation
- live/PROTOCOL.md: trial procedure and limitations
- live/grading/: independent scores and evidence
- live/blinded/: the exact graded snapshots
- live/condition_mapping.json: condition mapping, revealed after scoring
- live/timestamp_validation.json: matching-byte timing checks
- live/watchdog.py: measurement observer, not an agent runner or model-kill mechanism
- market/: source-backed buyer research, incumbent comparison, interview script and draft offer
