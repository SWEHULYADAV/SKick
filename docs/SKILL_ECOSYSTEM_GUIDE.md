# Official Skill Ecosystems and Discovery Guide

Last reviewed: **2026-09-03**.

Use this document when SKick must discover, compare, install, recommend, or learn from external Agent Skills/plugins. The objective is **best capability per phase**, not maximum Skill count.

## Discovery order

1. Current project/native capability already present.
2. Official vendor Skill/plugin repository for the relevant product or domain.
3. Maintained specialist repository with clear provenance and licensing.
4. Open discovery indexes/marketplaces such as skills.sh, GitHub search, or curated lists.
5. Generic community candidates only when the first four do not cover the gap.

Catalog rank, install count and stars are discovery signals—not proof of correctness or safety.

## High-value official/reference ecosystems

| Ecosystem | Why SKick cares | Adoption rule |
|---|---|---|
| `microsoft/skills` | large language/cloud/product catalog; metadata-first discovery and selective loading | reference/invoke narrow specialists, never bulk-load |
| `anthropics/skills` and Claude Code plugins | open Skill patterns, frontend-design specialist, host-specific invocation controls | reference/invoke when host/task matched |
| `openai/skills` and `openai/plugins` | OpenAI Skill/plugin patterns, apps/MCP/agents/hooks composition | official reference for OpenAI surfaces; inspect full bundle |
| Google/Gemini Skill repositories | Gemini CLI/Google domain Skills and runtime conventions | use official current docs and exact host |
| `vercel-labs/agent-skills` | web-design and React/performance specialists | invoke only when stack/use case matches |
| `vercel-labs/web-interface-guidelines` | broad web UI/a11y/forms/motion/performance review rules | reference current/pinned rules; do not blindly fetch mutable `main` in reproducible workflows |
| `android/skills` | official Android SOTA-gap Skills and performance/security workflows | invoke for fast-moving Android gaps, not generic syntax |
| `aws/agent-toolkit-for-aws` | umbrella Skill + routed subskills and AWS MCP integration | route to smallest relevant subskill |
| `supabase/agent-skills` | versioned multi-host skills and `.well-known/agent-skills` discovery | use immutable release artifacts when reproducibility matters |
| `stripe/ai` | official multi-host plugin/Skill distribution and manual-install update caveats | use least-privilege keys and current official docs |
| `cloudflare/skills` | explicit retrieval-over-pretraining discipline for fast-moving platform knowledge | prefer current docs retrieval |
| `expo/skills` | category metadata and explicit service/cost prerequisites | surface cost/plan/dependency gates before activation |
| `getsentry/sentry-agent-skills` | phased troubleshooting and version requirements | use read-only/current evidence first |
| `trailofbits/skills` | security context-building and variant-analysis discipline | reference/invoke for authorized security work |
| `pbakaus/impeccable` | design direction, PRODUCT/DESIGN separation and bounded QA concepts | absorb portable principles; do not make a mandatory dependency |
| `skills.sh` / `vercel-labs/skills` | broad discovery and popularity signals | discovery only; resolve canonical upstream and review before install |

## Discovery protocol

Use:

`NEED -> OFFICIAL SEARCH -> CANDIDATE METADATA -> SOURCE RESOLUTION -> PREVIEW -> VALUE GATE -> SECURITY/COMPOSITION REVIEW -> PIN/HASH -> INSTALL -> DISCOVERY VERIFY -> SMOKE -> RECORD`

Important mechanisms now seen across mature ecosystems:
- **metadata-first discovery**: expose name/description before loading full Skill bodies;
- **tiered precedence**: built-in/extension/user/workspace or equivalent, with explicit override rules;
- **umbrella router Skills**: one narrow routing Skill dispatches to subskills instead of loading all domains;
- **preview before install**: e.g. current `gh skill preview`;
- **immutable pinning/provenance**: tag/SHA/tree hash and update metadata;
- **`.well-known/agent-skills` indexes**: useful for machine discovery, but still not a trust root;
- **plan/cost capability metadata**: tell users when a Skill requires a paid service, account, region or external CLI;
- **manual-copy update warning**: a copied Skill may not auto-update even when a plugin/managed install would.

## Currentness vs reproducibility

Two goals can conflict:
- for fast-moving SDK/platform questions, current official retrieval may be necessary;
- for repeatable production behavior, a mutable remote instruction source is undesirable.

Resolve this explicitly. Discover from current upstream, then pin/tag/hash the reviewed version when reproducibility matters. Do not execute a production workflow by fetching arbitrary mutable `main` instructions on every invocation unless that behavior is intentional and risk-reviewed.

## GitHub CLI Skill workflow

GitHub CLI 2.90+ currently provides a useful inspect-first pattern:

```text
gh skill search TOPIC
gh skill preview OWNER/REPOSITORY SKILL
gh skill install OWNER/REPOSITORY SKILL --pin TAG_OR_SHA
gh skill update SKILL
```

Use `--agent` and `--scope` when targeting a supported host. Preview remains mandatory for untrusted sources; GitHub explicitly states that Skills are not verified for safety merely because they are installable.

## `npx skills` and marketplaces

`npx skills`/skills.sh can reduce installation friction across many agents. Treat it as **transport/discovery**, not as the owner of the Skill's truth. Resolve the canonical upstream, inspect the actual package, record the installed version/source, and verify which host path was written.

## What not to absorb

Reject a candidate when it mainly adds:
- generic syntax the base model already handles;
- another full engineering methodology that conflicts with SKick;
- duplicated tools/MCPs without marginal value;
- hidden network/install/telemetry behavior;
- host-specific assumptions that would leak into canonical core;
- popularity without current maintenance/evidence.
