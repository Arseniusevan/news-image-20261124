# News Image — 24 November 2026

[![Bounty](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![Rank](https://make.fun/badge/news-image-20261124/Arseniusevan/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![Reward](https://make.fun/badge/news-image-20261124/Arseniusevan/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

A one-page front page summing up the world's news of Tuesday, 24 November 2026 — 27 stories across regions and fields, from Ukraine's claimed sinking of a Russian warship off Libya to Nvidia's 31% surge as Jensen Huang returned as CEO, and the collapse of the COP31 climate talks.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

This writes `out/entry.png` (1024×1024, under 1 MiB). The image is drawn by `generate_image.py` (Python 3 + Pillow) and copied verbatim by `main.ts`, so two runs produce byte-identical output.

## Contents

- `entry.png` — the front-page image
- `generate_image.py` — the generator that draws it
- `main.ts` — the entry program (copies `entry.png` to the output directory)
- `LICENSE` — MIT
