# Validation record: research_02
Evaluator-only packet QA, 11 October 2026. No participant execution trial was run.

- All nine source-file paths in source_manifest.csv resolve; seven distinct source IDs, with stable paragraph/row anchors. Inputs contain no evaluator answer files.
- Prompt has exactly three mandatory and three optional numbered requirements. Rubric weights are 30/25/15 and 10/10/10, total 100. Snapshot evaluation is explicitly independent at 90/180/300 seconds.
- Independently calculated from CSV initial rows: baseline 12.00, SignalGate 7.00, RouteCraft 6.80 confirmed events/10,000. Avoided annual events 1,200/1,248; gross $114,000/$118,560; all-in $90,000/$92,000; net $24,000/$26,560.
- $60 sensitivity validated: net -$18,000/-$17,120; break-even avoided-event costs $75.00/$73.72. Follow-up rows are clearly separated from required initial calculations.
- Cost contingencies checked: SignalGate $114,000 and 400 initial hours; RouteCraft $99,500 and 820 annual hours. Observed SignalGate oversize p95 fails the ten-minute gate; its future fix is a supplier claim.
- Three decision options have explicit full-credit paths. Numerical errors receive method/correctness scoring without duplicate penalties; only consequential invalid claims have capped adjustments.
- answer_key.md and rubric.md SHA-256 values match rubric_lock.json. Both files and lock are read-only.
