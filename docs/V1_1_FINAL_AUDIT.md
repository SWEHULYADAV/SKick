# SKick v1.1 Final Second-Pass Audit

This document records the independent second-pass release audit for SKick v1.1. It is an evidence boundary, not a marketing claim. Source validation, candidate package construction, clean extraction, packaged-copy validation, unit tests, deterministic local evaluations, distribution validation, and archive-hygiene checks were completed before the release status below was promoted.

## Architecture and dependency map

SKick v1.1 preserves the v1 architecture instead of replacing it:

`SKILL.md -> core/ -> runtime + schemas -> scripts -> INSTALLATION_MANIFEST.json -> thin adapters -> generated docs -> evals/tests/release tooling`

Canonical ownership is intentionally split by concern:

- `SKILL.md` is the lean declarative control plane and progressive-loading index.
- `core/` (73 Markdown modules) is the canonical portable methodology and declarative fallback.
- `runtime/` (16 Python modules plus structured policy/catalog data) owns deterministic task interpretation, depth, capability state, module compilation, evidence/claim state, research planning/ledger, teaming plans, and reporting when code execution is available.
- `schemas/` (18 JSON schemas) defines structured contracts. Runtime-state instances are actively validated by `runtime/schema_validation.py`; several other schemas are validated at package/test boundaries rather than mechanically intercepting every host action.
- `scripts/` owns installation, doctor/status tooling, deterministic evaluation, generated metadata, package validation, provenance, distribution building, and release auditing.
- `INSTALLATION_MANIFEST.json` is the single compatibility/install source of truth. Platform catalog, platform audit, activation matrix, and adapter install blocks are downstream/generated surfaces.
- `adapters/` contains host transport differences only. Canonical engineering/research methodology does not fork into adapters.
- `evals/` contains deterministic local suites plus external-runner behavioral definitions. Definitions are not treated as evidence that a model passed them.
- `tests/` exercises runtime, installer, compatibility, migration, security fixture, release, schema, generation, and declarative-fallback behavior.

There are no new third-party runtime dependencies in v1.1; the executable runtime remains Python-standard-library based. Optional external tools remain capability providers rather than mandatory dependencies.

## Loose-ends audit

The second pass searched code and maintained documentation for TODO/FIXME/TEMP/HACK/PLACEHOLDER/NOT IMPLEMENTED/FUTURE/STUB/MOCK/DUMMY/UNUSED/DEPRECATED/LEGACY/UNKNOWN/ASSUME/HARDCODED patterns. Material findings were traced rather than mechanically deleted.

Resolved release-relevant loose ends include:

- vNext/v1.0 development identity was replaced by canonical v1.1 identity while historical v1.0 evidence was preserved as history.
- claim verification no longer accepts unrelated passing evidence.
- current-fact and live-platform claims have stronger proof requirements.
- positive user constraints are locked by prompt interpretation instead of only negative constraints.
- runtime probes no longer create a missing project directory as a side effect.
- candidate evaluators no longer receive deterministic scoring oracles.
- installer path resolution rejects package symlinks and destination escapes.
- DOC_VERIFIED platform records accept and validate current first-party documentation, support, official repositories, or first-party release notes.
- active Serena-first and universal starter-stack policy residue was removed; capability/project fit now owns routing.

Historical, compatibility, and explicit `UNKNOWN`/`DEPRECATED` terminology that describes real states remains intentionally present.

## Specification vs implementation

| Capability | v1.1 status | Evidence boundary |
| --- | --- | --- |
| Task/prompt interpretation and constraint locking | EXECUTABLE + TESTED | deterministic runtime/tests |
| quick/standard/deep/exhaustive selection | EXECUTABLE + TESTED | deterministic runtime/tests; host auto-activation remains host-dependent |
| Capability discovery/state | EXECUTABLE + TESTED where locally observable | unknown stays unknown for host-only capabilities |
| Capability routing | EXECUTABLE + TESTED planner | actual host tool execution remains host-controlled |
| Module/context compilation and budget | EXECUTABLE + TESTED | token counts are estimates unless host tokenizer data exists |
| Evidence ledger and claim firewall | EXECUTABLE + TESTED | cannot mechanically intercept arbitrary prose on declarative-only hosts |
| Prompt-intelligence modes | EXECUTABLE + TESTED | output quality of a downstream model is NOT_MEASURED |
| Research question/source/lateral/disconfirmation planner | EXECUTABLE + TESTED | planner quality is deterministic; actual web/repo research uses host capabilities |
| Research findings, lineage, contradiction/frontier state | EXECUTABLE + TESTED | facts require evidence; source independence is lineage-aware |
| Red/Blue/Purple/Black planning | EXECUTABLE + TESTED planner | candidate-agent security behavior is not claimed from planner tests |
| Controlled authorization security fixture | TESTED locally | external candidate-model discovery/remediation remains NOT_MEASURED |
| Installation/doctor/status states | EXECUTABLE + TESTED | COPIED/INSTALLED/DISCOVERED/INVOKABLE/LIVE-TESTED remain distinct |
| Evaluation scoring/comparison | EXECUTABLE + TESTED | candidate self-report is not scoring authority |
| Compatibility registry/generation | EXECUTABLE + TESTED metadata | LIVE_TESTED = 0 external routes in this release environment |
| Declarative fallback | TESTED structurally | depends on host-model compliance, not runtime enforcement |
| Baseline vs v1 vs v1.1 model task success | NOT_MEASURED | equivalent clean model runners were unavailable |
| Cross-model behavioral robustness | NOT_MEASURED | external model/runtime infrastructure unavailable |

