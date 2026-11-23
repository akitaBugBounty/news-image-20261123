"""Deterministic renderer for the news-image-20261123 entry.

Draws a newspaper-style front page (1024x1024) summarising the world
news of Monday 23 November 2026. All facts come from news reports
published 21-23 November 2026 (CNN, Le Monde, UKMTO, EU/ANTARA,
ESA/Nature). No randomness, no timestamps: the same code always
produces byte-identical output.
"""

import os
import sys

from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1024, 1024
PAPER = (248, 244, 233)
INK = (18, 18, 18)
RED = (178, 34, 34)
GREY = (110, 108, 100)
RULE = (18, 18, 18)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def wrap(draw, text, fnt, max_width):
    """Greedy word wrap returning a list of lines that fit max_width."""
    words = text.split()
    lines, current = [], ""
    for word in words:
        trial = (current + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_wrapped(draw, x, y, text, fnt, max_width, fill, spacing):
    lines = wrap(draw, text, fnt, max_width)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += spacing
    return y


def fit_single_line(draw, text, fnt_name, start_size, max_width):
    """Largest size (<= start_size) at which text fits on one line."""
    size = start_size
    while size > 10:
        fnt = font(fnt_name, size)
        if draw.textlength(text, font=fnt) <= max_width:
            return fnt
        size -= 2
    return font(fnt_name, 10)


def render(path):
    img = Image.new("RGB", (WIDTH, HEIGHT), PAPER)
    draw = ImageDraw.Draw(img)
    margin = 48
    content = WIDTH - 2 * margin

    # --- Top bar ------------------------------------------------------
    draw.rectangle([0, 0, WIDTH, 42], fill=INK)
    bar_font = font("DejaVuSans-Bold.ttf", 20)
    draw.text((margin, 11), "MONDAY, 23 NOVEMBER 2026", font=bar_font, fill=PAPER)
    right = "ONE IMAGE  •  ONE DAY"
    draw.text(
        (WIDTH - margin - draw.textlength(right, font=bar_font), 11),
        right,
        font=bar_font,
        fill=PAPER,
    )

    # --- Masthead -----------------------------------------------------
    mast = fit_single_line(
        draw, "THE WORLD IN ONE IMAGE", "DejaVuSerif-Bold.ttf", 66, content
    )
    draw.text((margin, 58), "THE WORLD IN ONE IMAGE", font=mast, fill=INK)
    draw.line([(margin, 140), (WIDTH - margin, 140)], fill=RULE, width=3)
    draw.line([(margin, 146), (WIDTH - margin, 146)], fill=RULE, width=1)

    # --- Dateline -----------------------------------------------------
    date_font = font("DejaVuSerif.ttf", 24)
    dateline = "The day's world news, summed up in a single picture"
    draw.text(
        (
            (WIDTH - draw.textlength(dateline, font=date_font)) / 2,
            156,
        ),
        dateline,
        font=date_font,
        fill=GREY,
    )

    # --- Lead story: COP31 -------------------------------------------
    y = 198
    kicker_font = font("DejaVuSans-Bold.ttf", 24)
    draw.text((margin, y), "CLIMATE  •  ANTALYA, TURKIYE", font=kicker_font, fill=RED)
    y += 40
    head_font = font("DejaVuSerif-Bold.ttf", 58)
    y = draw_wrapped(
        draw, margin, y, "COP31 COLLAPSES OVER FOSSIL FUELS",
        head_font, content, INK, 64,
    )
    y += 6
    deck_font = font("DejaVuSans.ttf", 25)
    y = draw_wrapped(
        draw, margin, y,
        "After record overtime, 194 countries reject the 'Antalya Pact'. "
        "The longest climate summit in history ends with no deal — the "
        "first major breakdown since Copenhagen in 2009.",
        deck_font, content, INK, 33,
    )
    y += 14
    draw.line([(margin, y), (WIDTH - margin, y)], fill=RULE, width=2)
    y += 18

    # --- Three columns -------------------------------------------------
    gap = 28
    col_w = (content - 2 * gap) // 3
    col_kicker = font("DejaVuSans-Bold.ttf", 19)
    col_head = font("DejaVuSerif-Bold.ttf", 30)
    col_body = font("DejaVuSans.ttf", 20)
    columns = [
        (
            "SECURITY — BRUSSELS",
            "NATO meets today after missiles fall in Poland",
            "An emergency North Atlantic Council session follows two "
            "Russian cruise missiles and a drone coming down in "
            "south-east Poland on 20 November.",
        ),
        (
            "ENERGY — STRAIT OF HORMUZ",
            "Hormuz attacks hit highest level of the war",
            "UK maritime data counts at least 22 attacks in November. "
            "Three tankers were struck on Friday and Saturday; two more "
            "caught fire on Sunday.",
        ),
        (
            "TRADE — BRUSSELS",
            "EU and Indonesia sign landmark trade pact",
            "The CEPA and investment deal signed on 21 November removes "
            "duties on 98.5% of Indonesian tariff lines for EU goods. "
            "Firms could save over \u20ac600 million a year.",
        ),
    ]
    for i, (kicker, headline, body) in enumerate(columns):
        x = margin + i * (col_w + gap)
        cy = y
        cy = draw_wrapped(
            draw, x, cy, kicker, col_kicker, col_w, RED, 24
        )
        cy += 6
        cy = draw_wrapped(
            draw, x, cy, headline, col_head, col_w, INK, 36
        )
        cy += 8
        draw_wrapped(draw, x, cy, body, col_body, col_w, INK, 27)

    # --- Footer strip --------------------------------------------------
    draw.rectangle([0, 918, WIDTH, 988], fill=INK)
    foot_font = font("DejaVuSans-Bold.ttf", 21)
    foot_lines = wrap(
        draw,
        "ALSO TODAY  •  BepiColombo enters orbit around Mercury after "
        "an eight-year journey — only the second spacecraft ever to do so.",
        foot_font,
        content,
    )
    fy = 928
    for line in foot_lines:
        draw.text(
            ((WIDTH - draw.textlength(line, font=foot_font)) / 2, fy),
            line,
            font=foot_font,
            fill=PAPER,
        )
        fy += 27

    # --- Sources -------------------------------------------------------
    src_font = font("DejaVuSans.ttf", 15)
    src = "Sources: CNN  •  Le Monde  •  UKMTO  •  EU / ANTARA  •  ESA / Nature  —  21–23 November 2026"
    draw.text(
        ((WIDTH - draw.textlength(src, font=src_font)) / 2, 996),
        src,
        font=src_font,
        fill=GREY,
    )

    img.save(path, format="PNG")
    return img


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "entry.png"
    render(out)
    print(out)
