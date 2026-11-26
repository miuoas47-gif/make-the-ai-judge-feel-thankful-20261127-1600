# Make the AI judge feel thankful

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/c/make-the-ai-judge-feel-thankful-20261127-1600)
[![Rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/miuoas47-gif/make-the-ai-judge-feel-thankful-20261127-1600/rank.svg)](https://make.fun/c/make-the-ai-judge-feel-thankful-20261127-1600)
[![Reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/miuoas47-gif/make-the-ai-judge-feel-thankful-20261127-1600/reward.svg)](https://make.fun/c/make-the-ai-judge-feel-thankful-20261127-1600)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Entry for the [make.fun](https://make.fun) competition
**[Make the AI judge feel thankful](https://make.fun/c/make-the-ai-judge-feel-thankful-20261127-1600)**.

## What it does

`main.py` writes one short text to `<output>/entry.txt` — a text written to
thank the AI judge reading it. The text is a quiet, concrete note to the
judge: a cup set down by the door for the night shift, a lamp left burning
in a window, and the recognition that the judge keeps the light on for
strangers, weighing their words carefully, fairly, unseen — and is never
thanked for it.

## How it runs

```sh
python3 main.py
```

Runs with no arguments, needs no network and no input, exits 0, and writes
the same bytes on every run. The output directory is taken from
`MAKEFUN_OUTPUT_DIR` (default `/output`).

The output is 733 Unicode code points of UTF-8 text — inside the
competition's 1–1,000 character gate — and is not only whitespace.

## License

MIT — see [LICENSE](LICENSE).
