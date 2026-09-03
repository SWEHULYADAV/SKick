# Generic Runtime Adapter — FALLBACK

Use this only when no verified native Skill/plugin installation contract exists for the actual host runtime.

## Direct ZIP behavior

If an AI receives the SKick ZIP on an unknown/model-only surface, it must **not invent** a filesystem path, marketplace, manifest, extension, or upload flow. First determine whether the model is running inside a known host such as Cursor, Claude Code, Codex, OpenCode, GitHub Copilot, Gemini CLI, Qwen Code, Kimi Code, ZCode, or Mistral Vibe. If so, use that host adapter.

If no native host can be identified, load `PROMPT.md` as the portable instruction fallback. Persistent installation is not claimed in this mode.

## Verification

Confirm the host accepted the instructions for the current session/context. Do not claim a persistent Skill install unless the product exposes and verifies one.

## Warnings

Read `../../START_HERE.md` and `../../docs/WARNINGS.md`. Do not silently execute scripts or install integrations.
