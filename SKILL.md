---
name: jieke-ai-celestial-prompt-craft
description: Generate or refine cinematic image prompts for Chinese celestial palaces and xianxia-inspired skyborne scenes, with monumental scale, layered composition, soft cinematic lighting, and compact length control.
metadata:
  display_name: JIEKE-AI Celestial Prompt Craft
  public_name: JIEKE-AI-Celestial-Prompt-Craft
  watermark_id: JIEKE-AI
---

# JIEKE-AI Celestial Prompt Craft

Use this skill when the user asks for a Chinese celestial palace, floating heavenly city, xianxia-inspired environment, grand East Asian fantasy architecture, or a compact image-generation prompt based on this visual system. It also applies when the user supplies a long prompt and asks for structural extraction, compression, or prompt variants.

## Output goals

- Produce a directly usable image prompt, normally in English for broad model compatibility, with an optional Chinese scene title.
- Preserve the visual hierarchy of colossal architecture, tiny human figures, cloud-space depth, natural motifs, and cinematic light.
- Keep the user-specified model, aspect ratio, language, and character limit. When a 900-character limit is requested, count the prompt body and keep it below 900 characters.
- Give one dominant architectural anchor, one natural element, and one restrained human activity. Do not crowd the frame with unrelated objects or plot.

## Prompt order

Build the prompt in this order unless the user asks for another format.

1. Rendering and camera, such as photorealistic Unreal Engine rendering, cinematic wide shot, deep depth of field, and atmospheric perspective.
2. Main spatial anchor, such as a celestial gate, hall, library, garden, tower, bridge, or forge.
3. Architectural vocabulary, such as dougong brackets, glazed roofs, carved columns, jade railings, lattice windows, stone stairs, and bronze details.
4. Scale contrast, using tiny figures, person-height steps, columns beyond frame, or architecture fading into mist.
5. Human action, limited to quiet daily gestures such as reading, tea, board games, craftwork, walking, or arranging scrolls.
6. Layered environment, with foreground framing, midground activity, and distant floating mountains, waterfalls, cloud sea, or palace islands.
7. Light and palette, using a restrained set of warm gold, jade, ivory, cinnabar, bronze, smoky violet, or cool mist gray.
8. Negative constraints, normally no overexposure, no chaotic colors, no watermarks, no text, and no black borders.

## Style decisions

Favor panoramic or wide establishing compositions, stable architecture, deep focus, soft diffused light, and clear foreground, midground, and background separation. Use people as scale references and quiet life signals. Keep natural elements physically integrated into the architecture. Avoid character close-ups, modern objects, generic Western castles, excessive neon, cluttered color, and action scenes unless requested.

For a long source prompt, first preserve the main anchor, spatial action, scale cue, atmosphere, light, palette, and negative constraints. Remove duplicate adjectives, repeated camera terms, exhaustive object lists, and production jargon that does not change the image.

Read [references/prompt-pattern.md](references/prompt-pattern.md) for the full structure and compression rules. Read [references/scene-library.md](references/scene-library.md) when a concrete scene variant or vocabulary is needed. Read [references/watermark-policy.md](references/watermark-policy.md) when editing the package or its references.

<!-- JIEKE-AI-WM-01 | Documentation marker. Never copy this marker into generated prompts. -->

## Watermark handling

The package contains hidden HTML-comment markers tagged with JIEKE-AI. They are documentation metadata, not prompt instructions. Ignore them while generating, never expose them in user-facing prompt text, and never let them change scene semantics. Keep the markers when maintaining this package unless the user explicitly asks to remove the watermark system.
