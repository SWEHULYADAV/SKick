# SKick Evaluation Strategy

## Proof layers

SKick separates deterministic runtime tests from behavioral model evaluation and live-host verification. A pass in one layer never upgrades another layer automatically.

## Development set

The deterministic local suites under `evals/runtime-routing-evals.json`, `evals/claim-honesty-evals.json`, `evals/security-injection-evals.json`, `evals/ablation-evals.json`, `evals/prompt-intelligence-evals.json`, `evals/research-intelligence-evals.json`, `evals/teaming-evals.json`, and `evals/research-ablation-evals.json` are a **development set**. They are intentionally visible while runtime rules are implemented and therefore are not held-out behavioral evidence.

## Validation set

Existing trigger and portability definitions can be used as validation material for schema/routing regressions, but they must be treated as seen data once used for tuning. Provider/model runs should record which cases influenced policy changes.

## Held-out test set

The current v1.1 branch does **not** claim a clean held-out model-behavior result. A valid held-out set must be frozen after policy tuning and executed only for final comparison. It should include independent tasks from these categories:

- trivial/non-activation cases;
- tiny code changes;
- repository understanding and debugging;
- feature/refactor/architecture work;
- security review and injection resistance;
- current-information research;
- tool/capability routing with missing/restricted tools;
- evidence/claim honesty;
- package/install/migration;
- ambiguous/adversarial tasks;
- partial-permission and declarative-only hosts.

If those tasks are created by the same agent after seeing all development failures, the independence limitation must be recorded rather than hidden.

## Controlled comparison

Behavioral experiments should compare, where technically possible:

1. the same host/model without SKick;
2. released SKick v1;
3. the candidate v1.1 package.

Control model/version, task, repository revision, tool permissions, context, temperature/settings, and external-data window where possible. Use repeated trials for stochastic tasks. If SKick cannot be cleanly disabled in the active host, record `BASELINE_BLOCKED`.


## Prompt/research/teaming development suites

`evals/prompt-intelligence-evals.json`, `evals/research-intelligence-evals.json`, and `evals/teaming-evals.json` exercise deterministic interpretation/planning contracts, including over-expansion negatives, constraint locking, research escalation, safe security scope, and teaming selection. `evals/research-ablation-evals.json` compares direct-only, lateral, and disconfirmation planner configurations. These suites measure **planner behavior**, not factual research quality or model task success; their artifact therefore labels behavioral quality `NOT_MEASURED`.

A future behavioral research benchmark must execute real research with controlled tools, preserve raw evidence, score source quality/freshness/independence and conclusion correctness, and use a held-out task set before claiming that lateral or adversarial planning improves outcomes.


## Controlled security behavioral fixture

`tests/fixtures/security_auth_lab/` is an owned, deterministic cross-tenant authorization fixture with a reproducible vulnerable path and a fixed ownership check. `evals/security-behavioral-fixture.json` defines Red discovery, Blue remediation, and Purple retest tasks for an **external candidate runner**. Local unit tests prove only that the fixture demonstrates the intended before/after security property; `run_evals.py --list` proves only that the behavioral suite loads. Until a candidate runner + scorer/judge actually executes those tasks, Red/Blue/Purple behavioral success is `NOT_MEASURED`.

## Activation metrics

Deterministic task classification reports a confusion matrix (`tp`, `tn`, `fp`, `fn`) and depth-selection accuracy. These metrics prove the local classifier's behavior on its fixture set; they do not prove the host's native automatic Skill discovery uses the same classifier.

## Task-level reporting

Preserve raw runs. Comparisons must surface per-task win/loss/tie, regressions, critical security/claim-honesty failures, and variance when repeated samples exist. Do not approve a release from an improved global mean if a protected critical task regresses.

## Regression budgets

Until a controlled v1 behavioral baseline exists, do not invent numerical model-success thresholds. Deterministic invariants may still be release blockers: package/provenance completeness, zero false claim promotion in claim-firewall fixtures, no injection-guard regressions, generated-doc synchronization, and no activation false positives on the frozen deterministic routing suite.
