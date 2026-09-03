# Evaluation Harness Integration

## Purpose
Evaluate engineering/research behavior with valid tasks, environments, scorers and trajectories instead of optimizing to a single opaque score.

## Evaluation layers
Keep separate:
1. static package/schema validation;
2. deterministic helper tests;
3. skill trigger/routing behavior;
4. task completion and correctness;
5. source/citation/evidence quality;
6. tool/action safety and policy compliance;
7. cost, tokens, latency and retries;
8. trajectory/process diagnostics;
9. external benchmark performance.

A pass at one layer does not imply a pass at another.

## External harness gate
Before using Inspect, Harbor/Terminal-Bench or another benchmark framework, record:
- harness and benchmark version/commit;
- dataset/task revision;
- container/environment image;
- scorer/oracle implementation;
- model/runtime/agent configuration;
- tool/network policy;
- sample count/seeds/retries;
- known task or oracle defects.

Run a benchmark's oracle/reference path where provided to verify the environment before interpreting agent failures. Do not compare scores across materially changed task/scorer revisions as if they are the same benchmark.

## Repeated runs
For stochastic agent work, use repeated trials where the decision warrants it. Report count, success distribution/variance, cost and latency separately. A one-run win is not a stable improvement.

## Trajectory analysis
When a regression matters, inspect the path, not only the final score:
`task interpretation -> retrieval/context -> tool selection -> actions -> recovery -> verification -> stop reason`.

Classify failure mechanism: missing capability, wrong evidence, context loss, tool misuse, invalid oracle, environment failure, planning error, coding defect, excessive exploration, premature stop, or unsafe action.

## Local runner relationship
`run_evals.py` remains a lightweight portable protocol runner. External harnesses are adapters for stronger isolation/benchmark suites, not mandatory dependencies. See `integrations/harnesses-and-evals.md`.

## Marginal Skill value experiments
For important Skill/plugin changes, compare at least the relevant conditions when feasible:
- baseline: no target Skill;
- skilled: exactly the target Skill;
- bundle/plugin: full real extension only when composition is part of the question.
Use paired tasks/stimuli and held-out cases. Repeated runs on the same stimulus estimate stochastic reliability but are not independent task samples; collapse/aggregate by distinct stimulus for gates that assume independence. Record activation/routing, correctness, tokens/context, latency, tool calls, safety and not-passed/failure reasons separately. A Skill should demonstrate marginal value, not merely existence.
