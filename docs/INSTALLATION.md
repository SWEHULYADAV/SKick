# SKick Installation and Setup

This guide explains **what to install, where, when, why, how to verify it, how to update it, and what not to assume**.

## 1. First determine the host

Before copying files or uploading an archive, identify the runtime that actually loads instructions/Skills.

Examples:

- `Qwen model in OpenCode` -> install for **OpenCode**.
- `MiniMax model in Claude Code` -> install for **Claude Code**.
- `LongCat model in Kilo Code` -> install for **Kilo Code**.
- `MiMoCode` -> install for **MiMoCode** because it is itself a coding host.
- `ByteDance/Seed model in TRAE` -> install for **TRAE**.
- `DeepSeek model in Cursor` -> install for **Cursor**.

Do not infer an installation contract from the model name.

## 2. GitHub URL bootstrap

Publish the canonical SKick repository root and give the target AI the URL plus the short prompt in `../BOOTSTRAP_PROMPTS.md`. The target AI must read `GITHUB_BOOTSTRAP.md`, detect the real host/runtime, then follow `../INSTALLATION_MANIFEST.json` and the matching adapter.

GitHub-capable coding agents may use a documented native remote-Skill command or may fetch/clone the repository and run the conservative local installer. Managed AI apps may require the generated archive through their native upload/import UI. Do not pretend a GitHub URL can bypass product permissions.

Installing SKick does not authorize installing a semantic repository provider or any other executable dependency. Discover existing capabilities first; configure an optional provider only when the task needs it and the user/host authorization permits it.

## 3. Direct ZIP installation protocol

If an AI receives SKick as a ZIP with only “install this”:

1. inspect the archive without executing bundled code;
2. read `START_HERE.md`;
3. read `INSTALLATION_MANIFEST.json`;
4. read `docs/RUNTIME_COMPATIBILITY.md`;
5. identify the current host/surface from environment evidence;
6. read the exact host adapter under `adapters/`;
7. choose project scope by default for coding repositories unless the user requested personal/global scope;
8. inspect any existing `skick` installation before replacement;
9. install only SKick—optional MCPs/plugins/tooling are separate;
10. reload/refresh only if the host requires it;
11. verify the host can actually discover and invoke SKick;
12. report the path/UI flow, version, verification performed, and any step that could not be completed.

If the host cannot be safely identified, ask only for the missing runtime/surface instead of guessing.

## 4. Scope

### Project/repository scope

Recommended default for coding agents because it is reviewable, versioned with the project, reproducible for teammates, and easy to roll back.

### User/personal scope

Use when the user wants SKick across many projects and the runtime documents a personal Skill root. Inspect duplicate-name precedence before creating more than one `skick` install.

### Managed account/workspace scope

Use the product's native Skills/admin UI. An AI must not claim it changed an account or workspace unless it actually has the authorized action.

## 5. Filesystem installer

List targets:

```bash
python3 scripts/install_skick.py --list-targets
```

Inspect likely runtime markers without installing:

```bash
python3 scripts/detect_runtime.py --project /path/to/repo
```

Dry-run first:

```bash
python3 scripts/install_skick.py \
  --target github-copilot \
  --scope project \
  --project /path/to/repo \
  --dry-run
```

Examples:

```bash
python3 scripts/install_skick.py --target claude-code --scope project --project /path/to/repo
python3 scripts/install_skick.py --target browsercode --scope project --project /path/to/repo
python3 scripts/install_skick.py --target qwen --scope user
python3 scripts/install_skick.py --target kimi --scope project --project /path/to/repo
python3 scripts/install_skick.py --target mimo --scope project --project /path/to/repo
python3 scripts/install_skick.py --target opencode --scope project --project /path/to/repo
python3 scripts/install_skick.py --target factory-droid --scope project --project /path/to/repo
python3 scripts/install_skick.py --target crush --scope project --project /path/to/repo
python3 scripts/install_skick.py --target agents --scope project --project /path/to/repo
```

The installer refuses blind overwrites unless `--force` is explicitly supplied. A successful copy is **filesystem installation only** until runtime discovery is verified.

## 6. Common verified host roots

| Runtime | Project/local | User/personal |
|---|---|---|
| GitHub Copilot | `.github/skills/skick/`, `.agents/skills/skick/`, `.claude/skills/skick/` | `~/.copilot/skills/skick/`, `~/.agents/skills/skick/` |
| Claude Code | `.claude/skills/skick/` | `~/.claude/skills/skick/` |
| Cursor | `.cursor/skills/skick/`, `.agents/skills/skick/`, compatible Claude/Codex roots | `~/.cursor/skills/skick/`, `~/.agents/skills/skick/`, compatible Claude/Codex roots |
| OpenCode | `.opencode/skills/skick/`, `.agents/skills/skick/` | `~/.config/opencode/skills/skick/`, `~/.agents/skills/skick/` |
| BrowserCode | OpenCode-compatible `.opencode/skills/skick/` and supported shared roots | OpenCode-compatible user roots; verify current build |
| Qwen Code | `.qwen/skills/skick/` | `~/.qwen/skills/skick/` |
| Kimi Code | `.kimi-code/skills/skick/`, supported shared root | documented Kimi home/shared root |
| MiMoCode | `.mimocode/skills/skick/` | use only a currently documented user root; do not invent one |
| Cline | `.cline/skills/skick/` | `~/.cline/skills/skick/` |
| Roo Code | `.roo/skills/skick/`, `.agents/skills/skick/` | `~/.roo/skills/skick/`, `~/.agents/skills/skick/` |
| Windsurf | `.windsurf/skills/skick/` | `~/.codeium/windsurf/skills/skick/` |
| TRAE | `.trae/skills/skick/` | `~/.trae/skills/skick/` or product/region-specific documented root |
| Gemini CLI | `.gemini/skills/skick/`, `.agents/skills/skick/` | `~/.gemini/skills/skick/`, `~/.agents/skills/skick/` |
| Factory Droid | `.factory/skills/skick/`, `.agents/skills/skick/`, `.agent/skills/skick/` | `~/.factory/skills/skick/`, compatible shared roots |
| Crush | `.crush/skills/skick/`, `.agents/skills/skick/`, compatible roots | `~/.config/crush/skills/skick/`, compatible shared roots |
| Codex | `.agents/skills/skick/` | `~/.agents/skills/skick/` |

