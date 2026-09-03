# Universal Engineering Lifecycle

## Purpose
Make SKick an end-to-end engineering control plane rather than a research-only assistant. Cover the complete engineering lifecycle while loading only the branches and specialists the task actually needs.

## Main goal
Handle substantial engineering work from understanding through verified delivery:

`UNDERSTAND -> ENHANCE -> ROUTE CAPABILITIES -> RESEARCH -> MAP REPOSITORY/SYSTEM -> PLAN -> DESIGN -> IMPLEMENT -> VERIFY -> REVIEW -> PACKAGE/OPERATE -> LEARN`

## Entry gates
For non-trivial work, do these before broad execution:
1. resolve intent and run the SILENT `prompt-enhancement.md` pass;
2. use `capability-and-skill-routing.md` to select the best task-matched phase owners;
3. for repository/code work, apply the Serena-first gate from `serena-integration.md`;
4. for version-sensitive decisions, verify current primary/project evidence and search laterally;
5. for substantial changes, pass `system-design-and-architecture.md` before broad implementation;
6. define observable acceptance/verification criteria.

## Research before engineering commitment
Before choosing architecture, dependencies, APIs, security controls or a production implementation:
- inspect the existing project/system when one exists;
- resolve current versions/platform/runtime behavior;
- search laterally for renamed, historical, adjacent, competing and failure-mode terminology;
- use lateral thinking to generate alternate mechanisms/ideas from side clues, then verify them;
- read full relevant units plus clue-bearing neighboring material for Deep/Exhaustive work;
- identify contradictions, rejected approaches and operational evidence;
- convert findings into a compact engineering decision/plan.

Do not substitute generic best practices for project-specific evidence.

## Adaptive lifecycle by task type
- **Greenfield / major redesign**: research -> domain/invariants -> architecture alternatives -> interfaces/data/control/failure/operations -> filesystem/UI where relevant -> risk/test/package plan -> vertical implementation slices.
  - For ordinary new web products without a stronger constraint, load `python-vanilla-web-stack.md`: Python backend, vanilla HTML/CSS/JS frontend, root `app.py`, backend implementation in `backend/`, frontend implementation/assets in `frontend/`; deeper folders are need-based, not prescribed.
- **Feature**: semantic/public-seam map -> current API/version constraints -> change-impact graph -> acceptance criteria -> smallest vertical slice -> tests -> neighboring regression checks.
- **Bug**: reproduce red -> minimize -> competing mechanisms -> semantic callers/references -> targeted source/history/lateral research -> fix cause -> regression test -> broader checks.
- **Refactor**: establish preserved behavior/invariants -> map references -> choose the smallest coherent seam -> change -> differential/property/regression validation.
- **Migration**: version boundary -> breaking/deprecation matrix -> architecture/data impact -> staged reversible migration -> compatibility/config validation -> rollback path.
- **Performance/reliability**: workload/SLO -> measure -> bottleneck mechanism -> controlled intervention -> benchmark under matched conditions -> regression guard.
- **Security / adversarial engineering**: research prerequisites/primitive/path/bypasses and actual reachability -> map trust boundaries/observables/choke points -> prevent/detect/limit/respond/recover -> safe verification and residual-risk review.
- **Incident/production debugging**: preserve evidence -> timeline -> telemetry/log/trace analysis -> competing mechanisms -> containment when needed -> root cause -> remediation -> prevention/detection tests.
- **Data/ML**: source/lineage/quality -> methodology -> leakage/bias/eval design -> implementation -> reproducible evaluation -> monitoring.
- **Release/package/deploy**: build provenance -> configuration/secrets -> compatibility -> smoke/regression -> artifact integrity -> rollback/recovery.

## One workflow owner per phase
Do not stack duplicate methodologies. If a narrower Skill/plugin clearly owns a phase, delegate it through `capability-and-skill-routing.md` and `specialist-skill-orchestration.md`. SKick remains responsible for the objective, evidence, version boundaries, safety/trust, provenance, cross-phase coherence and final verification.

## Serena-first repository intelligence
For non-trivial repository work, check Serena before broad file-by-file reads. When available, use it for semantic repository exploration, symbols, references/call relationships and targeted edits; complement it with git/search/config/tests/runtime/browser tools. When unavailable, use the strongest native semantic/LSP/indexed fallback and continue without pretending Serena ran.

## Architecture and change-impact gate
For substantial implementation, be able to explain the entry point, owning component, affected interfaces/state/data, callers/dependencies, failure/trust boundaries, operational constraints and regression-detection plan. Keep architecture proportional to complexity; do not add speculative layers.

## Completion contract
Do not declare engineering work complete until the relevant chain is satisfied:
`acceptance criteria -> targeted verification -> broader relevant checks -> security/compatibility/performance checks as applicable -> diff/artifact review -> remaining risk`.

A compile, passing happy-path test, plausible screenshot or specialist's "done" message is not sufficient proof by itself.

## Harness engineering and feedback
For agent-heavy or repeatedly automated repositories, load `harness-and-runtime-intelligence.md` and `engineering-learning-loop.md`. Keep repository knowledge discoverable and mechanically enforced where possible. Feed repeated friction back into tests, invariants, observability, task environments and compact repository maps rather than a giant instruction manual.
