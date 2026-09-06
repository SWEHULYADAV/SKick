<p align="center">
  <img src="assets/readme/hero-banner.webp" alt="SKick — engineering and research control plane" />
</p>

# SKick

SKick is a portable engineering/research Skill with an **optional executable runtime**. The declarative Skill remains usable on hosts that can only load instructions; the runtime adds deterministic capability discovery, depth selection, module compilation, evidence/claim state, installation diagnostics, and local evaluation where Python execution is available.

Canonical repository: https://github.com/SWEHULYADAV/SKick

> **Release status:** SKick `1.1` packages the optional executable runtime after a second-pass hardening audit. Local deterministic proof is reported separately from model-behavior and external live-platform proof; unexecuted layers remain `NOT_MEASURED` or `LIVE_TESTED = 0`.

## What SKick is

SKick is a control plane for technical work. It combines a compact `SKILL.md` entrypoint with lazily loaded methodology under `core/`, thin host adapters, structured compatibility metadata, deterministic Python runtime helpers, schemas, release validation, and evaluation fixtures.

Its durable rules emphasize evidence, project constraints, reversible changes, capability fit, progressive loading, and truthful verification. The runtime does not replace the host agent; it makes selected SKick decisions observable and mechanically testable when the host permits execution.

## What SKick is not

SKick is not an LLM, IDE, coding agent, MCP server, browser, or universal capability provider. It cannot create filesystem, shell, network, browser, secret, subagent, or model capabilities that the active host does not expose.

A model-provider name is not automatically a Skill host. Documentation support is not runtime availability. Files copied to a directory are not proof of discovery or invocation. Static package validation is not behavioral evaluation, and `DOC_VERIFIED` is not `LIVE_TESTED`.

## Architecture

```text
USER TASK
   |
ACTIVATION / TASK CLASSIFICATION
   |
DEPTH SELECTION
   |
CAPABILITY DISCOVERY + PROJECT POLICY
   |
MODULE / CONTEXT COMPILER
   |
INSTRUCTION BUDGET
   |
HOST AGENT EXECUTION
   |
STRUCTURED RUN STATE
   |
EVIDENCE LEDGER -> CLAIM FIREWALL
   |
REPORT + EVALUATION TRACE
```

Key ownership boundaries:

- `SKILL.md` — declarative control plane and progressive-loading index.
- `core/` — canonical methodology; vendor-neutral unless a module is explicitly a provider profile.
- `runtime/` — optional deterministic runtime contracts.
- `scripts/` — installer, doctor/status, validation, generation, provenance, release and evaluation tooling.
- `schemas/` — machine-readable contracts.
- `INSTALLATION_MANIFEST.json` — canonical compatibility and installation registry.
- `adapters/` — thin host-specific transport/install differences.
- `evals/` + `tests/` — deterministic and behavioral-eval definitions.
- `docs/PLATFORM_CATALOG.md`, `docs/PLATFORM_AUDIT.md`, `docs/ACTIVATION_MATRIX.md` — generated compatibility views.
- `docs/V1_1_FINAL_AUDIT.md` — second-pass architecture, proof-boundary, schema, and Black-review release record.

<p align="center">
  <img src="assets/readme/capabilities-banner.webp" alt="SKick capabilities" />
</p>

## Execution modes

The existing depth vocabulary is preserved:

- `quick` — minimum sufficient process for trivial or tightly bounded work.
- `standard` — default non-trivial engineering/research work.
- `deep` — high uncertainty, production/security impact, cross-system work, or expensive verification.
- `exhaustive` — explicitly expensive investigation with a defined evidence/resource stop condition.

`runtime/depth.py` makes the selection observable. `runtime/depth_model.json` contains the deterministic feature/weight model used by the local runtime. Explicit user depth overrides remain authoritative unless a higher-priority safety constraint applies.

## Prompt, research, and teaming intelligence

The full runtime turns several former prose-only decisions into inspectable plans. `python scripts/skick_runtime.py enhance --task ...` preserves the original request while producing constraints, unknowns, success criteria, research/verification needs, contradiction flags, and optional strict-spec output. `research-plan` produces an adaptive question/source/query/freshness/budget/frontier plan; `team-plan` selects no team for ordinary debugging, Red/Blue for scoped security review, Purple for remediation/retest, and Black/Blind review only when independent challenge is justified.

`compile` combines those plans with depth, capabilities, project policy, module selection, and instruction budget. The planners **do not claim that research, attacks, tests, or host actions occurred**; actual findings must enter the evidence/research ledger before claims can be upgraded. On hosts without the Python runtime, the corresponding `core/` modules remain the declarative fallback.

## Capability discovery

`scripts/detect_runtime.py` and `runtime/capabilities.py` distinguish observed capability state from assumptions. States include:

`available`, `unavailable`, `unknown`, `restricted`, `permission_required`, and `host_dependent`.

Important invariants:

- unknown is not silently converted to unavailable;
- documentation support is not treated as observed availability;
- installed, discovered, invoked, executed, and live-tested remain separate states;
- capability selection is based on fit, trust, context cost and testability rather than vendor brand;
- secrets are not dumped while probing the environment.

