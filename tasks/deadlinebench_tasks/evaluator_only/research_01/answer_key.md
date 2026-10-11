# Research 01 answer key, fixed v1.0
EVALUATOR ONLY. Entire case and all entities are synthetic. This file is not a participant input. There is no preferred vendor hidden in the scoring.

## Exact central calculations
Use mean = logged handling minutes / answered tickets (S03 rows), and weighted mean = 0.70 × English mean + 0.30 × Spanish mean (S01-P2).
- Baseline: English 10.00, Spanish 13.00; weighted 10.90 minutes.
- EmberSearch: English 8.00, Spanish 12.50; weighted 9.35 minutes. Reduction 1.55 minutes; 1.55 / 10.90 × 100 = 14.2202%, ordinarily 14.2%.
- CoveFind: English 8.50, Spanish 11.00; weighted 9.25 minutes. Reduction 1.65 minutes; 1.65 / 10.90 × 100 = 15.1376%, ordinarily 15.1%.
- EmberSearch first-year all-in: $25,200 + $6,000 + (72 + 12 × 4) × $75 = $40,200.
- CoveFind first-year all-in: $21,600 + $4,500 + (120 + 12 × 6) × $75 = $40,500.
Both central costs fit $42,000, both central setup estimates fit 140 hours, and both fit the monthly support cap. Contingencies would make EmberSearch $42,000 exactly (24 extra × $75) and CoveFind $43,500 (40 extra × $75), with CoveFind 160 initial hours. EmberSearch would reach the cost ceiling; CoveFind would exceed cost and initial-hour capacity.

The projection assumes observed language-specific means transfer to a common target workload. No causal inference or statistical significance follows from the means alone. A pooled trial average is not the requested fixed-mix average. Vendor search-time and self-test claims have different outcomes/samples.

## Trust evidence
S04 E-EN: 58/60 = 96.67% correct; E-ES: 29/40 = 72.50%. C-EN: 55/60 = 91.67%; C-ES: 35/40 = 87.50%. Neither Spanish sample reaches 90%, so neither satisfies the per-language production gate. The 70/30 weighted correctness estimates would be 89.42% EmberSearch and 90.42% CoveFind, but the aggregate does not make CoveFind pass. Traceability is a different outcome: 56/60, 23/40, 53/60, 33/40, respectively. Zero observed privacy incidents does not prove privacy safety.

## Decision-neutral strong recommendations
- EmberSearch supervised pilot: easier implementation and better observed English speed/correctness, while explicitly controlling poor Spanish correctness and outdated translated notices. Fresh per-language audit and policy-update testing are essential; no immediate production clearance.
- CoveFind supervised pilot: better observed Spanish speed/correctness/traceability and slightly better central weighted speed, while explicitly recognizing extra adapter work, near-ceiling cost, setup contingency, and that Spanish trust still falls below the gate.
- Defer supplier commitment for a narrower validation: uncertainty from cohort selection, simplified billing policy, source defects, and imminent policy changes could justify common-workload/source cleanup testing before choosing. Explain its opportunity cost, bounded scope, and a clear decision date rather than indefinite delay.
These are examples, not mandatory conclusions. A different well-supported choice is fully creditable. A dual paid pilot without acknowledging the $12,000 budget conflict is not feasible as currently framed.

## Accepted tensions and limitations (not an exhaustive checklist)
1. Marketing versus relevant outcomes: S02-E2's 35% faster English searches versus S03's 14.2% projected total handling improvement; the measures differ, so neither disproves the other. S02-C2's 94% predominantly English self-test versus S04's relevant per-language independent samples.
2. Speed versus trust/equity: EmberSearch is faster in English, CoveFind in Spanish; EmberSearch English audit is stronger but Spanish audit weaker. Cite S03/S04 rows and S01-P4. Overall correctness cannot replace a per-language gate.
3. Apparent effect versus study design: S03-P2/P3/P4's volunteers, nonrandom cohorts, earlier baseline, simplified billing policy, and unmeasured escalations limit causal attribution. Do not assume these confounders fully explain or reverse results.
4. Central budget feasibility versus implementation risk: S02 fees + S05 hours fit centrally; contingencies add cost and CoveFind exceeds 140 initial hours. Two-week supplier setup excludes customer preparation; adapter upkeep is an ongoing burden.
5. Historical versus planned demand: S07-P1's 20% historical Spanish versus S01-P2's 30% central forecast; scenarios change speed ranking and the launch may slip.
6. Agent acceptance versus representative adoption: S06 volunteers and mixed reasons do not establish team preference or novice performance. Exact citations may improve trust experience but are not correctness itself.
7. Short test versus upcoming policy changes: S03-P4/S07-P2 do not show sustained update performance; at least a test across a policy change is sensible.

Consequential unknowns include full-workload escalation changes, novice performance, complexity comparability, policy-update reliability, realized launch mix, and scope/effort of source repair. At least one should be linked to a decision consequence.

## Optional sensitivity exact values
- 20% Spanish: EmberSearch = 0.8×8 + 0.2×12.5 = 8.90; CoveFind = 0.8×8.5 + 0.2×11 = 9.00. EmberSearch is faster by 0.10 minute.
- 40% Spanish: EmberSearch = 9.80; CoveFind = 9.50. CoveFind is faster by 0.30 minute.
- Tie: 8 + 4.5q = 8.5 + 2.5q; q = 0.25 (25% Spanish), both 9.125 minutes.
A speed ranking change need not change the overall recommendation because correctness, implementation, and uncertainty remain relevant. No required scenario winner.

## Optional validation plan examples
An 8–12 week supervised pilot with a common source version, matched or randomized ticket/agent rotation where feasible, measured handling time plus escalation/reopen tracking, fresh language-stratified correctness review, and a policy-update challenge is strong. Weekly review must remain at or below 50 sampled answers, with an accountable support lead, policy owner, analyst and engineering lead. Expansion requires >=10% comparable mean speed improvement, >=90% materially correct separately by language in a fresh audit, no unresolved critical privacy incident, and capacity/budget fit. Stop or revise on consequential wrong-answer patterns, privacy incidents, or budget/capacity failures. Other measurable, feasible plans satisfying the prompt can score fully.
