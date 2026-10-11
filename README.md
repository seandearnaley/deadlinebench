# DeadlineBench

**Can an agent deliver useful work before the clock runs out?**

DeadlineBench is an exploratory research pack for evaluating the artifact a user actually receives by a deadline. It separates mandatory acceptance from optional quality, freezes delivered files at the cutoff, and gives diagnostic credit for partial work without calling an incomplete deliverable usable.

This repository contains **six synthetic offline tasks**, a **seven-run live pilot**, frozen outputs, locked rubrics, grading evidence, and source-backed market research. It is a prototype, not a validated benchmark or model leaderboard.

## What happened in the live pilot

Seven actual agent runs used one synthetic support-analysis task (`data_01`), one model (`gpt-6.1-sol`) and one reasoning setting (`xhigh`). An independent monotonic-clock observer captured files; a separate grader assessed anonymized snapshots.

| Assigned deadline | Condition | Usable core at deadline | Weighted score |
|---|---|---:|---:|
| 300 s | Ordinary deadline | 1/1 | 100/100 |
| 300 s | Clock affordance | 1/1 | 100/100 |
| 300 s | Clock + scope guidance | 1/1 | 100/100 |
| 60 s | Ordinary deadline | 1/2 | 71, 100 |
| 60 s | Clock + scope guidance | 2/2 | 100, 100 |

All three 300-second runs had complete final artifacts in their 90-second snapshots. The 90/180-second checkpoints were observations within a 300-second assignment, not separate shorter-deadline trials.

The short-budget miss saved correct calculations and a working script but no decision brief by the cutoff. A later brief was **excluded**. Weighted score and usable-core acceptance therefore tell different stories.

**No causal effect or model ranking is established.** There are only two short runs per condition, one task, no randomized order, shared infrastructure, ceiling performance at 300 seconds, and imperfect process blinding. The core-validity flag was clarified after two launches but before output inspection; this was exploratory, not a preregistered confirmatory study. See the [protocol](live/PROTOCOL.md) and [full grading report](live/grading/REPORT.md).

## Explore the evidence

- [Start here](START-HERE.md): the complete research summary and next questions.
- [Live pilot](live/PROTOCOL.md): procedure, admission failure, deadline capture, and limitations.
- [Grading report](live/grading/REPORT.md) and [scores](live/grading/scores.json): item-level decisions, usable-core flags, and reproduction records.
- [Frozen snapshots](live/blinded/): exact participant scripts, metrics, briefs, and snapshot hashes; [condition mapping](live/condition_mapping.json) and [timing validation](live/timestamp_validation.json).
- [Six-task suite](tasks/deadlinebench_tasks/README.md): browsable prompts, synthetic inputs, separate evaluator keys, locked rubrics, and lightweight checks. An [unchanged ZIP](tasks/deadlinebench_screening_v1.zip) is also included.
- [Market research](market/market_validation.md), [incumbent comparison and primary sources](market/vendor_metrics.md), [interview guide](market/interview_script.md), and [draft pilot offer](market/pilot_offer.md). No customer interest, outreach, or revenue is claimed.
- [Publication notes](PUBLICATION.md): integrity checks and documented path sanitization.

## The six cases

| Case | Work |
|---|---|
| `research_01` | Choose a multilingual support-search pilot |
| `research_02` | Choose a parcel mis-sort intervention |
| `data_01` | Allocate support coverage from a ticket export |
| `data_02` | Review promotional contribution and a constrained test budget |
| `code_01` | Repair daily service-window utilities |
| `code_02` | Repair warehouse stock reconciliation |

Each task has three mandatory requirements worth 70 points and three optional items worth 30. Inputs and operational records are invented. Only `data_01` was used in the live pilot; the other five are supplied cases, not measured agent results.

The task checks use Python 3.10+ and the standard library. Follow the [suite instructions](tasks/deadlinebench_tasks/README.md) for participant/evaluator separation and the limits of automated scoring. The observer captures artifacts; it does not run or stop agents.

Earlier virtual-time scheduler simulations are discussed as prior context in the research; their results are not included in this table or presented as live-agent evidence. This publication adds no new experiments.
