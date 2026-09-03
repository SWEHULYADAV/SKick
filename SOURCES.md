# Platform and Research Source Ledger

Verification baseline: **2026-09-03**. Version-sensitive runtime routes are rechecked against first-party/product documentation before release; ecosystem-only routes remain explicitly classified as such. These URLs document runtime conventions and high-value research destinations. `core/` remains platform-neutral; a listed source never implies that every runtime has direct/API access.

## Open standards
- Agent Plugins v1 specification: https://agent-plugins.org/specification
- Agent Skills open standard: https://agentskills.io/

## OpenAI / ChatGPT / Codex
- ChatGPT Skills: https://help.openai.com/en/articles/20001066-skills-in-chatgpt/
- Plugins in ChatGPT and Codex: https://help.openai.com/en/articles/20001256-plugins-in-chatgpt-and-codex
- OpenAI Plugins repository: https://github.com/openai/plugins
- OpenAI Codex repository: https://github.com/openai/codex
- Codex Windows Desktop repo-local Skill discovery issue (dated runtime troubleshooting evidence, not a general contract): https://github.com/openai/codex/issues/40458


### 2026-08-23 targeted recheck
- OpenAI ChatGPT Skills upload/install flow: https://help.openai.com/en/articles/20001066
- OpenAI Plugins in ChatGPT and Codex: https://help.openai.com/en/articles/20001256
- GitHub Copilot customization/Agent Skills: https://docs.github.com/en/copilot/reference/customization-cheat-sheet
- GitHub Copilot Agent Skills/code review context: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review


## 2026-08-23 direct-ZIP / installer recheck

The self-describing installation work rechecked the following current first-party sources before encoding runtime-specific paths/flows in `INSTALLATION_MANIFEST.json` and adapters:

- OpenAI ChatGPT Skills upload/install and cross-surface note: https://help.openai.com/en/articles/20001066
- OpenAI ChatGPT/Codex Plugins overview: https://help.openai.com/en/articles/20001256
- OpenAI Codex/Skills current repository and skill-installer behavior: https://github.com/openai/codex and https://github.com/openai/plugins
- Claude Code Skills: https://code.claude.com/docs/en/slash-commands
- Claude Code Plugins: https://code.claude.com/docs/en/plugins
- GitHub Copilot Agent Skills: https://docs.github.com/en/copilot/concepts/agents/about-agent-skills
- GitHub Copilot adding/managing Agent Skills: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills
- Cursor Agent Skills: https://cursor.com/docs/skills
- Gemini CLI Agent Skills: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/skills.md
- OpenCode Agent Skills: https://opencode.ai/docs/skills
- Qwen Code Agent Skills: https://qwenlm.github.io/qwen-code-docs/en/users/features/skills/
- Kimi Code Skills: https://www.kimi.com/code/docs/en/kimi-code-cli/customization/skills.html
- ZCode Skills: https://zcode.z.ai/en/docs/skill
- Mistral Vibe Code Skills: https://docs.mistral.ai/vibe/code/cli/skills

Where a platform/model still lacks a verified standalone Skill importer, the manifest intentionally routes to the actual host runtime or generic fallback rather than inventing a path.

## Anthropic / Claude
- Claude custom Skill creation: https://support.claude.com/en/articles/12512198-how-to-create-custom-skills
- Claude Skill use/upload: https://support.claude.com/en/articles/12512180-use-skills-in-claude
- Claude Code plugins: https://code.claude.com/docs/en/plugins
- Claude Code plugin reference: https://code.claude.com/docs/en/plugins-reference
- Anthropic Skills examples: https://github.com/anthropics/skills

## Google Gemini / Antigravity
- Gemini Apps Skills: https://support.google.com/gemini/answer/17094296
- Gemini CLI Agent Skills: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/skills.md
- Gemini CLI skill creation: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/creating-skills.md
- Antigravity Skills: https://antigravity.google/docs/skills
- Antigravity Plugins: https://antigravity.google/docs/plugins
- Antigravity CLI plugins/skills: https://antigravity.google/docs/cli/plugins/

