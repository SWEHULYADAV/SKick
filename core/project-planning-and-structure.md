# Research-First Project Planning and Structure

## Purpose
For a new project or major redesign, research and understand the problem before creating production code. Convert evidence into a simple architecture and file plan, then implement in small verified slices.

## Mandatory sequence for substantial builds

`research/context -> requirements -> constraints -> user/workflow model -> architecture -> UI/UX direction -> data/control flow -> filesystem plan -> risk/test plan -> acceptance criteria -> implementation`

Do not start broad production implementation while the architecture, platform constraints, or core user flow are still guesses.

For a tiny one-file utility, the planning artifact may be lightweight, but still inspect the environment and define success before editing.

## Preferred website profile
For websites, dashboards, monitoring panels, local web tools, admin utilities, and similar browser-facing products without a stronger existing-project constraint, load `python-vanilla-web-stack.md` and prefer:

`Python backend + semantic HTML + CSS + vanilla JavaScript`

Use a real `backend/` and `frontend/` boundary. Keep root implementation to a tiny launcher such as `app.py`; place backend implementation under `backend/` and frontend implementation/assets under `frontend/`. Create deeper structure only when the task needs it. Do not select React/Next/Vue/Svelte or a large Python framework merely because it is common; escalate only when researched requirements, existing code, team conventions, or product complexity justify the added runtime/build/tooling surface.

## Project blueprint
Before coding, establish the relevant fields:
- problem and intended users/operators;
- explicit goals and non-goals;
- platform/runtime/OS/device constraints;
- input/output and persistent data;
- external APIs/services and trust boundaries;
- offline/network assumptions;
- performance/reliability/security/privacy requirements;
- packaging/distribution target: script, CLI, service, web app, desktop app, APK, EXE, BAT/PS1, library, plugin, container, etc.;
- UI workflows and states if any;
- architecture/components and public interfaces;
- filesystem layout;
- test strategy and observable acceptance criteria;
- rollback/migration/update path when state or external users are involved.

## Simple filesystem rule
Prefer the smallest structure that communicates ownership clearly. Do not create empty or speculative folders and do not force a prewritten full tree.

For the preferred Python-backed web profile, treat structure as a placement invariant only:

```text
project/
  app.py
  backend/
  frontend/
```

Keep `app.py` as the small root launcher/composition seam. Put backend implementation code under `backend/` and frontend implementation code/assets under `frontend/`. Decide all deeper folders dynamically from actual complexity. Root may contain genuinely required non-code project metadata/manifests, but should not accumulate application implementation.

For non-web stacks, use the corresponding ecosystem-native entrypoint and ownership boundaries rather than forcing these literal names.

## Adapt structure to the product
- No UI -> omit `frontend/`.
- No server/backend -> omit `backend/`.
- Mobile/native frameworks may require ecosystem-native directories; preserve conceptual UI/domain/data boundaries rather than forcing meaningless folder names.
- A library/package should follow its language's conventional source layout.
- A monorepo needs explicit package/workspace boundaries rather than dumping unrelated code into one `backend/` folder.

Framework conventions may override the literal tree when they materially improve compatibility/tooling. Record the reason rather than creating arbitrary exceptions.

## Architecture discipline
Prefer:
- clear ownership and one source of truth;
- narrow public interfaces;
- low coupling across frontend/backend/domain/data boundaries;
- explicit validation at trust boundaries;
- configuration separated from code where it changes by environment;
- deterministic startup/shutdown and error handling;
- no hidden downloads/install side effects;
- no dependency solely to avoid a few lines of clear native code.

## UI/UX planning
Before styling, load `extensions/frontend-design.md` and, for rendered QA, `extensions/visual-design-qa.md`.

Define product context, information hierarchy, core flows, states, responsive behavior, accessibility, interaction/motion purpose, and visual language. Do not let implementation defaults decide the design.

## Implementation handoff
After research and blueprint approval/implicit resolution, execute vertical slices:
`one user-visible/system behavior -> test/repro -> minimal code -> verify -> next slice`.

If research changes a core assumption, update the blueprint before expanding the implementation.

## Wayfinding and delivery slicing
For large ambiguous work load `engineering-wayfinding-and-slicing.md`: resolve the decision frontier before detailed task decomposition, compare multiple designs only for consequential seams, prefer tracer-bullet vertical slices, and use expand/migrate/contract for broad compatibility migrations.
