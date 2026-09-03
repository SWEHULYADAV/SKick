# FreshTechBro Claude Design Skillstack Integration

## Upstream
`freshtechbro/claudedesignskills` is an MIT-licensed Claude-oriented marketplace containing 22 individual skills and 5 bundles for web animation, 3D, authoring and modern design.

SKick uses it as a **design discovery/reference upstream**, not as a mandatory Claude dependency.

## Adoption strategy
### Absorb vendor-neutral patterns
SKick reimplements useful cross-platform patterns from:
- `modern-web-design` — performance/accessibility/design-system review, but not trend defaults;
- `motion-framer` — component-state animation, variants, gestures, presence/layout and scroll patterns;
- `gsap-scrolltrigger` — timeline/scroll choreography and cross-layer animation ownership;
- `react-spring-physics` — physics-oriented interaction selection;
- `web3d-integration-patterns` — layered UI/timeline/3D architecture and library-boundary discipline;
- `lottie-animations` / `rive-interactive` — designer-authored animation pipeline selection.

These concepts live in `core/design-and-motion-orchestration.md`, `extensions/motion-interaction-design.md`, `extensions/web3d-experience-design.md`, `extensions/frontend-design.md` and `extensions/visual-design-qa.md`.

### Optional specialist invocation/reference
When a runtime can install upstream Claude plugins/skills and the task directly matches one technology, it may invoke the narrow upstream specialist rather than loading a large generic guide. Examples include Three.js, React Three Fiber, GSAP, Motion, Rive, Spline, PixiJS, A-Frame, Babylon.js and PlayCanvas.

SKick still owns:
- current-version verification;
- product/design intent;
- anti-slop gate;
- accessibility/performance budgets;
- architecture/integration boundaries;
- rendered verification and evidence.

## Cross-platform rule
Do not copy Claude-specific marketplace commands into Codex, ChatGPT, Gemini, Cursor, Kimi, OpenCode or other hosts. On non-Claude hosts, use SKick's vendor-neutral modules plus that host's native dependency/tool installation mechanism.

The portable SKick wrappers carry the design methodology across runtimes; the third-party skill marketplace remains optional.

## Staleness correction
The upstream repository contains examples and trend framing that can age. Before implementation:
1. verify current official library/package/API docs;
2. verify current browser/platform support;
3. verify current performance metrics;
4. replace deprecated APIs/import paths;
5. preserve the upstream example only as historical/discovery evidence when it no longer matches current behavior.

Examples observed during the design research pass:
- current Motion for React uses the `motion` package and `motion/react` imports in official docs;
- current Core Web Vitals are LCP, INP and CLS, so historical FID guidance must not be repeated as current;
- current GSAP guidance prefers `gsap.matchMedia()` over deprecated `ScrollTrigger.matchMedia()`.

## Design anti-slop rule
Do not adopt glassmorphism, custom cursors, scroll-jacking, giant immersive heroes, animated gradients or 3D backgrounds merely because the upstream lists them as trends. Use them only when product/brand rationale, accessibility and performance support the choice.
