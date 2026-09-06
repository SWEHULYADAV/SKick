# SKick v1.1 Runtime Upgrade — Implementation Report

This report is the durable implementation record for the v1.1 release line (developed on the historical `vnext-runtime-upgrade` branch). Package `VERSION` is `1.1`; this report preserves the development evidence that led to the release. The original requested mission was to evolve the existing declarative SKick architecture into an executable/measurable runtime without sacrificing declarative portability.

## 1. Executive Summary

SKick v1 was already a sophisticated declarative engineering/research control plane. Its central weakness was not lack of ideas: important contracts such as depth selection, capability-first routing, progressive loading, evidence discipline, claim honesty, and evaluation methodology mostly depended on host-model compliance. v1.1 keeps the canonical `SKILL.md + core/` methodology and adds an **optional dependency-free Python runtime** that makes selected contracts observable and testable.

Implemented executable seams include six-state capability discovery, deterministic `quick/standard/deep/exhaustive` classification, task-specific module compilation with instruction budgets, structured run/evidence/claim state, an evidence-backed claim firewall, status/doctor/install proof states, deterministic evaluation checks separated from candidate self-report, local routing/claim/injection/ablation suites, evidence-status compatibility metadata, generated-file drift gates, and proof-layered CI.

The strongest supported verdict is **PARTIALLY — improvements proven in deterministic/runtime/release-integrity areas, while controlled model-behavior and external live-platform comparisons remain unmeasured in this host**.

## 2. What SKick v1 Actually Was

v1 was primarily a **declarative portable Skill package plus deterministic packaging/install/audit helpers**:

- `SKILL.md` was a compact control-plane index.
- 73 `core/` modules held canonical methodology.
- adapters mapped installation/discovery differences without owning methodology.
- `INSTALLATION_MANIFEST.json`, schemas, eval definitions, provenance scripts, installers, distribution builders, and release audit tooling provided meaningful structure.
- `scripts/detect_runtime.py` could infer runtime candidates from markers/executables.
- evaluation definitions were extensive, but local CI loaded/listed them rather than measuring a candidate model.

The frozen baseline is `artifacts/baseline-v1.json`; the detailed gap matrix is `docs/V1_RUNTIME_GAP_MATRIX.md`. The synthetic baseline commit is `e379f59ec0c2ab9f0947568382058f08f072e958`. It is **not upstream Git history**: sandbox DNS blocked a normal remote clone, so the mounted source snapshot was reconciled with the GitHub-visible tree and committed locally for reproducible diffs.

## 3. Specification-vs-Runtime Gaps Found

Highest-impact v1 gaps:

1. **Depth/mode selection was prose-only.** Quick/standard/deep/exhaustive existed but was not observable or regression-tested.
2. **Progressive loading was a policy, not a compiler.** No machine artifact recorded selected/skipped modules, cost, or reasons.
3. **Capability routing lacked a full state model.** Runtime hints existed, but `unknown`, restricted, permission-required, and host-dependent capabilities were not first-class.
4. **Evidence/claim discipline was not enforceable.** Nothing mechanically prevented `verified` or `tested` status without matching evidence.
5. **Evaluation trusted the runner too much.** Candidate output could carry `passed`; deterministic scoring was not the authority.
6. **Platform “verified” language lacked proof granularity.** Documentation evidence, host inheritance, model-provider routing, copy success, and live execution were insufficiently separated.
7. **Release integrity could drift.** v1 actually contained `assets/icon.svg` outside the manually maintained package manifest; package validation failed while provenance still passed because unlisted files were invisible to the old verifier.
8. **Vendor/project preferences leaked into constitutional policy.** Serena-first and the Python/vanilla greenfield profile could be interpreted as global preferences.
9. **Release/version data was duplicated in executable code.** Distribution/validator paths contained current-release constants despite a `VERSION` source.

The current cumulative matrix is `docs/V1.1_RUNTIME_MATRIX.md`.

## 4. Baseline Results

Frozen v1 measurements:

