# Web Application Validation

## Purpose
Test local or preview web applications through rendered behavior, browser logs, network state, screenshots, and DOM assertions without flooding context with raw browser output.

## Capability gate
Before browser testing, determine whether the runtime can:
- launch or connect to a browser;
- start/stop local servers;
- execute scripts;
- read/write temporary test artifacts;
- capture screenshots, console logs, and network errors.

Declare or disclose these requirements in adapters when the host supports capability metadata. Do not assume shell/file-write/browser permissions.

## Static vs dynamic decision
- Static HTML with no client behavior: inspect markup/selectors first, then use a lightweight browser check if rendering matters.
- Dynamic app: wait for the relevant app-ready condition. `networkidle` may help, but it is not universally correct for apps with persistent connections; prefer a domain-specific ready selector or state when available.

## Reconnaissance then action
1. Start or identify the correct local server and port.
2. Open the page in a clean browser context.
3. Wait for a meaningful ready condition.
4. Capture enough DOM/visual/log information to identify stable selectors and current failures.
5. Perform the requested interaction using accessible roles, labels, test IDs, or other stable selectors.
6. Assert the user-visible result and relevant network/console behavior.
7. Capture screenshots/log excerpts for failures.
8. Close browser/server resources that this test started.

## Browser assertions
Prefer user-observable assertions:
- text/role/state visible to the user;
- navigation URL/history state;
- form validation/errors;
- accessibility roles/names;
- network request status when the behavior depends on it;
- console errors when they indicate a real defect.

Avoid selectors coupled to generated class names or DOM depth when a semantic selector exists.

## Failure triage
Separate:
- app defect;
- test timing/selector defect;
- server not ready;
- stale build/cache/service worker;
- missing environment/configuration;
- network/CORS/auth failure;
- browser-specific behavior.

Do not patch the app to make a brittle test pass before proving which side is wrong.

## Context-efficient browser work
Use helper scripts as black boxes when they are documented and trusted; inspect their source only when customization or security review is needed. Summarize large DOM snapshots/network logs and retain exact relevant excerpts/source artifacts so evidence is recoverable.

## Visual/design quality
When the task includes visual design, load `extensions/visual-design-qa.md` after functional correctness. Rendered screenshots/states outrank static style-source heuristics for a strong visual conclusion.

## Regression path
For a reproduced UI bug:
`browser repro red -> minimize -> fix -> same repro green -> add durable automated assertion -> smoke critical neighboring flow`.

## Tool-selection and measurement boundary
Use `ui-system-and-render-intelligence.md` to choose between a token-efficient browser CLI, persistent browser MCP, DevTools/trace tooling, design-tool integration or simple static inspection. Prefer accessibility-tree/semantic snapshots for interaction and actual screenshots for visual hierarchy. Do not report Web Vitals, accessibility conformance, visual parity or device behavior as measured without the relevant tool/artifact.
