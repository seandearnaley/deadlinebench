# April support coverage decision

**Recommendation:** Assign both additional four-hour shifts to Technical in the first May week: Technical 2, Billing 0, Account 0. This uses exactly eight extra analyst-hours and respects the single-queue, indivisible-shift constraint. The available specialist can cover both Technical shifts. Treat this as a one-week trial.

## Overall first-response risk

The qualifying April cohort contains **420 tickets**, with **206 SLA breaches (49.05%)**, **58 unanswered** and **172 unresolved** at May 1, 2026, 00:00 UTC. Median first-response time among the **362 responded tickets** is **4.23 hours**.

All 420 qualifying April tickets are the breach-rate denominator, including unanswered and unresolved tickets. Priority targets are P1: 1 hour; P2: 4 hours; P3: 12 hours, elapsed continuously including nights and weekends. A breach means strictly exceeding the target. For unanswered tickets, age runs to the evaluation instant; tickets still within target are not breaches. Unanswered tickets are excluded from the response-time median. Unresolved means retained status is not resolved.

## Queue comparison and capacity trade-off

| Queue | Tickets | Breaches | Breach rate | Unanswered | Unresolved | Median response hours |
|---|---:|---:|---:|---:|---:|---:|
| Billing | 143 | 59 | 41.26% | 11 | 55 | 3.96 |
| Technical | 199 | 142 | 71.36% | 42 | 87 | 6.95 |
| Account | 78 | 5 | 6.41% | 5 | 30 | 2.63 |

Technical accounts for 68.93% of all breaches and 72.41% of unanswered tickets, and has the highest breach rate and volume. Concentrating both shifts there prioritizes the strongest observed first-response risk. Account's 30 unresolved tickets do not by themselves imply first-response failure; its breach rate is much lower.

The trade-off is leaving Billing's substantial 59 breaches without extra coverage. A generalist and checklist make Billing feasible, and invoice disputes may cluster near month-end, but the export does not identify their timing or establish the effect of added capacity. The reported INC-42 fix shipped April 24, yet incident tickets are unlabeled: it cannot establish that Technical demand has disappeared. No estimate of tickets cleared per shift is available.

During the trial, log actual extra-shift hours and queue; compare May arrivals' priority-specific breach rates, unanswered tickets already beyond SLA, and responded-ticket median against comparable weekday/time windows. Use equal follow-up windows so recent arrivals are not advantaged. Review both Technical and uncovered Billing; a one-week observational comparison cannot isolate staffing effects from changing demand.

## Cleaning and audit

There were **670 raw snapshot rows**. Discard **11** updates at or after May 1 00:00 UTC. Retain the latest eligible update per ID: **576 distinct ticket IDs**, removing **83 duplicate snapshot rows**. Exclude **16 retained test IDs**, then **140 non-test March IDs**, leaving **420 April arrivals**. The cutoff is exclusive for updates and arrivals; April begins inclusively on April 1. Snapshots are not summed as events. The metrics audit's deduplicated_ids is the distinct-ID count after cutoff filtering, not the removed-row count.

## Weekly and segment checks

| Arrival period | Tickets | Breaches | Breach rate |
|---|---:|---:|---:|
| Apr 1–7 | 83 | 48 | 57.83% |
| Apr 8–14 | 115 | 51 | 44.35% |
| Apr 15–21 | 90 | 46 | 51.11% |
| Apr 22–30 | 132 | 61 | 46.21% |

Rates fluctuate rather than showing a steady improvement. The last period spans nine days and recent unanswered tickets have less exposure to breach.

Enterprise: **85 tickets, 44 breaches, 51.76%**; Small business: **158, 75, 47.47%**; Consumer: **177, 87, 49.15%**. Rates are fairly close, while Consumer contributes the most breaches by count. Segment differences do not establish causation or account for queue/priority mix.

This snapshot omits staffing worked, complexity, reopening histories and satisfaction; current queue ownership may differ from ownership at first response. April results do not forecast May workload or quantify shift effectiveness.

Reproduce metrics from the supplied CSV with Python's standard library:

`python3 output/analyze.py input/ticket_export.csv output/metrics.json`
