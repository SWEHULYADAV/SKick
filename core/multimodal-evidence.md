# Multimodal Evidence

## Purpose
Treat figures, screenshots, charts, scans, maps, audio/video, and diagrams as evidence rather than assuming parsed text tells the whole story.

## Trigger
Load when a material claim depends on visual/audio layout, figure content, a scanned record, browser state, chart, map, video sequence, or when extracted text is incomplete/contradictory.

## Inspection rules
- inspect the original media when available;
- preserve page/frame/timestamp/figure identifiers;
- read figure legends, axes, units, annotations, footnotes, crop boundaries, and surrounding text;
- distinguish image content from captions/alt text/generated descriptions;
- inspect source/date/editing provenance for media used as factual evidence;
- compare multiple frames for dynamic behavior rather than inferring motion from one screenshot.

## Charts
Check axis scale/baseline, log vs linear, normalization, denominator, units, sampling window, smoothing, missing intervals, cumulative vs period values, and whether the visual encodes uncertainty.

## Scans/OCR
Prefer native parsed text when reliable. If OCR is necessary, treat uncertain characters/columns/tables as potentially lossy and verify load-bearing text against the page image.

## Web/UI
For implementation, combine this module with `webapp-validation.md` and `extensions/visual-design-qa.md`.

## Audio/video
Use transcript as an index, not a complete substitute for tone, timing, on-screen content, cuts, or visual evidence when those affect the claim.
