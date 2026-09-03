# MCP Capability Stack

## Purpose
Use MCP as a portable capability layer for engineering tasks without turning every server into a permanent dependency, executing unknown configs, or flooding context with overlapping tools.

## Selection rule
`host-native capability -> installed narrow specialist -> qualified task-matched MCP -> simpler fallback`.

Before activation, resolve current upstream/version, license, transport, permissions, secrets, network/file access, telemetry/external data handling, write surface and overlap. For unfamiliar servers load `mcp-validation-and-security.md`.

## Core engineering providers
- **Serena** — preferred semantic repository navigation, symbols/references and targeted edits.
- **Context7** — changing library/framework/SDK documentation; not project-business-logic authority.
- **GitHub MCP Server** — forge, PR/issues/CI/security metadata when GitHub is the real forge; research read-only/least-scope by default.
- **agent-browser** — fast exploratory browser automation/QA with a small default MCP profile when installed.
- **Playwright MCP** — deterministic/stateful user-flow and e2e automation.
- **Chrome DevTools MCP** — console/network/source-map/performance diagnosis.
- **Hugging Face MCP** — AI/ML Hub models, datasets, papers, Jobs and community tool discovery when that ecosystem is relevant.
- **Sentry MCP** — production issues/traces only when the project already uses Sentry.
- **Docker MCP Gateway** — optional multi-server isolation/governance when Docker is acceptable.

## Project-conditional platform providers
- **MCP Toolbox for Databases** — database schema/query/tooling; prefer read-only discovery and restricted structured production tools.
- **Agent Toolkit for AWS** — AWS docs/API/skills/operations with agent-specific IAM/audit controls.
- **Azure MCP Server/skills** — Azure resources/operations with Entra/RBAC and stable-GA preference.

Never auto-enable production database/cloud write surfaces merely because credentials are available.

## Optional research providers
Native trustworthy web search/read remains first choice. If the task needs a specialized provider, activate **one of** Exa, Tavily or Firecrawl based on need. Use `integrations/research-providers.md`; do not enable all three by default.

## Qualification and scanners
Unknown/new MCPs follow:
`static/config inspection -> isolated MCP Inspector handshake/schema snapshot -> synthetic read-only probe -> least-privilege activation`.

The bundled static scanner does not execute anything. Snyk Agent Scan is an optional second opinion and may execute configured stdio servers; its use therefore requires sandbox/consent and external-data review.

## Profiles
Canonical profile metadata lives in `mcp/catalog.json`:
`core-code`, `forge`, `browser-fast`, `browser-e2e`, `browser-diagnostics`, `ai-ml`, `database`, `cloud-aws`, `cloud-azure`, `prod-debug`, `gateway`, `research-web`, `engineering`.

Load one overlapping provider per capability unless a second provider has a distinct independent purpose. `scripts/generate_mcp_config.py` emits only local profiles whose stdio shape is stable enough to provide as an example; it never installs packages or writes credentials.
