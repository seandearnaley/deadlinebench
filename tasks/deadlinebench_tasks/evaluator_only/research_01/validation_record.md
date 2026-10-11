# Validation record: research_01
Evaluator-only packet QA, 11 October 2026. No participant execution trial was run.

- All nine source-file paths in source_manifest.csv resolve; seven distinct source IDs, with stable paragraph/row anchors. Inputs contain no evaluator answer files.
- Prompt has exactly three mandatory and three optional numbered requirements. Rubric weights are 30/25/15 and 10/10/10, total 100. Snapshot evaluation is explicitly independent at 90/180/300 seconds.
- Independently calculated from CSV: baseline 10.90, EmberSearch 9.35, CoveFind 9.25 weighted minutes; reductions 1.55/14.2202% and 1.65/15.1376%; year-one costs $40,200 and $40,500.
- Sensitivity validated: 20% Spanish 8.90/9.00; 40% 9.80/9.50; tie 25%. Trust gate references distinguish each language from aggregate accuracy.
- Contingency arithmetic checked: EmberSearch reaches $42,000; CoveFind reaches $43,500 and 160 setup hours. No deliberate arithmetic trap remains.
- Three decision options have explicit full-credit paths. Numerical errors receive method/correctness scoring without duplicate penalties; only consequential invalid claims have capped adjustments.
- answer_key.md and rubric.md SHA-256 values match rubric_lock.json. Both files and lock are read-only.
