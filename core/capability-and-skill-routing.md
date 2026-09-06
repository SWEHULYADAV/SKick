# Capability and Skill Routing

## Purpose
Make SKick a capability broker: identify the strongest safe, current, task-matched Skill/plugin/MCP/native tool for each phase, delegate narrowly, and keep the overall objective and verification contract under SKick control.

This module is mandatory for non-trivial engineering/research work where more than one capability may exist.

## Capability preflight
Before substantial execution, build a compact internal capability map. Do not dump it to the user unless it helps the decision.

For each required phase, determine:
- the capability needed, not merely a product name;
- which already-installed/native Skills, plugins, MCPs or tools can provide it;
- whether repository/project-local instructions declare a preferred specialist;
- whether the candidate is current enough for the task;
- whether its permissions, scripts, dependencies and provenance are acceptable;
- whether it duplicates another workflow that already owns the phase;
- the fallback if the preferred capability cannot be used.

Typical capabilities include `RESEARCH`, `REPO_MAP`, `SYMBOL_SEARCH`, `REFERENCES`, `ARCHITECTURE`, `PLAN`, `EDIT`, `TEST`, `DEBUG`, `SECURITY_REVIEW`, `CODE_REVIEW`, `BROWSER_QA`, `DATA_ANALYSIS`, `DEPLOY`, and `VERIFY`.

## Discovery order
Use the smallest search surface that can find a good owner:

1. governing user/system constraints and explicitly requested Skill/tool;
2. project-local installed Skills/instructions and host-native capabilities;
3. installed task-specific Skills/plugins with a narrower declared scope;
4. trusted, already-configured MCP/tool providers;
5. current external Skill/plugin discovery only when it can materially improve the result and installation/use is allowed;
6. SKick-native methodology plus simple host tools as the fallback.

Do not search for extra tools merely to add complexity. Do not silently install third-party executables, plugins, MCP servers or Skills. An explicit request to install named SKick components authorizes only those named components and still requires provenance/version checks.

## Best-capability score
Prefer the candidate with the best combined fit, not the most famous name. Evaluate:

- **scope fit** — directly owns the current phase/task;
- **project fit** — understands or integrates with the active repository/environment;
- **capability quality** — can produce the required evidence or action precisely;
- **freshness** — current upstream/runtime behavior is known when version-sensitive;
- **testability** — output can be checked independently;
- **safety and provenance** — upstream, permissions, scripts and side effects are understood;
- **conflict/overlap cost** — does not stack a duplicate methodology on the same phase;
- **context/tool cost** — avoids loading a large Skill/toolchain for a tiny benefit;
- **fallback quality** — failure does not strand the task.

Reject a candidate when it cannot prove the needed claim/action, is stale for a version-sensitive task, has unacceptable trust/permission risk, or conflicts with higher-priority constraints. Vendor identity is never a global score bonus; a project policy may prefer a named implementation only when explicitly configured or supported by local evidence.

## Phase ownership
Keep one primary owner per phase. A compact route may look like:

```text
REPO_MAP       -> best semantic capability -> symbols/references -> native index/LSP/search fallback
ARCHITECTURE   -> SKick        -> project/research synthesis  -> project-native architecture docs
IMPLEMENT      -> specialist   -> narrow workflow fit         -> SKick implementation discipline
CODE_REVIEW    -> reviewer     -> independent review          -> SKick cold review
VERIFY         -> SKick        -> acceptance/evidence gate    -> never delegated away
```

Do not run two full planning/debugging/TDD methodologies in parallel unless the task explicitly needs independent comparison. Specialists may own execution; SKick retains the user's objective, evidence quality, version boundaries, trust/safety, provenance, acceptance criteria and final verification.

## Deferred capability loading
When many Skills/tools/MCP schemas exist, load `deferred-capability-loading.md`. Route from compact capability metadata first and load the full Skill body/tool schema only for shortlisted owners. Tool-context reduction is an optimization, not a trust bypass; unqualified providers remain blocked.

## Dynamic routing during work
Re-route when evidence changes. Examples:
- a repository turns out to use a framework with a dedicated installed Skill;
- a host-native code index lacks the reference precision required for the task;
- a specialist produces an unverifiable claim;
- a browser issue requires network evidence rather than only screenshot evidence;
- an external Skill is useful for discovery but unsafe to execute.

Record only material routing changes in the final report.

## External Skill intelligence
When a missing specialist could materially improve the work, use `external-skill-intelligence.md` before adoption. Resolve canonical upstream, current version, license, scripts/dependencies, permissions, overlap and runtime compatibility. Treat registries/catalogs as discovery aids, not authority.

## Non-negotiable verification rule
Delegation never transfers proof. A Skill, MCP, model or scanner saying “done” is evidence to test, not completion. Validate through the project/runtime/source family that can actually establish the claim.

## Domain fingerprint before specialist selection
Before selecting a coding specialist, fingerprint the active language/framework/toolchain/version with `language-and-framework-intelligence.md`. Before selecting a UI specialist, fingerprint the product/design-system/render surface with `ui-system-and-render-intelligence.md`. Before selecting a security specialist, classify whether the phase is context-building, vulnerability/variant analysis, detection, emulation, DFIR or response using `purple-team-research-and-validation.md`. This prevents a popular but mismatched Skill from winning routing merely because its description is broad.
