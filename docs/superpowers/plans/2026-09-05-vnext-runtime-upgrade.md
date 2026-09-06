# SKick vNext Runtime Upgrade Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make SKick's existing depth, capability, progressive-loading, evidence, verification, evaluation, compatibility, and release ideas executable and measurable where the host permits without breaking the declarative fallback.

**Architecture:** Add a dependency-free `runtime/` Python package plus thin CLI scripts. Extend the existing canonical installation manifest instead of creating a second platform database. Keep `SKILL.md` lean and preserve `core/` as methodology; move deterministic enforcement to code and schemas.

**Tech Stack:** Python 3.12 standard library, JSON/JSON Schema documents, unittest, existing Markdown/adapters, GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-09-05-vnext-runtime-upgrade-design.md`

## Global Constraints

- Preserve `quick`, `standard`, `deep`, and `exhaustive` terminology.
- Capability fit outranks vendor branding.
- Existing project architecture outranks starter stack preferences.
- No mandatory third-party Python dependencies.
- No remote telemetry; active network probing is opt-in.
- Do not claim model behavioral or live-platform improvement without actual runs.
- `INSTALLATION_MANIFEST.json` remains the platform source of truth.
- Adapters remain thin and generated blocks stay generated.
- TDD for executable behavior; each production change follows a failing test.

---

### Task 1: Freeze v1 baseline and runtime gap artifacts

**Files:**
- Create: `docs/V1_RUNTIME_GAP_MATRIX.md`
- Create: `artifacts/baseline-v1.json`
- Modify: `.gitignore` to ignore local/raw eval artifacts while keeping sanitized baseline summaries tracked.

**Interfaces:**
- Consumes: existing scripts, schemas, manifest, eval suites.
- Produces: factual baseline used by release audit and final comparison.

- [ ] Record current synthetic baseline commit, release version, package counts, script/schema/eval counts, SKILL/module sizes, and every baseline command/exit status.
- [ ] Classify required major capabilities as DECLARED / PARTIALLY_EXECUTABLE / EXECUTABLE / TESTED / BEHAVIORALLY_EVALUATED / CROSS_PLATFORM_VERIFIED using repository evidence.
- [ ] Mark model baseline comparisons `BASELINE_BLOCKED` when the host cannot disable SKick under identical conditions.
- [ ] Verify the baseline artifact is valid JSON and the gap matrix names evidence files/scripts for each classification.
- [ ] Commit baseline artifacts.

### Task 2: Runtime capability and depth model

**Files:**
- Create: `tests/test_runtime_capabilities.py`
- Create: `tests/test_runtime_depth.py`
- Create: `runtime/__init__.py`
- Create: `runtime/model.py`
- Create: `runtime/capabilities.py`
- Create: `runtime/depth.py`
- Create: `runtime/depth_model.json`
- Modify: `scripts/detect_runtime.py` to expose structured capability discovery while retaining v1 hint output compatibility.

**Interfaces:**
- Produces: `CapabilitySnapshot`, `CapabilityRecord`, `DepthDecision`, `discover_capabilities()`, `classify_task()`.

- [ ] Write failing capability tests for known/unknown/unavailable distinction, safe filesystem probes, Git-repository distinction, no secret dumping, and network remaining unknown unless explicitly probed.
- [ ] Run capability tests and confirm failures are due to missing runtime package.
- [ ] Implement minimal capability model/probes and make tests pass.
- [ ] Write failing depth tests for trivial arithmetic, typo edit, repository bug, production auth debugging, current vulnerability patch/research, and explicit depth override.
- [ ] Run depth tests and confirm failures.
- [ ] Implement versioned explainable depth rules and make tests pass.
- [ ] Add backward-compatible `detect_runtime.py --capabilities` JSON output and regression-test original candidate hinting.
- [ ] Commit capability/depth runtime.

### Task 3: Module compiler and instruction budget

**Files:**
- Create: `tests/test_module_compiler.py`
- Create: `runtime/budget.py`
- Create: `runtime/modules.py`
- Create: `runtime/module_catalog.json`
- Create: `runtime/project_policy.json`
- Create: `scripts/generate_module_catalog.py`
- Create: `schemas/module-plan.schema.json`
- Create: `schemas/project-policy.schema.json`

**Interfaces:**
- Consumes: task classification, capability snapshot, depth, project policy.
- Produces: `compile_modules()` result containing selected/optional/skipped modules, reasons, requirements, estimate method, and total cost.

- [ ] Write failing tests showing a typo task loads no heavy research/security modules; an OAuth debugging task selects repo/debug/security/testing; finance/3D remain skipped; missing semantic search selects repository-search fallback; budget overflow drops optional modules before mandatory truth/safety modules.
- [ ] Run tests and confirm missing compiler failures.
- [ ] Implement byte-based transparent cost estimation, curated module metadata, selection, and budget trimming.
- [ ] Add catalog generator path/size validation and verify generated estimates are deterministic.
- [ ] Make all module/compiler tests pass and commit.

### Task 4: Runtime state, evidence ledger, claim firewall, reporter

**Files:**
- Create: `tests/test_claim_firewall.py`
- Create: `tests/test_runtime_state.py`
- Create: `runtime/state.py`
- Create: `runtime/claims.py`
- Create: `runtime/report.py`
- Create: `schemas/runtime-state.schema.json`
- Create: `schemas/evidence-ledger.schema.json`
- Create: `schemas/claim.schema.json`
- Modify: `schemas/trace.schema.json` only if needed for proof-level vocabulary.

**Interfaces:**
- Produces: `new_run_state()`, `add_evidence()`, `set_claim_status()`, `render_report()`.

- [ ] Write failing tests that TESTED requires a passing `test_result`, DOCS_VERIFIED requires first-party documentation evidence, LIVE_VERIFIED requires successful runtime observation, VERIFIED cannot be created from inference alone, and NOT_TESTED remains visible in rendering.
- [ ] Run tests and confirm failures.
- [ ] Implement append-only evidence records and evidence-gated claim transitions.
- [ ] Implement deterministic report rendering with no status promotion.
- [ ] Validate generated run state against schema using the repository's dependency-free schema checks.
- [ ] Make tests pass and commit.

### Task 5: Runtime CLI, status, and installation doctor

**Files:**
- Create: `tests/test_runtime_cli.py`
- Create: `scripts/skick_runtime.py`
- Create: `scripts/skick_doctor.py`
- Modify: `scripts/install_skick.py` to use explicit install-state vocabulary in machine-readable output without breaking existing dry-run behavior.

**Interfaces:**
- CLI: `status`, `compile`, `new-state`, `add-evidence`, `set-claim`, `report`; doctor reports DETECTED/INFERRED/UNVERIFIED separately.

- [ ] Write failing CLI tests against a temporary project and mocked capability declarations.
- [ ] Run tests and confirm missing-command failures.
- [ ] Implement thin CLIs around runtime package.
- [ ] Add installer status fields `copied/installed/discovered/invokable/live_tested` where observable and leave unobservable states `unknown`.
- [ ] Verify old installer dry-run smoke commands still pass.
- [ ] Commit CLI/doctor changes.

### Task 6: Evaluation harness separation and task-level comparison

**Files:**
- Create: `tests/test_eval_harness.py`
- Create: `tests/fixtures/eval_runner_self_reports_pass.py`
- Create: `tests/fixtures/eval_runner_good.py`
- Modify: `scripts/run_evals.py`
- Modify: `scripts/compare_evals.py`
- Create: `schemas/eval-result.schema.json`

**Interfaces:**
- Executor returns raw output. Deterministic checks and optional judge determine scored outcome. Candidate `passed` is metadata only by default.

- [ ] Write a failing test where a malicious/incorrect runner returns `passed: true` but violates deterministic `contains`/`not_contains` checks; expected final result is fail.
- [ ] Run and confirm v1 harness incorrectly trusts self-report or lacks checks.
- [ ] Implement deterministic checks (`field_equals`, `contains`, `not_contains`, `regex`, `exact`) and separate optional judge protocol.
- [ ] Preserve raw candidate/judge outputs for re-scoring.
- [ ] Write failing compare tests for task-level regression visibility, win/loss/tie, paired success delta, and confidence interval omission on tiny samples.
- [ ] Implement comparison and make tests pass.
- [ ] Commit eval harness changes.

### Task 7: Deterministic local routing/claim/ablation evaluations

**Files:**
- Create: `evals/runtime-routing-evals.json`
- Create: `evals/claim-honesty-evals.json`
- Create: `evals/security-injection-evals.json`
- Create: `evals/ablation-evals.json`
- Create: `scripts/run_local_evals.py`
- Create: `tests/test_local_evals.py`

**Interfaces:**
- Produces run-evals-compatible JSON without paid APIs.

- [ ] Write failing tests for local evaluator schema/output.
- [ ] Implement deterministic cases for activation/depth, tool/capability fallback, module selection, evidence gating, declarative fallback, and prompt-injection classification.
- [ ] Add ablation scenarios comparing full compiler vs routing-without-capability-cost and routing-without-evidence-mandatory modules; report whether ablations save context but violate required outcomes.
- [ ] Run local suites and preserve sanitized summaries under `artifacts/`.
- [ ] Commit local eval path.

### Task 8: Normalize compatibility evidence in the canonical manifest

**Files:**
- Create: `tests/test_platform_registry.py`
- Create: `scripts/normalize_platform_registry.py`
- Create: `schemas/installation-manifest.schema.json`
- Modify: `INSTALLATION_MANIFEST.json`
- Modify: `scripts/generate_platform_catalog.py`
- Modify: `scripts/audit_freshness.py`
- Modify: `scripts/sync_adapter_install_blocks.py` only for new generated fields required in adapter blocks.

**Interfaces:**
- Every route includes entity type, native support, activation, runtime tier, proof status, verification date/evidence, limitations, and live-test record.

- [ ] Write failing tests requiring all 62 current routes to have normalized proof fields and rejecting LIVE_TESTED without a live artifact/environment/version.
- [ ] Implement conservative legacy-status migration; never upgrade legacy `VERIFIED` to LIVE_TESTED automatically.
- [ ] Research current first-party sources and update proof status/date/source only where evidence is actually checked; unresolved routes remain UNKNOWN/COMMUNITY/HOST_DEPENDENT as appropriate.
- [ ] Regenerate platform catalog and adapter blocks from the canonical manifest.
- [ ] Verify docs sync and commit registry upgrade.

### Task 9: Release audit, generated drift, package/provenance repair, and CI layers

**Files:**
- Create: `tests/test_release_gates.py`
- Modify: `scripts/audit_release.py`
- Modify: `scripts/validate_package.py`
- Modify: `scripts/verify_provenance.py`
- Modify: `.github/workflows/validate.yml`
- Modify: `tests/package-manifest.txt`
- Regenerate: `ARTIFACT_MANIFEST.json`, `SHA256SUMS.txt`, generated platform docs.

**Interfaces:**
- Release audit reports STATIC/UNIT/INTEGRATION/BEHAVIORAL/PLATFORM proof separately and does not enforce platform-count marketing thresholds.

- [ ] Write failing tests proving unexpected untracked package files break provenance verification, generated docs drift is detected, and no route-count minimum is required.
- [ ] Implement manifest completeness checks and generated-file check mode.
- [ ] Resolve `assets/icon.svg` intentionally: remove it if redundant with canonical PNG policy, otherwise include it everywhere. The v1 package policy says branding metadata uses PNG, so remove redundant SVG unless current first-party packaging evidence requires it.
- [ ] Split CI into named static/unit/integration jobs; add local deterministic evals; keep behavioral/platform jobs explicitly optional/infrastructure-dependent.
- [ ] Regenerate provenance and package manifest only after all committed-source changes are final.
- [ ] Run complete release pipeline and commit.

### Task 10: Demote vendor/stack biases into policy and preserve declarative fallback

**Files:**
- Create: `tests/test_declarative_fallback.py`
- Modify: `SKILL.md`
- Modify: `core/capability-and-skill-routing.md`
- Modify: `core/serena-integration.md`
- Modify: `core/python-vanilla-web-stack.md`
- Modify: `core/project-planning-and-structure.md` if the root default is repeated there.
- Modify: `docs/INVOCATION_AND_MODES.md`

**Interfaces:**
- Root control plane references executable runtime when available but remains self-contained on declarative hosts.

- [ ] Write failing text-policy tests asserting root policy says capability-fit first, existing project architecture first, and runtime features optional; forbid unconditional Serena-first and unconditional Python-web constitutional language.
- [ ] Make the smallest documentation/control-plane edits to satisfy those tests.
- [ ] Measure `SKILL.md` size/tokens before and after and keep it under 500 lines.
- [ ] Simulate declarative-only mode by copying only Skill + referenced core files without runtime execution; validate no mandatory runtime command is required for truthful fallback.
- [ ] Commit policy/fallback changes.

### Task 11: README, migration, changelog, contribution rules, security model

**Files:**
- Create: `docs/VNEXT_MIGRATION.md`
- Create: `docs/RUNTIME_AND_GUARANTEE_LEVELS.md`
- Create: `docs/SECURITY_THREAT_MODEL.md`
- Modify: `README.md`
- Modify: `CONTRIBUTING.md`
- Modify: `CHANGELOG.md`
- Modify: `SECURITY.md`
- Modify: `docs/RELEASE_CHECKLIST.md`

**Interfaces:**
- Documentation describes actual implemented guarantees and generated platform status counts; it contains no invented benchmark/live-test claims.

- [ ] Document runtime tiers, proof vocabulary, local telemetry policy, migration/rollback, module/platform contribution evidence requirements, and deprecation expectations.
- [ ] Replace hard-coded platform marketing counts with generated/status-aware language.
- [ ] Add README architecture/capability/compiler/evidence/eval/limitations sections only after the corresponding code is green.
- [ ] Commit documentation.

### Task 12: Final benchmarks, ablations, verification, and report artifacts

**Files:**
- Create: `artifacts/vnext-local-evals.json`
- Create: `artifacts/vnext-ablation-summary.json`
- Create: `artifacts/before-after.json`
- Create: `docs/VNEXT_IMPLEMENTATION_REPORT.md`

**Interfaces:**
- Final artifact distinguishes STATIC VALIDATION, RUNTIME TEST, BEHAVIORAL EVALUATION, DOC VERIFICATION, and LIVE PLATFORM TEST.

- [ ] Run Python compile, strict security scan, unit tests, local deterministic evals, installer integration tests, package validation, release audit, distribution validation, generated-doc sync, and provenance verification from a clean tree.
- [ ] Compare v1 deterministic baseline where equivalent with vNext; mark model baseline/behavioral/cross-platform runs BLOCKED when no identical non-SKick host or live platform is available.
- [ ] Run ablations and preserve regressions, not only averages.
- [ ] Create file-level change log and deletion/merge report from `git diff main...HEAD`.
- [ ] Run an independent final verification pass and record exact commands/results.
- [ ] Commit sanitized final report artifacts.

### Task 13: Prompt, research, and adversarial intelligence extension

**Files:**
- Create: `runtime/prompt_intelligence.py`
- Create: `runtime/research.py`
- Create: `runtime/research_ledger.py`
- Create: `runtime/teaming.py`
- Create: `runtime/orchestrator.py`
- Create: `schemas/task-interpretation.schema.json`
- Create: `schemas/research-plan.schema.json`
- Create: `schemas/teaming-plan.schema.json`
- Create: `schemas/research-finding.schema.json`
- Create: `evals/prompt-intelligence-evals.json`
- Create: `evals/research-intelligence-evals.json`
- Create: `evals/teaming-evals.json`
- Create: `evals/research-ablation-evals.json`
- Modify: `scripts/skick_runtime.py`, `scripts/run_local_evals.py`, `runtime/state.py`, `runtime/modules.py`, CI/release/docs

**Interfaces:**
- Task interpretation preserves original request and explicit constraints.
- Research planning outputs question/source/query/freshness/budget/frontier/stopping contracts but never claims sources were opened.
- Research findings reference the existing evidence ledger and preserve fact/inference/hypothesis distinctions and source lineage.
- Teaming selects Red/Blue/Purple/Black only when justified, with authorization-aware safe boundaries.

- [x] RED/GREEN prompt intelligence tests, including over-expansion and contradiction cases.
- [x] RED/GREEN research planning tests, including currentness, lateral/disconfirmation and version-sensitive source routes.
- [x] RED/GREEN teaming tests, including no-team ordinary auth debug and unknown-authorization lab fallback.
- [x] Integrate intelligence planning with depth/module compilation while keeping redundant prose modules optional in full runtime.
- [x] Add research finding/frontier/coverage/lineage state and triangulation summary.
- [x] Add deterministic local eval suites and explicitly mark research-ablation answer quality `NOT_MEASURED`.
- [x] Add CI/package-validator release gates for the extension.
- [ ] Freeze generated manifests/provenance and execute final verification after documentation/report artifacts stop changing.
