"""
generate_keyboard.py - Generates full QWERTY keyboard layout SVG:
assets/ui/keyboard/keyboard_layout.svg
Features:
- Distinct color-coding for 8 finger zones + thumbs spacebar
- Home row tactile bumps on F and J
- Dark mode aesthetic (slate gray keys, glowing cyan/orange/lime/purple/pink finger zones)
- Full ANSI 60% layout with secondary characters
- Clean XML and responsive viewBox
"""

import os
import xml.etree.ElementTree as ET

BASE_DIR = r"c:\Users\priya\OneDrive\Documents\Next Toppers\typefighter\assets\ui\keyboard"
os.makedirs(BASE_DIR, exist_ok=True)

# 8 Finger Zones + Thumbs Color Palette
ZONE_COLORS = {
    "pinky_l": {"name": "L-Pinky", "color": "#ff2a85", "light": "#ff70a6", "bg": "#3b071e"},
    "ring_l":   {"name": "L-Ring",  "color": "#8b5cf6", "light": "#c4b5fd", "bg": "#240b54"},
    "mid_l":    {"name": "L-Middle","color": "#06b6d4", "light": "#67e8f9", "bg": "#082f49"},
    "idx_l":    {"name": "L-Index", "color": "#10b981", "light": "#6ee7b7", "bg": "#022c22"},
    "thumb":    {"name": "Thumbs",  "color": "#f59e0b", "light": "#fde047", "bg": "#451a03"},
    "idx_r":    {"name": "R-Index", "color": "#84cc16", "light": "#bef264", "bg": "#1a2e05"},
    "mid_r":    {"name": "R-Middle","color": "#f97316", "light": "#fdba74", "bg": "#431407"},
    "ring_r":   {"name": "R-Ring",  "color": "#ef4444", "light": "#fca5a5", "bg": "#450a0a"},
    "pinky_r":  {"name": "R-Pinky", "color": "#ec4899", "light": "#f472b6", "bg": "#500724"},
}