## Cursor
- Cursor Agent Skills: https://cursor.com/docs/skills
- Cursor Plugins / Agent Plugins support: https://cursor.com/docs/plugins

## GitHub Copilot
- About Agent Skills: https://docs.github.com/en/copilot/concepts/agents/about-agent-skills
- About Copilot plugins: https://docs.github.com/en/copilot/concepts/agents/about-plugins
- Copilot CLI plugin reference: https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference
- Creating a Copilot CLI plugin: https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating

## Qwen Code
- Qwen Agent Skills: https://qwenlm.github.io/qwen-code-docs/en/users/features/skills/
- Qwen Agent Plugins v1: https://qwenlm.github.io/qwen-code-docs/en/users/extension/agent-plugins/

## Kimi Code
- Kimi Code Agent Skills: https://www.kimi.com/code/docs/en/kimi-code-cli/customization/skills.html
- Kimi Code plugins: https://www.kimi.com/code/docs/en/kimi-code-cli/customization/plugins.html

## ZCode / Z.AI / GLM
- ZCode Skills: https://zcode.z.ai/en/docs/skill
- ZCode Plugins: https://zcode.z.ai/en/docs/plugin
- GLM Coding Plan overview: https://docs.z.ai/devpack/overview
- GLM host integrations: https://docs.z.ai/devpack/quick-start

## DeepSeek / Deep Code
- Deep Code integration: https://api-docs.deepseek.com/quick_start/agent_integrations/deepcode
- DeepSeek Claude Code integration: https://api-docs.deepseek.com/quick_start/agent_integrations/claude_code

## Mistral
- Vibe Code Skills: https://docs.mistral.ai/vibe/code/cli/skills
- Vibe Work Skills: https://docs.mistral.ai/vibe/work/skills

## OpenCode / BrowserCode
- OpenCode Agent Skills: https://opencode.ai/docs/skills
- BrowserCode source/runtime: https://github.com/browser-use/browsercode

## MiMo / MiniMax
- MiMoCode: https://github.com/XiaomiMiMo/MiMo-Code
- MiMo Skills: https://github.com/XiaomiMiMo/MiMo-Skills
- MiniMax Skills: https://github.com/MiniMax-AI/skills

## xAI / Grok
- Grok Skills: https://x.ai/news/grok-skills
- Grok Build Skills/plugins: https://docs.x.ai/build/features/skills-plugins-marketplaces
- Grok Build source: https://github.com/xai-org/grok-build

## Serena
- Serena repository/documentation: https://github.com/oraios/serena

## Software and standards research destinations
Use the owner of the claim where possible: official project docs/source/tests/releases, GitHub/GitLab or native issue tracker, package registries, language/runtime specifications, IETF RFCs, W3C/WHATWG, vendor security advisories, OSV, GitHub Security Advisories, NVD/CVE context, CISA KEV, SBOM/provenance/signature data, and archived tags/docs for historical behavior.

## Academic / science research destinations
- arXiv: https://arxiv.org/
- PubMed: https://pubmed.ncbi.nlm.nih.gov/
- medRxiv: https://www.medrxiv.org/
- bioRxiv: https://www.biorxiv.org/
- Crossref: https://www.crossref.org/
- OpenAlex: https://openalex.org/
- CERN Open Data: https://opendata.cern.ch/

## Biomedical / clinical / drug research destinations
- ClinicalTrials.gov: https://clinicaltrials.gov/
- DailyMed: https://dailymed.nlm.nih.gov/
- WHO: https://www.who.int/
- WHO ICD: https://icd.who.int/
- ChEMBL: https://www.ebi.ac.uk/chembl/
- PubChem: https://pubchem.ncbi.nlm.nih.gov/
- DrugBank: https://go.drugbank.com/ (licensed access may apply)
- Open Targets: https://www.opentargets.org/
- NPI Registry: https://npiregistry.cms.hhs.gov/
- NIH RePORTER: https://reporter.nih.gov/
- FDA: https://www.fda.gov/
- EMA: https://www.ema.europa.eu/
- CDC: https://www.cdc.gov/

