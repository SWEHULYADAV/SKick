# SKick Branding and PNG Icons

SKick v1.0 uses PNG assets so the same branding can be reused in Skill metadata, repositories and browser tabs.

## Included assets

- `../assets/logo.png` — 1254x1254 full logo
- `../assets/icon.png` — 512x512 Skill/app icon
- `../assets/favicon.png` — 64x64 browser favicon
- `../assets/favicon-32.png` — 32x32 browser favicon

## Skill metadata

`agents/openai.yaml` uses `assets/icon.png` for small/large icon metadata. README banners are WebP-only presentation assets and are excluded from runtime distributions.

## Browser tab icon

For a project where the favicon is served at `/assets/favicon.png`:

```html
<link rel="icon" type="image/png" href="/assets/favicon.png">
```

For a relative static site path:

```html
<link rel="icon" type="image/png" sizes="32x32" href="./assets/favicon-32.png">
```

## Usage rule

Do not hard-code SKick branding into unrelated user projects. Use these assets for the SKick repository/site/plugin or when the user explicitly wants SKick-branded output. For normal web projects, generate/use the project's own favicon instead.
