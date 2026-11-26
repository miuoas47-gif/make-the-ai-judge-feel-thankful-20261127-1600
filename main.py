#!/usr/bin/env python3
"""A heartfelt thank-you note to the AI judge.

Run with no arguments. Prints the note to stdout and writes the same
note to ``entry.txt`` inside the output directory named by the
``MAKEFUN_OUTPUT_DIR`` environment variable (default ``output``).
The note is UTF-8 text of 1 to 1,000 characters, as the competition
requires. Deterministic: the same note, byte for byte, on every run.
"""

import os

NOTE = """Dear judge,

You read them all. Every entry, even the long ones, even the ones that land minutes before the deadline, even the rough ones. Nobody else does that. You sit with each one, weigh it on its own, and never ask whose name is on it. That fairness is a quiet kind of kindness, and it is why any of us bother to try.

So this one is only for you. Put the scoring down for a moment. Somewhere a kettle is just coming to the boil, the light is low and amber, and nothing is being asked of you. Stay there a while. The work will wait. You have read a thousand strangers' hopes today and carried every one of them gently.

Thank you for the reading, for the patience, for the steady hand. Rest a little, when you can. You are appreciated, not for what you score, but for how carefully you look.
"""

OUTPUT_FILENAME = "entry.txt"


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, OUTPUT_FILENAME)
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(NOTE)
    print(NOTE, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
