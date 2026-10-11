# Can your support agent deliver an acceptable reply by its deadline?

**Draft pilot offer | For an AI engineering lead and support-quality owner**

## The decision

Choose the simplest policy that produces a grounded, usable support reply within your actual response budget. Test whether adapting optional work improves acceptance beyond your current workflow and a strong fixed-priority timeout policy.

## Scope

One read-only technical-support workflow. Start with separate calibration cases, then at least 100 de-identified held-out cases and representative timing traces. Your team defines the real deadline, required answer/handoff rules, and which work is optional. A complete draft must be received by the cutoff; acknowledgments, initial tokens, and late results do not count.

Compare four policies with the same model, evidence, tools, and checkpoint capability:

- Your shipping workflow
- Shipping workflow with fixed timeout and an approved fallback
- Mandatory-first scope, with optional work chosen before execution
- Mandatory-first scope, with optional work adjusted to remaining time

Use matched normal and tail-latency conditions. Report the representative case mix separately from injected stress tests. Include controller, tool, and final-output overhead.

## What you provide

A workflow owner, a support reviewer, the written response target, approved/de-identified cases and evidence, and permission to inspect their traces. Any execution uses a separately agreed data route and compute budget; this draft authorizes no data transfer, model spend, or production change.

## What you receive

A reusable acceptance contract and test pack for your existing eval stack; a policy comparison at the real deadline; reviewed examples of failures and cutbacks; and a recommendation to keep the current approach, adopt a simpler baseline, or test an adaptive policy further.

## Agree the decision rule before testing

Proposed success: at least a 10-percentage-point increase in accepted-on-time artifacts over the strongest simple baseline at your actual deadline, with a paired 95% uncertainty interval excluding zero. Optional quality is reported separately. Answer-required cases cannot pass through unnecessary escalation.

Required safeguards: no observed critical unsupported claim, mandatory-check omission, or policy bypass; no increase in unnecessary handoffs. This bounded test is not a production safety certification.

Stop if adaptation fails to beat the simple baseline, the deadline does not bind, gains require unrealistic delays, or overhead removes them. An uncertain result is reported as inconclusive. Do not expand the experiment automatically.

## Before starting

Confirm acceptance rules, case mix, deadline, review owner, permitted data/compute scope, and success thresholds. Timing and commercial terms remain to be agreed. No price, performance guarantee, or claimed customer result is included.
