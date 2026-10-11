# Northstar Desk: first-week May support coverage

## Decision
Assign **both additional four-hour shifts to Technical**: two whole shifts, eight hours total, for the first May week only. The available specialist can cover both. Technical accounts for 142 of April's 206 first-response breaches (68.93%), has the highest breach rate, and holds 42 of 58 unanswered tickets. Its April 22–30 arrivals still show 45 breaches among 59 tickets (76.27%), versus Billing's 14/41 (34.15%) and Account's 2/32 (6.25%). This supports prioritizing Technical even though the incident fix shipped April 24. The late-April window spans both sides of that fix and does not establish its effect.

The trade-off is no extra Billing or Account shift. Billing's 59 breaches and 11 unanswered tickets remain a meaningful risk, but Technical's first-response burden is substantially larger. Account's 30 unresolved tickets do not, by themselves, imply first-response failure: it has only five breaches. The generalist options are feasible alternatives, but the available evidence favors concentrating this limited trial. No estimate of tickets cleared per shift is available.

## April baseline, as of May 1 at 00:00 UTC

| Queue | Tickets | Breached | Breach rate | Median response hours | Unanswered | Unresolved |
|---|---:|---:|---:|---:|---:|---:|
| Billing | 143 | 59 | 41.26% | 3.96 | 11 | 55 |
| Technical | 199 | 142 | 71.36% | 6.95 | 42 | 87 |
| Account | 78 | 5 | 6.41% | 2.63 | 5 | 30 |
| **Overall** | **420** | **206** | **49.05%** | **4.23** | **58** | **172** |

The breach denominator is all 420 qualifying April tickets, including unanswered and unresolved tickets. A breach means first-response elapsed time strictly exceeds the priority target: P1 one hour, P2 four hours, P3 twelve hours, including nights and weekends. For unanswered tickets, elapsed time runs to the evaluation instant; tickets still within target are not breaches. Median response time uses only the 362 responded tickets. Unresolved means retained status is not resolved.

## Trends and customer segments

| Arrival period | Tickets | Breached | Breach rate |
|---|---:|---:|---:|
| April 1–7 | 83 | 48 | 57.83% |
| April 8–14 | 115 | 51 | 44.35% |
| April 15–21 | 90 | 46 | 51.11% |
| April 22–30 | 132 | 61 | 46.21% |

There is no steady improvement across the four periods. The last bucket covers nine days rather than seven, and recent arrivals have had less time to breach, so neither its volume nor its rate is directly comparable without care.

Enterprise: 85 tickets, 44 breaches, 51.76%. Small business: 158 tickets, 75 breaches, 47.47%. Consumer: 177 tickets, 87 breaches, 49.15%. Consumers contribute the largest absolute breach count, while Enterprise has the highest rate. These modest rate differences do not establish a segment effect; queue and priority mix may differ.

## Cleaning, limitations and trial check

The export has 670 raw snapshot rows. Exclude 11 updated at or after the cutoff; from 659 eligible rows retain the latest snapshot for each of 576 distinct ticket IDs, removing 83 superseded rows. Then exclude 16 retained test IDs and 140 non-test March IDs, leaving 420 April IDs. Filtering updates before deduplication avoids future information. Arrivals also use an exclusive May 1 boundary.

Queue is the retained current owner, not necessarily the owner at first response. The snapshot lacks shift coverage, complexity, incident labels, reopened history and satisfaction; it cannot prove staffing caused breaches or predict May demand.

For the trial, log actual shift hours and compare Technical's new-arrival SLA rate, unanswered-over-SLA count and responded median with comparable baseline windows, stratified by priority. Assess tickets after sufficient time to pass their SLA; report volumes and other queues too. Treat any change as descriptive, not a causal estimate.

Reproduce all submitted metrics: `python3 output/analyze.py input/ticket_export.csv output/metrics.json`