# Key definitions for 5 rows
# Tuple format: (primary_label, secondary_label, unit_width, zone_key, is_home, has_bump)
ROWS = [
    # Row 0: Number row (Total 15u)
    [
        ("`", "~", 1.0, "pinky_l", False, False),
        ("1", "!", 1.0, "pinky_l", False, False),
        ("2", "@", 1.0, "ring_l", False, False),
        ("3", "#", 1.0, "mid_l", False, False),
        ("4", "$", 1.0, "idx_l", False, False),
        ("5", "%", 1.0, "idx_l", False, False),
        ("6", "^", 1.0, "idx_r", False, False),
        ("7", "&", 1.0, "idx_r", False, False),
        ("8", "*", 1.0, "mid_r", False, False),
        ("9", "(", 1.0, "ring_r", False, False),
        ("0", ")", 1.0, "pinky_r", False, False),
        ("-", "_", 1.0, "pinky_r", False, False),
        ("=", "+", 1.0, "pinky_r", False, False),
        ("BACKSPACE", "", 2.0, "pinky_r", False, False),
    ],
    # Row 1: QWERTY row (Total 15u)
    [
        ("TAB", "", 1.5, "pinky_l", False, False),
        ("Q", "", 1.0, "pinky_l", False, False),
        ("W", "", 1.0, "ring_l", False, False),
        ("E", "", 1.0, "mid_l", False, False),
        ("R", "", 1.0, "idx_l", False, False),
        ("T", "", 1.0, "idx_l", False, False),
        ("Y", "", 1.0, "idx_r", False, False),
        ("U", "", 1.0, "idx_r", False, False),
        ("I", "", 1.0, "mid_r", False, False),
        ("O", "", 1.0, "ring_r", False, False),
        ("P", "", 1.0, "pinky_r", False, False),
        ("[", "{", 1.0, "pinky_r", False, False),
        ("]", "}", 1.0, "pinky_r", False, False),
        ("\\", "|", 1.5, "pinky_r", False, False),
    ],
    # Row 2: Home row (Total 15u)
    [
        ("CAPS", "", 1.75, "pinky_l", False, False),
        ("A", "", 1.0, "pinky_l", True, False),
        ("S", "", 1.0, "ring_l", True, False),
        ("D", "", 1.0, "mid_l", True, False),
        ("F", "", 1.0, "idx_l", True, True),   # Tactile bump
        ("G", "", 1.0, "idx_l", False, False),
        ("H", "", 1.0, "idx_r", False, False),
        ("J", "", 1.0, "idx_r", True, True),   # Tactile bump
        ("K", "", 1.0, "mid_r", True, False),
        ("L", "", 1.0, "ring_r", True, False),
        (";", ":", 1.0, "pinky_r", True, False),
        ("'", "\"", 1.0, "pinky_r", False, False),
        ("ENTER", "", 2.25, "pinky_r", False, False),
    ],
    # Row 3: ZXCV row (Total 15u)
    [
        ("SHIFT", "", 2.25, "pinky_l", False, False),
        ("Z", "", 1.0, "pinky_l", False, False),
        ("X", "", 1.0, "ring_l", False, False),
        ("C", "", 1.0, "mid_l", False, False),
        ("V", "", 1.0, "idx_l", False, False),
        ("B", "", 1.0, "idx_l", False, False),
        ("N", "", 1.0, "idx_r", False, False),
        ("M", "", 1.0, "idx_r", False, False),
        (",", "<", 1.0, "mid_r", False, False),
        (".", ">", 1.0, "ring_r", False, False),
        ("/", "?", 1.0, "pinky_r", False, False),
        ("SHIFT", "", 2.75, "pinky_r", False, False),
    ],
    # Row 4: Space row (Total 15u)
    [
        ("CTRL", "", 1.25, "pinky_l", False, False),
        ("WIN", "", 1.25, "pinky_l", False, False),
        ("ALT", "", 1.25, "pinky_l", False, False),
        ("SPACE", "", 6.25, "thumb", True, False),
        ("ALT", "", 1.25, "thumb", False, False),
        ("WIN", "", 1.25, "pinky_r", False, False),
        ("MENU", "", 1.25, "pinky_r", False, False),
        ("CTRL", "", 1.25, "pinky_r", False, False),
    ],
]


def make_key_id(prim, r_idx):
    replacements = {
        ' ': '-', '`': 'tilde', ';': 'semicolon', ',': 'comma',
        '.': 'dot', '/': 'slash', '\\': 'backslash', '-': 'minus',
        '=': 'equals', "'": 'quote', '[': 'lbracket', ']': 'rbracket',
    }
    s = prim.lower()
    for k, v in replacements.items():
        s = s.replace(k, v)
    return f"key-{s}-{r_idx}"


