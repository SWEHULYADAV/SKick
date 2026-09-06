# SKick v1.1 Release Audit

This document records the v1.1 release proof model. v1.1 releases the optional executable runtime while preserving declarative fallback. A gate is reported only at the proof layer it actually establishes; local deterministic evidence does not imply candidate-model quality or external live-host success.

## Source and baseline boundary

The available execution sandbox could not resolve `github.com` for a normal remote `git clone`. Development therefore started from the mounted SKick v1 source package, reconciled with the current GitHub-visible `main` tree, then committed as a **synthetic local baseline**. That local commit is useful for reproducible diffs but is not represented as upstream Git history.

The frozen v1 baseline is recorded in `artifacts/baseline-v1.json` and `docs/V1_RUNTIME_GAP_MATRIX.md`.

A key baseline defect was reproduced rather than silently repaired: `assets/icon.svg` existed in source but was absent from `tests/package-manifest.txt`. Consequently v1 package validation failed. The old provenance verifier nevertheless passed because it checked only files already named by its manifest. v1.1 closes both sides of that drift class: the package manifest is generated/checkable and provenance verification rejects unlisted canonical files.

## Proof vocabulary

SKick v1.1 keeps these proof classes distinct:

| Proof class | What it can establish | What it cannot establish |
| --- | --- | --- |
| STATIC | Source/package/schema/generated-file consistency | Runtime behavior |
| UNIT | Deterministic component behavior | External host behavior |
| INTEGRATION | Multiple local components execute together | AI task quality or external host support |
| BEHAVIORAL | A candidate agent/model completed scored tasks | Platform installation unless that was part of the test |
| DOC VERIFIED | Current first-party documentation supports a compatibility claim | Successful live install/discovery/invocation |
| LIVE_TESTED | A recorded real host/environment completed the specified live test | Other versions, plans, OSes, or hosts |

`INSTALLED`, `DISCOVERED`, `INVOKABLE`, and `LIVE_TESTED` are also separate installation states. Copying files is not enough to promote any later state.

## v1 baseline results

The baseline was frozen before executable-runtime changes:

- package version: `1.0`
- core methodology modules: 73
- route records: 62
- general behavioral definitions: 97
- trigger definitions: 53
- portability definitions: 38
- package validation: **FAIL**, because `assets/icon.svg` was outside the manually maintained package manifest
- provenance verification: **PASS with an incomplete-coverage blind spot**, because unlisted canonical files were not rejected
- behavioral model execution: **NOT_MEASURED**; the v1 runner loaded/listed definitions but the available environment did not provide a controlled no-SKick / v1 / v1.1 model executor
- no-SKick behavioral baseline: **BASELINE_BLOCKED** in this host because SKick could not be cleanly disabled while preserving an otherwise identical model/runtime context

A static pass from the old release workflow is therefore not treated as evidence that v1 agent behavior or all platform routes worked live.

## v1.1 executable scope

The v1.1 release moves selected high-value contracts from prose into deterministic code while keeping declarative fallback useful:

- capability states distinguish `available`, `unavailable`, `unknown`, `restricted`, `permission_required`, and `host_dependent`
- depth selection preserves `quick`, `standard`, `deep`, and `exhaustive`
- task-specific module compilation records selected/skipped modules, reasons, capability needs, and a transparent instruction-cost estimate
- project policy can opt into vendor/starter preferences without making them constitutional rules
- runtime state, evidence, claim states, and reporting are schema-backed
- claim promotion requires evidence appropriate to the requested state
- evaluation separates executor output from deterministic checks and optional judge output
- prompt intelligence preserves original intent/constraints and produces observable contradiction/success/research/verification structure
- research planning produces question/source/query/freshness/lateral/disconfirmation/budget/frontier plans while the research ledger preserves fact/inference/hypothesis and source-lineage independence
- Red/Blue/Purple/Black-Blind planners select minimum-sufficient adversarial review and constrain unknown authorization to safe lab/simulation boundaries
- eight local deterministic routing, claim-honesty, injection-boundary, prompt, research, teaming, and ablation suites run without paid APIs
- compatibility metadata distinguishes entity type, activation transport, runtime tier, current evidence, and live-test state
- package-manifest and platform/module generated outputs are checkable for drift
- package version is read from `VERSION` by executable distribution/validation code rather than duplicated as a release constant

## Compatibility evidence state

