# Research Core


## Executable-runtime ownership
When available, `runtime/research.py` owns the initial research decision, question map, source-class route, query classes, freshness flag, pivots, budget, stopping criteria, coverage/frontier seed, and next-best-evidence field. `runtime/research_ledger.py` owns typed finding/coverage/frontier state linked to the existing evidence ledger. This module governs deeper investigation procedure and the declarative fallback; the planner does not itself browse or prove a claim.
## Purpose
Provide the platform-neutral control loop for evidence-driven technical and cross-domain investigation.

## Task framing
Build a compact internal frame before non-trivial research:

```text
Problem / goal:
Domain / technology / project:
User intent:
Observed vs expected behavior:
Version / date / reporting period / jurisdiction:
Runtime/environment:
Constraints:
Initial mechanisms/hypotheses:
Unknowns:
Required deliverable / stop condition:
```

Classify the work into relevant categories only: direct technical question; bug/root-cause; research+implementation; project/system design; library/dependency selection; architecture/migration; performance/reliability; security; reverse engineering; paper/algorithm/empirical research; biomedical/clinical; financial/market/economic; legal/government/policy; patent/prior art; structured-data analysis; ML/AI evaluation; external skill/plugin/MCP; multimodal evidence.

## Universal loop

### FRAME
Understand the real outcome and consequence. Resolve discoverable ambiguity from project/source context before asking the user.

### BUDGET
For extended work load `resource-budgeting.md`. Reserve capacity for verification, contradictions, tests, and final synthesis.

### VERSION
Resolve the version dimension that owns the claim: software tag, protocol revision, publication status, dataset vintage, filing/reporting period, trial/label status, market timestamp/venue, law effective date, patent family/status, model/runtime snapshot, or similar.

### MAP
Map relevant actors, components, interfaces, data/control flow, trust boundaries, definitions, jurisdictions, symbols, dependencies, incentives, and assumptions. For Deep/Exhaustive work load `research-evidence-lifecycle.md` and maintain a compact explored/partial/unexplored frontier plus claim ledger for load-bearing conclusions.

### ROUTE
Use `research-source-router.md` to select source families that can prove/falsify the important claims. Do not equate preferred destination with actual runtime access.

### MUTATE + LATERAL
Use `query-mutation.md` and `coverage-and-lateral-search.md`. Expand terminology, old/new names, mechanisms, symptoms, implementation symbols, adjacent ecosystems, translations, competitors, historical terms, negative evidence, and source provenance.

### SEARCH
Start with high-information discovery and direct owners of facts. Use community/catalog/search snippets only to find better evidence.

### COVER
Once a high-value source/file/record is identified, read the full relevant unit and clue-bearing neighborhood. Inspect definitions, limitations, tests, footnotes, appendices, configs, examples, history, and cross-references that can change interpretation. Avoid indiscriminate whole-universe reading.

### VERIFY
Cross-check load-bearing claims with the evidence appropriate to the domain. Use `evidence-lineage.md` so repeated downstream copies do not masquerade as independent support.

### CHALLENGE
Search for contradictions, alternate mechanisms, unsupported cases, revisions/retractions/amendments, failure modes, changed versions, platform differences, hidden definitions, and negative evidence.

### DUAL-LENS
When a system can plausibly fail, be abused, bypassed, manipulated, evaded, attacked, or defended, load `offensive-defensive.md` even if the user did not explicitly say "security". Research both sides of the mechanism:
- how the behavior/attack/failure becomes possible, including prerequisites, trust boundaries, primitives, alternate paths, bypasses and attacker/operator constraints;
- how to prevent, detect, limit, contain, investigate, recover and safely validate against it.

Apply this lens where relevant to web/API systems, auth, automation/scraping, reverse engineering, agents/MCPs, supply chain, browser/client boundaries, cloud/IAM, deployments, data pipelines, reliability and abuse/fraud surfaces. Do not force adversarial analysis onto tasks where it adds no material value. Governing safety/authorization still controls real-world execution.

### MECHANISM
Use `mechanism-first-reasoning.md` when the task asks why, how, prevent, cure, fix, exploitability, reliability, or causation. Keep competing mechanisms until discriminating evidence exists. For adversarial questions, do not stop at either "how to attack" or "how to defend" when the other side is necessary to understand the mechanism and durable controls.

### LOCALIZE
When a project/repository exists, inspect actual dependencies, configuration, source, tests, CI, runtime, deployment, custom patches, and abstractions. Local evidence constrains generic recommendations. For coding work, load `language-and-framework-intelligence.md` to resolve the actual language/framework/toolchain/version before using version-sensitive specialist guidance.

### PLAN
For a new project/major redesign, load `project-planning-and-structure.md`. Research/context comes before architecture/UI/filesystem/implementation planning. For smaller changes, define the smallest coherent action and success criteria.

### ACT
For consequential option selection, load `decision-analysis.md` to separate evidence, assumptions, constraints, reversibility, and sensitivity. Implement/recommend the smallest correct action. Apply `action-safety-transactions.md` for consequential side effects.

### TEST
Use relevant engineering/browser/data/empirical verification. Compilation or one successful tool response is not semantic proof.

### FRONTIER
Run `research-frontier.md` for Deep/Exhaustive work. Reopen only blind spots that could materially change conclusion/action.

### QUALITY + REPORT
Run `output-quality-gate.md`; lead with the answer, evidence, uncertainty, and verified action rather than raw logs/private reasoning.

## Depth
- **QUICK**: direct primary/current source plus one useful validation when needed.
- **DEEP (default for non-trivial work)**: primary evidence, lateral terminology/source checks, full relevant-unit coverage, contradiction pass, project localization, and blind-spot scan.
- **EXHAUSTIVE**: high-impact/persistent/contradictory/historical work; add archives, rejected designs, old versions/vintages, independent literature/benchmarks, cross-language sources, systematic source coverage, cold review, and reproducibility/provenance where valuable.

Depth is not response length.

## Coverage rule
Use a funnel:
`targeted discovery -> lateral expansion -> authoritative anchors -> full relevant-unit reading -> linked neighboring evidence -> contradiction/independence checks -> saturation`.

The goal is not to read everything indiscriminately; it is to avoid missing small but decision-changing details because search stopped at the first matching snippet.

## Stop condition
Stop when the completion contract is satisfied, important claims are supported, versions/definitions are resolved, major contradictions are resolved/documented, relevant edge cases were covered, and further lateral/query expansion produces mostly duplicate or low-value evidence.

Never fabricate completeness or access.
