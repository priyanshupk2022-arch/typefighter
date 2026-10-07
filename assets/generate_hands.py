"""
generate_hands.py - Generates transparent hands guide overlay SVG:
assets/ui/hands/hands_guide.svg
Features:
- Transparent overlay of Left and Right hands resting in home-row posture
- Fingers clearly distinguished and labeled:
  Left Pinky = A, Left Ring = S, Left Middle = D, Left Index = F, Left Thumb = Space
  Right Thumb = Space, Right Index = J, Right Middle = K, Right Ring = L, Right Pinky = ;
- Individual group IDs for every finger:
  finger-left-pinky, finger-left-ring, finger-left-middle, finger-left-index, finger-left-thumb,
  finger-right-thumb, finger-right-index, finger-right-middle, finger-right-ring, finger-right-pinky
- Holographic keycap badges and tactile bumps on F and J
- Cyber-ergonomic aesthetic matching dark mode keyboard zones
"""

import os
import xml.etree.ElementTree as ET

BASE_DIR = r"c:\Users\priya\OneDrive\Documents\Next Toppers\typefighter\assets\ui\hands"
os.makedirs(BASE_DIR, exist_ok=True)


def generate_finger_segment(fid, fname, key_label, fx, fy, bx, by, color, light_color, is_bump=False, is_thumb=False, bend_x=0):
    """
    Generates a beautifully articulated finger with 3 phalanges, fingertip pulse node,
    guide line, and floating 3D keycap badge.
    """
    # Key badge position (hovering above fingertip)
    if is_thumb:
        badge_y = fy - 50
        badge_x = fx + (16 if bend_x > 0 else -16)
    else:
        badge_y = fy - 58
        badge_x = fx

    bump_markup = ""
    if is_bump:
        bump_markup = f'''
        <!-- Tactile Bump on Home Key -->
        <rect x="{badge_x - 10:.1f}" y="{badge_y + 14:.1f}" width="20" height="3" rx="1.5"
              fill="#ffffff" stroke="{color}" stroke-width="0.8" filter="url(#node-glow)"/>'''

    # Segment joint coordinates
    mid_x = (bx + fx) / 2.0 + bend_x * 0.6
    mid_y = (by + fy) / 2.0
    top_x = (mid_x + fx) / 2.0 + bend_x * 0.3
    top_y = (mid_y + fy) / 2.0

    # Finger width tapers from base (32px) to tip (22px)
    w_base = 16.0
    w_mid = 14.0
    w_top = 12.0
    w_tip = 10.0

    # Normal vector for width
    dx = fx - bx
    dy = fy - by
    length = (dx*dx + dy*dy)**0.5
    if length == 0: length = 1
    nx = -dy / length
    ny = dx / length

    p1_l = f"{bx + nx * w_base:.1f},{by + ny * w_base:.1f}"
    p1_r = f"{bx - nx * w_base:.1f},{by - ny * w_base:.1f}"

    p2_l = f"{mid_x + nx * w_mid:.1f},{mid_y + ny * w_mid:.1f}"
    p2_r = f"{mid_x - nx * w_mid:.1f},{mid_y - ny * w_mid:.1f}"

    p3_l = f"{top_x + nx * w_top:.1f},{top_y + ny * w_top:.1f}"
    p3_r = f"{top_x - nx * w_top:.1f},{top_y - ny * w_top:.1f}"

    tip_l = f"{fx + nx * w_tip:.1f},{fy + ny * w_tip:.1f}"
    tip_r = f"{fx - nx * w_tip:.1f},{fy - ny * w_tip:.1f}"
    tip_cap = f"{fx:.1f},{fy - 8:.1f}"

    finger_path = f"M {p1_l} Q {p2_l} {p3_l} L {tip_l} Q {tip_cap} {tip_r} L {p3_r} Q {p2_r} {p1_r} Z"

    # Badge width
    bw = 64 if key_label == "SPACE" else 42
    bh = 38

    return f'''
    <!-- FINGER: {fname} [{key_label}] -->
    <g id="{fid}" class="finger-group" data-finger="{fname}" data-key="{key_label}">
      <!-- Finger Cyber Contour & Shading -->
      <path d="{finger_path}"
            fill="url(#finger-skin-grad)" stroke="{color}" stroke-width="2.5" opacity="0.92"/>

      <!-- Inner Holographic Energy Track -->
      <path d="M {bx},{by} Q {mid_x},{mid_y} {fx},{fy}"
            fill="none" stroke="{color}" stroke-width="1.5" stroke-dasharray="6,4" opacity="0.6"/>

      <!-- Knuckle Creases -->
      <line x1="{mid_x + nx * (w_mid - 2):.1f}" y1="{mid_y + ny * (w_mid - 2):.1f}"
            x2="{mid_x - nx * (w_mid - 2):.1f}" y2="{mid_y - ny * (w_mid - 2):.1f}"
            stroke="{color}" stroke-width="1.8" opacity="0.7"/>
      <line x1="{top_x + nx * (w_top - 2):.1f}" y1="{top_y + ny * (w_top - 2):.1f}"
            x2="{top_x - nx * (w_top - 2):.1f}" y2="{top_y - ny * (w_top - 2):.1f}"
            stroke="{color}" stroke-width="1.8" opacity="0.7"/>

      <!-- Fingertip Target Pulse Circles -->
      <g transform="translate({fx:.1f}, {fy:.1f})" filter="url(#node-glow)">
        <circle cx="0" cy="0" r="14" fill="{color}" opacity="0.15"/>
        <circle cx="0" cy="0" r="9" fill="none" stroke="{color}" stroke-width="1.5" stroke-dasharray="4,3"/>
        <circle cx="0" cy="0" r="5" fill="{color}"/>
        <circle cx="0" cy="0" r="2" fill="#ffffff"/>
      </g>

      <!-- Laser Guide Line to Hovering Keycap -->
      <line x1="{fx:.1f}" y1="{fy - 14:.1f}" x2="{badge_x:.1f}" y2="{badge_y + bh/2.0:.1f}"
            stroke="{color}" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.8"/>

      <!-- Floating 3D Home Keycap Badge -->
      <g transform="translate({badge_x - bw/2.0:.1f}, {badge_y - bh/2.0:.1f})" filter="url(#badge-shadow)">
        <!-- Keycap Shell -->
        <rect x="0" y="0" width="{bw}" height="{bh}" rx="8"
              fill="#090d16" stroke="{color}" stroke-width="2"/>
        <!-- Keycap Top Inset Face -->
        <rect x="2" y="2" width="{bw - 4}" height="{bh - 8}" rx="6"
              fill="#161f30" stroke="#283548" stroke-width="1"/>
        <!-- Top Highlight -->
        <line x1="5" y1="4" x2="{bw - 5}" y2="4" stroke="#4a5568" stroke-width="1" stroke-linecap="round"/>
        <!-- Bottom Zone Underglow -->
        <rect x="6" y="{bh - 5}" width="{bw - 12}" height="2.5" rx="1.2" fill="{color}"/>

        {bump_markup}

        <!-- Primary Key Character -->
        <text x="{bw/2.0:.1f}" y="{'21' if key_label != 'SPACE' else '20'}"
              font-family="'JetBrains Mono', 'Chakra Petch', monospace, sans-serif"
              font-size="{'18' if key_label != 'SPACE' else '12'}" font-weight="900"
              fill="#ffffff" text-anchor="middle">{key_label}</text>
      </g>

      <!-- Finger Name Label -->
      <text x="{badge_x:.1f}" y="{badge_y - bh/2.0 - 6:.1f}"
            font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700"
            fill="{light_color}" text-anchor="middle" letter-spacing="1">{fname}</text>
    </g>'''


