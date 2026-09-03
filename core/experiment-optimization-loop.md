# Experiment Optimization Loop

## Purpose
Turn repeated improvement work into a measurable keep-or-revert loop instead of accepting changes because they sound promising.

Use this for performance tuning, prompt/Skill improvement, model/harness tuning, build optimization, search/routing changes, or any task with a meaningful automated metric or judge.

## Preconditions
Define before iterating:
- objective and metric/judge;
- direction of improvement and minimum material delta;
- immutable or independently protected evaluator/oracle;
- mutable surface allowed to change;
- baseline snapshot/commit and baseline measurement;
- run budget, timeout, cost ceiling, and stop condition;
- guardrails that must never regress.

If the evaluator can be modified by the same candidate that is being scored, the loop is not trustworthy.

## Candidate loop

`BASELINE -> HYPOTHESIS -> SNAPSHOT -> CHANGE -> RUN -> MEASURE -> COMPARE -> KEEP | REVERT | INCONCLUSIVE -> LOG -> NEXT`

For every candidate:
1. state the hypothesis and expected mechanism;
2. create a reversible snapshot/commit/worktree;
3. make one coherent change or a deliberately identified bundle;
4. run the fixed evaluator under the same relevant conditions;
5. capture metric, guardrails, cost/latency, failures, and environment;
6. keep only a material improvement that does not violate guardrails;
7. revert a regression or broken candidate cleanly;
8. mark noisy/ambiguous outcomes inconclusive rather than forcing a win;
9. retain a compact experiment ledger so failed ideas are not rediscovered blindly.

## Stochastic measurements
For noisy systems, use repeated trials/seeds where the decision warrants it. Compare distributions/variance and confidence, not a lucky single run. Keep cost, latency, and quality as separate dimensions unless the user explicitly defines a composite objective.

## Search strategy
Balance exploitation of mechanisms that already improved the metric with bounded exploration of new classes of change. Negative results are useful evidence. Periodically inspect whether the current metric is being gamed or whether an important guardrail is missing.

## Stop contract
SKick does not adopt an unbounded "never stop" rule. Stop at the user/runtime budget, evidence saturation, target attainment, repeated non-improvements, a safety/validity blocker, or an explicit manual interruption. Persist the best known snapshot and the experiment ledger when the runtime supports it.

## Skill/harness improvement
When optimizing SKick or another Skill, evaluate trigger quality, workflow behavior, safety, task correctness, token/context cost, latency, and portability separately. Static package validation is a guardrail, not the optimization metric.