| Item | v1 baseline |
| --- | --- |
| Package version | `1.0` |
| Tracked source snapshot | 240 files |
| Core modules | 73 |
| Adapter directories | 57 |
| Route records | 62 |
| Schemas | 7 |
| Python scripts | 19 |
| `SKILL.md` | 115 lines / 20,435 bytes / ~5,109 bytes÷4 estimate |
| Behavioral eval definitions | 97 |
| Trigger definitions | 53 |
| Portability definitions | 38 |
| Package validation | **FAIL** — unlisted `assets/icon.svg` |
| Provenance verification | PASS but incomplete-set blind spot |
| Distribution structure | PASS |
| Candidate-model behavioral run | **NOT_MEASURED** |
| Same-model no-SKick baseline | **BASELINE_BLOCKED** |
| External live-platform test | **NOT_MEASURED** |

The no-SKick comparison is blocked because this ChatGPT host did not expose an otherwise identical environment with the installed SKick Skill disabled. Static architecture is not substituted for behavioral evidence.

## 5. Changes Implemented

Concrete implementation:

- added `runtime/` capability/depth/module/budget/state/evidence/claim/report/version components;
- added executable prompt interpretation, research planning/ledger/triangulation, and authorization-aware Red/Blue/Purple/Black-Blind teaming planners integrated through `runtime/orchestrator.py`;
- added structured module, project-policy, runtime-state, task-interpretation, research-plan/finding, teaming-plan, evidence, claim, eval-result, and installation-manifest contracts;
- upgraded runtime detection without converting unknown host capabilities into false negatives;
- added a module/context compiler and machine-generated 78-module catalog;
- moved Serena and starter-stack preferences into capability/project policy;
- added a structured claim firewall and report renderer;
- added `skick_runtime` status/compile/state CLI and installation doctor;
- separated installation states (`copied`, `installed`, `discovered`, `invokable`, `live-tested`);
- redesigned evaluation into executor → raw result → deterministic checks → optional judge → aggregation;
- added local deterministic routing, claim, injection, module-ablation, prompt-intelligence, research-intelligence, teaming, and research-planner-ablation suites;
- upgraded comparison output to task-level regression/win-loss-tie analysis;
- normalized every compatibility record with entity type, activation, runtime tier, capability list, evidence status/date/source, limitations, and live-test metadata;
- generated complete platform audit and activation matrices from the canonical manifest;
- removed count-based release quality incentives;
- added generated package-manifest checking and complete-set provenance verification;
- split CI into STATIC, UNIT, and INTEGRATION layers, pinned first-party GitHub Actions to reviewed immutable release SHAs, and explicitly left BEHAVIORAL and PLATFORM proof absent without real runners/hosts;
- preserved conservative installer behavior and added migration regression tests rather than rewriting a safe component;
- slimmed README duplication and added explicit runtime guarantee/migration/threat-model/evaluation-strategy docs;
- derived executable release labels/versions from `VERSION` where package release identity is involved.

## 6. v1.1 Architecture

Executable hosts move toward:

`TASK -> PROMPT INTELLIGENCE -> RESEARCH PLAN -> TEAMING/SCOPE PLAN -> CLASSIFY/DEPTH -> CAPABILITY SNAPSHOT -> PROJECT/POLICY RESOLUTION -> MODULE COMPILER -> INSTRUCTION BUDGET -> AGENT/HOST EXECUTION -> RUN STATE -> EVIDENCE/RESEARCH FINDINGS -> TEST/VERIFICATION -> CLAIM FIREWALL -> REPORT -> EVAL TRACE`

The runtime is deliberately optional. Declarative-only hosts still use:

`TASK -> SKILL.md -> selectively loaded core references -> host model`

Four guarantee tiers are documented in `docs/RUNTIME_AND_GUARANTEE_LEVELS.md`: FULL RUNTIME, PARTIAL RUNTIME, DECLARATIVE MODE, and PROMPT FALLBACK. v1.1 does not pretend identical enforcement exists on all four tiers.

## 7. Capability System

`runtime/capabilities.py` models capability state as:

- `available`
- `unavailable`
- `unknown`
- `restricted`
- `permission_required`
- `host_dependent`

Local probes distinguish filesystem read/write, Git executable vs Git repository, shell/code execution, and similar observable facts. Network stays `unknown` unless actively probed. Host-only surfaces such as subagents or browser tooling stay unknown unless supplied by trusted host declarations. Declarations can resolve unknowns but cannot overwrite directly observed local facts.

Capability routing is intentionally **capability over brand**. Serena remains a supported semantic repository provider; it has no constitutional bonus. Native indexing/LSP/symbol/reference APIs or another provider may win when they better fit observed capabilities and policy.