This table is a convenience summary. `INSTALLATION_MANIFEST.json` plus the exact adapter is authoritative for SKick routing.

## 7. Managed products

### ChatGPT

Use the canonical `skill.zip` release artifact on an eligible surface:

1. sidebar -> **Plugins**;
2. **Skills** tab;
3. **Create**;
4. **Upload from your computer**;
5. select `skill.zip`;
6. review the scan result;
7. verify SKick appears as installed/enabled;
8. run a low-risk trigger test.

Personal Skills may need separate installation on desktop and web/mobile; availability can depend on plan, role, workspace policy, region, and surface.

### Claude web/app

Use the generated Claude managed-Skill archive, not Claude Code filesystem/plugin instructions.

### Gemini Apps

Use the generated Gemini Apps archive. That archive is intentionally **text-only**; repository PNG branding is not placed into the Gemini Apps upload package.

Manus supports a managed upload and direct public GitHub import flow; use `adapters/manus/README.md`. Other managed products must use their native current UI if one exists. Do not fabricate an upload/import feature.

## 8. Provider/model-only products

MiniMax, LongCat, DeepSeek, GLM, ByteDance/Seed/Doubao, Llama, Nova, Cohere, Granite, ERNIE, Hunyuan, and similar providers do not automatically get a filesystem Skill path merely because they support tools or coding.

Route to:

1. the actual host agent;
2. a verified native provider Skill system if one exists;
3. the generic session fallback if there is no persistent Skill contract.

## 9. Browser agents and BrowserCode

Browser capability and Skill discovery are separate.

For BrowserCode, use its OpenCode-compatible Skill roots and then verify inside the active BrowserCode build. When web-app validation is needed, SKick can combine its normal engineering workflow with the host browser/CDP capability and `core/webapp-validation.md`.

For an unknown browser coding agent, inspect whether it implements Agent Skills or exposes persistent project instructions with resource access. If neither is verified, do not invent an install location.

## 10. VS Code and IDEs

Install for the runtime powering the extension, not for the editor brand alone. GitHub Copilot, Cline, Roo Code, Windsurf, Claude Code, Cursor, Codex, Qwen Code, Gemini CLI, OpenCode, MiMoCode, and other agents can coexist in the same editor but use different discovery roots.

See `VS_CODE_AND_IDES.md`.

## 11. Update

Before replacing an existing SKick install:

1. inspect `VERSION`;
2. check whether the installed copy is a fork or has local edits;
3. commit/back up intentional changes;
4. replace the complete Skill directory from canonical source/release;
5. reload/refresh if required;
6. verify discovery and a low-risk task.

Never merge random files from two release archives.

## 12. Uninstall

For filesystem installations, remove only the installed `skick` Skill directory from the selected root, then refresh the runtime. For managed products, use the product's Skills/plugin management UI. Do not manipulate hidden browser/account state as a substitute for the official flow.

## 13. Remote / SSH / WSL / containers / Codespaces

Install where the **agent process actually reads files**. A Skill in the laptop home directory may not exist inside a remote container or SSH host. Project-local Skills committed to the repository are often the most reproducible option.

Never sync secrets with the Skill.

## 14. Optional integrations

SKick can route to optional MCPs, browser tools, semantic repository tools, cloud CLIs, databases, or specialist Skills when available. They are **not** silently installed as dependencies. Provider setup requires a separate capability-fit and authorization decision.

Before enabling one:

1. confirm it materially helps;
2. read current first-party docs;
3. review filesystem/network/credential/execution behavior;
4. use least privilege;
5. test it independently;
6. preserve version/provenance when reproducibility matters.

## 15. Verification checklist

Installation is complete only when relevant checks pass:

- correct host identified;
- correct scope/path or managed upload used;
- complete SKick package preserved;
- runtime lists/discovers `skick`;
- implicit or explicit invocation works as expected;
- relative references can be loaded;
- optional tools are verified separately;
- report distinguishes copy/upload success from live invocation success.

## 16. Future/custom runtimes

Use `RUNTIME_COMPATIBILITY.md` and `NEW_RUNTIME_INTEGRATION.md`. Preferred ladder:

native Agent Skills -> documented shared `.agents/skills` -> verified runtime instructions -> persistent instruction bridge -> session prompt -> custom harness implementation.

Do not make a new adapter “VERIFIED” until its discovery, activation, resource loading, precedence, update, and removal behavior are grounded in current evidence and tested as far as the release environment allows.


### Factory Droid / Crush / Manus

- Factory Droid: prefer the verified `.factory/skills/skick/` project route or a currently documented compatible shared Agent Skill root.
- Crush: prefer the verified `.crush/skills/skick/` or documented shared project Skill root.
- Manus: use the managed Skill import/share/upload flow; no filesystem path is asserted.

Always verify discovery in the active surface after installation.
