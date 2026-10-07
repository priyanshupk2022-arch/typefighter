"""
TypeFighter Vector Asset Generator
Generates clean, professional, high-resolution SVG asset files for TypeFighter:
1. Ranks: rank_d.svg, rank_c.svg, rank_b.svg, rank_a.svg, rank_s.svg, rank_ss.svg, rank_sss.svg
2. Belts: belt_white.svg, belt_yellow.svg, belt_orange.svg, belt_green.svg, belt_blue.svg,
          belt_purple.svg, belt_brown.svg, belt_red.svg, belt_black.svg, belt_grandmaster.svg
3. Streaks: streak_fire_15.svg, streak_lightning_30.svg, streak_overdrive_50.svg
4. Keyboard: keyboard_layout.svg
5. Hands: hands_guide.svg
"""

import os
import math
import xml.etree.ElementTree as ET

BASE_DIR = r"c:\Users\priya\OneDrive\Documents\Next Toppers\typefighter\assets"
RANKS_DIR = os.path.join(BASE_DIR, "icons", "ranks")
BELTS_DIR = os.path.join(BASE_DIR, "icons", "belts")
STREAKS_DIR = os.path.join(BASE_DIR, "icons", "streaks")
KEYBOARD_DIR = os.path.join(BASE_DIR, "ui", "keyboard")
HANDS_DIR = os.path.join(BASE_DIR, "ui", "hands")

for d in [RANKS_DIR, BELTS_DIR, STREAKS_DIR, KEYBOARD_DIR, HANDS_DIR]:
    os.makedirs(d, exist_ok=True)

print("Directories initialized successfully.")
