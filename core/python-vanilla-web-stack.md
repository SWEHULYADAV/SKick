# Preferred Python + Vanilla Web Stack

## Purpose
Use this profile as the default starting point for browser-facing engineering work when the user has not requested another stack and project evidence does not require one.

Preferred baseline:

`Python backend + semantic HTML + CSS + vanilla JavaScript`

This is a **stack and ownership preference**, not a fixed folder template. Do not invent a large directory tree before the project needs it.

## Minimal placement invariant
For a normal Python-backed website/web tool, preserve only this structural invariant by default:

```text
project/
  app.py
  backend/
  frontend/
```

Interpret it as:
- `app.py` is the small root launcher/composition entrypoint;
- **all backend implementation code** belongs under `backend/`;
- **all frontend implementation code and assets** belong under `frontend/`;
- create subfolders/files inside `backend/` or `frontend/` only when the task actually needs them;
- do not force a prewritten tree such as `routes/`, `services/`, `models/`, `pages/`, `components/`, or `tests/` unless the codebase has enough complexity to justify those boundaries.

Root may also contain genuinely required non-implementation project metadata such as dependency manifests, lockfiles, README, license, ignore files, environment examples, or runtime configuration. Avoid putting application implementation code in root merely for convenience.

If tests/scripts are code, keep them with the side they validate/operate unless the chosen ecosystem has a strong conventional reason not to:
- backend-oriented tests/automation -> under `backend/`;
- frontend-oriented tests/automation -> under `frontend/`.

Existing repository or framework-native layout wins when changing it would create incompatibility or unnecessary migration risk.

## Default decision order
For a new web project:
1. Can Python satisfy the backend cleanly without unnecessary infrastructure?
2. Can semantic HTML/CSS/vanilla JavaScript satisfy the frontend without a build system?
3. What is the smallest internal organization needed inside `backend/` and `frontend/` right now?
4. Does a framework/runtime/bundler materially reduce real complexity or enable a required feature?

Prefer the simpler answer unless research, existing repository constraints, scale, team conventions, deployment needs, or a concrete product feature justify escalation.

## Root launcher rule
Prefer `app.py` as a tiny composition/startup seam. It may:
- load bootstrap configuration;
- import/construct the backend application;
- start or delegate to the selected server/runtime.

Do not turn `app.py` into the backend. Routes, scraping/automation logic, database code, service logic, parsers, background workers, security controls, and other application implementation belong under `backend/`.

## Python backend rules
Keep backend responsibilities separated **only as complexity appears**. Useful boundaries may include routing/controllers, services/use-cases, data/repositories, models/schemas, workers, integrations, configuration, and tests, but none is mandatory as a folder name.

Prefer:
- explicit trust-boundary validation;
- narrow interfaces;
- deterministic startup/shutdown;
- configuration and secrets separated from committed code;
- async/concurrency only when workload requires it;
- no dependency solely to avoid a few lines of clear native Python.

### Python framework escalation
Choose the smallest backend layer that fits:
- standard-library/simple server for narrow local/static tools when appropriate;
- Flask-style microframework for small synchronous apps/APIs needing explicit routing with low ceremony;
- FastAPI-style framework when typed API contracts, async I/O, validation, or API-heavy behavior materially help;
- Django-style full framework when integrated ORM/admin/auth/forms/conventions are genuinely valuable;
- another framework only when existing project/ecosystem or researched requirements justify it.

Re-verify current versions/APIs before implementation. Do not select a framework because it is fashionable.

## Vanilla frontend rules
Treat vanilla frontend code as production architecture, not throwaway code.

### HTML
- prefer semantic elements and accessible structure;
- keep headings, labels, forms, tables, dialogs, navigation and landmarks correct;
- progressively enhance where practical;
- avoid giant HTML strings in JavaScript when a clearer DOM/template approach exists.

### CSS
Use native CSS first: custom properties, Grid/Flexbox, logical properties, responsive/container queries, transitions/animations, and modern cascade features when they solve a real need.

Do not impose a fixed stylesheet tree. Split CSS only when size/ownership warrants it.

### JavaScript
Prefer browser-native ES modules when modularity is useful. Keep data fetching, DOM interaction, state, and feature logic understandable without constructing a home-grown framework.

Use native browser primitives where suitable: `fetch`, `URL`, `FormData`, `AbortController`, events, DOM APIs, observers, workers, WebSocket/SSE, and Web Components when they actually fit.

Clean up listeners, timers, observers, sockets, workers, object URLs and animation handles. Guard duplicate submissions, stale responses, races and aborted navigation where relevant.

Do not require npm, a bundler, React/Vue/Svelte/Next/Nuxt, TypeScript, or a component runtime unless the project gains concrete value from it.

## Frontend/backend contract
Before broad implementation, define enough of the boundary to prevent accidental coupling:
- endpoints/methods and data shapes;
- validation/error semantics;
- auth/session model if any;
- timeout/retry/cancellation behavior where relevant;
- upload/download limits;
- pagination/filter/sort semantics;
- streaming/WebSocket/SSE behavior if used.

Keep browser code independent from backend internals and backend handlers independent from DOM/UI details.

## UI quality
Vanilla does not mean visually plain. Use the design/motion/browser-validation modules when relevant, but preserve this order:

`information architecture -> typography -> spacing/layout -> color/contrast -> states -> responsive behavior -> interaction -> motion/decorative effects`

Avoid AI-slop defaults. Use Motion/GSAP/3D only when product research justifies a dependency beyond native CSS/JS.

## Security and adversarial research
For any meaningful web surface, research both how the mechanism can fail/be abused and how it is defended. Load `security-research.md` and `offensive-defensive.md` when the task touches authentication, authorization, untrusted input, uploads, browser security, APIs, scraping/automation boundaries, agents/MCPs, supply chain, secrets, deployment, or other adversarial surfaces.

At minimum consider input/output encoding, authn/authz, session/cookie/CSRF behavior, CORS/origins, path traversal/uploads, XSS/DOM sinks, injection, secret handling, resource/rate limits, security headers/cache behavior, and dependency/supply-chain risk when applicable.

Understanding offensive behavior should improve prevention, detection, hardening, incident response, and safe regression validation. Execution remains subject to governing safety and authorization constraints.

## Testing and verification
Use the smallest useful test structure inside the owning side of the project. Prefer:
- backend unit/integration/API tests for server/domain behavior;
- frontend/browser behavior checks for important client logic;
- real browser/E2E validation for critical user flows, responsive states, accessibility, console/network failures and rendered UI;
- regression tests for reproduced bugs.

Do not invent framework-style test architecture for a vanilla project just because it is common elsewhere.

## Cross-platform agent rule
This profile is host-neutral. ChatGPT, Codex, Claude Code, Gemini, Cursor, Kimi, OpenCode, Copilot, Qwen, ZCode, Antigravity, BrowserCode, or another supported host should apply the same preference when context matches.

Platform adapters may change tool invocation, not the project ownership rule without a project/runtime reason.