## Schema enforcement map

Schemas are not all described as equally enforced:

- **Runtime-active:** `runtime-state.schema.json` is applied to actual runtime state via the standard-library validator. Nested task interpretation, evidence and claim structures are checked through that state contract.
- **Runtime/test-bound contracts:** `task-interpretation`, `research-plan`, `teaming-plan`, `research-finding`, `claim`, `module-plan`, `project-policy`, and evaluation-result schemas are exercised by producers/consumers and regression tests, but do not claim universal host-side interception.
- **Package/release contracts:** installation, artifact/provenance, integration, MCP, budget/evidence-lock, task-state and trace schemas are validated at package/release/static boundaries or used as long-horizon/declarative contracts.

A schema file parsing as JSON is never reported as proof that every runtime instance is enforced by that schema.

## Platform compatibility second pass

The canonical registry contains 62 audited route records. Current evidence states are generated from the manifest, not a minimum-count release invariant: 45 DOC_VERIFIED, 11 HOST_DEPENDENT, 3 COMMUNITY_VERIFIED, 2 GENERIC_PROMPT_FALLBACK, 1 UNKNOWN, and LIVE_TESTED = 0.

The second pass rechecked first-party evidence and corrected materially stale/over-broad transport claims, including Cursor manual slash invocation, Kiro slash/automatic activation, Gemini CLI model-driven discovery/consent semantics, TRAE `.agents/skills` evidence, and current OpenAI Skill/plugin documentation. No external platform was promoted to LIVE_TESTED because no real external host install/discovery/invocation/task run was performed in this environment.

## Security and claim-firewall adversarial review

The second pass attempted to over-promote results using unrelated passing tests, stale current-fact evidence, documentation-only platform evidence, ambiguous install states, and candidate self-report. The v1.1 claim model requires claim-bound evidence and type-specific proof before strong statuses are permitted.

Security hardening additionally covers path/symlink escape protection, untrusted-content boundaries, prompt-injection fixtures, controlled authorization tests, local-only observability, and separation of offensive hypotheses from verified exploitation/remediation. Red/Blue/Purple/Black modes are planning/evaluation roles; they are not represented as independent human or model executions unless such runs actually occur.

## Evaluation and regression boundary

The deterministic local runtime/evaluation suites test activation/depth, claim honesty, injection handling, module ablations, prompt intelligence, research intelligence, teaming/scope, and research-planner ablations. Behavioral model-quality comparisons remain NOT_MEASURED when equivalent baseline/v1/v1.1 runners are unavailable.

Critical release regressions include false verified claims, trivial-task over-activation, package/provenance drift, installer safety, compatibility overclaiming, and generated-document drift. The release audit reports proof layers separately rather than collapsing static validation into behavioral or live-platform verification.

## Black / blind release review

The final Black / blind release review treats the main implementation conclusion as untrusted. It checks for architecture breakage, fallback loss, stale version identity, broken links, orphaned/generated drift, unsupported live-platform claims, over-triggering, evidence/claim bypasses, installer/symlink problems, new dependency or telemetry requirements, secret/local-path leakage, archive hygiene, and packaged-copy divergence.

The Black / blind pass found and closed material issues including stale generated adapter text, a remaining generic fallback stack bias, absolute local-path leakage in deterministic evaluation artifacts, overly broad bootstrap Serena expectations, and a packaging-stage omission of the canonical package-manifest file. A rebuilt extracted package then passed its package/static/release/provenance gates, 180/180 unit tests, 37/37 deterministic local evaluations, distribution validation, symlink checks, and archive/local-path hygiene checks. Final release bytes are regenerated from the same source after this audit record is frozen and must repeat these gates.

## Release status and known limits

**Release status: READY WITH DOCUMENTED LIMITATIONS.**

Known evidence limits that do not by themselves block v1.1:

- external commercial/remote hosts were not live-tested here;
- baseline-without-SKick vs v1 vs v1.1 candidate-model task quality is NOT_MEASURED;
- cross-model behavior is NOT_MEASURED;
- exact runtime tokens/latency/cost are host-dependent unless measured by that host;
- upstream GitHub cloning/pushing is unavailable in this sandbox, so Git history used for this release workspace is explicitly synthetic/local.
