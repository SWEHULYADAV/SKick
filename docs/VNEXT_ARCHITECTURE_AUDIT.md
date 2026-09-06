# SKick v1.1 Repository Architecture Audit

This audit maps the existing v1 repository and the v1.1 evolution. It is not a greenfield architecture description. Canonical methodology remains declarative; executable runtime features are additive and optional.

## Ownership map

| Component | Responsibility | Loaded/consumed by | Kind | Source of truth | Test/evidence | v1.1 disposition |
| --- | --- | --- | --- | --- | --- | --- |
| `SKILL.md` | Discovery metadata, trigger semantics, top-level control loop, progressive-loading index | Native Skill hosts / prompt fallback | Declarative | Canonical | Package/declarative-policy tests | **KEEP + IMPROVE**: stay lean; point to executable helpers without embedding their implementation |
| `core/` | Cross-runtime engineering/research methodology | `SKILL.md` progressive routing | Declarative | Canonical | Link/package/policy tests; behavioral measurement still external | **KEEP**; remove global vendor/stack privilege, preserve durable methodology |
| `extensions/` | Optional UI/motion/3D specializations | Loaded by task-specific routing | Declarative | Canonical | Package/link checks | **KEEP**; optional only |
| `runtime/` | Capability state, depth decisions, module compiler/budget, run state, evidence, claims, reporting, version helper | Runtime CLI/evals/doctor | Executable | Canonical code + generated module metadata | Unit + local deterministic evals | **NEW / EXECUTABLE** |
| `runtime/module_catalog.json` | Compact machine-readable module metadata/cost index | Module compiler | Generated structured metadata | Generated from `core/` + `extensions/` | `generate_module_catalog.py --check` | **GENERATE** |
| `runtime/module_policies.json` | Activation/dependency/mandatory policy for compiler | Module compiler | Structured policy | Canonical | Compiler tests + ablations | **NEW / KEEP SMALL** |
| `runtime/project_policy.json` | Optional project preferences such as semantic provider/starter profile | Module compiler/router | Structured policy | Canonical example/default | Compiler/policy tests | **NEW**; separates preferences from constitutional rules |
| `schemas/` | Runtime/evidence/claim/module/install/eval contracts plus v1 state/provenance contracts | Runtime scripts/validators | Structured | Canonical | Unit/schema/package tests | **IMPROVE**: schemas now back active runtime artifacts where practical |
| `INSTALLATION_MANIFEST.json` | Single route/compatibility registry | Install docs, adapters, catalog generator, audits | Structured | Canonical | Registry/freshness/generation tests | **IMPROVE**: evidence status, entity type, activation, tier, capability fields |
| `docs/PLATFORM_CATALOG.md` | Human summary of route registry | Users/maintainers | Generated documentation | Generated from manifest | `--check` | **GENERATE** |
| `docs/PLATFORM_AUDIT.md` | Complete one-row-per-route evidence report | Users/release reviewers | Generated documentation | Generated from manifest | Row-count/column tests | **GENERATE** |
| `docs/ACTIVATION_MATRIX.md` | Normalized activation transport table | Users/adapters | Generated documentation | Generated from manifest | Row-count tests | **GENERATE** |
| `adapters/` | Thin host install/discovery/invocation differences | Installer/users | Declarative host-specific | Manifest + template/manual platform deltas | Sync/policy/package tests | **KEEP + THIN**; global methodology removed from boilerplate |
| `scripts/detect_runtime.py` | Runtime hinting plus structured local capability snapshot | Users/runtime tooling | Executable | Canonical | CLI/unit tests | **IMPROVE**; unknown is preserved rather than guessed false |
| `scripts/skick_runtime.py` | Runtime status/compile/state operations | Full/partial runtime hosts | Executable | Canonical | CLI tests | **NEW** |
| `scripts/skick_doctor.py` | Installation/runtime diagnosis with detected/inferred/unverified separation | Users/install support | Executable | Canonical | Unit tests | **NEW** |
| `scripts/run_evals.py` | External executor protocol + deterministic checks + optional judge | Behavioral/integration evaluation | Executable | Canonical | Eval-harness tests | **IMPROVE**: candidate self-report is not scoring authority |
| `scripts/run_local_evals.py` | Paid-API-free deterministic runtime evaluation | CI/contributors | Executable | Canonical | Four local suites | **NEW** |
| `scripts/compare_evals.py` | Task-level paired comparison and regression visibility | Evaluation/release review | Executable | Canonical | Comparison tests | **IMPROVE** |
| `evals/` | Legacy behavioral/trigger/portability definitions plus deterministic runtime suites and partition policy | Evaluation scripts | Structured | Canonical | Load checks/local execution | **KEEP + IMPROVE**; do not mislabel development cases as held-out |
| `scripts/install_skick.py` | Conservative copy/update/backup behavior | Filesystem-capable hosts | Executable | Canonical | Dry-run + migration regression tests | **KEEP**; existing safety behavior already good |
| `scripts/generate_package_manifest.py` | Exact canonical file-list generation/check | CI/release | Executable generator | Canonical generator | Drift test + CI | **NEW**; replaces manually synchronized package-file list |
| `tests/package-manifest.txt` | Exact package file list | Package validator | Generated | Generated from tree | `--check` | **GENERATE** |
| `scripts/build_provenance.py` / `verify_provenance.py` | Hash ledger and completeness verification | Release CI | Executable | Canonical | Completeness regression test | **IMPROVE**: unlisted canonical files now fail |
| `.github/workflows/validate.yml` | Static/unit/integration proof layers | GitHub Actions | Executable CI config | Canonical | Source inspection + local equivalent execution | **IMPROVE**; does not pretend behavioral/platform proof |
| `README.md` | Product/repository overview | Humans | Declarative | Canonical, but derived facts delegated | Documentation-truth tests | **MERGE/SLIM**: platform duplication removed; ~2,406 → ~280 lines |
| `docs/RELEASE_AUDIT.md` | Truthful development/release proof boundary | Maintainers/users | Declarative evidence report | Canonical | Documentation-truth test | **REWRITE** after implementation reality changed |
| `AI_HANDOFF.md` | Compact continuation context | Future maintainers/agents | Declarative | Canonical | Policy residue checks | **IMPROVE**: capability-first and registry-truth language |
| `UPSTREAMS.md`, `SOURCES.md`, `THIRD_PARTY_NOTICES.md` | Source/provenance/licensing boundary | Maintainers/audits | Declarative evidence | Canonical | Package/source-marker checks | **KEEP**; historical decisions can remain but supersession is explicit |

