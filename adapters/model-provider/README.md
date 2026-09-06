# Model / Provider Adapter — ROUTE TO THE HOST

A model or API provider is not automatically a Skill runtime. SKick installs into the **agent/harness that runs the model**, not into the provider name.

Examples include model-only use of Meta Llama, ByteDance/Doubao/Seed, Amazon Nova, Cohere, IBM Granite, Baidu ERNIE, Tencent Hunyuan, MiniMax, DeepSeek, GLM, LongCat, and other providers when they are accessed through an API, local server, or third-party coding agent.

## Routing

1. Identify the actual host: Claude Code, Codex, Cline, Cursor, OpenCode, BrowserCode, Qwen Code, Kimi Code, TRAE, Windsurf, a custom harness, etc.
2. Install SKick using that host adapter.
3. If the user only has a chat/web/API surface with no persistent skill mechanism, use `../generic/PROMPT.md` as a session-level fallback.
4. If the user controls the harness, implement the open Agent Skills lifecycle described in `../../docs/NEW_RUNTIME_INTEGRATION.md`.

Never fabricate a provider-specific filesystem path just because a model supports tools or coding.

## Compatibility proof contract

- **Verification status:** `HOST_DEPENDENT`
- **Runtime tier:** `prompt_fallback` for the provider-only route; the selected host may provide a stronger tier.
- **Native Skill support:** `host_dependent`
- **Literal `@SKick`:** `no` for the provider-only route. Any `@`/slash/dollar syntax belongs to the actual host and must be verified there.

A model-provider entry can be documentation-current without becoming a Skill host. Discovery, invocation, filesystem access, shell access, and live execution must be attributed to the host that actually supplies them.
