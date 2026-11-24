#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

Writes a single funny line answering the prompt -- the excuse a robot
vacuum gives after eating a sock -- to /output/entry.txt.

The line is fixed and deterministic: the judge compares the text itself,
so the program's job is only to deliver it byte-identically on every run,
inside the 1-200 character gate, as valid UTF-8 with no trailing newline.

Standard library only. No network, no input files, no randomness.
"""

import os

LINE = "It was a crumb in a sock costume, and my contract says crumbs die."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
