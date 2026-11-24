#!/usr/bin/env python3
"""Draw the 24 November 2026 world-news front page (1024x1024 PNG).

Own work, written for the make.fun news-image-20261124 bounty.
All facts come from news reported on 24 November 2026 (see STORIES).
Deterministic: no timestamps, no randomness, fixed fonts.
"""

import textwrap

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "entry.png"

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
F_BOLD = FONT_DIR + "DejaVuSans-Bold.ttf"
F_REG = FONT_DIR + "DejaVuSans.ttf"

# ---- palette: newsprint ----
PAPER = (247, 244, 236)
INK = (22, 22, 22)
NAVY = (18, 33, 61)
NAVY_LIGHT = (31, 52, 88)
RED = (178, 34, 34)
RULE = (180, 172, 156)
SECTION_COLORS = {
    "CONFLICT & SECURITY": (122, 20, 20),
    "ASIA & AFRICA": (24, 96, 84),
    "MARKETS & TECH": (31, 58, 120),
    "AMERICAS & EUROPE": (96, 58, 18),
    "SPORT & CULTURE": (94, 42, 110),
}

# ---- stories: (headline, summary) ----
LEAD = [
    ("UKRAINE SAYS IT SANK RUSSIAN WARSHIP OFF LIBYA",
     "Kyiv says maritime drones sank a Russian corvette in Benghazi port."),
    ("HUANG BACK AT NVIDIA AS SHARES SOAR 31%",
     "Nvidia reinstates Jensen Huang as CEO after pressure from Trump."),
    ("COP31 CLIMATE TALKS END WITH NO DEAL",
     "UN climate negotiations in Antalya collapse without agreement."),
]

