# Engineering Wayfinding and Slicing

## Purpose
Turn large ambiguous engineering work into resolved decisions, coherent interfaces and independently verifiable delivery slices without prematurely decomposing the problem into file-level tasks.

Use for major features, migrations, cross-cutting refactors, architecture decisions, prototypes, conflict resolution and long-horizon implementation.

## Decision frontier before task list
When a project is still ambiguous, map decisions and dependencies rather than asking a flat list of questions:

`environment facts -> product constraints -> architecture decisions -> interface decisions -> implementation choices`.

Research facts the agent can discover. Ask the user only for genuine preference/business decisions that cannot be derived. Resolve the currently-unblocked decision frontier first; downstream questions may disappear after an upstream choice.

## Domain context contract
For complex projects maintain a compact project vocabulary/context map when useful:
- canonical terms and definitions;
- invariants/state transitions;
- ownership seams/source-of-truth symbols;
- ADRs and consequential decisions;
- unresolved terminology conflicts;
- version/freshness anchors.

Consume the existing context before inventing synonyms. When code/docs/ADR conflict, surface the conflict instead of silently choosing one.

## Design it twice, selectively
For a consequential/hard-to-reverse interface or seam, generate at least two genuinely different feasible designs before committing. Vary the structure, not just names:
- minimum surface/deep module;
- flexibility/extensibility;
- common-case optimized;
- ports/adapters or data-oriented alternative.

Compare with the same criteria: caller knowledge, invariants, testability, change locality, migration cost, failure modes, performance and reversibility. Do not run multi-design fan-out for trivial helpers.

## Tracer-bullet slicing
Prefer vertical slices that traverse enough of the real system to prove architecture and user value:
- independently understandable;
- independently verifiable/demoable;
- small enough for one bounded context/work unit;
- exposes integration risks early;
- leaves the repository green where practical.

Avoid default horizontal decomposition such as "database ticket, backend ticket, frontend ticket" when no slice works end-to-end until all are done.

Represent meaningful dependencies as a DAG and make blockers explicit.

## Wide migration exception
When a change cannot be safely vertical-sliced, use:
`EXPAND -> MIGRATE IN BOUNDED BATCHES -> CONTRACT`.

Examples: schema/API compatibility, renamed protocol fields, cross-repo interface migration. Keep old/new paths compatible during migration when justified, validate each batch, then remove the compatibility layer after all consumers move.

## Prototype as a question instrument
A prototype should answer a named uncertainty, not become an accidental feature branch.

Record:
`question -> hypothesis -> cheapest representative prototype -> observation -> decision -> what is reusable -> what must be discarded`.

Use a UI prototype for interaction/visual uncertainty, a technical spike for architecture/performance/integration uncertainty, and an experiment for measurable behavior. Preserve useful evidence, not prototype debt.

## Intent-based merge/conflict resolution
For non-trivial conflicts, reconstruct intent from commits, issue/ticket, surrounding code/tests and architecture decisions before choosing lines. Ask:
- what behavior was each side protecting?
- are the intents compatible?
- which side is stale relative to current architecture/version?
- what regression test proves the merged intent?

Resolve behavior, then syntax. A clean textual merge can still destroy one side's purpose.

## Human-only procedure handoff
When a required step genuinely cannot/should not be automated (credentials, privileged dashboard action, physical/device step, production approval/cutover), generate an explicit operator procedure:
- prerequisites and exact target;
- safe ordered steps;
- expected observations;
- stop/failure conditions;
- rollback/recovery;
- evidence to return so the agent can continue.

Do not disguise a human-only blocker as automated success.