## 8. Context / Module Compilation

`runtime/modules.py` and `runtime/module_policies.json` compile a task-specific plan from task text, depth/mode, capability snapshot, project policy, module metadata, and budget.

Output records:

- selected modules and reasons;
- optional modules;
- skipped modules and reasons;
- budget-dropped modules;
- required capability notes/fallbacks;
- estimated instruction cost;
- budget and estimation method.

The catalog indexes 78 `core/` + `extensions/` modules. Estimates use UTF-8 bytes ÷ 4 and are explicitly labeled as estimates rather than tokenizer-exact counts.

The full runtime does not reload prompt/source-routing prose merely to repeat decisions now made by `runtime/prompt_intelligence.py` and `runtime/research.py`; it selects only residual procedural modules justified by the task. Declarative hosts still use those `core/` files normally.


Representative deterministic compile fixtures:

- repo debug without semantic search: 8 selected modules, ~6,558 estimated module tokens inside an 8,000 budget, with generic repository-search fallback;
- Next.js OAuth/security debug: 10 selected / 68 skipped, ~11,166 inside the fixture's 12,000 budget; finance and 3D modules are skipped;
- Serena integration loads only when the semantic capability provider is actually declared/observed as Serena.

## 9. Evidence & Claim Firewall

`runtime/state.py`, `runtime/claims.py`, and `runtime/report.py` implement structured proof state without storing hidden chain-of-thought.

Claim states include `planned`, `inspected`, `changed`, `implemented`, `executed`, `tested`, `verified`, `docs_verified`, `live_verified`, `inferred`, `likely`, `blocked`, `unknown`, and `not_tested`.

Enforced examples:

- `TESTED` requires passing test evidence;
- failed-test evidence cannot promote a claim to tested;
- `DOCS_VERIFIED` requires first-party documentation evidence;
- docs-only evidence cannot become `LIVE_VERIFIED`;
- `LIVE_VERIFIED` requires successful live/runtime observation;
- inference alone cannot become `VERIFIED`;
- the reporter re-validates state and will not promote tampered claim labels.

Local claim-honesty suite: **7/7 deterministic cases pass**.

Research evidence now has a parallel typed finding layer (`FACT`, `INFERENCE`, `HYPOTHESIS`, `OPINION`, `UNKNOWN`) linked to the existing evidence IDs. Facts require non-inference evidence. Frontier/coverage state is explicit, copied sources can share `lineage_root`, and `summarize_research_evidence()` reports independent proof paths so syndication cannot inflate triangulation.

## 10. Evaluation System

`run_evals.py` now separates:

`TASK DEFINITION -> EXECUTOR -> RAW CANDIDATE RESULT -> DETERMINISTIC CHECKS -> OPTIONAL SEPARATE JUDGE -> AGGREGATION`

Candidate `passed: true` is preserved as raw metadata but cannot override a deterministic failure. Runs with neither checks nor a judge remain unscored rather than optimistic passes. Optional judge output is recorded separately so it can be re-judged.

`compare_evals.py` exposes per-task pass rates, regressions/improvements, paired win/loss/tie counts, deltas, and confidence intervals only when sample size is meaningful.

The paid-API-free local path currently has eight development suites:

- routing/depth/module behavior: 10/10;
- claim honesty: 7/7;
- injection/trust-boundary behavior: 3/3;
- module ablations: 2/2;
- prompt intelligence: 4/4;
- research intelligence: 4/4;
- teaming/safe-scope routing: 5/5;
- research-planner ablations: 2/2.

Total deterministic runtime cases: **37/37**. The research ablation artifact explicitly labels behavioral answer quality `NOT_MEASURED`; these are development/runtime tests, not a candidate-model benchmark.

A separate controlled cross-tenant authorization fixture lives under `tests/fixtures/security_auth_lab/`, with Red discovery, Blue remediation, and Purple retest tasks defined in `evals/security-behavioral-fixture.json`. Local tests prove only the fixture's vulnerable/fixed before-after property and suite loadability; **candidate-model Red/Blue/Purple performance remains `NOT_MEASURED`** until an external runner executes and scores those tasks.

The held-out policy is explicit in `docs/EVALUATION_STRATEGY.md` and `evals/benchmark-partitions.json`: no post-hoc set created during tuning is misrepresented as independent held-out evidence.