def generate_hands_svg():
    # Left Hand Palm Silhouette Coordinates (offset down for breathing room)
    left_palm = """
    <!-- Left Hand Palm Contour -->
    <path d="M 230,570 C 220,500 220,440 240,400 C 255,370 290,365 335,365 C 380,365 415,380 430,420
             C 445,460 450,500 400,570 Z"
          fill="url(#palm-skin-grad)" stroke="#38bdf8" stroke-width="2" opacity="0.85"/>
    <!-- Wrist Band & Grid -->
    <path d="M 220,560 L 410,560 L 400,590 L 230,590 Z"
          fill="#0c1322" stroke="#1e293b" stroke-width="1.5"/>
    <text x="315" y="580" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700"
          fill="#64748b" text-anchor="middle" letter-spacing="3">LEFT HAND</text>
    <!-- Palm Lifeline Creases -->
    <path d="M 270,420 C 300,450 330,470 350,510" fill="none" stroke="#38bdf8" stroke-width="1.5" opacity="0.4"/>
    <path d="M 300,410 C 330,430 360,445 380,480" fill="none" stroke="#38bdf8" stroke-width="1.5" opacity="0.4"/>
    """

    # Right Hand Palm Silhouette Coordinates
    right_palm = """
    <!-- Right Hand Palm Contour -->
    <path d="M 970,570 C 980,500 980,440 960,400 C 945,370 910,365 865,365 C 820,365 785,380 770,420
             C 755,460 750,500 800,570 Z"
          fill="url(#palm-skin-grad)" stroke="#38bdf8" stroke-width="2" opacity="0.85"/>
    <!-- Wrist Band & Grid -->
    <path d="M 790,560 L 980,560 L 970,590 L 800,590 Z"
          fill="#0c1322" stroke="#1e293b" stroke-width="1.5"/>
    <text x="885" y="580" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700"
          fill="#64748b" text-anchor="middle" letter-spacing="3">RIGHT HAND</text>
    <!-- Palm Lifeline Creases -->
    <path d="M 930,420 C 900,450 870,470 850,510" fill="none" stroke="#38bdf8" stroke-width="1.5" opacity="0.4"/>
    <path d="M 900,410 C 870,430 840,445 820,480" fill="none" stroke="#38bdf8" stroke-width="1.5" opacity="0.4"/>
    """

    # Generate Individual Left Fingers
    # Left Pinky = A
    f_l_pinky = generate_finger_segment(
        fid="finger-left-pinky", fname="Pinky", key_label="A",
        fx=210, fy=190, bx=242, by=398,
        color="#ff2a85", light_color="#ff70a6", is_bump=False, is_thumb=False, bend_x=-14
    )
    # Left Ring = S
    f_l_ring = generate_finger_segment(
        fid="finger-left-ring", fname="Ring", key_label="S",
        fx=272, fy=155, bx=288, by=375,
        color="#8b5cf6", light_color="#c4b5fd", is_bump=False, is_thumb=False, bend_x=-6
    )
    # Left Middle = D
    f_l_mid = generate_finger_segment(
        fid="finger-left-middle", fname="Middle", key_label="D",
        fx=338, fy=135, bx=338, by=365,
        color="#06b6d4", light_color="#67e8f9", is_bump=False, is_thumb=False, bend_x=0
    )
    # Left Index = F (Tactile bump!)
    f_l_idx = generate_finger_segment(
        fid="finger-left-index", fname="Index", key_label="F",
        fx=402, fy=155, bx=388, by=375,
        color="#10b981", light_color="#6ee7b7", is_bump=True, is_thumb=False, bend_x=8
    )
    # Left Thumb = Space
    f_l_thumb = generate_finger_segment(
        fid="finger-left-thumb", fname="Thumb", key_label="SPACE",
        fx=490, fy=330, bx=420, by=445,
        color="#f59e0b", light_color="#fde047", is_bump=False, is_thumb=True, bend_x=24
    )

    # Generate Individual Right Fingers
    # Right Thumb = Space
    f_r_thumb = generate_finger_segment(
        fid="finger-right-thumb", fname="Thumb", key_label="SPACE",
        fx=710, fy=330, bx=780, by=445,
        color="#f59e0b", light_color="#fde047", is_bump=False, is_thumb=True, bend_x=-24
    )
    # Right Index = J (Tactile bump!)
    f_r_idx = generate_finger_segment(
        fid="finger-right-index", fname="Index", key_label="J",
        fx=798, fy=155, bx=812, by=375,
        color="#84cc16", light_color="#bef264", is_bump=True, is_thumb=False, bend_x=-8
    )
    # Right Middle = K
    f_r_mid = generate_finger_segment(
        fid="finger-right-middle", fname="Middle", key_label="K",
        fx=862, fy=135, bx=862, by=365,
        color="#f97316", light_color="#fdba74", is_bump=False, is_thumb=False, bend_x=0
    )
    # Right Ring = L
    f_r_ring = generate_finger_segment(
        fid="finger-right-ring", fname="Ring", key_label="L",
        fx=928, fy=155, bx=912, by=375,
        color="#ef4444", light_color="#fca5a5", is_bump=False, is_thumb=False, bend_x=6
    )
    # Right Pinky = ;
    f_r_pinky = generate_finger_segment(
        fid="finger-right-pinky", fname="Pinky", key_label=";",
        fx=990, fy=190, bx=958, by=398,
        color="#ec4899", light_color="#f472b6", is_bump=False, is_thumb=False, bend_x=14
    )

    svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 640" width="100%" height="100%">
  <defs>
    <!-- Filters -->
    <filter id="hand-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="node-glow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="4" result="glow"/>
      <feMerge>
        <feMergeNode in="glow"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="badge-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000000" flood-opacity="0.85"/>
    </filter>

    <!-- Gradients -->
    <linearGradient id="palm-skin-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1e293b" stop-opacity="0.75"/>
      <stop offset="50%" stop-color="#0f172a" stop-opacity="0.85"/>
      <stop offset="100%" stop-color="#050811" stop-opacity="0.95"/>
    </linearGradient>

    <linearGradient id="finger-skin-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#2a3850" stop-opacity="0.85"/>
      <stop offset="60%" stop-color="#162032" stop-opacity="0.88"/>
      <stop offset="100%" stop-color="#0d1422" stop-opacity="0.95"/>
    </linearGradient>
  </defs>

  <!-- Central Home Row Guidance Indicator Header -->
  <g transform="translate(600, 24)">
    <rect x="-140" y="-14" width="280" height="28" rx="14" fill="#090d16" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="-120" cy="0" r="3.5" fill="#38bdf8"/>
    <circle cx="120" cy="0" r="3.5" fill="#38bdf8"/>
    <text x="0" y="4" font-family="'Impact', 'Arial Black', sans-serif" font-size="12" font-weight="900"
          letter-spacing="4" fill="#f8fafc" text-anchor="middle">HOME ROW REST POSTURE</text>
  </g>

  <!-- Ambient Home Row Guideline Track -->
  <g opacity="0.35" stroke="#38bdf8" stroke-dasharray="6,6">
    <!-- Connecting Arc along home-row keypads -->
    <path d="M 210,132 Q 338,75 402,97" fill="none" stroke-width="1.5"/>
    <path d="M 798,97 Q 862,75 990,132" fill="none" stroke-width="1.5"/>
    <!-- Spacebar connecting bracket -->
    <path d="M 505,275 C 550,305 650,305 695,275" fill="none" stroke="#f59e0b" stroke-width="2"/>
  </g>

  <!-- LEFT HAND (id="hand-left") -->
  <g id="hand-left" class="hand-container">
    {left_palm}
    {f_l_pinky}
    {f_l_ring}
    {f_l_mid}
    {f_l_idx}
    {f_l_thumb}
  </g>

  <!-- RIGHT HAND (id="hand-right") -->
  <g id="hand-right" class="hand-container">
    {right_palm}
    {f_r_thumb}
    {f_r_idx}
    {f_r_mid}
    {f_r_ring}
    {f_r_pinky}
  </g>
</svg>'''

    filepath = os.path.join(BASE_DIR, "hands_guide.svg")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg_content.strip() + "\n")

    # XML validation
    try:
        ET.fromstring(svg_content)
        print(f"  [OK] hands_guide.svg created and validated (valid XML).")
    except ET.ParseError as e:
        print(f"  [ERROR] hands_guide.svg XML parse error: {e}")
        raise


if __name__ == "__main__":
    generate_hands_svg()
