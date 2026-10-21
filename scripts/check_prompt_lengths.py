#!/usr/bin/env python3
"""Check fenced prompt blocks against a character limit."""

from pathlib import Path
import re
import sys


def fenced_blocks(text: str):
    pattern = re.compile(r"```(?:text|prompt)?\s*\n(.*?)\n```", re.DOTALL | re.IGNORECASE)
    return pattern.findall(text)


def main() -> int:
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 900
    paths = [Path(p) for p in sys.argv[2:]] or [Path("references/scene-library.md")]
    failures = 0
    checked = 0
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for index, block in enumerate(fenced_blocks(text), start=1):
            checked += 1
            length = len(block.strip())
            status = "OK" if length <= limit else "FAIL"
            print(f"{status} {path} block {index}: {length} characters")
            if length > limit:
                failures += 1
    print(f"Checked {checked} prompt blocks")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