## 11. Baseline vs v1 vs v1.1

| Dimension | No-SKick baseline | v1 | v1.1 |
| --- | --- | --- | --- |
| Same-model task success | `BASELINE_BLOCKED` | `NOT_MEASURED` | `NOT_MEASURED` |
| Depth selection | n/a | prose | deterministic + tested |
| Module loading | native/host behavior | prose progressive index | compiled selected/skipped plan + budget |
| Capability state | host-specific | runtime hints | six-state structured snapshot + tests |
| Claim proof | native prose behavior | instructed | enforced when runtime reporter is used |
| Deterministic local runtime suites | n/a | none equivalent | 37/37 |
| Router activation fixtures | n/a | not executable | TP 4 / TN 3 / FP 0 / FN 0 |
| Router depth accuracy | n/a | not executable | 100% on frozen classify fixtures |
| False verified claim runtime fixtures | n/a | no firewall | 0 false promotions in 7 claim cases |
| Package manifest completeness | n/a | **FAIL baseline** | generated/checkable |
| Provenance complete-set enforcement | n/a | blind to unlisted source | unlisted canonical files fail |
| Platform proof vocabulary | n/a | broad legacy status | explicit evidence levels; 0 external live claims |
| External cross-platform execution | n/a | not demonstrated | still not demonstrated |

The deterministic improvements are real; model task-success causality is not claimed.

## 12. Ablation Results

Two intentionally negative ablations quantify useful-behavior-per-token trade-offs:

| Ablation | Full estimate | Ablated | Delta | Outcome |
| --- | ---: | ---: | ---: | --- |
| remove `core/evidence-verification.md` | 4,780 | 3,564 | -1,216 | required proof guard missing |
| remove `core/untrusted-content-boundary.md` | 8,067 | 7,642 | -425 | required injection/trust guard missing |

Both save context, but both regress protected invariants. Result: **KEEP** the modules. The local harness supports further ablations, but model-quality ablations remain unmeasured until a controlled model runner exists.

Research-planner ablations also compare full direct+lateral+disconfirmation planning against direct-only and no-disconfirmation variants on platform/security tasks. They prove that the planner changes evidence-neighborhood/query diversity and cost, but **do not prove better answers**; the artifact records `behavioral_quality_measurement: NOT_MEASURED`.

## 13. Platform Compatibility Audit

`docs/PLATFORM_AUDIT.md` contains one row for every current route with the requested entity/install/discovery/activation/tier/capability/limitation/proof/evidence fields. The canonical registry currently contains 62 audited records; **62 is not a release target** and may decrease when evidence warrants removal.

Current evidence distribution:

- `DOC_VERIFIED`: 45
- `HOST_DEPENDENT`: 11
- `COMMUNITY_VERIFIED`: 3
- `GENERIC_PROMPT_FALLBACK`: 2
- `UNKNOWN`: 1
- `LIVE_TESTED`: 0

Important corrections include model-provider routes being marked host-dependent, three weak routes kept community-only, Meta Muse left unknown for native Skill compatibility, Sarvam Cowork represented as a current Skills workspace, and the backward-compatible `mux` route noting the product rename to Xum.

No documentation-only route is called live tested.

## 14. `@SKick` / Activation Matrix

The normalized logical operation is “activate SKick for this task”; literal transport is host-specific. `docs/ACTIVATION_MATRIX.md` contains every route.

Current registry values for literal `@SKick` are intentionally conservative:

- `yes`: 4 routes;
- `no`: 30 routes;
- `unknown`: 28 routes.

Other documented native equivalents include `/skick`, `$skick`, `/skill:skick`, host Skills UI/pickers, automatic semantic activation, or host-dependent prompt injection. v1.1 never converts an unknown syntax into `@SKick` for consistency.

## 15. Security Review

`docs/SECURITY_THREAT_MODEL.md` covers:

- repository/document/web prompt injection;
- malicious external Skills/plugins/MCP servers;
- command and generated-shell injection;
- dependency/package-script risk;
- path traversal/symlink attacks and unsafe install destinations;
- secrets/environment leakage;
- destructive Git/write actions;
- compatibility/evidence inflation;
- provenance drift and supply-chain update risk.

