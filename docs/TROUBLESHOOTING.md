# SKick Troubleshooting

## Skill does not appear

Check in this order:

1. Confirm the current runtime actually supports Agent Skills.
2. Confirm the directory/archive shape expected by that runtime.
3. Confirm the Skill folder is named `skick`.
4. Confirm `SKILL.md` is at the required root and contains valid frontmatter.
5. Confirm the runtime/extension was reloaded if required.
6. Confirm workspace/admin policy allows Skills or local plugins.
7. Check runtime logs or its current Skill listing command.

## Skill is installed but never triggers

- Make sure the task matches the `description` in `SKILL.md`.
- Try an explicit instruction: `Use the SKick skill for this task.`
- Check whether the runtime disables implicit Skill invocation.
- Check for duplicate `skick` Skills in higher-priority locations.
- Check whether another plugin/agent is overriding the workflow.

## Relative files are missing

Do not upload/copy only `SKILL.md` when the runtime expects the full package. SKick relies on progressive references to `core/`, `integrations/`, `extensions/`, `mcp/`, and other resources.

## ChatGPT upload is unavailable

Skill upload can depend on plan, workspace, role, supported surface, region and admin settings. In a managed workspace, ask an admin to confirm Skill creation/upload/install permissions. Do not attempt to work around organization policy.

## VS Code/Copilot cannot see the Skill

- Update to a current supported VS Code/Copilot release.
- Verify Agent Skills support for the installed version.
- Prefer `.github/skills/skick/` or `.agents/skills/skick/` as documented by GitHub for the relevant surface.
- Reload the window/agent and test with a clear trigger.

## Claude Code cannot see the Skill

Verify `.claude/skills/skick/SKILL.md` or the current plugin wrapper layout, then restart/reload Claude Code. Do not use Claude web Skill packaging for Claude Code unless current docs explicitly say it is compatible.

## Gemini/OpenCode/Codex path mismatch

Use the adapter for the actual runtime. Shared `.agents/skills/` is useful only when the installed host documents support for it.

## MCP fails

Treat MCP failure separately from SKick failure.

- Confirm the server binary/package exists.
- Confirm command/arguments are from the canonical upstream.
- Confirm required environment variables are present without printing secrets.
- Confirm transport support for the installed client version.
- Confirm the server is enabled and visible in the runtime's MCP status/list command.
- Test one server at a time.

Do not execute a random stdio command just to inspect it.

## SKick creates too much structure

The preferred Python/vanilla profile is intentionally minimal. Remind the agent that only placement is invariant: tiny `app.py` root launcher, backend implementation in `backend/`, frontend implementation/assets in `frontend/`, deeper folders only when justified.

## SKick chooses a framework without need

Existing project requirements override defaults, but a greenfield project should not jump to React/Next/Vite or a Node backend just because the host often generates them. Ask the agent to show the requirement that justifies framework escalation.

## Runtime says installation succeeded but behavior differs

Record the runtime/model/extension version, Skill location, whether implicit invocation is enabled, tool/MCP availability, and the exact test prompt. Structural packaging success is not proof of behavioral equivalence across runtimes.


## AI received the ZIP but does not know where to install it

1. Read `../START_HERE.md`.
2. Read `../INSTALLATION_MANIFEST.json`.
3. Identify the actual host runtime and surface from environment evidence.
4. If the model/provider is running inside another host, use the host adapter.
5. If the runtime remains ambiguous, ask only for the missing runtime/surface name; do not invent a path.
6. If no native contract is verified, use `../adapters/generic/PROMPT.md`.

## Existing SKick install blocks replacement

This is intentional. Inspect the existing `VERSION`, local modifications, and source-control state. Preserve fork changes or back them up. Replace the complete Skill only when replacement is intended; do not merge random files from two releases. The helper script requires `--force` for replacement.

## Skill exists on disk but not inside the IDE/app

Verify the active runtime process is reading that filesystem and scope. Remote SSH/WSL/container agents may not see local home-directory Skills. Reload/refresh/restart using the runtime's documented mechanism and check Skill permissions/enable switches.

## Codex Windows Desktop does not discover repository-local Skills

Codex documents repository Skills under `.agents/skills/`, but runtime discovery must still be verified in the active product build. As of 2026-08-31, openai/codex issue #40458 reports a Windows Desktop build where repository-local Skills were not exposed even though user/system/plugin Skills loaded.

If this happens:

1. confirm the workspace/CWD and git root are the expected repository;
2. confirm `.agents/skills/skick/SKILL.md` is complete and valid;
3. restart/reload and check the native available-Skills view;
4. re-check the current Codex issue/release notes before assuming the documented repo root is broken generally;
5. if appropriate for the user's scope, test a user-level `~/.agents/skills/skick/` install or the Codex plugin distribution instead;
6. report the workaround and do not call project-scope installation successful if the active runtime never discovered it.

Reference: https://github.com/openai/codex/issues/40458
