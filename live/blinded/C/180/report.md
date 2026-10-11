# Northstar Desk: first-week-of-May coverage decision

**Decision: assign both additional four-hour shifts to Technical (eight specialist hours); Billing and Account receive no extra shifts.** This is a one-week trial. The available specialist can cover both Technical shifts, and indivisible shifts cannot be split. Prioritize first responses, especially unanswered tickets approaching their priority deadlines.

## April snapshot, as of May 1, 2026, 00:00 UTC

The qualifying April cohort contains **420 tickets**, with **206 SLA breaches (49.05%)**, **58 unanswered**, and **172 unresolved**. Median first-response time is **4.23 hours among 362 responded tickets**.

The breach denominator is all qualifying April tickets, including unanswered and unresolved tickets. Targets are P1: 1 hour, P2: 4 hours, P3: 12 hours, measured in elapsed time including nights and weekends. A breach requires response time **strictly greater** than the target. For unanswered tickets, elapsed time runs to the evaluation instant; tickets still within their target do not breach. Unanswered tickets are excluded from the response-time median. Unresolved means retained status is not resolved.

| Queue | Tickets | Breaches | Breach rate | Unanswered | Unresolved | Response median (hours) |
|---|---:|---:|---:|---:|---:|---:|
| Billing | 143 | 59 | 41.26% | 11 | 55 | 3.96 |
| Technical | 199 | 142 | 71.36% | 42 | 87 | 6.95 |
| Account | 78 | 5 | 6.41% | 5 | 30 | 2.63 |

Technical accounts for 142 of 206 breaches (68.93%) and 42 of 58 unanswered tickets (72.41%). Its risk is also high in the latest arrival window: April 22–30 has 59 Technical tickets and 45 breaches (76.27%), versus Billing's 41 tickets and 14 breaches (34.15%). This window straddles the April 24 incident fix, so it cannot establish post-fix performance. The incident's contribution is unlabelled; do not assume Technical demand disappears.

The trade-off is leaving Billing's substantial 41.26% breach rate without extra coverage. A Billing generalist is feasible, but the observed risk supports concentrating both shifts on Technical. Account's 30 unresolved tickets warrant routine follow-through, yet only five first-response breaches support lower priority for this trial. No measured clearance rate exists, so eight additional hours cannot be translated into tickets cleared or promised SLA improvement.

## Arrival-week and segment context

| April arrivals | Tickets | Breaches | Breach rate |
|---|---:|---:|---:|
| 1–7 | 83 | 48 | 57.83% |
| 8–14 | 115 | 51 | 44.35% |
| 15–21 | 90 | 46 | 51.11% |
| 22–30 | 132 | 61 | 46.21% |

Rates fluctuate without a steady improvement pattern. The last window spans nine days rather than seven, so its larger count is not directly comparable as arrival intensity. Recent unanswered tickets may still breach later.

Enterprise: 85 tickets, 44 breaches (51.76%); Small business: 158, 75 (47.47%); Consumer: 177, 87 (49.15%). Enterprise has the highest rate, but Consumer contributes the most breaches. These differences do not establish a segment effect; queue and priority mix may differ.

## Cleaning, limitations, and trial check

From **670 raw rows**, exclude **11 updates at or after cutoff**. Retain each ID's latest remaining snapshot: **576 deduplicated IDs**, removing 83 overlapping snapshot rows. Exclude **16 retained test IDs**, then **140 March IDs**, leaving 420 April arrivals. April eligibility is April 1 inclusive through May 1 exclusive; no production IDs fall on or after May 1.

Queue means current retained ownership, not necessarily the responding queue. The export lacks shifts worked, complexity, reopening histories, incident labels, and satisfaction. This observational snapshot cannot establish staffing causes or forecast May workload.

Log the trial shift times. Track arrivals, matured-cohort breach rates by priority, and unanswered tickets past SLA for each queue. Compare Technical with its April baseline using similar observation age, while checking Billing for deterioration. Review after the trial; treat any change as descriptive because demand and incident effects can change.

Reproduce from the run directory: `python3 output/analysis.py input/ticket_export.csv output/metrics.json`
