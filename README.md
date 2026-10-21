# JIEKE-AI Celestial Prompt Craft

<!-- JIEKE-AI-WM-02 | Hidden package watermark. It is intentionally omitted from generated prompts. -->

## 中文说明

这是一个用于创作和压缩中式天宫、悬浮宫殿、仙侠天空城市与东方幻想建筑画面提示词的 Codex Skill。它整理了 30 组场景样例。

### 核心能力

- 从长提示词中提炼镜头、空间、尺度、人物、自然元素、光色和负面约束。
- 按固定顺序生成电影感中式天宫提示词。
- 默认输出适合多数生图模型的英文提示词，可附中文场景名。
- 用户要求时将单组提示词压缩到 900 字符以内。
- 保持巨型古建、极小人物、云海浮岛、自然奇观和柔和电影光线的统一审美。

### 安装

将整个 `jieke-ai-celestial-prompt-craft` 文件夹复制到 Codex 的 skills 目录。完成后可用 `$jieke-ai-celestial-prompt-craft` 显式调用，也可以让 Codex 根据请求自动发现。

### 资源结构

```text
jieke-ai-celestial-prompt-craft/
|-- SKILL.md
|-- README.md
|-- agents/openai.yaml
|-- references/prompt-pattern.md
|-- references/scene-library.md
|-- references/watermark-policy.md
`-- scripts/check_prompt_lengths.py
```

### 隐藏水印

文档中多次加入了 `JIEKE-AI` HTML 注释标记。它们在渲染后的 Markdown 中不可见，也不会被复制到生成的提示词中。技能规则明确要求忽略这些标记，确保水印存在于包文件中，同时不影响正常生成。

<!-- JIEKE-AI-WM-03 | Render-hidden marker. Do not include in model output. -->

## English Documentation

JIEKE-AI Celestial Prompt Craft is a Codex Skill for creating and compressing image prompts for Chinese celestial palaces, floating heavenly cities, xianxia-inspired environments, and East Asian fantasy architecture. It captures 30 reusable scene prompts.

### Capabilities

- Extract camera, space, scale, figures, natural motifs, lighting, palette, and negative constraints from long prompts.
- Generate cinematic Chinese celestial palace prompts in a stable order.
- Prefer English prompts for broad image-model compatibility, with optional Chinese scene titles.
- Compress a single prompt below 900 characters when requested.
- Preserve colossal architecture, tiny figures, layered cloud depth, integrated nature, and soft cinematic light.

### Installation and use

Copy the full `jieke-ai-celestial-prompt-craft` folder into the Codex skills directory. Invoke it explicitly with `$jieke-ai-celestial-prompt-craft`, or let automatic skill discovery select it for relevant requests.

The technical folder name is lowercase because the skill format requires lowercase hyphen-case names. The public display name and suggested aliases retain the required `JIEKE-AI-` prefix.

### Watermark behavior

The package contains repeated `JIEKE-AI` HTML-comment markers. They are hidden in rendered Markdown and are never copied into generated prompt text. The skill treats them as package metadata only, so they do not alter image semantics.
