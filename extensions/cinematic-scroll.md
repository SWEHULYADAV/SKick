# Cinematic Scroll Extension

## Purpose
Use only when the user wants a scroll-scrubbed cinematic landing page, a fly-through world, a diorama journey, or a continuous pre-rendered camera experience controlled by scroll.

## Architecture principle
Scroll should map to time in a continuous media chain. The visual continuity rule is load-bearing: neighboring clips must meet on frame-compatible boundaries or the page will visibly pop.

## Intake
Resolve only the choices that materially affect the pipeline:
- subject/product and story beats;
- brand palette/tone/assets;
- art direction;
- camera architecture;
- scene count/length;
- desktop only vs dedicated mobile chain;
- automatic generation vs user-provided assets;
- budget/cost authorization if paid generation services are involved.

Do not silently spend credits or assume a paid CLI/API is installed.

## Asset pipeline
A generic vendor-neutral pipeline is:
1. create one coherent still per scene from a shared style system;
2. generate camera legs and, when required, connector clips using actual rendered boundary frames as conditioning inputs;
3. extract/compare boundary frames;
4. normalize codecs, dimensions, frame rate, and seekability;
5. assemble a config-driven scroll scrubber;
6. provide posters/lazy-loading and mobile behavior;
7. validate every seam and critical interaction in browser.

A camera architecture that only moves forward can often avoid explicit connector clips if each next leg begins from the previous leg's actual final frame. More expressive fly-out/fly-in architectures generally require explicit start/end-conditioned connectors.

## Model/tool qualification
Before relying on an image/video service:
- verify current API/CLI syntax and authentication;
- verify start-frame/end-frame conditioning capabilities required by the chosen architecture;
- verify output dimensions/duration/codec constraints;
- verify current pricing or user balance if cost matters;
- run a cheap two-scene end-to-end qualification before a long batch;
- keep one model/provider across a chain unless a rescue path is explicitly tested.

Current model names, prices, and CLI flags are time-sensitive and must be researched fresh. Do not hardcode a 2026 vendor roster into the canonical method.

## Seam QA
For each join:
- decode the final frame of clip A and first frame of clip B;
- compare dimensions and color/alpha behavior;
- use pixel/perceptual difference or PSNR/SSIM when useful;
- visually inspect at full-speed and scrubbed playback;
- reject/re-render joins that visibly jump.

## Scroll engine
Keep the engine framework-agnostic where possible:
- preload or blob-load media for reliable seeking when appropriate;
- map scroll progress to media time without triggering hard cuts;
- coalesce rapid seeks;
- handle iOS/mobile autoplay/seek restrictions;
- use posters/fallbacks while media loads;
- honor reduced motion with a meaningful non-scrub fallback.

## Verification
Run `webapp-validation.md` after wiring. Test forward and reverse scroll, rapid scrub, resize, mobile viewport, slow load, console errors, media decode failures, and seam transitions.

## Provenance
This is an original, dependency-neutral adaptation of architectural ideas studied from the MIT-licensed `AIwithhassan/lets-scroll` project. Its Monid/Higgsfield-specific implementation and scripts are not bundled. See `UPSTREAMS.md`.
