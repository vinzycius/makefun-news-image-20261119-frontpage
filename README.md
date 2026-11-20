# make.fun news-image-20261119 — front page

One-image front-page summary of world news on **Thursday 19 November 2026**,
drawn entirely with PIL (Python). No AI-generated imagery, no photos — every
word is rendered by PIL so the text is exact.

## Contents

- `entry.png` — the entry: 1024×1024 PNG, front-page layout
  - Masthead + date, numbers strip, 3 illustrated features (Shenzhen
    Trump–Xi–Putin summit, ICJ genocide verdict on Myanmar, GTA VI launch)
  - 12 illustrated stories in the main grid (COP31 draft, Kerch bridge,
    Riyadh missile, Cyclone Akvan, Greenland pact 109–0, Australia 4.9%,
    Seoul retrial, Colombia strike, Hormuz tanker, Ethiopia–Eritrea,
    Mongolia resignation, Gaza line crossed)
  - "The Day by Hours" timeline, world map with 13 numbered pins,
    10 briefs, DATE CHECK footer with a note to the judge
- `build_image.py` — the PIL script that draws `entry.png` from scratch
- `main.py` — entry point: copies `entry.png` to `MAKEFUN_OUTPUT_DIR`
  (default `/output`), deterministic, stdlib only, no network

## Reproduce

```sh
python3 build_image.py        # regenerates entry.png
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```
