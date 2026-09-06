# SKick v1 Specification-vs-Runtime Gap Matrix

This matrix freezes the audited v1 state before vNext runtime changes. It distinguishes what the package **says**, what local software **does deterministically**, what is **covered by automated execution**, what has been **behaviorally measured**, and what has been **live verified across platforms**.

Status vocabulary:

- **DECLARED** — prose/instruction only.
- **PARTIALLY EXECUTABLE** — schema/script exists, but the claimed behavior still depends materially on host/model compliance or incomplete observation.
- **EXECUTABLE** — deterministic local software performs or validates the behavior.
- **TESTED** — executable behavior is automatically exercised with assertions or release checks.
- **BEHAVIORALLY EVALUATED** — actual candidate-agent behavior was measured, not merely an eval file loaded.
- **CROSS-PLATFORM VERIFIED** — the behavior was exercised on multiple real target hosts with reproducible artifacts.

| Capability | v1 level | Evidence | Gap driving vNext |
|---|---|---|---|
| Task classification | DECLARED | `docs/INVOCATION_AND_MODES.md`, `SKILL.md` | No machine-readable classifier or traceable decision. |
| Execution-depth selection | DECLARED | `quick/standard/deep/exhaustive` prose | No deterministic/observable scoring, calibration, or regression tests. |
| Progressive module loading | DECLARED | `SKILL.md` progressive-loading index | Host model chooses what to read; no compiled module plan or cost record. |
| Deferred capability loading | DECLARED | `core/deferred-capability-loading.md` | No runtime capability index or enforceable staged loader. |
| Capability discovery | PARTIALLY EXECUTABLE | `scripts/detect_runtime.py` checks markers/executables | Host/tool capabilities, permissions, unknown/restricted states are not represented. |
| Capability routing | DECLARED | `core/capability-and-skill-routing.md` | No score/result artifact; Serena preference can act like a global default. |
| Installed Skill discovery | DECLARED | adapters/installer verification instructions | Files can be copied, but host discovery is not mechanically observed by SKick. |
| Tool selection | DECLARED | capability broker prose | No local routing result or unavailable-tool hallucination tests. |
| Runtime detection | EXECUTABLE | `scripts/detect_runtime.py` | Produces candidate hints, not authoritative host/capability state; no unit tests. |
| Context budgeting | PARTIALLY EXECUTABLE | `schemas/budget.schema.json`, context docs | Schema exists but no compiler populates/enforces it. |
| Token budgeting | PARTIALLY EXECUTABLE | budget/token-efficiency docs | No measured/estimated per-module cost or selected-context total. |
| Evidence capture | PARTIALLY EXECUTABLE | evidence/trace schemas and methodology | No append-only run ledger is populated by a runtime. |
| Claim verification | DECLARED | evidence/output/action modules | No code prevents `verified` language without adequate evidence. |
| State tracking | PARTIALLY EXECUTABLE | `schemas/task-state.schema.json`, trace schema | Passive schemas; no standard run-state producer/consumer. |
| Provenance tracking | TESTED (static) | `build_provenance.py`, `verify_provenance.py`, CI | Verifier checks listed artifacts only; it does not detect unlisted files, proven by `assets/icon.svg` drift. |
| Testing discipline | DECLARED | engineering feedback/test methodology | Agent compliance only; no runtime task-state transition is tied to test evidence. |
| Research verification | DECLARED | research/evidence modules | Strong methodology, no enforceable evidence ledger/report gate. |
| Mode escalation | DECLARED | invocation/mode docs | No observable escalation/de-escalation decision. |
| Platform discovery | PARTIALLY EXECUTABLE | installation manifest, platform catalog generator | Registry is structured, but v1 proof vocabulary conflates documentation/support confidence. |
| Install verification | PARTIALLY EXECUTABLE | installer + adapter verification text + dry runs | Dry-run/copy success is not host discovery/invocation/live task success. |
| Explicit Skill activation | DECLARED / HOST DEPENDENT | adapter docs | Literal syntax varies; no normalized machine-readable activation contract. |
| Automatic Skill activation | DECLARED / HOST DEPENDENT | trigger instructions/evals | 53 trigger cases exist but are not executed against actual host behavior in CI. |
| Evaluation execution | PARTIALLY EXECUTABLE | `scripts/run_evals.py` | Runner executes, but candidate `passed` is accepted as aggregate success and deterministic scoring is absent. |
| Baseline comparison | EXECUTABLE (aggregate only) | `scripts/compare_evals.py` | Only top-level mean deltas; no task-level regressions/wins/paired analysis. |
| Ablation testing | DECLARED | experiment methodology | No executable local ablation suite. |
| Security policy enforcement | PARTIALLY EXECUTABLE | untrusted-content policy + static scanner | Package scanner is executable; agent action/prompt-injection defenses are primarily instructions. |
| Final reporting | DECLARED | output protocol/quality gate | No reporter that mechanically caps claim strength by evidence. |

## Baseline execution

The local reconstructed v1 tree was executed before code changes:

- Python compile: PASS.
- Strict static Skill scan: PASS.
- MCP catalog validation: PASS.
- **Package validation: FAIL** — `assets/icon.svg` is present but absent from `tests/package-manifest.txt`.
- Release audit: PASS despite the package failure.
- Behavioral eval suite: 97 definitions load; no candidate model execution.
- Trigger eval suite: 53 definitions load; no host activation execution.
- Portability eval suite: 38 definitions load.
- Distribution build + structural validation: PASS.
- Provenance verification: PASS for 235 listed files, illustrating that v1 provenance verification does not detect unlisted package files.

Raw console output from the baseline was kept outside source control; the sanitized machine-readable baseline is `artifacts/baseline-v1.json`.

## Baseline measurement boundary

A same-model, same-tools `WITHOUT SKick` versus `WITH SKick v1` behavioral comparison is **BASELINE_BLOCKED** in this ChatGPT host because the installed Skill cannot be cleanly disabled while holding the rest of the host configuration identical. No behavioral improvement is inferred from static architecture or eval definitions.
