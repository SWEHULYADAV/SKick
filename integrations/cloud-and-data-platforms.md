# Cloud and Data Platform Integrations

## Database MCP Toolbox
Use Google's MCP Toolbox for Databases when structured database access materially improves the task. Prefer read-only schema/metadata/query tools for research and tightly parameterized tools over unrestricted SQL for production workflows. Keep credentials outside generated examples and gate writes/DDL through action transactions.

## AWS Agent Toolkit
Prefer the current official AWS Agent Toolkit/skills/MCP route over stale generic AWS MCP examples. Use agent-specific IAM identity/condition keys, least privilege and CloudTrail/CloudWatch audit where available. Resolve current tool names; do not hard-code deprecated API-tool identifiers.

## Azure MCP / Skills
Use the current stable Azure MCP Server/skills when Azure is the target. Prefer GA/stable versions by default, Entra ID/RBAC, read-only discovery and scoped operations; use beta only when the user/task explicitly needs it.

## Provider rule
Cloud/database MCPs are project-conditional, never universal defaults. Native CLIs/SDKs may be better when already authenticated and auditable. Destructive/provisioning/database writes require explicit scope, dry-run/plan where possible, postconditions and rollback/compensation.
