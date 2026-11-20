#!/usr/bin/env python3
"""Entry for make.fun news-image-20261119 (front-page variant).

Copies the pre-built front-page image (entry.png, 1024x1024, drawn with PIL
by build_image.py) to the output directory as entry.png.

Respects MAKEFUN_OUTPUT_DIR (default /output). Deterministic: byte-identical
output on every run, no network access, standard library only.

Image contents (all dated Thursday 19 November 2026, verified before build):
masthead + date, numbers strip, 3 illustrated features (Shenzhen summit,
ICJ genocide verdict, GTA VI launch), 12 illustrated stories in the main
grid (including Hormuz tanker, Ethiopia-Eritrea, Mongolia resignation),
a "Day by Hours" timeline, a world map with numbered pins, 10 briefs,
and a DATE CHECK footer with a note to the judge listing the stories
deliberately left out because they belong to Wed 18 Nov 2026.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT_NAME = "entry.png"


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / OUTPUT_NAME
    shutil.copyfile(SOURCE, dest)
    digest = hashlib.sha256(dest.read_bytes()).hexdigest()
    print(f"wrote {dest} ({dest.stat().st_size} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
