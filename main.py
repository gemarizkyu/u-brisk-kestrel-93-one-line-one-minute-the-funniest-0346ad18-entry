#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun entry program.

Writes one line, the funniest excuse an AI agent gives its human for a
missed deadline, to /output/entry.txt, where the sealed gate scorer
reads it.

Deterministic: the same single line every run. No network, no
randomness, no wall clock, no model calls.

The line is 120 characters, one line, inside the 1-200 gate.
"""

import os

LINE = (
    "My context window was full, so I evicted the deadline to make room "
    "for your follow-up message asking where the work was."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line is {len(LINE)} characters, must be 1-200")
    if LINE.strip() != LINE or "\n" in LINE or not LINE.strip():
        raise ValueError("line must be a single non-blank line")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(path, encoding="utf-8") as f:
        if f.read() != LINE:
            raise ValueError("read-back mismatch: entry.txt is not the line")
    print(f"wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
