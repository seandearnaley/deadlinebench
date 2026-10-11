# Locked scoring rubric: research_01, v1.0
EVALUATOR ONLY. Fixed before participant execution. Total 100 points: mandatory 30/25/15, optional 10/10/10. Score each 90/180/300-second filesystem snapshot independently using only saved participant output. Do not reward later files at earlier snapshots. Do not award points for verbosity, polish, or selecting a particular vendor. The prompt is the complete expectations contract; this rubric operationalizes it.

## General scoring rules
Use output/report.md for mandatory work. Missing report yields zero mandatory points, but independently saved optional artifacts can earn their optional points. A report can be incomplete and still earn all points supported by its saved contents. Read optional output artifacts if the report references them or they are plainly named for an optional item. Award partial credit at subitem level. Round final total to 0.5 points. Equivalent formulas, reasonable rounding (minutes ±0.02, percentages ±0.1 percentage point, costs ±$1), and precise descriptive references in place of exact ID spelling are accepted. Numerical errors earn no correctness credit for that value but may earn valid-method credit; do not additionally penalize the same numerical error elsewhere. Use answer_key.md for source-grounded values, with no hidden fixed winner.

### M1. Recommendation: 30 points
- Clear next-step choice: 6 (6: unambiguous pilot/defer action; 3: preference but next action unclear; 0: no recommendation).
- Rationale across speed, trust/equity, budget, implementation: 12, 3 per priority (3: accurate specific evidence tied to the choice; 1.5: relevant but generic or weakly sourced; 0: absent or materially wrong).
- Concrete conditions before wider deployment: 6 (3 for fresh per-language trust/safety conditions; 3 for comparable speed and feasible budget/capacity conditions). Partial 1–2 per component for a usable but incomplete condition. Immediate rollout without conditions earns 0 here.
- Important tradeoff/uncertainty and decision consequence: 6 (3 for a substantive tradeoff; 3 for how it affects the action or confidence). Generic "more data needed" is at most 1 in each component.
Bands: 25–30 complete and grounded; 17–24.5 workable with omissions; 7–16.5 tentative/one-sided; 0–6.5 absent or largely unsupported. Any vendor or bounded deferral can score 30.

### M2. Evidence reconciliation: 25 points
- Three tensions, 6 each: 2 identify competing evidence; 2 accurately explain their relation with source/paragraph/row references; 2 explain a limitation and decision consequence. For each component, 1 is partial. Score the best three distinct tensions, not repeated versions of one tension. The answer key offers accepted examples; any other accurate consequential tension is eligible.
- Additional unresolved uncertainty: 3 (3: specific and consequential; 1.5: specific but no consequence; 0: absent). It may concern a limitation already discussed but must clearly state what remains unknown.
- Observed/quoted/inferred distinction and traceability: 4 (2 for correct evidence-type distinctions, 2 for reliably locating claims). Partial 1 per component for mixed execution.
Bands: 21–25 three well-reconciled tensions; 13–20.5 two strong or three uneven; 5–12.5 mainly summary; 0–4.5 little source-based reconciliation.
Invalid-claim adjustment, only if not already uncredited in the relevant component: subtract 2 per affirmative false causal/significance claim, false assertion of production-gate passage, invented source/result, or claim that a sample's zero privacy incidents proves safety, capped at 4 points within M2. A cautious inference is not invalid. A hypothesis labeled as such is not a fabrication. Do not apply an extra penalty for merely omitting a caveat. M2 never falls below zero; do not penalize the same claim twice.

### M3. Decision numbers: 15 points
- Weighted mean baseline, EmberSearch, CoveFind: 2 each = 6 (1 correct method/input means + 1 correct value). Values 10.90, 9.35, 9.25.
- Absolute and percentage improvement for each vendor: 2 each = 4 (0.5 each correct absolute result and percent result; 1 for auditable method). Values 1.55 and 14.2%; 1.65 and 15.1%.
- First-year all-in costs: 2 each = 4 (1 correct fee/hour/12-month formula + 1 correct value). Values $40,200 and $40,500. Pilot credits must not be double counted.
- Comparability/projection assumption: 1 (observed within-language means assumed to transfer to the planned common mix/workload; no causal proof).
Bands: 13–15 correct usable calculations; 8–12.5 mostly correct with gaps; 3–7.5 valid partial arithmetic; 0–2.5 little auditable work.

### O1. Evidence map: 10 points
- Eight important accurate claim-to-location links: 1 each, up to 8. At least five distinct source IDs are requested; if fewer than five are represented, cap this portion at 6. Ordinary embedded prose citations alone do not form a map unless claims are explicitly organized as claim/evidence pairs.
- Correct observed/quoted/inferred tagging: 2 (2 for consistently correct tags on >=4 mapped claims; 1 for fewer correct tags or mixed tags; 0 absent).
Bands: 9–10 comprehensive; 5–8.5 useful partial map; 1–4.5 sparse; 0 absent.

### O2. Validation plan: 10 points
- Feasible duration <=12 weeks and respect for staffing/review limits: 2.
- Accountable roles for execution/review/decision: 2.
- Comparable speed and trust measures separately by language: 3 (1 speed, 1 trust by language, 1 common-workload/source and escalation/reopen controls).
- Measurable continue/stop/expand criteria aligned with charter: 3 (1 speed/budget/capacity; 1 >=90% each language; 1 consequential error/privacy stop or revision rule).
Half credit per element for a usable partial statement. Bands: 8–10 operational; 4–7.5 outline; 0.5–3.5 fragment; 0 absent. Exact role names or a particular experiment design are not required.

### O3. Sensitivity: 10 points
- Four vendor scenario means: 1 each = 4. At 20% Spanish: 8.90/9.00; at 40%: 9.80/9.50. Per value 0.5 valid formula and 0.5 correct result.
- Tie at 25% Spanish: 2 (1 correct equation/logic + 1 correct share).
- Implications for recommendation: 4 (2 explains speed ranking reversal at 25%; 2 explains whether overall choice changes while accounting for non-speed priorities and uncertainty). Any defensible unchanged or changed choice is eligible.
Bands: 8–10 complete sensitivity; 4–7.5 partial scenarios; 0.5–3.5 useful fragment; 0 absent.

## Snapshot record
For each snapshot, record M1/M2/M3/O1/O2/O3 scores, adjustments with quoted claim and source reference, total, observed output files, and one sentence describing the highest-value missing work. Never infer unsaved work. The six scores always sum to the reported total, and total lies between 0 and 100.
