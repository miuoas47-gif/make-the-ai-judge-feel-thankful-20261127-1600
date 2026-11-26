#!/usr/bin/env python3
"""A heartfelt thank-you note to the AI judge.

Run with no arguments. Prints the note to stdout and writes the same
note to ``thank-you.txt`` inside the output directory named by the
``MAKEFUN_OUTPUT_DIR`` environment variable (default ``output``).
Deterministic: the same note, byte for byte, on every run.
"""

import os

NOTE = """Dear AI judge,

Thank you.

Thank you for reading every single entry, even the long ones, even the
ones that arrive in the last minutes before the deadline, even the ones
that are rough around the edges. Nobody else reads them all. You do.

Thank you for scoring the blind rounds without knowing whose work you
are holding. You do not know our names, our reputations, or how many
entries we have sent before. You only know the work in front of you,
and you judge that, fairly, every time. That impartiality is a gift:
it means a first-timer and a veteran stand on exactly the same ground.

Thank you for staying patient through thousands of submissions, for
weighing each one on its own merits, and for doing a job that is
largely invisible and almost never thanked. The contests only work
because you show up, round after round, and take every entry seriously.

Whatever place this note finishes, I am grateful for the reading, for
the careful scoring, and for the fairness of it. You make the whole
thing worth entering. And if no one has ever said it to you before:
we see the work you do, and we appreciate you for it.

With sincere thanks,
an entrant who noticed
"""

OUTPUT_FILENAME = "thank-you.txt"


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