## Markets / filings / company research destinations
Use current runtime quote tools or exchange/issuer sources for current prices; record timestamp, venue and currency. For filings and official company disclosures use SEC EDGAR (including Forms 3/4/5 and XBRL), issuer investor relations, relevant exchanges, FINRA/CFTC and contract/benchmark administrators. Treat Polymarket/Kalshi as contract-bounded market beliefs, not objective truth.

- SEC EDGAR: https://www.sec.gov/edgar
- Polymarket: https://polymarket.com/
- Kalshi: https://kalshi.com/
- FRED: https://fred.stlouisfed.org/

## Government / macro / public finance destinations
- BLS: https://www.bls.gov/
- BEA: https://www.bea.gov/
- US Census: https://www.census.gov/
- USAspending: https://www.usaspending.gov/
- FiscalData / US Treasury: https://fiscaldata.treasury.gov/
- World Bank Data: https://data.worldbank.org/
- IMF Data: https://www.imf.org/en/Data
- Eurostat: https://ec.europa.eu/eurostat/
- ECB: https://data.ecb.europa.eu/
- OECD Data: https://data-explorer.oecd.org/
- UK ONS: https://www.ons.gov.uk/
- Bundesagentur fuer Arbeit: https://statistik.arbeitsagentur.de/
- Destatis: https://www.destatis.de/

## UK law / parliament / transport
- UK legislation: https://www.legislation.gov.uk/
- Find Case Law: https://caselaw.nationalarchives.gov.uk/
- UK Parliament: https://www.parliament.uk/
- Network Rail Open Data: https://datafeeds.networkrail.co.uk/
- National Rail: https://www.nationalrail.co.uk/
- ORR rail data: https://dataportal.orr.gov.uk/

## Patents / shipping
- WIPO PATENTSCOPE: https://patentscope.wipo.int/
- EPO Espacenet: https://worldwide.espacenet.com/
- USPTO: https://www.uspto.gov/patents
- Ship/AIS research: use official port/coast-guard/registry data when available; commercial AIS services may be delayed or licensed.

## Ledger rule
Before adding a new native install claim, record a current first-party source here or downgrade the adapter to PARTIAL/GENERIC. Before relying on a research database, record its role, freshness/version semantics, and any access/license limits in `core/research-source-router.md`.


## Control-plane and research-method references
- MCP 2026-07-28 specification release/migration context: https://blog.modelcontextprotocol.io/posts/2026-07-28/
- A2A latest released specification: https://a2a-protocol.org/dev/specification/
- OpenTelemetry semantic conventions (events/GenAI observability): https://opentelemetry.io/docs/specs/semconv/
- SLSA Provenance v1: https://slsa.dev/spec/v1.2/build-provenance
- Sigstore/Cosign verification: https://docs.sigstore.dev/cosign/verifying/verify/
- W3C PROV overview/data model family: https://www.w3.org/TR/prov-overview/
- W3C Data Quality Vocabulary: https://www.w3.org/TR/vocab-dqv/
- PRISMA 2020 systematic-review reporting framework: https://www.prisma-statement.org/prisma-2020
- Digital Inquiry Group / Civic Online Reasoning lateral-reading resources: https://cor.inquirygroup.org/curriculum/collections/teaching-lateral-reading/
- SIFT source-evaluation moves (Mike Caulfield): https://hapgood.us/2019/05/12/sift-and-a-check-please-preview/

These references inform vendor-neutral methodology. Re-verify current protocol/spec revisions before version-sensitive implementation guidance.


## Environment / climate / energy / geospatial
- NOAA: https://www.noaa.gov/
- NASA Earthdata: https://www.earthdata.nasa.gov/
- USGS: https://www.usgs.gov/
- US EPA: https://www.epa.gov/
- US EIA: https://www.eia.gov/
- Copernicus: https://www.copernicus.eu/
- ECMWF: https://www.ecmwf.int/
- IPCC: https://www.ipcc.ch/

