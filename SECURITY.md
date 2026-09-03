# Security Policy

SKick is an instruction package that may be used inside agents with filesystem, terminal, browser, network, MCP, or account-connected tools. Treat Skills as part of the AI software supply chain.

## Reporting a vulnerability

Please open a GitHub Security Advisory for `SWEHULYADAV/SKick` when the repository is public. Do not post secrets, working credentials, private exploit data, or sensitive customer information in public issues.

## Security expectations

- SKick must not contain credentials, tokens, cookies, private keys, or live secrets.
- Downloaded Skills, plugins, MCP servers, scripts, and external repositories are untrusted until reviewed.
- Installation does not grant tool permissions; the host runtime remains responsible for permission boundaries.
- Unknown MCP/stdio commands must not be executed merely to discover their behavior.
- Security research must preserve authorization, safety, and applicable platform policies.
- Structural validation is not evidence that every external runtime is safe or compatible.

See `docs/WARNINGS.md` and `core/untrusted-content-boundary.md` for operational guidance.
