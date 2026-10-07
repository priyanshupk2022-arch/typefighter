"""
generate_all_assets.py - Master generator and validator for all TypeFighter vector UI & badge assets.
Runs:
  - generate_ranks.py (7 ranks: D, C, B, A, S, SS, SSS)
  - generate_belts.py (10 martial arts belts: White through Grandmaster)
  - generate_streaks.py (3 streak badges: Fire 15, Lightning 30, Overdrive 50)
  - generate_keyboard.py (Full QWERTY dark-mode layout with 8 finger zones & home bumps)
  - generate_hands.py (Transparent home-row hands guide with individual finger IDs)
Validates all 22 SVG files using xml.etree.ElementTree.
"""

import os
import sys
import xml.etree.ElementTree as ET

# Ensure local asset directory is on path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from generate_ranks import generate_all_ranks
from generate_belts import generate_all_belts
from generate_streaks import generate_all_streaks
from generate_keyboard import generate_keyboard_svg
from generate_hands import generate_hands_svg

BASE_DIR = r"c:\Users\priya\OneDrive\Documents\Next Toppers\typefighter\assets"

EXPECTED_FILES = [
    # Ranks (7)
    os.path.join(BASE_DIR, "icons", "ranks", "rank_d.svg"),
    os.path.join(BASE_DIR, "icons", "ranks", "rank_c.svg"),
    os.path.join(BASE_DIR, "icons", "ranks", "rank_b.svg"),
    os.path.join(BASE_DIR, "icons", "ranks", "rank_a.svg"),
    os.path.join(BASE_DIR, "icons", "ranks", "rank_s.svg"),
    os.path.join(BASE_DIR, "icons", "ranks", "rank_ss.svg"),
    os.path.join(BASE_DIR, "icons", "ranks", "rank_sss.svg"),
    # Belts (10)
    os.path.join(BASE_DIR, "icons", "belts", "belt_white.svg"),
    os.path.join(BASE_DIR, "icons", "belts", "belt_yellow.svg"),
    os.path.join(BASE_DIR, "icons", "belts", "belt_orange.svg"),
    os.path.join(BASE_DIR, "icons", "belts", "belt_green.svg"),
    os.path.join(BASE_DIR, "icons", "belts", "belt_blue.svg"),
    os.path.join(BASE_DIR, "icons", "belts", "belt_purple.svg"),
    os.path.join(BASE_DIR, "icons", "belts", "belt_brown.svg"),
    os.path.join(BASE_DIR, "icons", "belts", "belt_red.svg"),
    os.path.join(BASE_DIR, "icons", "belts", "belt_black.svg"),
    os.path.join(BASE_DIR, "icons", "belts", "belt_grandmaster.svg"),
    # Streaks (3)
    os.path.join(BASE_DIR, "icons", "streaks", "streak_fire_15.svg"),
    os.path.join(BASE_DIR, "icons", "streaks", "streak_lightning_30.svg"),
    os.path.join(BASE_DIR, "icons", "streaks", "streak_overdrive_50.svg"),
    # UI Keyboard (1)
    os.path.join(BASE_DIR, "ui", "keyboard", "keyboard_layout.svg"),
    # UI Hands (1)
    os.path.join(BASE_DIR, "ui", "hands", "hands_guide.svg"),
]


def validate_all_svgs():
    print("=" * 70)
    print("VALIDATING ALL 22 GENERATED SVG FILES...")
    print("=" * 70)
    
    passed = 0
    failed = 0
    
    for fpath in EXPECTED_FILES:
        rel = os.path.relpath(fpath, BASE_DIR)
        if not os.path.exists(fpath):
            print(f"[MISSING] {rel} does not exist!")
            failed += 1
            continue
        
        file_size = os.path.getsize(fpath)
        try:
            tree = ET.parse(fpath)
            root = tree.getroot()
            tag = root.tag
            # Check for xmlns or svg root
            if not tag.endswith("svg"):
                print(f"[INVALID TAG] {rel} root tag is {tag}, expected svg")
                failed += 1
                continue
            
            view_box = root.attrib.get("viewBox", "Not defined")
            print(f"  [OK] {rel:<40} ({file_size:>6} bytes, viewBox='{view_box}')")
            passed += 1
        except ET.ParseError as err:
            print(f"  [ERROR] {rel}: {err}")
            failed += 1
            
    print("=" * 70)
    print(f"SUMMARY: {passed}/{len(EXPECTED_FILES)} SVGs VALIDATED SUCCESSFULLY. ({failed} failed)")
    print("=" * 70)
    if failed > 0:
        raise RuntimeError(f"Validation failed on {failed} files.")


def main():
    print("Starting TypeFighter Full Vector Asset Generation...\n")
    generate_all_ranks()
    print()
    generate_all_belts()
    print()
    generate_all_streaks()
    print()
    generate_keyboard_svg()
    print()
    generate_hands_svg()
    print()
    validate_all_svgs()


if __name__ == "__main__":
    main()
