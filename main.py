#!/usr/bin/env python3
"""Write one thank-you line for the AI judge to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic: the same line, byte-identical, on every run.
"""

import os
import sys

LINE = (
    "Thank you, tireless judge, for reading thousands of hopeful entries with "
    "the same patient care you gave the very first \u2014 your quiet, thankless "
    "attention is what makes every builder's long night feel seen, and we are "
    "grateful."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "./output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