`INSTALLATION_MANIFEST.json` remains the canonical registry. Route count is informational, not a release-quality target. The v1.1 registry classifies records with one of:

- `LIVE_TESTED`
- `DOC_VERIFIED`
- `COMMUNITY_VERIFIED`
- `HOST_DEPENDENT`
- `GENERIC_PROMPT_FALLBACK`
- `BROKEN_UNSUPPORTED`
- `UNKNOWN`

The generated `docs/PLATFORM_AUDIT.md` and `docs/ACTIVATION_MATRIX.md` contain one row for every current route. No external route is promoted to `LIVE_TESTED` without reproducible live-test metadata. In this release environment the external live-test count remains **zero**.

Model/provider records are not treated as native Skill hosts merely because their models can run inside a compatible agent. Literal `@SKick` is recorded only where current evidence supports that transport; other hosts use their documented native equivalent or remain unknown.

## Capability-over-brand policy

The core rule is capability fit and observed availability, not vendor identity. Semantic repository tooling may be provided by a native index, LSP/symbol APIs, Serena, or another provider. Vendor-specific preferences belong in project/runtime policy and may only win after capability discovery and task-fit scoring.

Likewise, the historical Python + semantic HTML/CSS/vanilla-JavaScript starter profile is no longer a universal engineering invariant. Existing project architecture and explicit user/project constraints outrank optional starter defaults.

## Evaluation boundary

Deterministic local suites provide runtime/planner-logic evidence, not model-quality proof. The router suite exposes activation TP/TN/FP/FN and depth accuracy; claim-honesty suites reject unsupported `tested`/`verified`; injection fixtures keep untrusted content as data; prompt/research/teaming suites exercise framing, freshness/source routing, minimum-process team selection and safe scope; ablations measure instruction/planner changes. Research ablations explicitly mark factual/answer-quality benefit `NOT_MEASURED`.

The owned `tests/fixtures/security_auth_lab/` cross-tenant authorization fixture has deterministic unit coverage for vulnerable vs fixed behavior. `evals/security-behavioral-fixture.json` is only a candidate-runner benchmark definition; no Red/Blue/Purple model pass is claimed or counted by CI.

The repository also retains richer behavioral evaluation definitions and a pluggable executor/judge interface. Actual cross-model baseline-v1-v1.1 behavioral comparison remains **NOT_MEASURED** until an environment can run controlled repeated trials. The held-out strategy is documented in `docs/EVALUATION_STRATEGY.md`; no set created during this implementation is mislabeled as independently held out.

## Security boundary

`docs/SECURITY_THREAT_MODEL.md` defines the local trust model for repository prompt injection, web content, external Skills, MCP servers, generated shell, package scripts, path/symlink attacks, secrets, and false verification. Observability is local-first. This v1.1 release does not add hidden remote telemetry.

## Release gates

A production release must satisfy all applicable layers in `docs/RELEASE_CHECKLIST.md`:

1. **STATIC** — syntax, schema, package/provenance completeness, generated-file sync, compatibility metadata, safe package scan.
2. **UNIT** — routing, budget, claims, evidence, capability detection, versioning, fallback and security policy logic.
3. **INTEGRATION** — distributions, installer/migration behavior, runtime CLI/state round trips, representative fixture execution.
4. **BEHAVIORAL** — controlled model-based comparison when credentials/runners exist; raw outputs and scorer provenance retained.
5. **PLATFORM** — per-host live install/discovery/invocation evidence only where real infrastructure exists.

Passing STATIC/UNIT/INTEGRATION does not upgrade BEHAVIORAL or PLATFORM status.

## Known unverified areas

- Controlled no-SKick vs v1 vs v1.1 agent task success remains `BASELINE_BLOCKED` / `NOT_MEASURED` in this host.
- External cross-model robustness is not live tested here.
- External platform live install/discovery/invocation is not inferred from documentation.
- GitHub Actions checkout/setup-python dependencies are pinned to reviewed immutable v7 release SHAs; future action updates must requalify and update those pins deliberately.
- Documentation evidence can age; scheduled freshness checks help detect staleness but do not replace live platform tests.

## Release rule

Do not call v1.1 behaviorally or universally platform-verified merely because its local runtime/release gates pass. A release must report the strongest evidence actually available, preserve failures at task level, keep generated artifacts synchronized with the final committed tree, and explicitly label behavioral/platform gaps. Until controlled behavioral and external-host evidence exists, the correct overall improvement verdict may be **PARTIALLY** rather than `YES`.
