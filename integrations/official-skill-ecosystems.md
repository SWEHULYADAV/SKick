# Official Skill Ecosystems

Use this map to route to current official/vendor Skills before generic community candidates. These entries are optional references/invocations, not vendored dependencies. Re-check the exact Skill, license and install path at use time.

| Ecosystem | Typical value | SKick rule |
|---|---|---|
| Microsoft Skills | language/cloud/product specialists, metadata-first loading | invoke only the narrow task-matched Skill |
| Anthropic Skills / Claude Code plugins | Skill patterns, frontend-design, host controls | use as host/task specialist; do not duplicate SKick core |
| OpenAI Skills / Plugins | Codex/ChatGPT patterns, apps/MCP/agents/hooks composition | inspect the full plugin payload |
| Google/Gemini Skills | Gemini/runtime and Google-domain specialists | use exact host/version evidence |
| Vercel Agent Skills | web-design, React/performance, deploy workflows | invoke when stack/use case matches |
| Android Skills | fast-moving Android gaps, Perfetto/security/adaptive UI | prefer for demonstrated model gaps |
| AWS Agent Toolkit | umbrella routing to AWS subskills + MCP | choose the smallest relevant subskill |
| Supabase Agent Skills | multi-host versioned distribution, machine discovery | prefer immutable releases for reproducible installs |
| Stripe AI | multi-host integration Skills/plugins | use restricted credentials and current docs |
| Cloudflare Skills | retrieval-first fast-moving platform guidance | prefer current official docs over memory |
| Expo Skills | mobile workflow specialists with service prerequisites | expose cost/plan/account gates first |
| Sentry Agent Skills | troubleshooting/observability workflows | preserve read-only/current evidence first |
| Trail of Bits Skills | security audit/variant/context methods | authorized security work only |
| Impeccable | design/product direction and QA concepts | absorb portable principles; optional reference |
| skills.sh / Vercel Skills | cross-agent discovery | popularity is not trust; resolve canonical upstream |

See `docs/SKILL_ECOSYSTEM_GUIDE.md` for the decision and supply-chain process.