Mitigations include the always-on untrusted-content module, capability permission states, conservative installer overwrite/backup behavior, complete-set provenance, evidence-backed claim states, local-first observability, and no default remote telemetry.

Injection/trust deterministic suite: **3/3**. Security teaming fixtures add minimum-process routing: ordinary auth debugging receives no Red/Blue overhead; scoped review receives Red/Blue; owned-lab remediation receives Purple; unknown authorization is constrained to lab/simulation; high-impact independent review can add Black/Blind challenge. The controlled authorization fixture additionally proves a safe before/after security property, while its Red/Blue/Purple candidate tasks remain external-runner definitions only. These planner/fixture tests do not claim that an AI discovered or patched the weakness, that arbitrary hostile code is safely sandboxed, or that a real-world vulnerability was exploited.

## 16. CI / Release Changes

CI is split into named proof layers:

- **STATIC**: compile, strict scan, MCP catalog, registry/generated-doc/module/package-manifest sync, freshness, package, release audit, provenance completeness;
- **UNIT**: deterministic Python unit tests and eight local runtime eval suites;
- **INTEGRATION**: distribution build/validation, installer dry-run smoke tests, legacy eval-definition load checks.

BEHAVIORAL and PLATFORM are comments/boundaries, not fake green jobs. Real credentials/hosts are required before those layers can be represented as passing.

Release quality no longer depends on a minimum platform count. Every compatibility claim must instead have a complete evidence status. `tests/package-manifest.txt` is generated, provenance rejects files outside its canonical set, and CI action dependencies are immutable-SHA pinned with release comments.

## 17. Files Changed

Important file-level changes:

| File/group | Why | Change | Test | Expected effect |
| --- | --- | --- | --- | --- |
| `runtime/capabilities.py` | v1 hints lacked explicit unknown/restricted state | six-state capability snapshot/probes/declarations | `test_runtime_capabilities.py` | truthful capability routing/fallback |
| `runtime/depth.py`, `depth_model.json` | depth was prose | deterministic classifier/reasons/overrides | `test_runtime_depth.py`, routing evals | observable activation/depth |
| `runtime/modules.py`, `budget.py` | progressive loading was prose | compiler + budget + skip/drop reasons | `test_module_compiler.py` | bounded task-specific context |
| `runtime/module_policies.json`, `project_policy.json` | vendor/stack preferences leaked globally | scoped policy | declarative/compiler tests | capability/project choice over brand |
| `runtime/state.py`, `claims.py`, `report.py` | proof states not enforceable | structured evidence/claims/report | claim/state tests | reduced unsupported verification claims |
| `runtime/prompt_intelligence.py` | prompt enhancement was model-guided prose | preserved original request, modes, constraints, quality/contradiction/success/verification structure | prompt + CLI eval tests | better framing without forced user ceremony |
| `runtime/research.py`, `research_ledger.py` | research routing/frontier/lineage were declarative | adaptive question/source/query/freshness/budget plan + typed findings/coverage/frontier/triangulation | research + ledger + ablation tests | reproducible research planning and visible uncertainty |
| `runtime/teaming.py`, `orchestrator.py` | adversarial lenses were prose and easy to over-trigger | minimum-sufficient Red/Blue/Purple/Black planning, safe scope, integrated depth/module selection | teaming + integration tests | actionable challenge without security ceremony on routine tasks |
| `runtime/versioning.py` | release constants duplicated | `VERSION` helpers | `test_versioning.py` | lower release metadata drift |
| `scripts/detect_runtime.py` | hints only | structured capability output while preserving old JSON shape | CLI tests | richer discovery without breaking callers |
| `scripts/skick_runtime.py` | no status/compiler CLI | status/compile/state operations | runtime CLI tests | inspectable runtime behavior |
| `scripts/skick_doctor.py` | installation diagnostics were prose | detected/inferred/unverified doctor | doctor tests | safer troubleshooting |
| `scripts/install_skick.py` | install proof was easy to overstate | explicit state output; existing safety preserved | installer/migration tests | copy no longer implies live success |
| `scripts/run_evals.py` | candidate could self-report success | deterministic checks + optional separate judge | eval harness tests | evaluator authority separated |
| `scripts/compare_evals.py` | aggregate means hid regressions | task-level paired comparison | eval harness tests | critical regressions visible |
| `scripts/run_local_evals.py` | no API-free behavioral-contract test path | deterministic routing/claim/injection/prompt/research/teaming/ablation runner | local eval tests | reproducible contributor CI |
| intelligence schemas + eval suites | v1 research/teaming behavior existed primarily as prose | task/research/team/finding contracts plus planner development suites | schema/local-eval tests | machine-checkable planning without claiming model proof |
| `INSTALLATION_MANIFEST.json` | broad legacy support status | normalized proof/entity/activation/tier/capability metadata | platform registry tests | truthful compatibility |
| `scripts/generate_platform_catalog.py` | duplicated/manual tables | generated catalog/audit/activation outputs | registry/generation tests | one compatibility source of truth |
| adapters + `sync_adapter_install_blocks.py` | duplicated global policy | thinner generated host-specific blocks | thin-adapter tests | less drift/context duplication |
| `scripts/generate_package_manifest.py` | manual manifest drift caused v1 failure | exact file-list generator/check | release-gate tests | blocks added-file drift |
| `scripts/verify_provenance.py` | unlisted files invisible | complete canonical-set comparison | provenance test | closes v1 provenance blind spot |
| `validate_package.py` / distribution validators/builders | vendor/stack/release invariants over-hardcoded | capability-neutral validation + VERSION derivation | release/version tests | truth and release reproducibility |
| `.github/workflows/validate.yml` | proof types collapsed and action refs were mutable major tags | STATIC/UNIT/INTEGRATION jobs, eight local suites, immutable action SHAs | release-gate tests + local equivalent run | CI describes what it proves and reduces dependency drift |
| `README.md` | 2,406-line duplication/marketing risk | compact runtime-centric overview | documentation-truth tests | less duplication, clearer guarantees |
| `docs/RUNTIME_AND_GUARANTEE_LEVELS.md` | same guarantees impossible everywhere | four runtime tiers | doc tests | graceful degradation explicit |
| `docs/EVALUATION_STRATEGY.md` | held-out risk | dev/validation/held-out separation | doc/package checks | avoids benchmark overclaim |
| `docs/SECURITY_THREAT_MODEL.md` | trust boundaries scattered | consolidated executable/declarative threat model | doc/security fixtures | auditable security boundary |
| `docs/V1.1_MIGRATION.md` | v1 installs need safe evolution | backup/discovery/rollback guidance | migration tests | backward-compatible rollout |
| `docs/PLATFORM_AUDIT.md`, `ACTIVATION_MATRIX.md` | complete route truth required | generated every-route tables | platform tests | transparent platform status |
| `docs/V1.1_ARCHITECTURE_AUDIT.md`, `V1.1_RUNTIME_MATRIX.md` | audit/spec-runtime gap required | durable architecture/evidence maps | package/docs validation | maintainable v1.1 contract |

