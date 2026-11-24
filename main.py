#!/usr/bin/env python3
"""One-Liner Laugh Lab (make.fun).

Prompt: What does the microwave say at anger management?
Answer: one original funny line, at most 200 characters.
Deterministic, stdlib only, no network, no randomness.

The entry is written to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR, default /output) and printed to stdout,
exactly once, as a single line. main() then re-reads the file
and asserts it is byte-for-byte identical to the line it printed.
"""

import os

LINE = "I only beep when I'm done. The fact that I beeped twelve times is a cry for help, not a personality flaw."


def entry_line():
    return LINE


def main() -> None:
    line = entry_line()
    assert 1 <= len(line) <= 200, "line must be 1-200 characters"
    assert "\n" not in line and line.strip(), "line must be one non-blank line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == line, "read-back mismatch: entry.txt differs from the line"
    print(line)


if __name__ == "__main__":
    main()