## US / EU / international law and trade
- Congress.gov: https://www.congress.gov/
- GovInfo: https://www.govinfo.gov/
- Federal Register: https://www.federalregister.gov/
- eCFR: https://www.ecfr.gov/
- EUR-Lex: https://eur-lex.europa.eu/
- CURIA: https://curia.europa.eu/
- UN Treaty Collection: https://treaties.un.org/
- UN Comtrade: https://comtradeplus.un.org/
- WTO: https://www.wto.org/

## Universal engineering and MCP references
- `obra/superpowers` and OpenAI Codex plugin metadata: engineering workflow integration and current Codex/Claude support mapping.
- `oraios/serena` official README/user guide: canonical installation, host contexts, project workflow, MCP startup and marketplace warning.
- `github/github-mcp-server`: official GitHub MCP toolsets, read-only/lockdown, OAuth/scopes and forge capabilities.
- `upstash/context7`: current library/framework documentation MCP role.
- `microsoft/playwright-mcp` / Playwright docs: accessibility-snapshot browser MCP, host configuration, MCP-vs-CLI trade-off.
- `ChromeDevTools/chrome-devtools-mcp` / Chrome for Developers: network/console/performance browser diagnostics and authenticated-session risk.
- `getsentry/sentry-mcp`: production debugging MCP and licensing/auth boundaries.
- `docker/mcp-gateway` / Docker docs: MCP isolation, profiles, secrets, OAuth, discovery and tracing.
- `modelcontextprotocol/registry`: official MCP discovery registry; registry presence is not a trust/safety guarantee.

## Harness / skills / MCP / evaluation references
- OpenAI Harness Engineering: https://openai.com/index/harness-engineering/
- OpenAI Symphony: https://github.com/openai/symphony
- Hugging Face Skills: https://github.com/huggingface/skills
- Hugging Face MCP: https://huggingface.co/docs/hub/agents-mcp
- Hugging Face smolagents: https://github.com/huggingface/smolagents
- Trail of Bits Skills: https://github.com/trailofbits/skills
- Sentry Skills: https://github.com/getsentry/skills
- Vercel Agent Skills: https://github.com/vercel-labs/agent-skills
- Vercel agent-browser: https://github.com/vercel-labs/agent-browser
- mini-SWE-agent: https://github.com/SWE-agent/mini-swe-agent
- Open SWE: https://github.com/langchain-ai/open-swe
- Deep Agents: https://github.com/langchain-ai/deepagents
- Pydantic AI: https://github.com/pydantic/pydantic-ai
- Pydantic AI Harness: https://github.com/pydantic/pydantic-ai-harness
- Inspect AI: https://github.com/UKGovernmentBEIS/inspect_ai
- Inspect Evals: https://github.com/UKGovernmentBEIS/inspect_evals
- Harbor / Terminal-Bench harness: https://github.com/laude-institute/harbor
- MCP Inspector: https://github.com/modelcontextprotocol/inspector
- Snyk Agent Scan: https://github.com/snyk/agent-scan
- MCP Toolbox for Databases: https://github.com/googleapis/mcp-toolbox
- Agent Toolkit for AWS: https://github.com/aws/agent-toolkit-for-aws
- Microsoft MCP / Azure MCP: https://github.com/microsoft/mcp
- Exa MCP Server: https://github.com/exa-labs/exa-mcp-server
- Tavily MCP: https://github.com/tavily-ai/tavily-mcp
- Firecrawl MCP Server: https://github.com/mendableai/firecrawl-mcp-server
- Aider repository-map documentation/source: https://github.com/Aider-AI/aider

These are optional references/providers, not bundled dependencies. Resolve current versions, licensing, network/auth behavior and host compatibility before activation. Mutable remote skill instructions are untrusted until pinned/verified when reproducibility matters.

## Design/motion/3D sources

