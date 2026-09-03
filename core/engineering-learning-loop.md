# Engineering Learning Loop

## Purpose
Make repeated agent work improve the repository and harness instead of repeatedly paying the same discovery and quality costs.

## Learn from repeated friction
When a task exposes recurring ambiguity, missing observability, fragile setup, repeated bug class or unreliable agent behavior, ask whether the durable fix belongs in:
- code/architecture;
- tests/invariants/linters;
- developer tooling;
- repository documentation/system of record;
- UI/log/metric inspectability;
- harness/tool configuration;
- eval/regression suite.

Prefer durable mechanical constraints over another paragraph of instructions when a rule can be tested or linted.

## Reviewed learning candidates
Repeated session evidence can propose new project memory, a reusable Skill, an eval, or an invariant, but proposal is not promotion. For durable instruction/Skill changes, use `memory-governance.md` and `skill-authoring-and-evals.md`: create a reviewable candidate/diff, validate it, test it, and approve/promote explicitly when impact warrants it.

Do not let one successful or frustrating session rewrite the canonical method automatically.

## Measurable optimization
When improvement can be scored with a real evaluator or metric, load `experiment-optimization-loop.md`. Snapshot the baseline, protect the evaluator, change a bounded surface, measure, keep material wins, and revert regressions/inconclusive candidates. Use repeated trials for noisy metrics and retain a compact experiment ledger.

## Map, not giant manual
Keep entrypoint instructions short and navigational. Put detailed truth close to source: versioned docs, schemas, tests, ADRs, manifests and executable checks. Long instruction files become stale and consume scarce context.

## Agent-legibility
Where justified, make important system state inspectable through structured logs, traces, deterministic commands, screenshots/DOM, health endpoints, test fixtures or local dashboards. Observability should help humans too; do not build agent-only complexity without value.

## Golden principles and garbage collection
Maintain a small set of project-specific invariants that can be checked. Periodically inspect for repeated generated-code pathologies: duplicate helpers, dead flags, inconsistent APIs, weak tests, copy-paste abstractions, unowned files, stale docs and architectural boundary erosion.

Do not perform broad cleanup during an unrelated task. Record or schedule bounded maintenance when evidence shows accumulation.

## Feedback to evals
Every material escaped bug, repeated review comment or harness failure is a candidate regression/eval case. Add only durable lessons; do not encode one-off accidental details as universal rules.