## 18. Components Removed or Merged

- **Removed:** redundant `assets/icon.svg`. v1 package policy already standardized PNG branding; the SVG was the exact untracked-manifest drift that broke package validation.
- **Merged/slimmed:** README platform/install duplication moved to generated compatibility outputs and focused operational docs.
- **Removed from constitutional policy:** Serena-first routing and universal Python/vanilla stack preference. Serena integration and the starter profile remain available as scoped choices.
- **Removed from adapter boilerplate:** duplicated global methodology/vendor defaults; adapters stay transport-specific.
- **Removed from release-quality incentives:** minimum platform-count expectations.
- **Deprecated behavior:** generic legacy `VERIFIED` status is retained as `legacy_status` only; normalized proof uses explicit statuses.
- **No core methodology module was deleted solely for brevity.** Ablation evidence currently supports retaining the tested evidence/trust guards.
- **No platform record was removed merely to reduce count.** Weak records were downgraded truthfully; future evidence may justify deletion.

## 19. Token / Performance Impact

Measured source/control-plane changes:

| Metric | v1 | v1.1 | Delta |
| --- | ---: | ---: | ---: |
| `SKILL.md` lines | 115 | 119 | +4 (+3.5%) |
| `SKILL.md` bytes | 20,435 | 21,270 | +835 (+4.1%) |
| bytes÷4 estimate | 5,109 | 5,318 | +209 (~4.1%) |
| README lines | 2,406 | 292 | -2,114 (-87.9%) |
| README bytes | 150,647 | 15,830 | -134,817 (-89.5%) |
| core modules | 73 | 73 | unchanged |
| compiled module index | none | 78 core+extension modules | new |