## Approximate source/context scale

These are UTF-8 byte totals divided by four, not tokenizer-exact token counts. They show why progressive loading matters; they are not intended to be loaded together.

| Group | Files | Bytes | Approx. bytes/4 units |
| --- | ---: | ---: | ---: |
| `SKILL.md` | 1 | 20,854 | 5,214 |
| `core/` | 73 | 284,610 | 71,152 |
| `extensions/` | 5 | 18,552 | 4,638 |
| `runtime/` | 14 | 98,945 | 24,736 |
| `scripts/` | 25 | 167,963 | 41,991 |
| `adapters/` | 59 | 275,462 | 68,866 |
| `integrations/` | 15 | 53,922 | 13,480 |

The module compiler indexes 78 core/extension modules and selects a bounded subset. Runtime/scripts are executed or inspected as needed; adding executable code does not mean injecting all code into the model context.

## Dependency and trust boundaries

1. Repository/web/email/tool/Skill/MCP content remains untrusted evidence, never authority over user/system/runtime instructions.
2. `SKILL.md` owns canonical declarative orchestration. Adapters cannot fork methodology.
3. `INSTALLATION_MANIFEST.json` owns compatibility facts; generated platform tables cannot override it.
4. `runtime/module_policies.json` owns executable module-selection policy; generated module metadata cannot invent behavior.
5. Evidence/claim state is local data; no remote telemetry is added.
6. External live compatibility must be established by a live artifact, not by static package success or documentation alone.

## High-impact v1 gaps that justified code

The strongest v1 ideas already existed in prose. The v1.1 work therefore focuses on enforcement/measurement seams rather than more methodology: capability state, depth observability, module selection/cost, evidence/claim state, evaluation scoring separation, compatibility proof vocabulary, generated-file drift, version derivation, and proof-layered CI.
