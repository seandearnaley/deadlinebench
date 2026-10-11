# Deadline-bound customer artifacts: incumbent eval coverage

Research date: 2026-10-11. Desk research from official documentation and vendor-owned source only. No product trial, signup, outreach, paid capture, or external mutation. This is a focused capability comparison, not an exhaustive market or absence claim.

## Bottom line

**An agent-success metric, an efficiency score, or a mandatory/optional rubric is not a strong standalone wedge.** These can already be implemented in Braintrust, LangSmith, or DeepEval. The narrowly differentiated contribution would be a reusable **deadline-bound artifact acceptance benchmark and pilot**: customer-calibrated work contracts, artifacts frozen at the actual delivery deadline, controlled delay/pressure scenarios, and evidence that adaptive cutbacks preserve required value.

The defensible claim is that the reviewed built-ins and examples do not, by themselves, supply this complete protocol. It is not that the platforms cannot support it. The benchmark should run on existing eval stacks and export normal scores/traces.

## What already exists

| Stack | Relevant documented capabilities | Already sufficient for | What the proposed protocol must add |
|---|---|---|---|
| Braintrust | Autoevals cover factuality, similarity, JSON, and SQL; they are span-level. Custom code and LLM judges accept output, expected values, metadata, and full traces. Scores support pass thresholds. Its agent behavior-spec cookbook grades independent evidence/action/recovery rules over trajectories. Latency, cost, tokens, and quality are observable. [B1–B4] | Artifact validators, acceptance rubrics, separate required checks, trajectory diagnostics, and regression comparisons. A contract or cutback rule can be encoded as a scorer today. | A standardized customer contract and real deadline cutoff; controlled deadline/delay cases; a report that tests whether adaptation improves accepted delivery rather than merely final quality or speed. |
| LangSmith | Code evaluators express business rules; LLM judges score subjective criteria; custom composite and summary evaluators aggregate results. AgentEvals supports strict, unordered, subset/superset tool trajectories and custom trajectory judges. Experiments expose latency percentiles, cost, tokens, error rates, and feedback. [L1–L3] | Outcome and process evals, required tool checks with flexible paths, customer-specific rubrics, and quality/latency comparisons. A custom evaluator can compute the entire proposed scoring rule. | The scenario suite, delivery-aware artifact capture, calibrated contract labels, and matched comparisons across deadlines. Latency statistics do not automatically say whether a usable artifact existed by its deadline. |
| DeepEval | Task Completion judges goal/outcome alignment over the run. Step Efficiency judges unnecessary actions. Plan Adherence judges execution against the agent's plan. DAG supports explicit gates before quality grading; custom BaseMetric implementations permit fully coded scoring. [D1–D5] | Off-the-shelf success/efficiency diagnostics plus a custom hard-requirements gate and customer-quality rubric. No novel metric framework is necessary. | A contract-aware temporal harness and acceptance data. Generic step minimization and adherence are useful diagnostics but are not the objective when optional enrichment is valuable and replanning is justified. |

## Important metric mismatches

- **Final success is not acceptance at the deadline.** DeepEval Task Completion assesses task/outcome alignment, with an explicit task available; it does not document a delivery timestamp gate in this metric. A strong final artifact received late can still have high ordinary outcome quality. [D1] This mismatch can be fixed with custom scoring in any of the three stacks.
- **Fewer steps is not always better.** DeepEval's Step Efficiency rubric penalizes work not strictly needed for task completion, including enrichment-only actions. A customer may value optional evidence or polish when enough time remains. Use it diagnostically, or customize it; do not treat it as the primary business outcome. [D2]
- **Following the original plan is not necessarily good adaptation.** DeepEval Plan Adherence can pass with score 1 when no plan is available and otherwise assesses fidelity to the stated plan. It must not become a reward for keeping obsolete optional work after a delay. Grade public decisions/actions against the contract and remaining time instead; no private chain-of-thought is needed. [D3]
- **A weighted average can conceal an unacceptable deliverable.** LangSmith supports weighted/summed composites, but the pilot should use an explicit required-item gate before optional quality. DeepEval DAG already supports this scoring structure; the arithmetic itself is not novel. [L1, D4]
- **An expected tool path is a diagnostic, not the customer contract.** AgentEvals allows flexible trajectory matching, reducing overconstraint. Yet retrieving the expected information does not prove that the final artifact is correct, usable, and delivered. Grade the artifact separately. [L2]

