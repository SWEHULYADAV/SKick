# Agent Control Pattern References

## Purpose
Record high-value mechanisms observed in current coding-agent ecosystems without copying their control planes wholesale. These are research references, not mandatory dependencies.

## Piebald Claude Code prompt corpus
Upstream: https://github.com/Piebald-AI/claude-code-system-prompts

Observed value:
- conditionally loaded tool and agent instructions;
- tool search/deferred schema loading;
- separate plan/explore/review utilities;
- autonomous-action security review patterns;
- memory selection/consolidation utilities;
- batch/worktree and post-change simplification patterns.

Decision: **absorb mechanisms, reference corpus, do not vendor prompt text**. The repository is maintained by Piebald and says its material is extracted from Claude Code compiled distributions; treat it as reverse-engineering evidence, not an Anthropic specification or a license grant over Anthropic product behavior.

Implementation: `core/action-firewall.md`, `core/deferred-capability-loading.md`, `core/verified-review-and-simplification.md`, `core/memory-governance.md`, `core/multi-agent-orchestration.md`.

## Google Gemini CLI Auto Memory
Upstream: https://github.com/google-gemini/gemini-cli

Observed value:
- past-session mining produces memory/Skill candidates rather than silently mutating active instructions;
- candidates are stored in a review inbox;
- patch parsing, target allowlists, dry-run and atomic apply boundaries;
- experimental feature status and real failure modes show why candidate validation and explicit approval matter.

Decision: **absorb reviewed-candidate workflow; no background service dependency**.

Implementation: `core/memory-governance.md`, `core/skill-authoring-and-evals.md`.

## Qwen Code memory
Upstream: https://github.com/QwenLM/qwen-code

Observed value:
- user-authored project instructions plus agent-managed auto-memory;
- private project memory and opt-in git-shared team memory scopes;
- periodic consolidation/dream behavior;
- issue history demonstrates stale-index/compaction risks that a robust memory design must detect.

Decision: **absorb scoping, consolidation and refresh/invalidation lessons; keep SKick provenance/TTL rules authoritative**.

Implementation: `core/memory-governance.md`, `core/context-management.md`.

## Karpathy autoresearch
Upstream: https://github.com/karpathy/autoresearch

Observed value:
- small mutable surface plus protected evaluator;
- fixed measurable objective;
- snapshot/commit each candidate;
- keep measurable wins and revert regressions;
- compact experiment log.

Decision: **absorb the measurable keep-or-revert pattern, but bound it with SKick budgets/stop contracts and stochastic-eval rules**. README currently labels the project MIT; license-file history has been inconsistent, so do not copy source/templates without rechecking current licensing.

Implementation: `core/experiment-optimization-loop.md`.

## Kimi CLI hooks and subagents
Upstream: https://github.com/MoonshotAI/kimi-cli

Observed value:
- lifecycle hooks around pre/post tool calls, failures, session start/end, subagents and compaction;
- custom agents with bounded tool/subagent sets.

Decision: **absorb host-neutral lifecycle-hook semantics; treat hook commands as executable third-party/local code requiring normal safety review**.

Implementation: `core/multi-agent-orchestration.md`, `core/action-firewall.md`, `core/harness-and-runtime-intelligence.md`.

## Cline checkpoints / Kanban worktrees
Upstream: https://github.com/cline/cline and https://github.com/cline/kanban

Observed value:
- reversible checkpoints during agent work;
- task-board parallelism with per-task worktrees, auto-commit and dependency chains;
- headless/structured automation surfaces.

Decision: **absorb isolation/checkpoint/dependency patterns; do not require Cline as a runtime**.

Implementation: `core/multi-agent-orchestration.md`, `core/action-safety-transactions.md`.

## Smart MCP Proxy
Upstream: https://github.com/smart-mcp-proxy/mcpproxy-go

Observed value:
- compact tool discovery followed by on-demand schema loading;
- explicit read/write/destructive intent separation;
- quarantine of newly added servers;
- security inspection, audit and re-quarantine concepts.

Decision: **absorb security/routing patterns and keep the proxy optional**. Provider-reported token/accuracy claims must be measured independently before SKick repeats them as local gains.

Implementation: `core/deferred-capability-loading.md`, `core/mcp-validation-and-security.md`.

## Awesome MCP catalogs
Discovery lead: https://github.com/punkpeye/awesome-mcp-servers

Decision: **discovery only**. Use popular/curated lists to widen candidate coverage, then resolve every candidate to its canonical upstream and run SKick's license/security/maintenance/overlap gates before adoption. A catalog entry is never execution authorization.