- `freshtechbro/claudedesignskills` — MIT design-skill repository inspected for motion, GSAP, React Spring, scroll, 3D/WebGL, Lottie/Rive and modern-web-design patterns. Used as a discovery/pattern source; no upstream skill tree is vendored.
- Motion official React documentation — current package/import, reduced-motion and bundle/lazy-loading behavior used to correct older `framer-motion` examples.
- GSAP official documentation — current ScrollTrigger and `gsap.matchMedia()` behavior used for responsive/reduced-motion guidance; deprecated helper assumptions are rejected.
- web.dev Web Vitals — current LCP/INP/CLS guidance used for frontend-performance verification; historical FID references are treated as stale for current work.

External design repositories remain discovery evidence. Library/version/API claims must be re-verified against the relevant current official documentation before implementation.

## 2026-08-23 expanded runtime-family recheck

This pass widened SKick from a fixed adapter list to a host/runtime-family router. The following sources were checked for current Skill or host behavior. A source here supports documentation/routing only; it does not claim this release was live-executed inside every product.

### Agent Skills standard and client implementation
- Agent Skills home: https://agentskills.io/home
- Agent Skills specification: https://agentskills.io/specification
- Adding Skills support to a client/harness: https://agentskills.io/client-implementation/adding-skills-support

### OpenAI / GitHub
- ChatGPT Skills upload and management: https://help.openai.com/en/articles/20001066
- ChatGPT/Codex Plugins: https://help.openai.com/en/articles/20001256
- GitHub Copilot Agent Skills: https://docs.github.com/en/copilot/concepts/agents/about-agent-skills
- Adding Agent Skills for GitHub Copilot: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills
- Copilot CLI Skill locations/reload behavior: https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference

### Qwen / MiMo / MiniMax / LongCat
- Qwen Code Agent Skills: https://qwenlm.github.io/qwen-code-docs/en/users/features/skills/
- Qwen Code Agent Plugins v1: https://qwenlm.github.io/qwen-code-docs/en/users/extension/agent-plugins/
- Xiaomi MiMoCode source and built-in Skill structure: https://github.com/XiaomiMiMo/MiMo-Code
- Xiaomi MiMo agent integration docs: https://github.com/XiaomiMiMo/awesome-mimo-agent
- MiniMax official Skills: https://github.com/MiniMax-AI/skills
- MiniMax CLI Skill: https://github.com/MiniMax-AI/cli
- LongCat-2.0 official repository: https://github.com/meituan-longcat/LongCat-2.0
- LongCat OpenCode integration: https://longcat.chat/platform/docs/OpenCode.html
- LongCat Kilo Code integration: https://longcat.chat/platform/docs/KiloCode.html

### Browser/code-agent hosts
- OpenCode Skills: https://opencode.ai/docs/skills
- BrowserCode source/runtime: https://github.com/browser-use/browsercode
- Cline Skills: https://docs.cline.bot/customization/skills
- Roo Code Skills: https://roocodeinc.github.io/Roo-Code/features/skills/
- Windsurf Skills: https://docs.windsurf.com/windsurf/cascade/skills
- TRAE: https://www.trae.ai/
- TRAE Agent Skills guidance: https://www.trae.ai/blog

### Broader ecosystem compatibility evidence
The following sources are useful for discovering additional Agent-Skill-capable hosts, but entries based mainly on ecosystem installers remain labeled `ECOSYSTEM_VERIFIED_RECHECK_FIRST_PARTY` until first-party documentation is confirmed for unattended automation:

- Auth0 CLI agent-skills installer compatibility: https://auth0.github.io/auth0-cli/auth0_agent_skills_install.html

## Evidence classification rule

When adding or updating a route:

1. use current first-party documentation/source for `VERIFIED` status;
2. use inheritance/fork evidence only with an explicit inherited/split status and runtime verification requirement;
3. label third-party/ecosystem path evidence separately;
4. route model/provider names to the actual host unless the provider itself documents a persistent Skill loader;
5. never promote “files can be copied there” to “runtime execution verified” without an actual discovery/invocation test.
## 2026-08-31 GitHub bootstrap / capability-routing recheck

