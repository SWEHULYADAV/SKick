# System Design and Architecture Gate

## Purpose
Prevent premature coding. Build the smallest accurate system model needed to make implementation decisions, then preserve that model through interfaces, tests and operational checks.

Use this module for new systems, major features/redesigns, migrations, distributed/data-heavy work, security-sensitive changes, or any change whose blast radius is not obvious.

## Existing-system map
Before broad implementation in an existing project, establish enough of the following to explain how the change actually fits:
- system/product objective and acceptance criteria;
- repository boundaries and deployable/runtime units;
- entry points, major components/modules and ownership seams;
- public/internal interfaces, schemas, protocols and compatibility contracts;
- data flow, control flow, state transitions and persistence;
- dependencies and external services;
- configuration, secrets and environment boundaries;
- concurrency, queues/caches/background work where relevant;
- authentication/authorization and trust boundaries where relevant;
- failure modes, retries/idempotency/rollback/recovery;
- observability: logs, metrics, traces, alerts and debuggability;
- performance/SLO/resource constraints;
- tests, build/release/deployment path and operational constraints.

Use the best observed semantic repository capability for code structure and references (for example native indexes/LSP/symbol APIs, Serena, or semantic search), then use narrower repository search, tests, config, runtime evidence and external research for what that capability cannot prove.

## Change-impact graph
For a meaningful change, identify:

`requested behavior -> entry/public seam -> owning symbols/modules -> callers/dependents -> state/data contracts -> failure/security/performance consequences -> tests/operations`

Do not read every file. Expand from the public seam and semantic references until the material impact boundary is stable.

## Greenfield architecture gate
Before choosing implementation details for a substantial new system:
1. state goals, non-goals, constraints and scale assumptions;
2. identify domain model/invariants and primary user/system flows;
3. research current platform/library constraints where they can change the design;
4. generate at least two credible alternatives for consequential decisions;
5. compare simplicity, reversibility, operability, security, performance, ecosystem fit and maintenance cost;
6. choose the smallest architecture that satisfies the evidence-backed needs;
7. define component boundaries, interfaces, data/state/control flow and failure handling;
8. define test/evaluation, observability, deployment/package and rollback strategy;
9. implement in vertical slices that validate architecture assumptions early.

## Existing-system architecture gate
Before a large edit, be able to answer internally:
- Where does the behavior enter the system?
- Which component truly owns it?
- What contracts/invariants must not change?
- Which callers/data/state/deploy units are affected?
- What is the smallest coherent seam for the change?
- How will a regression be detected?

If these are unknown because the repository cannot be inspected, keep the implementation boundary narrow and state the uncertainty rather than inventing architecture.

## ADR threshold
Record or recommend an architecture decision record only for consequential, difficult-to-reverse, or surprising trade-offs. Capture context, credible alternatives, chosen option, reasons, consequences and revisit triggers. Do not create ADRs for routine implementation details.

## Simplicity rule
Architecture depth must scale with risk and complexity. A small script does not need distributed-system ceremony. Avoid framework proliferation, speculative layers and abstractions without a current seam or demonstrated variation pressure.

## Verification
Architecture is not validated by a diagram alone. Check it through the relevant combination of tests, builds, runtime traces/logs, dependency boundaries, schema/API compatibility, browser behavior, benchmarks, security checks and deployment/package evidence.
