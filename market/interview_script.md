# Customer interview guide: deadline-bound support replies

Draft for a 25-minute research conversation with an AI engineering/agent-product lead and, ideally, a support-quality owner. No invitation has been sent. Use a neutral discovery tone; show the pilot concept only after asking about existing behavior.

## Opening (1 minute)

“We're studying how teams handle support-agent work that runs longer than customers can reasonably wait. I'd like to understand a recent case, your current acceptance rules, and what you already use to manage it. This is research; there is no product commitment.”

## Ask about evidence, not hypothetical enthusiasm (18 minutes)

1. Walk me through the most recent support-agent reply that arrived too late or was fast but unusable. What did the customer or teammate actually receive, and what happened next?
2. What deadline or latency budget applied? Is it a customer commitment, a UX target, a platform timeout, or a reviewer workflow? Where does the clock start and end? Can you show the relevant trace or written target?
3. How often has this happened in the last month, out of how many eligible requests? Who notices, and what measurable consequence follows? Separate abandonments, handoffs, rework, and complaints from guesses.
4. For that case, what absolutely had to be checked or included before the reply was acceptable? Which steps could have been omitted? Could two reviewers independently agree on that distinction?
5. What should happen when a required lookup is unavailable? Which cases permit a handoff, and which still require an answer? Would a generic acknowledgment satisfy the original request?
6. What already addresses this: model choice, parallel retrieval, cached answers, fixed priorities, timeouts, fallback replies, or human escalation? Show what improved and what still fails.
7. How do Braintrust, LangSmith, DeepEval, your provider's tests, or internal scripts evaluate this today? Can they score the exact artifact visible at the cutoff, jointly with its required content? What decision remains hard after seeing those results?
8. Who controls orchestration and cancellation? Which parts can a pilot change? How much overhead could a new controller add before becoming counterproductive?
9. What would you change if a test showed an adaptive policy beating your strongest simple baseline? Who owns that decision, data access, and any evaluation budget? What would make this assessment unnecessary?

## Show the concept and ask for a concrete next step (6 minutes)

“The proposed assessment compares your current workflow, fixed timeout/fallback, mandatory-first static scope, and optional-work cutbacks. It grades only a complete reply or case-appropriate handoff present at your actual cutoff, using your acceptance rules. It can use your existing eval stack.”

10. What is wrong or missing in that proposal? If it addresses a current decision, what de-identified cases, traces, and reviewer time could your team actually provide? What procurement or security step would be required? If another person owns the decision, who is that?

Do not treat compliments, hypothetical willingness, or an introduction as a sale. Do not ask for credentials or raw customer data during the interview.

## Capture and qualify

Record the real deadline, denominator/failure frequency, recent concrete consequence, acceptance rules, available control, incumbent workaround, decision owner, usable evidence, and an explicit next-step commitment or refusal. Keep quotes distinct from interpretations.

Advance only if the team has an active workflow decision, documented deadline pressure, a quality owner, and a permitted data route. Stop if no deadline binds, the team cannot control the policy, or existing evals plus a simple static timeout already settle the decision. Interview count alone is not validation; repeated independently evidenced pain plus an actual data/reviewer commitment is stronger evidence.
