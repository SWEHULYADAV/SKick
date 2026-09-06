# Repository and Code Intelligence Research

## Purpose
Treat the actual project as ground truth and investigate source/history efficiently.

## Start with project context
Inspect relevant:
- dependency manifests and lock files;
- runtime/toolchain versions;
- environment/configuration;
- entry points;
- relevant symbols and call sites;
- wrappers/adapters/internal abstractions;
- tests/fixtures;
- CI workflows;
- Docker/container/deployment configuration;
- custom patches/forks.

Examples include `package.json`, lockfiles, `pyproject.toml`, requirements/poetry files, Cargo manifests, `go.mod`, Maven/Gradle files, project files, Dockerfiles, and deployment manifests.

## Serena preference
When semantic repository capabilities are available, compare native index/LSP, symbol/reference APIs, Serena, and other providers by capability fit and proof quality before broad text-only scanning. Load `serena-integration.md` only when Serena is actually selected. Do not depend on any single provider.

## Targeted source-code reading
Do not read entire repositories by default.

Start from:
`symbol / error / API / configuration / test / issue-linked commit`
then expand:
`definition -> callers/references -> dependencies -> tests -> history`.

Use exact symbol search and semantic references where possible. Do not infer behavior from names alone; trace execution paths when needed.

## Full relevant-unit coverage
Targeted search locates the likely area; it is not the end of reading. For Deep/Exhaustive work, read the full relevant function/class/module/test/fixture/config/issue/PR unit and inspect neighboring code that can alter control flow, defaults, cleanup, error handling, or version behavior.

Run a small-clue sweep over defaults, feature flags, TODO/FIXME/deprecation notes, warnings/error strings, examples, odd regression tests, CI matrices, migration notes, and linked history. Expand farther only when a dependency/contradiction/clue justifies it.

## Tests as implementation evidence
Search unit/integration/regression/e2e tests and fixtures. For a fixed bug, inspect tests added with the patch; they often define the intended behavior better than prose.

## Git archaeology
When behavior differs across versions or rationale matters:
- identify the introducing/fixing/removing commit;
- inspect blame/history around relevant lines/symbols;
- compare tags/branches;
- search commit messages for `fix`, `regression`, `breaking`, `remove`, `deprecate`, `workaround`, `race`, `performance`, and `compatibility`;
- inspect linked issues/PRs and regression tests.

## Rejected approaches
Research proposals or PRs deliberately rejected by maintainers. Architectural constraints often appear only in `why not`, `not planned`, `won't fix`, RFC, or maintainer discussion.

## Code search engines
When native repo navigation is insufficient, use repository/code-search services for discovery. Verify important findings against the actual repository/tag/version.

## Local vs external evidence loop
`inspect project -> resolve actual versions/environment -> external research -> inspect relevant local implementation -> compare -> identify smallest correct action -> test`.

External docs inform the project; project reality constrains the recommendation.

## Project-specific conflict rule
If generic docs say architecture A but the repository uses wrapper/custom architecture B, analyze B. Do not force generic best practice onto incompatible local abstractions.

## Repository context map
For large repositories, load `repository-context-map.md`. Build a compact symbol/component/dependency/coverage map first, then use it to choose full relevant units. The map saves context; it never substitutes for reading source/tests behind a load-bearing conclusion.