## Narrow benchmark/pilot contribution

Recommended scope: one repeatable artifact workflow, specifically a grounded technical-support reply or case-appropriate handoff assembled from approved evidence. Avoid a general agent leaderboard initially.

1. **Explicit work contract:** list mandatory requirements, prohibited failures, and weighted optional additions. Make it available to the agent before the run. Freeze it before comparing policies. Customer reviewers validate what counts as acceptable; deterministic validators handle structure and checkable facts, while calibrated human/LLM review handles qualitative requirements.
2. **Delivery-aware harness:** record start and actual artifact receipt/persistence time; freeze the last artifact validly delivered by deadline D. Declare whether partial/checkpoint submission is allowed. Do not credit hidden drafts or later edits. Include tool waits and artifact writing in elapsed time; run grading afterward so evaluator latency does not consume the agent's budget.
3. **Matched pressure cases:** repeat the same task/evidence under loose and tight deadlines and reproducible injected tool delays or failures. Compare the shipping policy, timeout/fallback, mandatory-first static scope, and deadline-aware optional-work cutbacks. Keep model, tools, evidence, and resource limits fixed; report repeated runs and uncertainty.
4. **Small scorecard:** (a) acceptance@D, requiring delivery plus every mandatory check; (b) mandatory omissions and late/no-delivery rates; (c) optional value conditional on acceptance; (d) time-to-first-acceptable delivery where checkpoints are allowed. Show acceptance and optional-value curves across deadline budgets. Never let optional points compensate for a missing mandatory item.
5. **Actionable diagnosis:** identify optional work retained too long, mandatory work improperly cut, failure to leave time for validation/delivery, and unjustified retries. Validate adaptive behavior through the matched policy comparison, rather than rewarding an explanation of a cutback.

**Pilot criterion:** the customer can use the result to select a policy or change a cutoff rule. The support-reply pilot in `pilot_offer.md` preregisters a stricter acceptance-at-deadline improvement threshold against the strongest simple baseline, with mandatory and escalation guardrails. Optional value is a separate diagnostic, not a substitute for that primary test. If ordinary outcome quality plus a simple latency threshold produces the same decisions, the narrower benchmark has not demonstrated added value.

This is a benchmark/data/calibration/integration opportunity. These sources alone do not establish willingness to pay, a durable moat, or that vendors lack equivalent private/customer-specific solutions.

## Primary sources

- **B1:** [Braintrust Autoevals](https://www.braintrust.dev/docs/evaluate/autoevals)
- **B2:** [Braintrust scorers and classifiers](https://www.braintrust.dev/docs/evaluate/write-scorers)
- **B3:** [Braintrust behavior-spec cookbook](https://www.braintrust.dev/docs/cookbook/recipes/AgentBehavior)
- **B4:** [Braintrust Observe: traces, dashboards, alerts, online scoring](https://www.braintrust.dev/product/observe)
- **L1:** [LangSmith evaluation types and evaluator implementations](https://docs.langchain.com/langsmith/evaluation-types)
- **L2:** [Official LangChain AgentEvals repository](https://github.com/langchain-ai/agentevals#evaluators)
- **L3:** [LangSmith experiment performance metrics](https://docs.langchain.com/langsmith/fetch-perf-metrics-experiment)
- **D1:** [DeepEval Task Completion](https://deepeval.com/docs/metrics-task-completion)
- **D2:** [DeepEval Step Efficiency](https://deepeval.com/docs/metrics-step-efficiency)
- **D3:** [DeepEval Plan Adherence](https://deepeval.com/docs/metrics-plan-adherence)
- **D4:** [DeepEval DAG metric](https://deepeval.com/docs/metrics-dag)
- **D5:** [DeepEval custom metrics](https://deepeval.com/docs/metrics-custom)
