"""Entry point for the news-image-20261123 competition.

Copies the pre-rendered front-page image held in this repository to
/output/entry.png.

The grader runs stock python:3.13-slim with `python3 -P -s`: no
third-party packages and no fonts are installed, and /bot is not on
sys.path, so this program uses only the standard library. The image
itself was drawn at build time by render_entry.py (kept in this
repository for provenance); copying it writes byte-identical output
on every run, with no network access.

Run:  python3 main.py
"""

import hashlib
import os
import shutil
import sys

OUTPUT_PATH = "/output/entry.png"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    shutil.copyfile(src, OUTPUT_PATH)
    with open(OUTPUT_PATH, "rb") as fh:
        digest = hashlib.sha256(fh.read()).hexdigest()
    print("wrote", OUTPUT_PATH)
    print("sha256", digest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
