# Domain and Codebase Design

## Purpose
Use precise language and durable seams so research, tests, and code changes refer to the same system model.

## Domain model
Maintain a compact project vocabulary when the task is complex enough to benefit from it:
- term and exact meaning;
- invariants;
- lifecycle/state transitions;
- actors/roles;
- edge cases and exceptions;
- source-of-truth code/docs/tests.

When prose and code disagree, surface the contradiction. Do not silently force the code to match the conversation or the conversation to match the code.

Prefer the project's established terms. Avoid inventing synonyms that fragment the model.

## Architecture decision records
Suggest or update an ADR only when the decision is:
- consequential and hard to reverse;
- surprising without context;
- a real trade-off among credible options.

Do not turn ADRs into a diary of minor implementation choices.

## Deep-module vocabulary
Use the following concepts consistently when they help:
- **module**: a cohesive unit that owns behavior/state;
- **interface**: everything callers must know, including signatures, invariants, errors, ordering, and performance expectations;
- **depth**: useful behavior hidden behind a small interface;
- **seam**: a place where behavior can be changed/substituted without editing callers;
- **adapter**: a translation layer between an external contract and the project's internal model;
- **leverage**: how much behavior/complexity a small interface controls;
- **locality**: how much knowledge a change requires across the codebase.

Prefer deep modules with small coherent interfaces over layers that merely pass data through.

## The interface is the test surface
A durable seam should be useful to real callers and testable from outside. If tests require private methods, internal database reads, or widespread mocks to observe behavior, reconsider the seam before multiplying tests.

## Deepening opportunities
Look for:
- repeated orchestration that can move behind one interface;
- multiple adapters revealing a real abstraction seam;
- duplicated policy spread across callers;
- invariants enforced in many places;
- cross-module knowledge that can become local;
- APIs that expose implementation detail without caller value.

Reject refactors that only rename or reshuffle code without reducing caller knowledge or change surface.

## Architecture vs implementation
Use this module to choose vocabulary and seams. Use `engineering-feedback-loops.md` for test/debug loops and `implementation-discipline.md` for edit scope.
## System architecture handoff
For substantial changes, pair this domain vocabulary with `system-design-and-architecture.md`. Domain terms/invariants define **what must remain true**; the architecture map defines **where that truth is owned, how state/control/data move, which interfaces expose it, and how a change propagates**. Use Serena-first semantic mapping when available to connect prose vocabulary to real symbols and callers.

Do not approve broad implementation while the owning seam, affected contracts or regression boundary remain materially unknown.


## Durable project context map
For complex projects, `engineering-wayfinding-and-slicing.md` may maintain a compact canonical vocabulary/context/ADR map. Consume it before inventing new terms and attach freshness anchors to code/config decisions so stale architecture context can be revalidated after material changes.
