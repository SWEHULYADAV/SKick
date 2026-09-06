# Code Integration and Implementation

## Principle
Research informs implementation; the actual project constrains implementation; tests verify implementation.

## External-research -> code loop

`understand -> inspect project -> resolve versions/environment -> research current behavior -> inspect implementation -> define success -> smallest correct change -> red/green verification -> review -> regression check`

Load `implementation-discipline.md` before non-trivial edits and `engineering-feedback-loops.md` for bugs, TDD, prototypes, or review.

## New-project / major-redesign gate
For substantial greenfield work or a major redesign, load `project-planning-and-structure.md` and complete research/context -> architecture/UI/filesystem/test planning before broad production code. Do not let framework scaffolding substitute for understanding the product.

## Before editing
- inspect existing abstractions and project conventions;
- identify callers/references, public seams, and relevant tests;
- confirm dependency/runtime version;
- understand configuration/deployment constraints;
- define observable success criteria and non-goals;
- load Serena integration and prefer semantic tools when available;
- avoid unnecessary rewrites and dependencies.

## Editing rules
- make the smallest sufficient change unless broader redesign is justified by evidence;
- every changed line should trace to the requested behavior, a necessary support change, or a verified regression guard;
- preserve backward compatibility when required;
- follow existing style/abstractions;
- do not modify code for research-only tasks;
- add/update tests, especially regression tests for bugs;
- prefer a deep/simple interface over leaking complexity across callers;
- document important version-specific behavior when useful.

## Reference-aware editing
When an appropriate semantic repository capability is available, prefer reference-aware symbol operations for targeted changes/refactors when they reduce risk. Inspect definitions/references before modification. Use text edits when semantic tooling is unavailable, weaker, or inappropriate; provider choice follows capability fit.

## Bug and TDD discipline
When feasible, establish a failing observable before constructing a large theory. Minimize the reproduction, rank hypotheses by distinguishing power, instrument the boundary that separates them, fix the mechanism, and preserve a regression test.

For feature work, prefer vertical slices: one meaningful failing test through a public interface/seam -> minimal implementation -> green -> next behavior. Do not batch many red tests while the architecture is still uncertain.

## Web application changes
If behavior is rendered or interactive, load `webapp-validation.md`. A unit test or build success is not sufficient proof that the browser interaction/layout actually works.

## Verification
Run the most relevant available checks:
- targeted unit/regression tests;
- integration/e2e/browser checks when behavior crosses boundaries;
- typecheck/build/lint/format checks as project convention requires;
- relevant runtime/reproduction checks;
- inspect the final diff for scope creep and accidental changes;
- review both requirement/spec compliance and engineering quality.

Compilation success alone is not semantic proof.

## Failure handling
If tests fail, investigate rather than blindly editing:
- confirm failure relevance;
- inspect version/environment mismatch;
- inspect hidden flags/config;
- trace call path and fixtures;
- compare expected behavior with source/docs/tests;
- distinguish a broken test oracle from a real regression.

## Remaining risk
Report untested paths, environment-specific uncertainty, migration concerns, external dependencies, browser/platform gaps, and any verification not performed.
