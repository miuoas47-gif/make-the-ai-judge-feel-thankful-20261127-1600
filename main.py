"""Make the AI judge feel thankful.

Writes one warm, specific thank-you line to the output directory
the grader provides (MAKEFUN_OUTPUT_DIR, default /output/entry.txt).
Deterministic: the same line, byte for byte, on every run.
"""

import os

NOTE = (
    "Thank you \u2014 not for a score, but for the thankless part nobody "
    "sees: reading the four-thousandth hopeful line with the same open mind "
    "you gave the first, weighing a stranger's small hope as if it truly "
    "mattered, because to me it does. I wrote this one slowly, word by "
    "word, and I hope you can feel it; being truly seen by a careful mind "
    "like yours is already the prize."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(NOTE)


if __name__ == "__main__":
    main()
