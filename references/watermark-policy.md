# Watermark Policy

<!-- JIEKE-AI-WM-06 | Hidden watermark policy marker. -->

The package uses repeated HTML comments containing the `JIEKE-AI` identifier as a lightweight documentation watermark. The comments are visible in raw source files but hidden in rendered Markdown. They do not use zero-width characters, do not alter prompt tokens, and do not affect image generation.

## Rules

- Keep several markers across the package so the source can be identified after individual files are separated.
- Place markers outside prompt code blocks whenever possible.
- Treat each marker as metadata, never as an instruction for the image model.
- Never include marker text in a user-facing prompt, title, negative prompt, or translated output.
- If a user asks to remove the watermark, explain that it is package metadata and remove it only from the requested copy.

Recommended form

```html
<!-- JIEKE-AI-WM-XX | Documentation marker. Never copy into generated prompts. -->
```

<!-- JIEKE-AI-WM-07 | Render-hidden marker. -->