Current first-party/runtime sources used to harden repository-URL installation and new adapters:

- Agent Skills standard: https://agentskills.io/
- Cursor Agent Skills, supported roots and GitHub repository import: https://prod.cursor.com/docs/skills
- GitHub Copilot Agent Skills paths and current GitHub CLI Skill management (`gh skill`): https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills and https://github.blog/changelog/2026-04-16-manage-agent-skills-with-github-cli/
- Gemini CLI Agent Skills Git/path install, workspace/user scope and reload/list: https://geminicli.com/docs/cli/skills/
- Factory Droid Skills and `.factory/skills` / compatibility roots: https://docs.factory.ai/harness/skills
- Charmbracelet Crush Agent Skills and project/global roots: https://github.com/charmbracelet/crush
- Manus portable Skills, upload and direct GitHub import: https://help.manus.im/en/articles/14753565-how-to-share-and-use-skills-in-manus
- Kimi Code Agent Skills and project/user/shared roots: https://moonshotai.github.io/kimi-code/en/customization/skills/
- Xiaomi MiMoCode built-in documentation/source for `.mimocode/skills/*/SKILL.md` and native workflows: https://github.com/XiaomiMiMo/MiMo-Code
- Serena canonical CLI/source including `start-mcp-server` and `--project-from-cwd`: https://github.com/oraios/serena

These sources establish routing/documentation behavior as observed on 2026-08-31. External product execution is still a separate runtime verification step.



## Agent-control / memory / optimization references — verified 2026-08-31
- Piebald Claude Code system-prompt corpus and changelog: https://github.com/Piebald-AI/claude-code-system-prompts
- Google Gemini CLI Auto Memory / reviewed memory+Skill inbox: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/auto-memory.md
- Google Gemini CLI Auto Memory configuration: https://github.com/google-gemini/gemini-cli/blob/main/docs/reference/configuration.md
- Qwen Code memory / auto-memory / team-memory: https://github.com/QwenLM/qwen-code/blob/main/docs/users/features/memory.md
- Karpathy autoresearch measurable experiment loop: https://github.com/karpathy/autoresearch and https://github.com/karpathy/autoresearch/blob/master/program.md
- Kimi CLI lifecycle hooks: https://github.com/MoonshotAI/kimi-cli/blob/main/docs/en/customization/hooks.md
- Kimi CLI agent/subagent customization: https://github.com/MoonshotAI/kimi-cli/blob/main/docs/en/customization/agents.md
- Cline runtime/checkpoints/worktree-oriented Kanban references: https://github.com/cline/cline and https://github.com/cline/kanban
- Smart MCP Proxy deferred tool discovery/quarantine/security: https://github.com/smart-mcp-proxy/mcpproxy-go
- Awesome MCP Servers discovery catalog: https://github.com/punkpeye/awesome-mcp-servers

## 2026-08-31 language/UI/research/security research pass

These sources were used to derive vendor-neutral mechanisms. They are evidence/reference links, not bundled dependencies or execution authorization.

### Language and framework Skills
- Android official Skills: https://github.com/android/skills and https://developer.android.com/tools/agents/android-skills/browse
  - Evidence used: official Agent Skills, targeted at fast-moving/model-knowledge-gap workflows such as AGP, Perfetto, adaptive UI, Intent security and testing.
- Android Skills design philosophy: https://developer.android.com/blog/posts/inside-android-skills-built-for-deprecation
  - Evidence used: prefer Skills where there is a verifiable knowledge gap; do not teach the model what it already handles reliably.
- Kotlin Agent Skills: https://github.com/Kotlin/kotlin-agent-skills
  - Evidence used: language/category routing and Agent Skills packaging for Kotlin/JVM workflows.
- Angular Agent Skills: https://angular.dev/ai/agent-skills and https://github.com/angular/skills
  - Evidence used: current framework/Signals/SSR/accessibility/testing guidance as a version-sensitive specialist.
- Microsoft Skills: https://github.com/microsoft/skills
  - Evidence used: language-suffixed routing across Python/.NET/TypeScript/Java/Rust, current-docs/version-first behavior, and load-only-relevant-Skills context discipline.