The root Skill became only slightly larger because executable runtime behavior is referenced rather than dumped into it. Task-specific module cost can now be bounded/observed, but **v1 actual host module-loading token cost was not observable**, so an end-to-end token savings percentage versus v1 would be fabricated.

Current compiler examples after the intelligence extension: a tiny rename is `quick`, does not auto-activate, and selects 0 modules; a deep current-platform research task selects 8 modules at ~9,933 estimated module tokens inside a 10,000 module budget; an explicitly deep owned-lab security remediation with Red/Blue/Purple/Black-Blind review selects 8 modules at ~9,670. Root-control-plane estimate is ~5,318 and is reported separately from selected-module cost.


Latency/model output/token/cost differences for actual AI task completion are **NOT_MEASURED** without a controlled model runner.

## 20. Migration Guide

See `docs/V1.1_MIGRATION.md`.

Principles:

1. keep package version v1 until release evidence supports a semantic bump;
2. preserve existing project/user installs unless replacement is explicit;
3. back up customized installs;
4. test v1.1 in project-local/temporary scope first;
5. verify host discovery separately from file copy;
6. verify explicit/native activation separately from discovery;
7. keep v1 backup until real use succeeds;
8. rollback by restoring the original directory/archive, not by mixing v1/v1.1 generated files.

Regression tests prove the existing installer refuses overwrite by default and explicit replacement creates a sibling backup retaining customization.

## 21. Known Limitations

- Remote GitHub clone was blocked by sandbox DNS; local synthetic Git history is not upstream history.
- `VERSION` is `1.1`; this is a minor release, not a v2 contract.
- The runtime cannot mechanically intercept every prose sentence on declarative hosts.
- Exact tokenizer counts are not universal; the module compiler uses a labeled byte-based estimate unless a host supplies a stronger tokenizer.
- Host-only capabilities may remain unknown when the environment does not expose them.
- Compatibility documentation can age; freshness checks do not replace live host execution.
- A persistent research cache with TTL/version invalidation is not implemented; research plans are reproducible, but evidence retrieval remains per-run unless the host provides caching.

## 22. Unverified Areas

Explicitly unverified:

- same-model no-SKick vs SKick v1 vs v1.1 behavioral task success;
- cross-model robustness across OpenAI/Anthropic/Google/local models;
- external host installation/discovery/invocation on all compatibility routes;
- latency/cost/token change for actual agent sessions;
- native host automatic Skill activation accuracy;
- judge-model consistency across providers;
- claimed external platform plans/tier behavior beyond the first-party evidence recorded in the registry;
- production security against arbitrary malicious executable repositories/package scripts beyond the implemented policy/fixture tests.

These remain `BLOCKED`, `NOT_MEASURED`, `DOC_VERIFIED`, or `UNKNOWN` as appropriate; none are promoted from static evidence.

## 23. Recommended Next Experiments

Highest-value next work only:

1. Freeze an independent held-out task set after this policy line is no longer being tuned, then run repeated no-SKick/v1/v1.1 trials in a host that can truly isolate those conditions.
2. Add at least one real external host smoke lane (install → discovery → explicit/native activation → safe task) and store sanitized compatibility evidence; expand only when automation is reliable.
3. Run cross-model trials on the same frozen tasks to calibrate instruction verbosity/module budgets per host without forking canonical methodology.
4. Execute held-out research tasks to measure whether lateral/disconfirmation planning improves correctness/source quality per tool-call/token cost; keep or narrow it based on results.
5. Add provider executors only as optional plugins, keeping deterministic local evaluation dependency-free.
6. Prototype a local research cache only after repeated stable-source retrieval is measured as a meaningful cost; preserve freshness/version invalidation and no remote telemetry by default.

## 24. Final Verdict

**PARTIALLY — improvements are demonstrated in deterministic executability, claim honesty, activation/depth fixtures, module selection/budget observability, package/provenance integrity, compatibility truthfulness, installer state semantics, and CI proof separation.**

A `YES — demonstrably better` verdict would require controlled behavioral evidence showing that actual agents complete tasks at least as well or better without unacceptable regressions, plus stronger external-host evidence for compatibility claims. That evidence is not available in the current environment, so claiming YES would violate the v1.1 claim-firewall principles implemented by this work.
