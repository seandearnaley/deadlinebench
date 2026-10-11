# DeadlineBench: narrow customer-wedge validation

Research date: 11 October 2026. Desk research only. No interviews, outreach, signups, live customer tests, paid API calls, or evidence of willingness to pay.

## Recommendation

Test one hypothesis: **AI engineering teams at B2B software companies that own a multi-tool technical-support agent need help choosing a deadline policy that delivers an acceptable, grounded reply or justified handoff before their actual response cutoff.** The first deliverable should be a customer-specific offline test pack and decision report that works inside their existing eval stack.

The proposed next research step is evidence-gathering interviews and one bounded pilot. The current evidence does not support building a platform. Public documentation establishes latency and quality constraints; it does not establish an unmet commercial need. Mandatory/optional contracts, custom quality gates, and latency metrics are already readily expressible in incumbent tools.

## Three concrete buyer segments

### 1. Owners of multi-tool technical-support agents at B2B SaaS companies — selected

**Likely buyer/user:** AI engineering or agent-product lead; support operations/quality lead adjudicates the reply. This is a role hypothesis, not a verified budget owner.

**Primary documented constraints:** Salesforce distinguishes first-token, last-token, and full end-to-end latency. Its current guidance treats roughly 6–10 seconds as acceptable for complex chat requests and waits beyond roughly 20 seconds as concerning, explicitly as guidelines rather than a guaranteed SLA. Its Agent API has a documented 120-second timeout. These are different limits; the API timeout is not a desirable customer-experience target. [Salesforce latency guide](https://help.salesforce.com/s/articleView?id=005391243&language=en_US&type=1), [Agent API considerations](https://developer.salesforce.com/docs/ai/agentforce/guide/agent-api-considerations.html).

Intercom documents configured first/next-response and resolution targets, including customer-specific response commitments. Those SLA definitions primarily describe teammate/ticket operations, so they do not prove that Fin has a particular autonomous-reply deadline. Its guidance separately covers using trusted content and required escalation behavior. [Intercom SLAs](https://www.intercom.com/help/en/articles/6546152-set-slas-for-conversations-and-tickets), [Fin guidance](https://www.intercom.com/help/en/articles/10560969-fin-guidance-best-practices), [Fin escalation rules](https://www.intercom.com/help/en/articles/12396892-manage-fin-ai-agent-s-escalation-guidance-and-rules).

**Candidate work contract, to validate with the customer:** mandatory = answer the actual question from approved evidence, include required troubleshooting steps and provenance, respect support/security policy, or produce a case-appropriate handoff with its reason and required context. Optional = extra related-document searches, secondary diagnostics, alternatives, longer explanations, or polishing. Which lookups are mandatory is case-dependent; a needed account-entitlement check cannot become optional merely because it is slow.

**Why first:** a bounded, inspectable text artifact; repeatable historical cases; existing quality owners; clear latency instrumentation; and potentially controllable orchestration. Restrict entry to teams that actually own sequencing/timeouts/cancellation. A customer using only a managed agent UI may have no control over the intervention being tested.

**Main risk:** a fixed mandatory-first policy, a smaller model, parallel retrieval, or existing timeout/fallback logic may solve the problem. Observed tail latency might be entirely infrastructural. No differentiation is established until the adaptive policy beats these practical alternatives.

### 2. SRE/platform teams operating incident-communication copilots

**Likely buyer/user:** platform/SRE engineering lead and incident communications owner.

**Primary documented constraints:** Atlassian advises early acknowledgment, known impact, promised further updates, roughly 30-minute updates where appropriate, accurate plain-language communication, and consistency across channels. PagerDuty describes committing to the maximum time before the next update and recommends a default 30-minute interval while warning that early suspicions can be wrong. These are published operating practices, not universal contractual guarantees. [Atlassian incident communication](https://support.atlassian.com/statuspage/docs/incident-communication-tips/), [PagerDuty update frequency](https://docs.pagerduty.com/ops-guides/stakeholder-comms-guide/frequency).

**Candidate contract:** mandatory = currently supported impact, current response state, uncertainty, and next-update time in an approved draft; optional = expanded timeline, wider log correlation, alternative causal hypotheses, or extra stakeholder variants. Root cause cannot be invented to fill space.

**Opportunity/risk:** a deadline-bound artifact and meaningful cutbacks are natural. However, the deadline is a wall-clock communication cadence, often much longer than a model call. Human review, evolving evidence, and publication authority may dominate. A pilot must demonstrate that drafting/retrieval time genuinely threatens the remaining update budget; otherwise a timer and template suffice. Keep any pilot draft-only, with no automatic publication.

### 3. Engineering teams building voice/contact-center agents with tool lookups

**Likely buyer/user:** voice-agent engineering lead or contact-center automation product lead.

**Primary documented constraints:** Vapi's API tool has a default 20-second wait and configurable bounds; timeouts do not establish whether the destination operation completed. Its documented tests combine required latency limits and structured success criteria, while its reliability guide requires truthful failure handling and safe retry behavior. These tool waits differ from a conversational response target. [Vapi tool reliability](https://docs.vapi.ai/tools/api-request/reliability), [Vapi simulation criteria](https://docs.vapi.ai/observability/simulations-advanced).

**Candidate contract:** mandatory = a supported answer or truthful failure/handoff, no unconfirmed success claim, and any required identity/business-rule checks; optional = extra knowledge lookups or richer explanations. Avoid transactional or regulated flows in an initial experiment.

**Why defer:** tight latency matters, but full speech pipelines, endpointing, interruptions, and tool state make attribution harder. Vapi already couples correctness checks with required latency gates, so generic quality-plus-latency testing is particularly weak differentiation. Its documented mocks replace result strings but do not add network delay or a real timeout; controlled tool-delay tests are a possible implementation gap, not proof of a market.

## What must be distinctive, if anything

The prior-art overlap flagged in the existing research rules out pitching time-aware agent evaluation as a new category. No novelty claim is made for an on-time-success metric, a mandatory/optional rubric, or deadline-aware scheduling.

A narrowly useful contribution could be the combination of:

1. A customer-approved acceptance contract, including exactly which fallback/handoff modes are acceptable for each case.
2. A complete, versioned artifact frozen at the actual client-visible cutoff. Progress text, first tokens, late files, and retrospective reconstructions do not count.
3. Matched cases with realistic tool-delay/error conditions and a measured output/packaging reserve; adaptation may drop optional work but never required checks.
4. A comparison against the strongest cheap policy, using customer quality judgments and failure explanations to decide whether to change the shipping workflow.

This combination can still be implemented with a small adapter and incumbent evaluators. Defensibility, if it emerges, would need to come from hard-to-recreate workflow cases, calibrated acceptance labels, and repeatable decisions customers value. Desk research has not established any of these assets.

## Existing metrics: sufficiency test

Braintrust, LangSmith, and DeepEval can already express task outcomes and custom rubrics. Braintrust's behavior-spec evaluator and DeepEval's branching DAG further weaken claims that essential-vs-extra requirements need a new product. Salesforce itself already reports completeness, conciseness, instruction adherence, and output latency. [Salesforce testing API](https://developer.salesforce.com/docs/ai/agentforce/guide/testing-api-use-results.html).

The primary score is simple: fraction of cases with a complete artifact received by deadline D that passes every required acceptance check. Existing stacks suffice if they capture the relevant artifact and timestamps, then evaluate that snapshot. A custom evaluator can gate optional scores on mandatory passes and on-time receipt. The missing work is principally experimental design, trustworthy cutoff capture, and customer-specific adjudication. See `vendor_metrics.md` for the official-doc comparison.

**Substitution test:** first ask the team to reproduce this decision using their existing stack and a fixed-priority timeout policy. If they can get the same actionable answer cheaply, stop pursuing a separate product. An integration or narrowly scoped assessment may still be useful, but even that requires evidence of a buyer and budget.

## Pilot design and stopping criteria

See `pilot_offer.md` for the one-page draft and `interview_script.md` for the interview guide. Proposed thresholds below are decision rules, not achieved results or industry benchmarks.

- Entry: one real support workflow, an actual response deadline, historical misses, controllable orchestration, a quality owner, and permissioned/de-identified data.
- Baselines: current shipping pipeline; that pipeline plus timeout/fallback; fixed mandatory-first scope with optional work chosen before the run; adaptive optional-work cutbacks. Use identical model/tool access, artifact-checkpoint capabilities, and acceptance rules.
- Test: calibrate on separate cases; lock the contract and customer deadline before held-out evaluation. Evaluate at least 100 held-out cases with paired normal/tail conditions. Report the representative historical mix as primary; oversampled or artificially severe stress cases are diagnostic only.
- Capture: monotonic start and cutoff; end-to-end artifact receipt/persistence; latest complete approved-format version at cutoff; model/tool/packaging timing and any work after cutoff. Charge full controller overhead to the adaptive policy. Never score a late result as on-time.
- Primary proposed go criterion: at least a 10-percentage-point gain in accepted-on-time artifacts over the strongest simple baseline at the customer's actual deadline, with a case-clustered paired 95% interval excluding zero. Keep answer-required and handoff-allowed cases separate; an unnecessary escalation is a failed answer-required case.
- Guardrails: no observed critical unsupported claim, policy bypass, or skipped mandatory check; no increase in unnecessary handoffs. Zero observed failures in this small pilot is not a production safety guarantee. Report optional quality separately, so an acceptance gain cannot conceal degraded usefulness.
- Failure: the actual deadline seldom binds; adaptation cannot beat the strong static baseline; gains exist only under unrealistic delays; controller overhead removes the benefit; required work cannot reliably fit; or the result does not change a concrete customer release/configuration decision. If uncertainty remains, label the pilot inconclusive and do not expand it automatically.

The earlier local pilot was a virtual-time scheduler simulation. It demonstrated sensitivity to assumed scheduling/utility choices, assessed no model-produced customer artifact, and measured no willingness to pay. Its numbers should not appear in customer collateral as real-agent or commercial performance.

## Research status

These materials contain desk research and drafts. No customer interviews or customer pilots have been conducted. A future pilot would need a defined data route and compute budget. No price, revenue estimate, market size, customer interest, or purchase intent is claimed.
