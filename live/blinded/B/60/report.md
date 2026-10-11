# Northstar Desk: first-week May support coverage
As of 2026-05-01 00:00 UTC; April arrival cohort. Source: supplied synthetic export, dictionary and April 30 staffing notes.

## Decision
Assign **both additional four-hour shifts to Technical**, covered by the available specialist. This uses exactly two indivisible shifts, eight hours total, for the one-week trial. Technical has the largest volume, highest breach rate and most unanswered tickets. Its April 22–30 cohort still has 59 tickets, 45 breaches (76.27%) and 12 unanswered. This supports prioritizing continuing first-response risk despite the April 24 incident fix; the export cannot identify incident tickets or establish the fix's effect.

The trade-off is no extra Billing coverage, despite its 59 breaches and 11 unanswered. Billing is the next priority if May demand changes. Account's 30 unresolved tickets deserve follow-through, but its five first-response breaches give less reason to allocate these shifts there. No tickets-cleared forecast is justified because shift productivity is unmeasured.

## April results
Overall: **420 tickets; 206 breached (49.05%); median first response 4.23 hours among 362 responded tickets; 58 unanswered; 172 unresolved.**

| Queue | Tickets | Breaches | Breach rate | Unanswered | Unresolved | Response median, hours |
|---|---:|---:|---:|---:|---:|---:|
| Billing | 143 | 59 | 41.26% | 11 | 55 | 3.96 |
| Technical | 199 | 142 | 71.36% | 42 | 87 | 6.95 |
| Account | 78 | 5 | 6.41% | 5 | 30 | 2.63 |

All rates divide breaches by all qualifying tickets, including unanswered and unresolved. SLA targets are 1/4/12 elapsed hours for P1/P2/P3, including nights and weekends. Breach means strictly greater than the target, measured to first response or, when unanswered, to the evaluation instant. Unanswered tickets still within target are not breaches. Response medians exclude unanswered tickets; unresolved means status other than resolved.

## Cleaning and audit
The 670 raw rows contain overlapping snapshots. Excluded 11 rows updated at or after the cutoff. From 659 eligible rows, retained the latest pre-cutoff snapshot for each of **576 deduplicated ticket IDs**, removing 83 duplicate snapshots. Then excluded **16 test IDs** and **140 March IDs**, leaving 420 April arrivals. Arrival boundaries are April 1 inclusive and May 1 exclusive. Filtering updates before deduplication prevents future snapshots from replacing valid historical state. Queue and segment are from each retained snapshot.

## Arrival-week and customer comparisons
| Arrival period | Tickets | Breaches | Breach rate |
|---|---:|---:|---:|
| Apr 1–7 | 83 | 48 | 57.83% |
| Apr 8–14 | 115 | 51 | 44.35% |
| Apr 15–21 | 90 | 46 | 51.11% |
| Apr 22–30 | 132 | 61 | 46.21% |

The latest period has most arrivals, but spans nine days rather than seven. Its lower rate than the earliest period does not demonstrate improvement: newer unanswered arrivals have had less time to breach, and queue/priority mix may differ.

| Segment | Tickets | Breaches | Breach rate |
|---|---:|---:|---:|
| Enterprise | 85 | 44 | 51.76% |
| Small business | 158 | 75 | 47.47% |
| Consumer | 177 | 87 | 49.15% |

Consumer contributes the largest breach count; Enterprise has the highest rate. These descriptive differences do not show segment-driven service effects; priority and queue mix could matter.

## Trial check and limitations
Record actual extra-shift hours and queue, arrivals, priority, first responses and aged unanswered tickets. After May's first week, allow every arrival at least its SLA window, then compare Technical breach rates and response medians against comparable April weekdays, stratifying by priority and monitoring Billing/Account. Review direction and displacement risk before extending the trial; this observational comparison cannot prove causation.

This snapshot lacks shifts worked, complexity, reopen histories, incident attribution and satisfaction. Unresolved status is not a first-response failure. April arrivals are not the complete backlog or a guaranteed May forecast.

Reproduce: `python3 output/analyze.py input/ticket_export.csv output/metrics.json`
