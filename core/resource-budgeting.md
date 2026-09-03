# Resource Budgeting

## Purpose
Control token, time, tool-call, data-volume, browser, subagent, and external monetary cost while preserving evidence quality.

## Budget contract
For extended work, define only the dimensions that matter:

```text
TOKENS_TOTAL / FINAL_RESERVE
WALL_TIME
WEB_QUERIES
SOURCE_READS
TOOL_CALLS
BROWSER_RUNS
SUBAGENT_CALLS
EXTERNAL_COST
STORAGE / ARTIFACT SIZE
```

Use `schemas/budget.schema.json` when persistent state is useful.

## Allocation
Allocate budget by unresolved risk/information value rather than equally across categories. Keep a reserve for contradiction resolution, testing, and final synthesis.

A possible initial allocation for deep technical work is discovery < primary verification + local source/tests < challenge + validation. Do not encode fixed percentages as universal truth.

## Reallocation
Increase a branch budget when it reveals:
- a material contradiction;
- a version boundary;
- a security/safety issue;
- a failed reproduction;
- an assumption that changes architecture.

Cut/reclaim a branch when new queries are duplicative or no longer decision-relevant.

## Cost gates
External paid APIs, model generation, market feeds, remote compute, or other billable services require an explicit cost/authorization path when the runtime would incur new user-visible spend.

## Final reserve
Do not spend the entire context/tool budget on discovery. Preserve enough capacity to verify load-bearing claims, run tests, reconcile contradictions, and report accurately.

## Measurement labels
Use `Measured locally | Provider-reported | Benchmarked | Inferred` for resource claims. Never claim token/cost savings from architecture alone without measurement.
