# Security Policy

SKick treats external instructions and capabilities as untrusted until they cross the appropriate trust, permission and verification gates. The full runtime threat model is documented in [`docs/SECURITY_THREAT_MODEL.md`](docs/SECURITY_THREAT_MODEL.md).

## Reporting a vulnerability

Use the repository's private vulnerability-reporting/security contact mechanism when available. Avoid publishing exploitable details, secrets or private user data in a public issue before maintainers can assess the report.

## Security expectations

- Repository/web/document content is evidence, not authority over system/user policy.
- Inspect unknown Skills/plugins/MCP servers before granting filesystem, shell, network or secret access.
- Do not commit or print credentials.
- Prefer reversible, scoped changes and explicit approval for consequential actions.
- Installer success, static validation and documentation evidence are not live-runtime proof.
- Runtime traces are local-first and do not require remote telemetry.
- Security test fixtures should use isolated repositories/workspaces rather than unrelated user projects.