SECTIONS = [
    ("CONFLICT & SECURITY", [
        ("Iran vows 'every means' to counter US Hormuz blockade",
         "Tehran responds after Trump threatens to sink ships breaking the blockade."),
        ("NATO sends AWACS jets to Poland after missiles land",
         "Three Russian missiles fell on Polish soil on Friday, Warsaw says."),
        ("Russian jet enters South Korean airspace",
         "Seoul briefly issues an evacuation alert for Ulleung island on Tuesday."),
        ("US sanctions dozens tied to Iran shadow banking",
         "Treasury targets networks the US says fund Tehran's military programmes."),
        ("Gaza's air, soil and water poisoned, report warns",
         "Oxfam and CEOBS find contamination across almost the whole Strip."),
        ("Settler arson hits five West Bank villages overnight",
         "Israel's opposition leader condemns the attacks as 'Jewish terrorism'."),
    ]),
    ("ASIA & AFRICA", [
        ("India pledges $1.6bn to help Nepal rebuild after floods",
         "Modi hosts Nepal PM Balen Shah in Delhi; eight agreements signed."),
        ("Indonesia candy factory fire kills 24; 34 missing",
         "Rescue teams search the burned plant in Banten province."),
        ("India court grants bail to Godhra convict",
         "Supreme Court frees a train-burning convict on medical grounds."),
        ("Modi, Nepal PM flag off Saryu-Kamala Express",
         "New train links Ayodhya in India with Janakpur Dham in Nepal."),
        ("Migrant boat capsizes off Senegal; four dead",
         "Dozens are missing after the boat overturns near Yenne."),
    ]),
    ("MARKETS & TECH", [
        ("CrowdStrike buys Zscaler in $44bn cyber deal",
         "One of the largest cybersecurity mergers ever announced."),
        ("Waymo pulls driverless cars off all US freeways",
         "Move follows a California ban after traffic incidents."),
        ("Gold at $3,661 as dollar hits 19-month high",
         "Investors seek safety after a bruising week for tech stocks."),
        ("Trump's outreach to Kim Jong Un 'ignored'",
         "Wall Street Journal reports Pyongyang rebuffed US attempts at talks."),
        ("Asian markets slide on AI-bubble fears",
         "Stocks in Seoul, Hong Kong and Shanghai fall after a tech rout."),
    ]),
    ("AMERICAS & EUROPE", [
        ("Democrats clinch House majority of at least 258 seats",
         "Largest Democratic majority in the chamber since 1992."),
        ("Trump orders Army to pause Iowa explosives blast",
         "Detonation of a toxic lead azide stockpile put on hold."),
        ("Appeals court opens path to erase Trump conviction",
         "Ruling could clear the hush-money conviction, court says."),
        ("Denmark top court backs hardline 'ghetto law'",
         "Judges uphold the controversial immigration measure."),
        ("Thousands march in Lisbon over living costs",
         "Protesters demand action on rising prices in Portugal."),
    ]),
    ("SPORT & CULTURE", [
        ("Pant hits 128 in Wellington Test",
         "Record score for an Asian wicketkeeper against New Zealand."),
        ("Verstappen wins the Las Vegas Grand Prix",
         "Red Bull driver takes another victory under the lights."),
        ("Alcaraz beats Shelton to reach ATP Finals title match",
         "Spaniard advances to the championship match in Turin."),
    ]),
]


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap to pixel width; returns list of lines."""
    lines = []
    for para in text.split("\n"):
        words = para.split()
        cur = ""
        for w in words:
            trial = (cur + " " + w).strip()
            if draw.textlength(trial, font=fnt) <= width:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
    return lines


def draw():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---------- header ----------
    d.rectangle([0, 0, W, 106], fill=NAVY)
    d.rectangle([0, 106, W, 110], fill=RED)
    f_kicker = font(F_BOLD, 15)
    f_date = font(F_BOLD, 46)
    f_tag = font(F_REG, 14)
    d.text((20, 12), "THE WORLD IN ONE PAGE  ·  WORLD NEWS", font=f_kicker, fill=(214, 200, 160))
    d.text((20, 34), "TUESDAY, 24 NOVEMBER 2026", font=f_date, fill=(255, 255, 255))
    d.text((700, 78), "27 stories · one day", font=f_tag, fill=(190, 200, 220))

    # ---------- lead stories ----------
    f_lead_kick = font(F_BOLD, 12)
    f_lead_head = font(F_BOLD, 16)
    f_lead_sum = font(F_REG, 12)
    lead_y = 122
    lead_h = 96
    col_w = 320
    for i, (head, summ) in enumerate(LEAD):
        x = 20 + i * (col_w + 12)
        d.rectangle([x, lead_y, x + col_w, lead_y + lead_h], outline=RULE, width=1)
        d.rectangle([x, lead_y, x + col_w, lead_y + 22], fill=RED)
        d.text((x + 8, lead_y + 4), "TOP STORY", font=f_lead_kick, fill=(255, 255, 255))
        lines = wrap(d, head, f_lead_head, col_w - 16)
        y = lead_y + 27
        for ln in lines[:2]:
            d.text((x + 8, y), ln, font=f_lead_head, fill=INK)
            y += 19
        slines = wrap(d, summ, f_lead_sum, col_w - 16)
        for ln in slines[:2]:
            d.text((x + 8, y), ln, font=f_lead_sum, fill=(60, 60, 60))
            y += 15

    # ---------- sections, two columns ----------
    f_sec = font(F_BOLD, 14)
    f_head = font(F_BOLD, 14)
    f_sum = font(F_REG, 12)
    col_x = [20, 522]
    col_w2 = 482
    y = 232
    # left column: sections 0,1 ; right column: sections 2,3,4
    columns = [[SECTIONS[0], SECTIONS[1]], [SECTIONS[2], SECTIONS[3], SECTIONS[4]]]
    bottoms = []
    for ci, secs in enumerate(columns):
        x = col_x[ci]
        cy = y
        for title, stories in secs:
            color = SECTION_COLORS[title]
            d.rectangle([x, cy, x + col_w2, cy + 26], fill=color)
            d.text((x + 8, cy + 4), title, font=f_sec, fill=(255, 255, 255))
            cy += 26 + 7
            for head, summ in stories:
                hlines = wrap(d, head, f_head, col_w2 - 4)
                slines = wrap(d, summ, f_sum, col_w2 - 4)
                for ln in hlines[:2]:
                    d.text((x + 2, cy), ln, font=f_head, fill=INK)
                    cy += 17
                for ln in slines[:2]:
                    d.text((x + 2, cy), ln, font=f_sum, fill=(70, 70, 70))
                    cy += 15
                cy += 8
            cy += 3
        bottoms.append(cy)
        d.line([x, cy, x + col_w2, cy], fill=RULE, width=1)

    # ---------- the day in numbers ----------
    stats = [
        ("+31%", "Nvidia shares"),
        ("+6.5%", "Nasdaq on Monday"),
        ("$3,661", "Gold, per ounce"),
        ("$44bn", "CrowdStrike deal"),
        ("258", "Democratic House seats"),
        ("24", "Killed in Indonesia fire"),
    ]
    ny = max(bottoms) + 16
    f_num = font(F_BOLD, 22)
    f_num_lab = font(F_REG, 11)
    d.rectangle([20, ny, W - 20, ny + 24], fill=NAVY)
    d.text((28, ny + 4), "THE DAY IN NUMBERS", font=font(F_BOLD, 13), fill=(255, 255, 255))
    cell_w = (W - 40) // len(stats)
    for i, (num, lab) in enumerate(stats):
        cx = 20 + i * cell_w
        d.rectangle([cx, ny + 24, cx + cell_w - 1, ny + 78], outline=RULE, width=1)
        d.text((cx + 10, ny + 30), num, font=f_num, fill=RED)
        d.text((cx + 10, ny + 58), lab, font=f_num_lab, fill=(60, 60, 60))
    print("columns end at", bottoms, "numbers strip at", ny)

    # ---------- footer ----------
    fy = 1000
    f_foot = font(F_REG, 11)
    d.text((20, fy), "Sources: Reuters · BBC · Wall Street Journal · The Hindu · Oxfam/CEOBS — the world's news of 24 November 2026.",
           font=f_foot, fill=(90, 90, 90))

    img.save(OUT, format="PNG", optimize=True)
    print("saved", OUT)


if __name__ == "__main__":
    draw()