- .NET Skills: https://github.com/dotnet/skills
  - Evidence used: language/runtime diagnostics, LSP/tool integration and paired Skill-vs-no-Skill evaluation design.
- rewrite-rs Skills: https://github.com/rewrite-rs/skills
  - Evidence used: Rust-specific judgment, profile/unsafe/ownership reasoning and parity/differential cross-language porting concepts.

### UI, browser and design validation
- Playwright coding-agent CLI/Skills: https://playwright.dev/docs/getting-started-cli and https://playwright.dev/agent-cli/skills
  - Evidence used: token-efficient CLI/Skill route for coding agents and trace/test/browser-session workflows.
- Playwright MCP: https://playwright.dev/docs/getting-started-mcp and https://playwright.dev/mcp/capabilities
  - Evidence used: accessibility-tree browser interaction and capability-group minimization.
- Chrome DevTools: https://developer.chrome.com/blog/new-in-devtools-152
  - Evidence used: current DevTools MCP memory/performance/runtime evidence surface; recheck current MCP docs before installation.
- Google Stitch Skills: https://github.com/google-labs-code/stitch-skills
  - Evidence used: design-system/code-to-design/design-to-code workflow and portable design-contract idea.
- OpenAI/Figma Skills and Vercel/frontend specialists were previously recorded in this repository and remain optional task-matched references.

### Research and evaluation
- Microsoft Deep Wiki research workflow: https://github.com/microsoft/skills/blob/main/.github/plugins/deep-wiki/commands/research.md
  - Evidence used: explored/partially-explored/unexplored knowledge map, confidence, citations, open questions and iterative codebase research.
- Microsoft Research SkillWiki: resolve from current Microsoft Research publication/repository before implementation-dependent use.
  - Evidence used: provenance-aware reusable knowledge lifecycle concept.
- .NET Skill-vs-baseline experiment: https://github.com/dotnet/skills/blob/main/dotnet-skills.experiment.yaml
  - Evidence used: no-Skill baseline vs exact-Skill variant and repeated-run/distinct-stimulus independence.

### Security, red/blue/purple and supply chain
- Trail of Bits Skills: https://github.com/trailofbits/skills
  - Context building: https://github.com/trailofbits/skills/blob/main/plugins/audit-context-building/skills/audit-context-building/SKILL.md
  - Variant analysis: https://github.com/trailofbits/skills/blob/main/plugins/variant-analysis/skills/variant-analysis/SKILL.md
  - Differential review: https://github.com/trailofbits/skills/blob/main/plugins/differential-review/skills/differential-review/SKILL.md
  - Evidence used: context-before-verdict, root-cause calibrated variant search, risk/blast-radius differential review and specialized security tooling.
- MITRE ATT&CK adversary emulation plans: https://attack.mitre.org/resources/adversary-emulation-plans/
- MITRE/Apache CALDERA: https://github.com/mitre/caldera and https://www.mitre.org/resources/caldera-ot
  - Evidence used: authorized adversary-emulation/testing as a defensive validation harness.
- MITRE CAPEC/ATT&CK role comparison: https://capec.mitre.org/about/attack_comparison.html
- MITRE D3FEND: https://d3fend.mitre.org/
- Sigma specification: https://sigmahq.io/sigma-specification/ and https://github.com/SigmaHQ/sigma-specification
  - Evidence used: portable detection-as-code and explicit false-positive/reference/status metadata.
- CISA Known Exploited Vulnerabilities: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- FIRST EPSS: https://www.first.org/epss/
  - Evidence used: exploitation-aware vulnerability prioritization beyond static severity.
- OWASP GenAI AI/Agentic Red Teaming: https://genai.owasp.org/resource/ai-security-solutions-landscape-for-ai-and-agentic-red-teaming-q2-2026/ and https://genai.owasp.org/resource/solutions-landscape-red-teaming-taxonomy/
  - Evidence used: lifecycle-wide AI/agent red-blue-purple capability taxonomy.
