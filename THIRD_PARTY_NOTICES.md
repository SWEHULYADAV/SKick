# Third-Party Notices and Licensing Boundaries

SKick v1.0 contains original, vendor-neutral instructions informed by publicly available projects listed in `UPSTREAMS.md`.

## No bundled upstream source trees
This package does not intentionally vendor source code, generated assets, model binaries, or full skill trees from the reviewed external repositories. Therefore their licenses are recorded for provenance and boundary decisions rather than because their complete licensed works are redistributed here.

## Important boundaries
- MIT-licensed projects were used as research/reference material; attribution is retained in `UPSTREAMS.md` where their ideas materially informed a module.
- Apache-2.0 Anthropic skills were studied and reimplemented in original form; no upstream scripts are included. If future revisions copy or modify Apache-licensed source, preserve the Apache license and required notices/modification statements.
- `JuliusBrussee/caveman` has mixed licensing. BSL-licensed engine/proxy/core code is not bundled.
- `mksglu/context-mode` is Elastic License 2.0. Its engine/plugin source is not bundled; v1.0 contains a vendor-neutral context-management protocol and optional reference/integration guidance.
- Catalog licenses do not automatically cover the individual projects they list. Resolve each candidate's own license before adoption.

Licenses and repository terms can change. Re-verify current upstream licensing before future vendoring, redistribution, or deep integration.

- v1.0 does not bundle Superpowers, Serena, Context7, GitHub MCP Server, Playwright MCP, Chrome DevTools MCP, Sentry MCP, Docker MCP Gateway, or MCP Registry code. It bundles only original integration/routing instructions and metadata.
- Sentry MCP was reviewed under FSL-1.1-Apache-2.0 future licensing; no Sentry source is copied into this package.

## Additional boundaries
- OpenAI Symphony is Apache-2.0; no Symphony implementation code is bundled. Harness Engineering article concepts are re-expressed as vendor-neutral methodology.
- Hugging Face Skills were observed Apache-2.0; Trail of Bits Skills are CC-BY-SA-4.0; Sentry Skills are Apache-2.0. Their skill trees are not copied into this package.
- Vercel agent-browser is Apache-2.0 and includes install-time/package behavior; it is optional metadata/integration only, not bundled executable code.
- mini-SWE-agent, Open SWE, Deep Agents, Pydantic AI and Pydantic AI Harness are reference harnesses; no source is bundled.
- Inspect AI/Inspect Evals and Harbor are optional external evaluation backends; benchmark/task datasets may have additional licenses even when the harness is permissively licensed.
- Snyk Agent Scan is optional and may send component metadata to Snyk and execute configured stdio MCP commands during inspection; it is never silently run by this package.
- AWS/Azure/database/research MCP providers are metadata/routing entries only. Credentials, binaries, SDKs, hosted-service rights and usage charges are not included.

## freshtechbro/claudedesignskills
- Upstream: https://github.com/freshtechbro/claudedesignskills
- Observed license: MIT.
- Use in v1.0: research/reference and original vendor-neutral reimplementation of selected design, motion and WebGL methodology.
- No upstream skill files, generated assets, framework packages, or Claude marketplace bundle are included in this package.

See `UPSTREAMS.md` for the adoption boundary and current-source corrections.


## Agent-control research references (2026-08-31)
- Piebald Claude Code system-prompt corpus is used as reverse-engineering/reference material only; no extracted prompt files are bundled or copied verbatim into SKick.
- Gemini CLI and Qwen Code are Apache-2.0 references; Kimi CLI and Cline are also referenced under their observed permissive repository licenses. SKick contains original vendor-neutral methodology, not their source trees.
- `karpathy/autoresearch` is referenced for the measurable keep/revert experiment pattern. Because repository license metadata has had inconsistency reports, SKick does not copy its source or `program.md` template.
- `smart-mcp-proxy/mcpproxy-go` is an MIT-licensed optional reference; no proxy binary/source is bundled.
- `punkpeye/awesome-mcp-servers` is used only as a discovery catalog. Candidate servers retain their own independent licenses and trust boundaries.

## 2026-08-31 research/reference additions

The language/UI/research/purple-team hardening pass references Android Skills, Kotlin Agent Skills, Angular Skills, Microsoft/.NET Skills, rewrite-rs Skills, Playwright, Microsoft Deep Wiki, Matt Pocock Skills, Trail of Bits Skills, MITRE ATT&CK/D3FEND/CAPEC/CALDERA, SigmaHQ, CISA KEV, FIRST EPSS, OWASP GenAI and skills-lock.

SKick does **not** vendor their source code, rule corpora, prompt text or binaries in this repository as part of this pass. Vendor-neutral mechanisms were reimplemented in original SKick wording. When an external Skill/tool is invoked or later vendored, re-check its current component-level license, attribution, data-egress and execution behavior first. Trail of Bits Skills are treated as CC-BY-SA reference/invocation material rather than copied into the MIT canonical core. Sigma specification/rules and OWASP/site content have their own terms; no corpus content is redistributed here.
