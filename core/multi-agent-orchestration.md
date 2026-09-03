# Multi-Agent Orchestration

## Purpose
Use parallel/specialized agents when they reduce uncertainty or wall time without duplicating work, colliding on shared state, or diluting accountability.

## Decomposition
Split by independent evidence or responsibility boundaries, for example:
- official docs/source;
- repository/tests/history;
- empirical literature/data;
- security/adversarial review;
- implementation/testing;
- independent cold review.

Do not create agents merely to increase count.

## Independence contract for parallel implementation
Parallelize implementation only when each unit is independently:
- understandable from a bounded handoff;
- implementable without continuously editing the same mutable state;
- testable with a local or clearly owned check;
- mergeable with a defined dependency/base revision.

Prefer one worktree/isolated workspace per implementation unit when the host supports it. Record base commit, owned paths/symbols, dependency edges, expected artifacts/tests, and merge order. If two tasks must frequently touch the same files or state, serialize them or redesign the boundary instead of accepting collision-heavy parallelism.

Do not share one mutable checkout among simultaneous writers unless the harness provides deterministic locking/merging and the task truly benefits from it.

## DAG and budgets
Represent material branches in `execution-ledger.md`. Give each branch a bounded goal, source priority, budget, return contract, and dependency state. Detect cycles, duplicate scopes, and shared-write collisions before delegation.

## Minimal handoff
Send only what the worker needs:
`goal, scope/version, base revision, owned surface, known anchors, exclusions, budget, requested evidence/output`.

Avoid flooding every worker with the full research manual/history.

## Lifecycle hooks
When the runtime exposes lifecycle hooks (for example before/after tool use, failure, session start/end, subagent start/stop, or pre-compaction), use them as optional enforcement/observability seams for:
- dangerous-command or sensitive-file checks;
- format/lint/test triggers;
- checkpoint/state persistence;
- action-firewall policy checks;
- compact trace events.

Hook commands are executable code. Review their provenance, permissions, inputs/outputs, failure semantics and secret handling before enabling them. A hook must not silently expand the authority of the agent that triggered it.

## Merge
The coordinator must:
- deduplicate identical evidence origins;
- reconcile version/environment differences;
- preserve contradictions;
- detect missing branches;
- detect implementation collisions and stale-base edits;
- decide confidence from evidence, not agent voting;
- merge/rebase in a deterministic order and rerun integration checks.

## Independent review
For high-impact conclusions, a reviewer should preferably receive the claim/evidence scope without being anchored to the preferred conclusion. Ask it to falsify, find missing evidence, and classify confidence. For code review, load `verified-review-and-simplification.md`.

## Failure control
Bound delegation depth and retries. A worker failure should return a structured blocker and artifacts gathered so far; do not recursively spawn agents without a new information reason. Preserve a clean best-known workspace/snapshot so a failed branch can be discarded without contaminating others.
