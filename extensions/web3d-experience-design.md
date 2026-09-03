# Web 3D and Spatial Experience Extension

## Purpose
Design and implement production-quality 3D/WebGL/WebGPU experiences only when spatial interaction, visualization or storytelling provides real product value.

## Technology routing
- **Three.js**: low-level/custom web 3D, shaders, rendering control, non-React scenes.
- **React Three Fiber**: React-owned product state with declarative Three.js scene composition.
- **Babylon.js / PlayCanvas**: engine/editor/physics/game-style requirements.
- **A-Frame/WebXR**: XR-first scenes where its entity/component model is appropriate.
- **Spline**: designer-authored/embed-oriented 3D workflow when design-tool handoff is central.

Do not add 3D for generic hero decoration when an image/video/CSS effect communicates the same thing more efficiently.

## Architecture
Separate application state, UI, timeline orchestration and render loop. Do not let UI rerenders recreate scenes, loaders or expensive GPU resources. Maintain explicit refs/bridges for animation libraries that manipulate 3D properties.

## Asset pipeline
Research and document:
- source asset format and authoring tool;
- export format (commonly glTF/GLB when appropriate);
- mesh/material/texture budgets;
- compression strategy;
- LOD/fallbacks;
- caching/CDN behavior;
- licensing/provenance of 3D assets;
- mobile/device constraints.

## Loading states
Never render a blank heavy canvas as the only content. Provide semantic HTML and useful placeholder/fallback. Lazy-load scenes below the fold or after user intent when possible.

## Interaction
Spatial controls must have clear constraints and reset behavior. Product viewers need predictable camera bounds, zoom/rotate affordances and non-3D equivalents for critical product information.

## Scroll-driven 3D
If GSAP or another timeline drives camera/mesh properties:
- keep one timeline owner;
- map narrative sections to explicit scene states;
- avoid per-frame React state updates for raw animation values;
- handle resize/refresh/route teardown;
- reduce or disable camera travel/parallax under reduced motion;
- test rapid scroll and reverse scroll.

## Performance QA
Inspect frame time, long tasks, asset transfer, texture memory, draw calls, shader cost, post-processing, device pixel ratio and thermal/mobile behavior where tooling allows. Optimize the bottleneck shown by evidence rather than blindly reducing quality everywhere.

## Failure/fallback QA
Validate:
- WebGL/WebGPU unavailable;
- asset 404/corruption;
- slow network;
- low-memory mobile;
- tab background/visibility changes;
- resize/orientation;
- route unmount/remount;
- reduced motion;
- keyboard/touch interaction.
