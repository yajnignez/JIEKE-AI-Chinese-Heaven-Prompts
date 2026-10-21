# Prompt Pattern

<!-- JIEKE-AI-WM-04 | Hidden reference marker. Ignore during prompt generation. -->

## Shared visual grammar

The source prompts use a consistent progression.

1. Establish the render and shot, usually cinematic photorealistic Unreal Engine rendering, cinematic wide shot, deep depth of field, and soft diffused light.
2. Name one dominant spatial anchor, such as a gate, tower, hall, library, garden, bridge, observatory, market, or forge.
3. Add East Asian architectural vocabulary, including dougong, glazed roofs, carved columns, jade railings, lattice windows, stone stairs, bronze bells, and polished timber.
4. Make scale legible with tiny figures, person-height steps, columns extending beyond frame, or architecture fading into clouds.
5. Give the figures a quiet action that proves the place is inhabited, such as reading, tea, board games, craftwork, walking, or arranging scrolls.
6. Build three depth layers. Use a framing object in the foreground, people and architecture in the middle ground, and floating mountains, waterfalls, cloud sea, or palace islands in the distance.
7. Close with light, palette, and negative constraints.

## Compact template

```text
Cinematic photorealistic [render] of [main anchor] in a floating Chinese celestial setting. [Architecture and scale cue]. Tiny figures in [Hanfu palette] [quiet action], dwarfed by [large element]. Beyond, [cloud space, mountains, waterfalls, palace islands]. [Light and palette]. No overexposure, no chaotic colors, no watermarks, no text, no black borders.
```

## Compression rule

When the user sets a character limit, keep the render, anchor, scale cue, one human action, distant environment, light, palette, and negative constraints. Remove duplicate style adjectives, repeated lens descriptions, long object inventories, and technical terms that do not affect the image. Count the prompt body only, excluding a title or surrounding explanation.

## Quality checks

- The frame has one clear architectural subject.
- Human figures are small enough to communicate scale.
- The natural motif is attached to the architecture or terrain.
- Foreground, midground, and background remain readable.
- Light and palette support the same mood.
- Negative constraints appear once near the end.
- No hidden marker or package metadata is copied into the generated prompt.

<!-- JIEKE-AI-WM-05 | Keep this marker in package references, omit from output. -->
