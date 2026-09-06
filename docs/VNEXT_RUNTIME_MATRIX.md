# SKick v1.1 Specification-vs-Runtime Matrix

Levels are cumulative only where evidence supports them. `TESTED` below means deterministic automated tests. `BEHAVIORALLY EVALUATED` means an actual candidate model/agent was measured; deterministic router fixtures do not qualify. `CROSS-PLATFORM VERIFIED` requires reproducible real-host execution.

| Capability | v1 | v1.1 | Evidence / remaining boundary |
| --- | --- | --- | --- |
| Task classification | DECLARED | EXECUTABLE + TESTED + deterministic local eval | `runtime/depth.py`; routing fixtures. Host-native auto-discovery remains separate. |
| Prompt enhancement / intent preservation | DECLARED | EXECUTABLE + TESTED + deterministic local eval | `runtime/prompt_intelligence.py` preserves `original_request`, locks explicit constraints, reports contradictions, and supports silent/visible/execution/strict-spec planning. Host prose behavior remains separate. |
| Research-need selection and question/source/query planning | DECLARED | EXECUTABLE + TESTED + deterministic local eval | `runtime/research.py`; plans research level, question map, source/query classes, freshness, pivots, budget, stopping criteria and frontier. It does not browse by itself. |
| Lateral/disconfirmation planning | DECLARED | EXECUTABLE + TESTED planner + deterministic ablation | Deep/lateral plans add distinct evidence neighborhoods and disconfirmation branches; planner diversity/cost is measured, answer-quality benefit is **NOT_MEASURED**. |
| Research finding / frontier / source-lineage state | DECLARED | EXECUTABLE + TESTED | `runtime/research_ledger.py`; fact/inference/hypothesis/opinion/unknown findings link to evidence; lineage groups prevent copied sources counting as independent paths. |
| Research execution and factual source quality | DECLARED | HOST-DEPENDENT / PARTIALLY EXECUTABLE | Planner selects capabilities and source classes, but real web/source/history/live experiments require host tools. No deterministic fixture is promoted to factual research proof. |
| Red/Blue/Purple/Black-Blind selection and safe scope | DECLARED | EXECUTABLE + TESTED + deterministic local eval | `runtime/teaming.py`; ordinary debugging avoids team overhead, security work is scoped, unknown authorization uses lab/simulation boundary. Real exploit/mitigation behavior remains host/safety dependent. |
| Execution-depth selection | DECLARED | EXECUTABLE + TESTED + deterministic local eval | `quick/standard/deep/exhaustive` preserved; explicit override tested. |
| Progressive module loading | DECLARED | EXECUTABLE + TESTED at plan/compiler layer | Compiler emits selected/skipped/reasons; actual host injection remains host-dependent. |
| Deferred capability loading | DECLARED | PARTIALLY EXECUTABLE + TESTED | Compiler/routing can request capabilities; universal host tool-schema loading still depends on host APIs. |
| Capability discovery | PARTIALLY EXECUTABLE | EXECUTABLE + TESTED for observable local probes | Six-state model; host-only surfaces remain `unknown`/declared where unobservable. |
| Capability routing | DECLARED | PARTIALLY EXECUTABLE + TESTED | Module/provider policy is executable; universal external-tool invocation broker is host-dependent. |
| Installed Skill discovery | DECLARED | PARTIALLY EXECUTABLE + TESTED | Doctor/install state can inspect files; managed-host discovery requires host API/UI evidence. |
| Tool selection | DECLARED | PARTIALLY EXECUTABLE + TESTED | Capability vocabulary/fallback is executable locally; host tool invocation is not universally interceptable. |
| Runtime detection | EXECUTABLE | EXECUTABLE + TESTED | Backward-compatible hinting plus structured capability snapshot. |
| Context budgeting | PARTIALLY EXECUTABLE | EXECUTABLE + TESTED | Compiler calculates selected-module budget and skip reasons. |
| Token budgeting | PARTIALLY EXECUTABLE | EXECUTABLE + TESTED estimate | Byte/4 estimate is labeled; exact tokenizer use remains optional/host-specific. |
| Evidence capture | PARTIALLY EXECUTABLE | EXECUTABLE + TESTED | Structured append-only-style run evidence ledger. |
| Claim verification | DECLARED | EXECUTABLE + TESTED | Claim firewall blocks unsupported promotion. Declarative hosts still rely on instructions unless reporter runs. |
| State tracking | PARTIALLY EXECUTABLE | EXECUTABLE + TESTED | Runtime state is produced/validated and contains no hidden chain-of-thought. |
| Provenance tracking | TESTED but incomplete | EXECUTABLE + TESTED, complete-set check | Unlisted canonical files now fail verification. |
| Testing discipline | DECLARED | PARTIALLY EXECUTABLE + TESTED | `TESTED` claim requires passing test evidence; agent cannot be forced to run tests on every host. |
| Research verification | DECLARED | PARTIALLY EXECUTABLE + TESTED | Evidence/claim/report structures enforce proof states; source-quality decisions remain partly agent/host work. |
| Mode escalation | DECLARED | EXECUTABLE + TESTED + deterministic local eval | Observable classification reasons/depth. |
| Platform discovery | PARTIALLY EXECUTABLE | PARTIALLY EXECUTABLE + TESTED | Registry is structured/current; real host capability is still probed/declared at runtime. |
| Install verification | PARTIALLY EXECUTABLE | EXECUTABLE + TESTED for state separation | `COPIED/INSTALLED/DISCOVERED/INVOKABLE/LIVE_TESTED` cannot collapse; external discovery may remain unknown. |
| Explicit Skill activation | DECLARED / HOST DEPENDENT | STRUCTURED + TESTED registry, HOST DEPENDENT live | Normalized activation fields; literal `@SKick` not generalized. |
| Automatic Skill activation | DECLARED / HOST DEPENDENT | deterministic classifier EVALUATED LOCALLY; HOST BEHAVIOR NOT MEASURED | Confusion matrix applies to frozen local fixtures, not native host semantics. |
| Evaluation | PARTIALLY EXECUTABLE | EXECUTABLE + TESTED deterministic core | Executor/raw result/checks/optional judge separated. Cross-model behavioral runs remain NOT_MEASURED here. |
| Baseline comparison | EXECUTABLE aggregate only | EXECUTABLE + TESTED task-level | Per-task deltas/regressions/win-loss-tie; repeated-sample statistics only when meaningful. |
| Ablation testing | DECLARED | EXECUTABLE + TESTED local | Guard-module ablations measure cost and missing required guard. Model-quality ablations remain NOT_MEASURED. |
| Security policy enforcement | PARTIALLY EXECUTABLE | PARTIALLY EXECUTABLE + TESTED | Static scan + trust/module/claim guards are executable; arbitrary host actions cannot be universally intercepted. |
| Final reporting | DECLARED | EXECUTABLE + TESTED | Structured renderer caps claim status to evidence when runtime is used. |

## Behavioral/cross-platform boundary

No row above is promoted to `BEHAVIORALLY EVALUATED` solely because local deterministic fixtures pass. Controlled same-model no-SKick/v1/v1.1 trials were `BASELINE_BLOCKED` in the active host. No external route is marked `LIVE_TESTED` without a real host record, so cross-platform verification remains incomplete by design.
