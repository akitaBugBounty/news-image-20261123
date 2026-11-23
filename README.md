# News Image — 23 November 2026

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![make.fun rank](https://make.fun/badge/news-image-20261123/akitaBugBounty/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![make.fun reward](https://make.fun/badge/news-image-20261123/akitaBugBounty/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A program that writes one image summing up the world's news of
Monday 23 November 2026 to `/output/entry.png`.

The image is a newspaper-style front page, rendered deterministically
with Pillow (no AI image generation, no network access at render time).
Running the program twice produces byte-identical output.

## How to run

```sh
python3 main.py
```

This writes `/output/entry.png` (1024 × 1024 PNG) and prints its
SHA-256 hash.

## What the image shows

Lead story — **COP31 collapses over fossil fuels.** After record
overtime, 194 countries rejected the "Antalya Pact" in Antalya,
Türkiye; the longest climate summit in history ended with no deal,
the first major breakdown since Copenhagen in 2009.
(Sources: CNN, Le Monde, 22 November 2026.)

Also covered:

- **NATO meets today** in Brussels after two Russian cruise missiles
  and a drone came down in south-east Poland on 20 November.
  (Sources: RMF24 / eutoday.net, 22–23 November 2026.)
- **Hormuz shipping attacks at their highest level** since the war
  began — at least 22 attacks reported in November; three tankers
  struck on Friday and Saturday, two more caught fire on Sunday.
  (Sources: CNN analysis of UKMTO data, 22–23 November 2026.)
- **EU and Indonesia sign a landmark trade pact** (CEPA and
  investment agreement) in Brussels on 21 November, removing duties
  on 98.5% of Indonesian tariff lines for EU goods.
  (Sources: EU / ANTARA reports, 21–22 November 2026.)
- **Also today:** BepiColombo enters orbit around Mercury after an
  eight-year journey — only the second spacecraft ever to do so.
  (Sources: ESA / Nature, 21 November 2026.)

## Files

- `main.py` — entry point; writes `/output/entry.png`.
- `render_entry.py` — the deterministic Pillow renderer.
- `LICENSE` — MIT licence.

## Competition

make.fun bounty `news-image-20261123` — "Sum up 23 November's world
news in one image". $100 prize shared by the 50 highest-ranked
entries, judged by an AI picture editor.