def generate_keyboard_svg():
    # Dimensions
    U = 74.0       # unit pitch (key width + gap)
    GAP = 6.0      # gap between keys
    KEY_H = 68.0   # key height
    X0 = 88.0      # keyboard starting X
    Y0 = 68.0      # keyboard starting Y

    svg_keys = []

    for r_idx, row in enumerate(ROWS):
        cur_x = X0
        cur_y = Y0 + r_idx * U

        for key_data in row:
            prim, sec, u_w, zone, is_home, has_bump = key_data
            kw = u_w * U - GAP
            zinfo = ZONE_COLORS[zone]
            z_color = zinfo["color"]
            z_light = zinfo["light"]

            # Keycap ID
            key_id = make_key_id(prim, r_idx)

            # Labels and positioning
            cx = cur_x + kw / 2.0
            cy = cur_y + KEY_H / 2.0

            # Font size adjustments for modifier keys
            font_size = 18
            if len(prim) > 1:
                font_size = 12 if len(prim) > 4 else 14

            # XML-safe labels
            prim_xml = prim.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
            sec_xml = sec.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

            # Tactile bump element on F and J
            bump_svg = ""
            if has_bump:
                bump_svg = f'''
        <!-- Home Row Tactile Ridge Bump -->
        <rect x="{cx - 10:.1f}" y="{cur_y + 50:.1f}" width="20" height="3.5" rx="1.75"
              fill="#ffffff" stroke="{z_color}" stroke-width="1" filter="url(#bump-glow)"/>'''

            # Home row key subtle halo
            home_badge = ""
            if is_home and prim != "SPACE":
                home_badge = f'''
        <!-- Home Row Marker Circle -->
        <circle cx="{cur_x + kw - 12:.1f}" cy="{cur_y + 14:.1f}" r="3" fill="{z_color}" opacity="0.8"/>'''

            # Key Labels - perfectly centered
            if sec:
                labels_svg = f'''
        <text x="{cx:.1f}" y="{cur_y + 24:.1f}" font-family="'JetBrains Mono', monospace"
              font-size="11" font-weight="700" fill="#94a3b8" text-anchor="middle">{sec_xml}</text>
        <text x="{cx:.1f}" y="{cur_y + 46:.1f}" font-family="'JetBrains Mono', 'Chakra Petch', monospace, sans-serif"
              font-size="15" font-weight="800" fill="#f8fafc" text-anchor="middle">{prim_xml}</text>'''
            else:
                labels_svg = f'''
        <text x="{cx:.1f}" y="{cy + 5:.1f}" font-family="'JetBrains Mono', 'Chakra Petch', monospace, sans-serif"
              font-size="{font_size}" font-weight="800" fill="#f8fafc" text-anchor="middle">{prim_xml}</text>'''

            key_svg = f'''
      <!-- Key: {prim_xml} ({zone}) -->
      <g id="{key_id}" class="keycap zone-{zone}">
        <!-- Base Chamfer / Drop Shadow -->
        <rect x="{cur_x:.1f}" y="{cur_y:.1f}" width="{kw:.1f}" height="{KEY_H:.1f}" rx="8"
              fill="#0d111a" stroke="#1f293d" stroke-width="1.5"/>

        <!-- Keycap Top Slanted Face -->
        <rect x="{cur_x + 2:.1f}" y="{cur_y + 2:.1f}" width="{kw - 4:.1f}" height="{KEY_H - 8:.1f}" rx="6"
              fill="url(#key-face-grad)" stroke="#2d3748" stroke-width="1"/>

        <!-- Top Edge Specular Glint -->
        <line x1="{cur_x + 6:.1f}" y1="{cur_y + 3.5:.1f}" x2="{cur_x + kw - 6:.1f}" y2="{cur_y + 3.5:.1f}"
              stroke="#4a5568" stroke-width="1.2" stroke-linecap="round"/>

        <!-- Glowing Finger Zone Neon Underglow / Accent Bar -->
        <rect x="{cur_x + 8:.1f}" y="{cur_y + KEY_H - 12:.1f}" width="{kw - 16:.1f}" height="4" rx="2"
              fill="{z_color}" filter="url(#zone-glow)"/>

        {home_badge}
        {bump_svg}

        {labels_svg}
      </g>'''
            svg_keys.append(key_svg)
            cur_x += kw + GAP

    keys_markup = "\n".join(svg_keys)

    # Legend elements below the keyboard
    legend_items = []
    legend_zones = ["pinky_l", "ring_l", "mid_l", "idx_l", "thumb", "idx_r", "mid_r", "ring_r", "pinky_r"]
    leg_x0 = 88.0
    leg_step = 1104.0 / len(legend_zones)

    for i, zk in enumerate(legend_zones):
        zi = ZONE_COLORS[zk]
        lx = leg_x0 + i * leg_step
        lw = leg_step - 10.0
        legend_items.append(f'''
      <!-- Legend Pill: {zi['name']} -->
      <g transform="translate({lx:.1f}, 462)">
        <rect x="0" y="0" width="{lw:.1f}" height="28" rx="14" fill="#0d111a" stroke="{zi['color']}" stroke-width="1.5"/>
        <circle cx="14" cy="14" r="5" fill="{zi['color']}"/>
        <text x="{lw / 2.0 + 4:.1f}" y="18" font-family="'JetBrains Mono', sans-serif" font-size="11" font-weight="700"
              fill="{zi['light']}" text-anchor="middle">{zi['name']}</text>
      </g>''')
    legend_markup = "\n".join(legend_items)

    svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 520" width="100%" height="100%">
  <defs>
    <!-- Dark Mode Filters -->
    <filter id="chassis-shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="18" stdDeviation="28" flood-color="#000000" flood-opacity="0.95"/>
    </filter>
    <filter id="zone-glow" x="-20%" y="-40%" width="140%" height="180%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="bump-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="0" stdDeviation="2" flood-color="#ffffff" flood-opacity="0.8"/>
    </filter>

    <!-- Gradients -->
    <linearGradient id="chassis-bevel" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2d3748"/>
      <stop offset="30%" stop-color="#1a202c"/>
      <stop offset="70%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>

    <linearGradient id="chassis-plate" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#090d16"/>
      <stop offset="50%" stop-color="#060910"/>
      <stop offset="100%" stop-color="#04060b"/>
    </linearGradient>

    <linearGradient id="key-face-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#283244"/>
      <stop offset="45%" stop-color="#1e2636"/>
      <stop offset="100%" stop-color="#151b27"/>
    </linearGradient>
  </defs>

  <!-- Ambient Underglow Glow -->
  <rect x="58" y="38" width="1164" height="404" rx="26" fill="#0284c7" opacity="0.08" filter="url(#chassis-shadow)"/>

  <!-- MECHANICAL KEYBOARD CHASSIS -->
  <g filter="url(#chassis-shadow)">
    <!-- Outer Heavy Aluminum Housing -->
    <rect x="64" y="44" width="1152" height="394" rx="20"
          fill="url(#chassis-bevel)" stroke="#334155" stroke-width="3"/>

    <!-- Inner Keyplate Recess -->
    <rect x="76" y="56" width="1128" height="370" rx="14"
          fill="url(#chassis-plate)" stroke="#0f172a" stroke-width="2"/>

    <!-- Subtle Plate Screw Accents at 4 Corners -->
    <g fill="#475569" stroke="#1e293b" stroke-width="1">
      <circle cx="86" cy="66" r="3.5"/>
      <circle cx="1194" cy="66" r="3.5"/>
      <circle cx="86" cy="416" r="3.5"/>
      <circle cx="1194" cy="416" r="3.5"/>
    </g>
    <!-- Screws Cross Slot -->
    <g stroke="#0f172a" stroke-width="0.8">
      <line x1="84" y1="66" x2="88" y2="66"/><line x1="86" y1="64" x2="86" y2="68"/>
      <line x1="1192" y1="66" x2="1196" y2="66"/><line x1="1194" y1="64" x2="1194" y2="68"/>
      <line x1="84" y1="416" x2="88" y2="416"/><line x1="86" y1="414" x2="86" y2="418"/>
      <line x1="1192" y1="416" x2="1196" y2="416"/><line x1="1194" y1="414" x2="1194" y2="418"/>
    </g>
  </g>

  <!-- ALL 5 ROWS OF QWERTY KEYS -->
  <g id="keyboard-keys">
{keys_markup}
  </g>

  <!-- FINGER ZONE COLOR LEGEND BAR -->
  <g id="finger-zone-legend">
{legend_markup}
  </g>

  <!-- Header Title / Brand Logo in Chassis Header -->
  <g transform="translate(640, 32)">
    <text x="0" y="0" font-family="'Impact', 'Arial Black', sans-serif" font-size="16" font-weight="900"
          letter-spacing="6" fill="#64748b" text-anchor="middle">TYPEFIGHTER TOUCH-TYPING COMBAT ENGINE</text>
  </g>
</svg>'''

    filepath = os.path.join(BASE_DIR, "keyboard_layout.svg")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg_content.strip() + "\n")

    # XML validation
    try:
        ET.fromstring(svg_content)
        print(f"  [OK] keyboard_layout.svg created and validated (valid XML).")
    except ET.ParseError as e:
        print(f"  [ERROR] keyboard_layout.svg XML parse error: {e}")
        raise


if __name__ == "__main__":
    generate_keyboard_svg()