## Progressive loading

`runtime/module_catalog.json` indexes canonical core/extension modules with estimated context cost and activation metadata. `runtime/modules.py` compiles a task-specific plan containing selected modules, skipped modules, reasons, capability requirements and estimated instruction cost.

`runtime/module_policies.json` carries machine-readable activation rules. `runtime/project_policy.json` contains optional project preferences. Existing repository architecture, explicit user constraints, ecosystem conventions and existing dependencies outrank optional starter profiles.

The module catalog is generated from source and CI checks it with:

```bash
python3 scripts/generate_module_catalog.py --check
```

## Instruction budget

`runtime/budget.py` treats budget as a maximum, never a loading target. The runtime records the root control-plane estimate, selected-module estimate and budget method. The current fallback estimate is clearly labeled `utf8_bytes_div_4`; hosts with a reliable tokenizer may replace it with measured tokens.

## Evidence and claim verification

`runtime/state.py` stores structured task/runtime state without hidden chain-of-thought. `runtime/claims.py` and `runtime/report.py` enforce evidence-aware claim states including:

`planned`, `inspected`, `changed`, `implemented`, `executed`, `tested`, `verified`, `docs_verified`, `live_verified`, `inferred`, `likely`, `blocked`, `unknown`, and `not_tested`.

Examples:

- code changed without a passing test cannot become `tested`;
- first-party documentation can support `docs_verified`, not `live_verified`;
- live proof requires an actual successful runtime observation;
- the final reporter refuses unsupported claim promotion.

See `schemas/runtime-state.schema.json`, `schemas/evidence-ledger.schema.json`, and `schemas/claim.schema.json`.

## Runtime guarantee levels

Hosts differ substantially. SKick therefore exposes four guarantee levels rather than a binary “supported” flag:

1. **FULL RUNTIME** — local scripts/state/probes/evals are executable.
2. **PARTIAL RUNTIME** — some deterministic runtime features are available.
3. **DECLARATIVE MODE** — the host loads the Skill and supporting references but does not execute SKick runtime code.
4. **PROMPT FALLBACK** — no native Skill mechanism is verified; SKick is supplied as instructions/context.

See [`docs/RUNTIME_AND_GUARANTEE_LEVELS.md`](docs/RUNTIME_AND_GUARANTEE_LEVELS.md).

## Installation

Start with `START_HERE.md`, then use the route in `INSTALLATION_MANIFEST.json`. Installation is conservative: project-local scope is preferred for coding repositories unless the user requests another scope; existing installs are inspected before replacement; ambiguous paths are not invented.

Dry-run example:

```bash
python3 scripts/install_skick.py --target opencode --scope project --project /path/to/repo --dry-run --json
```

Installer result states distinguish `copied`, `installed`, `discovered`, `invokable`, and `live_tested`. A successful copy does not automatically set later states.

Run the local doctor where Python execution is available:

```bash
python3 scripts/skick_doctor.py --json
```

## Activation

The normalized concept is **activate SKick for this task**. Literal syntax is host-specific. Depending on the host, transport may be a Skill picker, `/skick`, `$skick`, `@skick`, automatic semantic discovery, a project instruction, or prompt attachment.

Never assume literal `@SKick`. The generated activation matrix records `yes`, `no`, or `unknown` separately from the native equivalent:

[`docs/ACTIVATION_MATRIX.md`](docs/ACTIVATION_MATRIX.md)

For a runtime status snapshot:

```bash
python3 scripts/skick_runtime.py status --json
```

<p align="center">
  <img src="assets/readme/usage-guide.webp" alt="SKick usage workflow" />
</p>

## Platform compatibility

Compatibility is generated from the canonical manifest rather than maintained as duplicated prose. The proof vocabulary is:

- `LIVE_TESTED` — reproducible real-host install/discovery/invocation evidence exists.
- `DOC_VERIFIED` — current first-party documentation supports the route; no live proof is implied.
- `COMMUNITY_VERIFIED` — credible non-first-party evidence exists but first-party proof is incomplete.
- `HOST_DEPENDENT` — the named model/provider relies on a separate host for Skill support.
- `GENERIC_PROMPT_FALLBACK` — no native Skill mechanism is verified.
- `BROKEN_UNSUPPORTED` — a previously claimed route is known invalid.
- `UNKNOWN` — evidence is insufficient.

Use the generated reports instead of hard-coded platform counts:

- [`docs/PLATFORM_CATALOG.md`](docs/PLATFORM_CATALOG.md)
- [`docs/PLATFORM_AUDIT.md`](docs/PLATFORM_AUDIT.md)
- [`docs/ACTIVATION_MATRIX.md`](docs/ACTIVATION_MATRIX.md)

<p align="center">
  <img src="assets/readme/platforms-banner.webp" alt="SKick platform compatibility" />
</p>

## Evaluation

The evaluation pipeline separates:

```text
TASK DEFINITION
 -> EXECUTOR
 -> RAW RESULT
 -> DETERMINISTIC CHECKS
 -> OPTIONAL INDEPENDENT JUDGE
 -> AGGREGATION
```