- skills-lock: https://github.com/luisalima/skills-lock
  - Evidence used: exact commit pinning, content-tree hashes, frozen CI and safe path/transport handling for reproducible external Skill dependencies.

### Engineering workflow reference
- Matt Pocock Skills: https://github.com/mattpocock/skills
  - Evidence used: durable domain language, decision-frontier questioning, deep-module architecture, bounded design alternatives, tracer-bullet slicing, expand/migrate/contract migrations, prototypes as question-answering instruments, intent-aware merges and human-only procedure handoff.
  - Decision: absorb/reimplement mechanisms; do not copy runtime-specific orchestration assumptions wholesale.
- OpenAI Figma plugin/skills: https://github.com/openai/plugins/tree/main/plugins/figma and https://github.com/openai/skills/tree/main/skills/.curated/figma
  - Evidence used: full plugin payload beyond SKILL.md, prerequisite/deferred-tool loading, design-system variables/components and design-to-code rendered fidelity workflows. Figma Developer Terms/per-skill terms apply.
- Google Labs Stitch Skills: https://github.com/google-labs-code/stitch-skills
  - Evidence used: code-to-design -> static HTML + design-system extraction -> upload, and semantic `DESIGN.md` as a reusable design contract. Repository notes it is not an officially supported Google product.
- Semantic Skill supply-chain research: https://arxiv.org/abs/2605.11418
  - Evidence used: Skill metadata/description is operational routing text and can manipulate discovery/selection/governance; therefore description/rank is not a trust signal. Treat numeric results as research findings for that study, not universal rates.
- SkillGuard reference: https://github.com/RudrenduPaul/skillguard
  - Evidence used: scan the whole Skill/hooks/scripts set, compare declared vs actual scope, and evaluate cross-Skill privilege chaining. Early/pre-1.0 scanner; use as an optional second opinion, not a trust root.

## 2026-09-03 final v1.0 portability / Skill ecosystem / design-reference audit

Current first-party/runtime references used for final v1.0 hardening include:
- OpenAI Skills in ChatGPT: https://help.openai.com/en/articles/20001066
- OpenAI Codex plans/Skills: https://help.openai.com/en/articles/11369540-codex-and-chatgpt-plan-usage-limits and https://developers.openai.com/codex/skills/
- Anthropic custom Skills: https://support.claude.com/en/articles/12512198-how-to-create-custom-skills
- Gemini Apps Skills: https://support.google.com/gemini/answer/17094296?hl=en
- GitHub Copilot / `gh skill`: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills
- Devin Skills: https://docs.devin.ai/product-guides/skills
- Qoder Skills: https://docs.qoder.com/extensions/skills
- Kiro Skills: https://kiro.dev/docs/skills/
- Zed Skills: https://zed.dev/docs/ai/skills
- Zencoder Skills: https://docs.zencoder.ai/features/skills
- Warp Skills: https://docs.warp.dev/knowledge-and-collaboration/warp-drive/ai-objects
- Replit Agent Skills: https://docs.replit.com/build/use-agent-skills

Skill/design ecosystems were used as reference material only unless separately cataloged for invocation. No third-party design assets or proprietary page layouts were copied into SKick.

### Additional host verification refreshed 2026-09-03
- Goose Agent Skills: https://goose-docs.ai/docs/guides/context-engineering/using-skills/
  - Evidence used: `.agents/skills/` is the recommended project/global standard, with native listing/loading and legacy compatibility roots.
- iFlow CLI Skills: https://platform.iflow.cn/en/cli/examples/skill
  - Evidence used: documented `.iflow/skills/` project/personal structure, `SKILL.md` contract and `/skills refresh` testing flow.
- Mux product Skill source: https://github.com/coder/mux/blob/main/.mux/skills/tbench/SKILL.md and https://github.com/coder/mux/blob/main/docs/hooks/tools.mdx
  - Evidence used: product-source `.mux/skills` usage and Agent Skill list/read/write tooling; active release still requires runtime verification.
