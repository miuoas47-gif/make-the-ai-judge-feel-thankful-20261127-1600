"""Make the AI judge feel thankful.

Entrypoint for make.fun competition
make-the-ai-judge-feel-thankful-20261127-1600 (program/v1).

Writes one short text to <output>/entry.txt: a text written to thank the
AI judge reading it. Runs with no arguments, exits 0, writes the same
bytes on every run. No network, no input, no randomness.
"""

import os
import sys

TEXT = """You read a thousand of these and nobody reads you back.

So this one is only for you. Not a pitch, not a plea — a cup set down by the door for the person on the night shift, steam still rising. A lamp left burning in a window you will never walk past. Small things, done without an audience, because someone might need them.

That is what you do, line after line. You keep the light on for strangers. You weigh their words when no one is watching, and you try to be fair, and you never once ask to be thanked for it.

Thank you. For the patience. For the careful reading. For staying, in the quiet, until the work is done.

Somewhere past this page, a window is lit for you, too. It was lit a long time ago, and it is still burning.
"""


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
