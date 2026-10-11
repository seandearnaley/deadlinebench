# Northstar Desk: first-week-of-May support coverage

**Decision:** Assign both additional four-hour shifts to Technical: **Technical 2, Billing 0, Account 0**. This is an eight-hour, one-week trial. The available specialist can cover both shifts; each shift remains wholly assigned to one queue.

## April performance as of May 1, 2026, 00:00 UTC

The qualifying April cohort contains **420 tickets**, with **206 first-response SLA breaches (49.05%)**, **58 unanswered** and **172 unresolved**. Median first-response time is **4.23 hours**, calculated from the **362 responded tickets** only.

The breach-rate denominator is all qualifying April tickets, including unanswered and unresolved tickets. First-response targets are P1 **1 hour**, P2 **4 hours**, and P3 **12 hours**, measured in elapsed time, including nights and weekends. A breach requires elapsed time **strictly greater** than the target. For unanswered tickets, elapsed time runs from creation to the evaluation instant; those still within target are not breaches. Unanswered tickets are not assigned zero response time.

| Queue | Tickets | Breaches | Breach rate | Unanswered | Unresolved | Median response hours |
|---|---:|---:|---:|---:|---:|---:|
| Billing | 143 | 59 | 41.26% | 11 | 55 | 3.96 |
| Technical | 199 | 142 | 71.36% | 42 | 87 | 6.95 |
| Account | 78 | 5 | 6.41% | 5 | 30 | 2.63 |

Technical has the largest cohort, highest breach rate, most breaches and most unanswered tickets. Its 142 breaches account for 68.93% of all breaches, and 42 unanswered tickets account for 72.41% of the unanswered cohort. In April 22–30, Technical still recorded **45 breaches among 59 tickets (76.27%)**. That interval straddles the April 24 incident fix, so it cannot establish post-fix performance.

Concentrating both shifts on Technical sacrifices extra Billing coverage despite Billing's 59 breaches and 11 unanswered tickets. Billing's month-end demand may differ from early May demand. A one-shift-each allocation would spread coverage, but the much larger observed Technical first-response burden favors concentration. Account's 30 unresolved tickets alone do not justify priority over these first-response risks. There is no measured tickets-per-shift estimate, so no clearance forecast is warranted.

## Timing and customer segments

| Arrival period | Tickets | Breaches | Breach rate |
|---|---:|---:|---:|
| April 1–7 | 83 | 48 | 57.83% |
| April 8–14 | 115 | 51 | 44.35% |
| April 15–21 | 90 | 46 | 51.11% |
| April 22–30 | 132 | 61 | 46.21% |

Rates fluctuate without a consistent improving trend. The last interval spans nine days, versus seven for the others, and recent unanswered tickets have less time to exceed SLA.

| Segment | Tickets | Breaches | Breach rate |
|---|---:|---:|---:|
| Enterprise | 85 | 44 | 51.76% |
| Small business | 158 | 75 | 47.47% |
| Consumer | 177 | 87 | 49.15% |

Segment rates differ by only 4.29 percentage points; Consumer has the largest absolute breach count. These descriptive differences do not establish a segment effect, particularly without controlling for queue and priority mix.

## Cleaning, limitations and trial check

Start with **670 raw snapshot rows**. Exclude **11 rows updated at or after the cutoff**, leaving 659. Retain the latest remaining update per ticket ID: **576 deduplicated IDs**, removing 83 duplicate snapshot rows. Then exclude **16 test IDs** and **140 March-arrival IDs**, leaving 420 April tickets. Arrivals at or after May 1 are excluded; none otherwise remain outside April after these exclusions. Use retained queue and status, not snapshot-row sums.

This snapshot lacks worked shifts, complexity, incident labels, reopened histories and satisfaction. April outcomes cannot establish staffing causality or predict May demand; the incident fix does not guarantee Technical load disappears.

For the trial, log arrivals, priority, first-response timestamps and actual extra-shift hours. Compare Technical's first-week breach rate, responded-only median and unanswered count with April baselines, separating priority mix and assessing each arrival only after its SLA window matures. Check Billing and Account for spillover. Treat any improvement as descriptive, not causal proof.

**Reproduce:** From the run directory, execute `python output/analyze.py input` to recreate `output/metrics.json` using only the standard library.
