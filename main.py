"""Entry point for the news-image-20261123 competition.

Renders the newspaper-style front page summarising the world news of
Monday 23 November 2026 and writes it to /output/entry.png.

The render is fully deterministic: the same code always produces the
same PNG bytes (no randomness, no timestamps, no network access).

Run:  python3 main.py
"""

import hashlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from render_entry import render  # noqa: E402

OUTPUT_PATH = "/output/entry.png"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    render(OUTPUT_PATH)
    with open(OUTPUT_PATH, "rb") as fh:
        digest = hashlib.sha256(fh.read()).hexdigest()
    print("wrote", OUTPUT_PATH)
    print("sha256", digest)


if __name__ == "__main__":
    main()