The candidate cannot make itself pass by returning `{"passed": true}`. Deterministic checks are preferred where possible; optional judge output is recorded separately. `scripts/compare_evals.py` reports task-level regressions/improvements and paired outcomes instead of only top-level means.

Paid-API-free deterministic suites are available for runtime routing, claim honesty, injection safeguards, prompt/research/teaming planners and ablations:

```bash
python3 scripts/run_local_evals.py evals/runtime-routing-evals.json --output /tmp/routing.json
python3 scripts/run_local_evals.py evals/claim-honesty-evals.json --output /tmp/claims.json
python3 scripts/run_local_evals.py evals/security-injection-evals.json --output /tmp/injection.json
python3 scripts/run_local_evals.py evals/ablation-evals.json --output /tmp/module-ablations.json
python3 scripts/run_local_evals.py evals/prompt-intelligence-evals.json --output /tmp/prompt.json
python3 scripts/run_local_evals.py evals/research-intelligence-evals.json --output /tmp/research.json
python3 scripts/run_local_evals.py evals/teaming-evals.json --output /tmp/teaming.json
python3 scripts/run_local_evals.py evals/research-ablation-evals.json --output /tmp/research-ablations.json
```

`evals/security-behavioral-fixture.json` targets the owned local `tests/fixtures/security_auth_lab/` example for future Red/Blue/Purple candidate-model runs. CI only validates/lists that suite and proves the fixture's before/after behavior; it does **not** claim a model passed it.

## Benchmarks

Only measured data belongs here. Static/unit/integration results do not imply model-behavior improvement. Model baseline-vs-SKick-v1-vs-v1.1 comparisons require identical model/tool/environment control and remain `BLOCKED` when SKick cannot be cleanly disabled or provider access is unavailable.

Deterministic v1.1 runtime results are stored under `artifacts/` when generated. Behavioral AI results, if run, must preserve executor/model/environment metadata and raw evidence.

## Security

Repository, web, document, external Skill and MCP content is untrusted data, not governing authority. Consequential actions are separately authorized. Runtime observability is local-first; SKick has no requirement to upload prompts, source code, filenames, credentials or traces.

See:

- [`SECURITY.md`](SECURITY.md)
- [`docs/SECURITY_THREAT_MODEL.md`](docs/SECURITY_THREAT_MODEL.md)
- [`core/untrusted-content-boundary.md`](core/untrusted-content-boundary.md)
- [`core/action-firewall.md`](core/action-firewall.md)

## Validation and CI proof layers

Run locally:

```bash
python3 -m compileall -q scripts runtime tests
python3 scripts/scan_skill_package.py . --strict
python3 scripts/validate_mcp_catalog.py mcp/catalog.json
python3 scripts/normalize_platform_registry.py --check
python3 scripts/generate_platform_catalog.py --check
python3 scripts/generate_module_catalog.py --check
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 scripts/validate_package.py .
python3 scripts/audit_release.py
python3 scripts/verify_provenance.py .
```

CI is split into `STATIC`, `UNIT`, and `INTEGRATION` proof layers. Behavioral model evaluation and real-host platform verification are intentionally separate because credentials/infrastructure are not universally available.

## Limitations

- Hosts may ignore or only partially follow declarative instructions.
- Some capabilities cannot be probed from inside a managed chat surface; they remain `unknown` or host-reported.
- The module compiler compiles SKick context plans; whether a host mechanically injects exactly that plan is host-dependent.
- Byte-based token estimation is an approximation when no tokenizer is available.
- Cross-platform compatibility changes quickly and needs periodic first-party re-verification.
- Deterministic local evals do not prove model task-success improvement.
- No hidden chain-of-thought is captured or required for traces.

## Versioning

`VERSION` and package metadata identify the released SKick package. Compatibility evidence stores check dates and, for any future `LIVE_TESTED` status, the tested SKick/host version and environment. Project/package pinning is the portable reproducibility mechanism; SKick does not invent version-selection syntax on hosts that lack it.

SKick v1.1 is the first released line containing the optional executable runtime. Declarative-only and prompt-fallback modes remain supported; external live-host compatibility must still be reported per-route rather than inferred from the release version.

## Updating

Read [`docs/UPDATE_AND_PORTING.md`](docs/UPDATE_AND_PORTING.md) and [`docs/VNEXT_MIGRATION.md`](docs/VNEXT_MIGRATION.md). Inspect the installed version and local customization before replacing files. Rebuild generated metadata from canonical source instead of hand-editing generated reports.

## Uninstalling

For filesystem installs, remove only the specific SKick installation directory after confirming its path and local modifications. For managed hosts, use the host’s current Skill/plugin removal UI. Do not delete unrelated shared Skill roots or user configuration.

## Contributing

Read [`CONTRIBUTING.md`](CONTRIBUTING.md). New platform records require evidence status and activation semantics; new modules require activation rationale, context-cost estimate and evaluation coverage. Route/module count is not a quality target.

## License

MIT — see [`LICENSE`](LICENSE).
