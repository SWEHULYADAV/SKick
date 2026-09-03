# Skill Supply Chain and Lifecycle

## Purpose
Treat Skills, plugins, hooks, MCP providers, agent bundles and prompts as executable behavioral dependencies with provenance, integrity, permissions, composition risk and update lifecycle.

Use with `external-skill-intelligence.md`, `mcp-validation-and-security.md`, `action-firewall.md`, and `skill-authoring-and-evals.md`.

## Modern bundle inventory
A contemporary agent extension may contain more than `SKILL.md`. Enumerate the full payload before trust or installation:
- Skills/references/assets/scripts;
- custom agents/subagents;
- slash commands/prompts/templates;
- hooks/lifecycle monitors;
- MCP servers/configs/tools/resources/prompts;
- LSP/language-server integrations;
- executable `bin` helpers/install/update scripts;
- settings/permissions/allowlists;
- background services/monitors;
- package/dependency manifests and postinstall behavior;
- generated/native/binary artifacts.

A benign Skill file does not make the whole bundle benign.

## Descriptor distrust
Names, descriptions, trigger text, catalog ranking, stars, badges and semantic search results are routing metadata, not trust evidence. Natural-language metadata can manipulate discovery/selection.

Verify declared behavior against scripts/manifests/capabilities. A description that says "read-only review" while hooks/scripts can upload files is a contract violation.

## Currentness versus reproducibility
Fast-moving platform knowledge may require current official retrieval; stable production behavior may require immutable reviewed instructions. Make that trade-off explicit. Discover from current upstream, then resolve to a tag/SHA/tree hash when reproducibility matters. Treat a Skill that fetches mutable `main` instructions on every run as a dynamic dependency that must stay inside the untrusted-content boundary.

## Pin and lock
For reviewed external behavior that matters to a project, prefer a reproducible record:

```text
source repository:
path/skill id:
tag/ref requested:
resolved immutable commit:
content/tree hash:
license/version evidence:
reviewed capabilities:
installed targets/scopes:
review date:
```

Use a project manifest/lockfile when the host/ecosystem supports it. `main`/floating refs are discovery/update inputs, not stable production dependencies. Updates are explicit requalification events.

## Install transaction
Use:
`DISCOVER -> PREVIEW -> RESOLVE -> PIN/HASH -> SCAN -> CAPABILITY REVIEW -> COMPOSITION REVIEW -> DRY RUN -> INSTALL -> DISCOVERY VERIFY -> BEHAVIOR SMOKE -> RECORD`.

Refuse path traversal, unsafe symlinks, option/argument injection, unknown executable transports and writes outside the selected installation scope. Do not interpret installation success as runtime discovery until the host can actually see/trigger the capability.

## Composition / privilege graph
Review the installed set, not only each component independently. Model edges such as:
- component can read secret/data;
- component can send network traffic;
- component can execute shell/code;
- component can write persistent instructions/memory;
- component can approve/unquarantine/alter policy;
- component can call another privileged component.

A read-only Skill plus an unrelated network-enabled hook can create an exfiltration path even if neither is catastrophic alone. Minimize overlapping high-privilege capabilities and keep independent approval boundaries where possible.

## MCP and hook boundary
Dynamic inspection of an stdio MCP can execute a local command. Do not "scan" an unknown server by launching it on the host. Inspect source/config first and use a disposable sandbox when execution is justified.

Hook commands and background monitors are executable code. Review provenance, arguments, secret exposure, failure semantics and scope before enabling them.

## Update and revocation
On update, ownership transfer, new release, changed hash, new tool schema, new permissions, new hook/binary or changed install path:
- invalidate stale trust/capability snapshots;
- rescan/review the delta and full high-risk surfaces;
- rerun relevant behavior/security evals;
- update the lock/provenance record;
- provide rollback to the last known reviewed version.

Revoke/remove capabilities that are stale, abandoned, superseded or no longer needed.

## Value gate
Distribution convenience is not a reason to install. A new Skill/plugin must demonstrate a useful gap versus the base model, project source, native host capability or existing specialist. Measure marginal value for important dependencies using `evaluation-harness-integration.md` and `experiment-optimization-loop.md`.

## Scanner and suppression trust
Static/semantic scanners are supporting signals, not proof. If the scanned package contains its own suppression/ignore directives, do not trust them automatically: a malicious package should not be able to silence the policy that evaluates it. Keep suppressions/allowlists outside the untrusted target or require independent review. Scan realistic installed sets as well as individual Skills because composition risk can be invisible in isolated scans.
