# Bundled MCP Integration Catalog

This directory makes MCP support first-class without bundling or silently installing third-party server binaries.

`catalog.json` is a machine-readable routing/trust catalog. It records provider roles, profiles, write/external-data risk and validators. An already-connected provider may be used when it is the narrowest strong capability for the task; installation/authentication remains explicit.

## Important profiles
- `core-code` — Serena + Context7 as needed.
- `forge` — official GitHub MCP.
- `browser-fast` — agent-browser core profile for exploratory/high-throughput automation.
- `browser-e2e` — Playwright MCP.
- `browser-diagnostics` — Chrome DevTools MCP.
- `ai-ml` — official Hugging Face MCP/skills ecosystem.
- `database` — Google MCP Toolbox for Databases.
- `cloud-aws` / `cloud-azure` — official cloud provider stacks.
- `prod-debug` — Sentry only when used by the project.
- `research-web` — one of Exa/Tavily/Firecrawl, native web first.
- `engineering` — compact general coding/browser profile.

## Safety qualification
Before trusting an unfamiliar provider, follow `core/mcp-validation-and-security.md`. MCP Inspector is the preferred protocol/capability qualification tool; unknown stdio commands must be reviewed and isolated before launch. `scripts/scan_skill_package.py` is a no-execution local preflight for downloaded skill/plugin packages. Optional Snyk Agent Scan is a second signal, not a safety oracle.

## Config generation
`scripts/generate_mcp_config.py --list-profiles` shows locally renderable profiles. The generator produces examples only; it does not install, authenticate or mutate host config. Persistent configs should resolve/pin current package versions rather than treating `@latest` examples as reproducible.

Generate examples on demand with `scripts/generate_mcp_config.py`; do not commit generated host configs. Verify the active host's current MCP status/listing before relying on them.
