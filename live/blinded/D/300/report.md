# Northstar Desk: first-week May support coverage

**Decision:** Assign both additional four-hour shifts to **Technical**, for eight specialist hours in the first May week. The planning notes confirm one specialist can cover both. This is a one-week first-response trial, not a permanent staffing commitment.

## April arrivals as of May 1, 2026, 00:00 UTC

The qualifying cohort contains **420 tickets**, with **206 SLA breaches (49.05%)**, **58 unanswered** and **172 unresolved**. Median first response is **4.23 hours**, calculated among the **362 responded tickets**.

| Queue | Tickets | Breaches | Breach rate | Unanswered | Unresolved | Median response hours |
|---|---:|---:|---:|---:|---:|---:|
| Billing | 143 | 59 | 41.26% | 11 | 55 | 3.96 |
| Technical | 199 | 142 | 71.36% | 42 | 87 | 6.95 |
| Account | 78 | 5 | 6.41% | 5 | 30 | 2.63 |

Technical has the highest breach rate, largest arrival volume and most unanswered tickets. Its 142 breaches represent **68.93% of all April breaches**. Concentrating both shifts there prioritizes the clearest observed first-response risk. The trade-off is no extra Billing coverage despite its 59 breaches and 41.26% rate; Billing is the next candidate if May demand shifts. Account's 30 unresolved tickets warrant backlog attention, but its five first-response breaches do not justify diverting scarce response coverage on these figures.

INC-42 contributed to Technical load according to the notes, and its fix shipped April 24. The export cannot identify incident tickets or establish how much demand remains. Billing's potential month-end concentration also does not establish first-week May demand. Neither claim supports a quantified capacity forecast; there is no measured tickets-per-shift estimate.

## Definitions and cleaning audit

SLA targets are P1: 1 hour, P2: 4 hours and P3: 12 hours, measured in elapsed time including nights and weekends. A breach requires a wait **strictly greater** than the target. For unanswered tickets, wait runs from creation to the evaluation instant. The breach denominator is all qualifying April tickets, including unanswered and unresolved tickets. Response medians exclude unanswered tickets. Unresolved means retained status is not resolved.

Starting from **670 raw snapshot rows**, exclude **11 updated at or after the cutoff**, leaving 659. Retain the latest eligible update for each ID: **576 deduplicated IDs**, removing 83 duplicate snapshot rows. Exclude **16 retained test IDs**, then **140 March IDs**, leaving 420 April IDs. There are no other non-April exclusions. Arrivals must be on or after April 1 and strictly before May 1; filtering updates before deduplication prevents future information leaking into the snapshot.

## Timing and segment context

| Arrival period | Tickets | Breaches | Breach rate |
|---|---:|---:|---:|
| Apr 1–7 | 83 | 48 | 57.83% |
| Apr 8–14 | 115 | 51 | 44.35% |
| Apr 15–21 | 90 | 46 | 51.11% |
| Apr 22–30 | 132 | 61 | 46.21% |

Rates vary without a steady downward trend. The final period spans nine days, and its newer arrivals have had less time to exceed an SLA; its volume and rate cannot establish an incident-fix effect.

| Segment | Tickets | Breaches | Breach rate |
|---|---:|---:|---:|
| Enterprise | 85 | 44 | 51.76% |
| Small business | 158 | 75 | 47.47% |
| Consumer | 177 | 87 | 49.15% |

Consumer contributes the most breaches by count, while Enterprise has the highest rate. The narrow rate range and unknown priority/queue mix do not establish a segment-driven cause.

## Trial check and limitations

Record actual added shift hours, arrivals, priority, first replies and queue ownership during May 1–7. After every arrival has at least 12 hours of observation, compare queue-level breach rates, unanswered counts and responded-only medians with April, stratifying by priority where feasible. Treat changes as descriptive, not causal proof. Snapshot data lack worked shifts, complexity, reopening history and satisfaction; current queue ownership may differ from ownership at first response. April arrivals exclude older backlog.

**Reproduce:** From the run directory, execute `python3 output/analyze.py input/ticket_export.csv output/metrics.json`.
