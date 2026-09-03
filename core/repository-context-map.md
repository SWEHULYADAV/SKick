# Repository Context Map

## Purpose
Give the agent a compact, refreshable map of a large codebase so it can navigate broadly without dumping the repository into context.

## Map contents
Build only what helps navigation:
- top-level components/packages/services;
- entrypoints and public interfaces;
- important symbols/signatures;
- dependency/import relationships;
- ownership boundaries and generated/vendor areas;
- tests/fixtures associated with components;
- configs/build/deploy/CI surfaces;
- security/trust boundaries when relevant.

## Preferred construction
When Serena is available, use symbol overviews/references to build the map. Otherwise use language indexes/LSP/source parsing and a dependency/reference graph. A graph-ranked Aider-style repository map is a useful fallback pattern for selecting high-value symbols under a token budget.

The map is navigation evidence, not behavior proof. Re-open source/tests before making a load-bearing claim.

## Coverage map
For Deep/Exhaustive work, mark each relevant unit:
`UNSEEN | SKIMMED | READ | EXECUTED/TESTED | OUT_OF_SCOPE`.

This prevents both accidental gaps and wasteful rereading. Coverage is scoped to the task; do not claim the whole repository was read when it was not.

## Refresh triggers
Invalidate affected map nodes when repository HEAD, lockfiles, generated code, branch, build graph or relevant configuration changes. Keep maps compact and regenerate rather than hand-maintaining stale prose.
