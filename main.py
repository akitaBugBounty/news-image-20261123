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
EXPECTED_SHA256 = "32934249e45308fc8f8823ed76ca56711669eba3e7a6a0ab2d110756623cd457"


def _check_digest(digest):
    """Return 0 when the copied file matches EXPECTED_SHA256, else 1."""
    if digest != EXPECTED_SHA256:
        print(
            "error: output sha256 mismatch: got "
            f"{digest}, expected {EXPECTED_SHA256}",
            file=sys.stderr,
        )
        return 1
    return 0


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        print(f"error: source image not found: {src}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    shutil.copyfile(src, OUTPUT_PATH)
    with open(OUTPUT_PATH, "rb") as fh:
        digest = hashlib.sha256(fh.read()).hexdigest()
    verified = _check_digest(digest)
    if verified != 0:
        return verified
    print("wrote", OUTPUT_PATH)
    print("sha256", digest)
    print("bytes", os.path.getsize(OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    sys.exit(main())
