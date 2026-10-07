"""
generate_belts.py - Generates martial arts belt vector icons:
belt_white.svg, belt_yellow.svg, belt_orange.svg, belt_green.svg, belt_blue.svg,
belt_purple.svg, belt_brown.svg, belt_red.svg, belt_black.svg, belt_grandmaster.svg
"""

import os
import xml.etree.ElementTree as ET

BASE_DIR = r"c:\Users\priya\OneDrive\Documents\Next Toppers\typefighter\assets\icons\belts"
os.makedirs(BASE_DIR, exist_ok=True)

# Dragon embroidery path for black and grandmaster belts
DRAGON_PATH_LEFT_TAIL = """
<!-- Gold Dragon Embroidery Body -->
<g class="dragon-embroidery" filter="url(#gold-shimmer)">
  <!-- Dragon Coiled Spine -->
  <path d="M 218,270 C 205,285 192,295 198,312 C 204,330 226,335 222,352 C 218,368 196,380 190,400 C 185,415 188,425 186,432"
        fill="none" stroke="url(#dragon-gold-thread)" stroke-width="6" stroke-linecap="round"/>
  <!-- Dorsal Flame Spines -->
  <path d="M 218,270 L 225,264 L 222,274 M 205,285 L 214,282 L 208,290 M 198,312 L 190,308 L 196,318
           M 226,335 L 235,332 L 228,340 M 222,352 L 230,356 L 220,360 M 196,380 L 188,382 L 194,388"
        stroke="url(#dragon-gold-light)" stroke-width="2.5" fill="none"/>
  <!-- Dragon Scales Hatching -->
  <path d="M 212,278 L 222,282 M 202,298 L 212,302 M 210,324 L 220,328 M 212,345 L 222,349 M 198,368 L 208,372 M 190,392 L 200,396"
        stroke="#fde047" stroke-width="1.5" stroke-linecap="round" opacity="0.85"/>
  <!-- Dragon Front Claws -->
  <path d="M 200,314 L 182,318 M 182,318 L 176,314 M 182,318 L 176,322 M 182,318 L 178,326"
        stroke="url(#dragon-gold-thread)" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Dragon Rear Claws -->
  <path d="M 220,360 L 236,368 M 236,368 L 242,364 M 236,368 L 244,370 M 236,368 L 240,376"
        stroke="url(#dragon-gold-thread)" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Dragon Head & Whiskers -->
  <g transform="translate(216, 266)">
    <!-- Horn / Antler -->
    <path d="M 0,0 L -6,-12 L -12,-16 M -6,-12 L -2,-18" stroke="url(#dragon-gold-light)" stroke-width="2" fill="none"/>
    <!-- Head Snout -->
    <path d="M -4,-2 C 4,-6 14,-2 14,4 C 14,8 8,10 0,6 Z" fill="url(#dragon-gold-thread)" stroke="#78350f" stroke-width="1"/>
    <!-- Flaming Whiskers -->
    <path d="M 12,2 C 18,-4 26,-2 28,-8 M 12,6 C 18,8 24,6 26,12" stroke="url(#dragon-gold-light)" stroke-width="1.8" fill="none"/>
    <!-- Ruby Eye -->
    <circle cx="2" cy="0" r="1.8" fill="#ef4444" stroke="#ffffff" stroke-width="0.5"/>
  </g>
</g>
"""

DRAGON_PATH_RIGHT_TAIL = """
<!-- Gold Dragon Embroidery Body (Right Tail) -->
<g class="dragon-embroidery-right" filter="url(#gold-shimmer)">
  <!-- Dragon Coiled Spine -->
  <path d="M 294,270 C 307,285 320,295 314,312 C 308,330 286,335 290,352 C 294,368 316,380 322,400 C 327,415 324,425 326,432"
        fill="none" stroke="url(#dragon-gold-thread)" stroke-width="6" stroke-linecap="round"/>
  <!-- Dorsal Flame Spines -->
  <path d="M 294,270 L 287,264 L 290,274 M 307,285 L 298,282 L 304,290 M 314,312 L 322,308 L 316,318
           M 286,335 L 277,332 L 284,340 M 290,352 L 282,356 L 292,360 M 316,380 L 324,382 L 318,388"
        stroke="url(#dragon-gold-light)" stroke-width="2.5" fill="none"/>
  <!-- Dragon Scales Hatching -->
  <path d="M 300,278 L 290,282 M 310,298 L 300,302 M 302,324 L 292,328 M 300,345 L 290,349 M 314,368 L 304,372 M 322,392 L 312,396"
        stroke="#fde047" stroke-width="1.5" stroke-linecap="round" opacity="0.85"/>
  <!-- Dragon Front Claws -->
  <path d="M 312,314 L 330,318 M 330,318 L 336,314 M 330,318 L 336,322 M 330,318 L 334,326"
        stroke="url(#dragon-gold-thread)" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Dragon Rear Claws -->
  <path d="M 292,360 L 276,368 M 276,368 L 270,364 M 276,368 L 268,370 M 276,368 L 272,376"
        stroke="url(#dragon-gold-thread)" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Dragon Head & Whiskers -->
  <g transform="translate(296, 266)">
    <!-- Horn / Antler -->
    <path d="M 0,0 L 6,-12 L 12,-16 M 6,-12 L 2,-18" stroke="url(#dragon-gold-light)" stroke-width="2" fill="none"/>
    <!-- Head Snout -->
    <path d="M 4,-2 C -4,-6 -14,-2 -14,4 C -14,8 -8,10 0,6 Z" fill="url(#dragon-gold-thread)" stroke="#78350f" stroke-width="1"/>
    <!-- Flaming Whiskers -->
    <path d="M -12,2 C -18,-4 -26,-2 -28,-8 M -12,6 C -18,8 -24,6 -26,12" stroke="url(#dragon-gold-light)" stroke-width="1.8" fill="none"/>
    <!-- Ruby Eye -->
    <circle cx="-2" cy="0" r="1.8" fill="#ef4444" stroke="#ffffff" stroke-width="0.5"/>
  </g>
</g>
"""

BELT_CONFIGS = [
    {
        "id": "belt_white",
        "name": "WHITE BELT",
        "rank_title": "10th Kyu - Beginner",
        "base_light": "#ffffff",
        "base_mid": "#f1f3f5",
        "base_dark": "#dee2e6",
        "shadow": "#adb5bd",
        "stroke": "#ced4da",
        "stitch": "#adb5bd",
        "has_dragon": False,
        "is_grandmaster": False,
    },
    {
        "id": "belt_yellow",
        "name": "YELLOW BELT",
        "rank_title": "9th Kyu - Novice",
        "base_light": "#fff59d",
        "base_mid": "#ffd600",
        "base_dark": "#ffab00",
        "shadow": "#e65100",
        "stroke": "#ff8f00",
        "stitch": "#f57f17",
        "has_dragon": False,
        "is_grandmaster": False,
    },
    {
        "id": "belt_orange",
        "name": "ORANGE BELT",
        "rank_title": "8th Kyu - Apprentice",
        "base_light": "#ffb74d",
        "base_mid": "#ff6d00",
        "base_dark": "#e65100",
        "shadow": "#bf360c",
        "stroke": "#d84315",
        "stitch": "#bf360c",
        "has_dragon": False,
        "is_grandmaster": False,
    },
    {
        "id": "belt_green",
        "name": "GREEN BELT",
        "rank_title": "6th Kyu - Intermediate",
        "base_light": "#69f0ae",
        "base_mid": "#00c853",
        "base_dark": "#1b5e20",
        "shadow": "#0b3d14",
        "stroke": "#00701a",
        "stitch": "#054f15",
        "has_dragon": False,
        "is_grandmaster": False,
    },
    {
        "id": "belt_blue",
        "name": "BLUE BELT",
        "rank_title": "4th Kyu - Advanced",
        "base_light": "#82b1ff",
        "base_mid": "#2979ff",
        "base_dark": "#0d47a1",
        "shadow": "#002171",
        "stroke": "#1565c0",
        "stitch": "#0d3b82",
        "has_dragon": False,
        "is_grandmaster": False,
    },
    {
        "id": "belt_purple",
        "name": "PURPLE BELT",
        "rank_title": "2nd Kyu - Senior",
        "base_light": "#ea80fc",
        "base_mid": "#aa00ff",
        "base_dark": "#4a148c",
        "shadow": "#240046",
        "stroke": "#7b1fa2",
        "stitch": "#4a0072",
        "has_dragon": False,
        "is_grandmaster": False,
    },
    {
        "id": "belt_brown",
        "name": "BROWN BELT",
        "rank_title": "1st Kyu - Expert",
        "base_light": "#bcaaa4",
        "base_mid": "#8d6e63",
        "base_dark": "#4e342e",
        "shadow": "#271410",
        "stroke": "#3e2723",
        "stitch": "#321911",
        "has_dragon": False,
        "is_grandmaster": False,
    },
    {
        "id": "belt_red",
        "name": "RED BELT",
        "rank_title": "Candidate Master",
        "base_light": "#ff8a80",
        "base_mid": "#d50000",
        "base_dark": "#b71c1c",
        "shadow": "#7f0000",
        "stroke": "#8e0000",
        "stitch": "#630000",
        "has_dragon": False,
        "is_grandmaster": False,
    },
    {
        "id": "belt_black",
        "name": "BLACK BELT",
        "rank_title": "1st Dan - Master",
        "base_light": "#424242",
        "base_mid": "#212121",
        "base_dark": "#121212",
        "shadow": "#000000",
        "stroke": "#303030",
        "stitch": "#0d0d0d",
        "has_dragon": True,
        "is_grandmaster": False,
    },
    {
        "id": "belt_grandmaster",
        "name": "GRANDMASTER BELT",
        "rank_title": "10th Dan - Grandmaster",
        "base_light": "#d50000",
        "base_mid": "#1a1a1a",
        "base_dark": "#0a0a0a",
        "shadow": "#000000",
        "stroke": "#ffd700",
        "stitch": "#ffd700",
        "has_dragon": True,
        "is_grandmaster": True,
    },
]


def generate_belt_svg(cfg):
    bid = cfg["id"]
    name = cfg["name"]
    rank_title = cfg["rank_title"]
    base_l = cfg["base_light"]
    base_m = cfg["base_mid"]
    base_d = cfg["base_dark"]
    shadow = cfg["shadow"]
    stroke = cfg["stroke"]
    stitch = cfg["stitch"]
    has_dragon = cfg["has_dragon"]
    is_gm = cfg["is_grandmaster"]

    # Special backgrounds & accents
    bg_gradient = f'''
    <radialGradient id="{bid}-bg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{base_m}" stop-opacity="0.25"/>
      <stop offset="60%" stop-color="{base_d}" stop-opacity="0.1"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>
    '''
    if is_gm:
        bg_gradient = '''
    <radialGradient id="belt_grandmaster-bg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffd700" stop-opacity="0.35"/>
      <stop offset="35%" stop-color="#d50000" stop-opacity="0.25"/>
      <stop offset="70%" stop-color="#121212" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>
    '''

    gold_defs = '''
    <linearGradient id="dragon-gold-thread" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="20%" stop-color="#fef08a"/>
      <stop offset="50%" stop-color="#f59e0b"/>
      <stop offset="80%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#78350f"/>
    </linearGradient>
    <linearGradient id="dragon-gold-light" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fffbeb"/>
      <stop offset="100%" stop-color="#fde047"/>
    </linearGradient>
    <filter id="gold-shimmer" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="1" stdDeviation="2" flood-color="#ffd700" flood-opacity="0.6"/>
    </filter>
    ''' if (has_dragon or is_gm) else ""

    gm_aura = '''
    <!-- Grandmaster Aura Rays -->
    <g stroke="#fde047" stroke-width="1.5" opacity="0.35">
      <line x1="256" y1="210" x2="256" y2="30"/>
      <line x1="256" y1="210" x2="436" y2="70"/>
      <line x1="256" y1="210" x2="476" y2="210"/>
      <line x1="256" y1="210" x2="76" y2="70"/>
      <line x1="256" y1="210" x2="36" y2="210"/>
      <line x1="256" y1="210" x2="116" y2="380"/>
      <line x1="256" y1="210" x2="396" y2="380"/>
    </g>
    <!-- Floating Gold Dust Particles -->
    <g fill="#fde047" opacity="0.75">
      <circle cx="160" cy="140" r="3"/>
      <circle cx="352" cy="140" r="2.5"/>
      <circle cx="110" cy="270" r="2.5"/>
      <circle cx="400" cy="270" r="3"/>
      <circle cx="150" cy="380" r="2"/>
      <circle cx="360" cy="380" r="2.5"/>
      <circle cx="256" cy="110" r="3.5"/>
    </g>
    ''' if is_gm else ""

    # Belt Loop Fill: If Grandmaster, alternating red & black panels
    loop_fill = f'fill="url(#{bid}-loop-grad)"'
    knot_fill = f'fill="url(#{bid}-knot-grad)"'
    ltail_fill = f'fill="url(#{bid}-ltail-grad)"'
    rtail_fill = f'fill="url(#{bid}-rtail-grad)"'

    # Dan Rank Bar on Right Tail
    dan_rank_bar = ""
    if bid == "belt_black":
        dan_rank_bar = '''
    <!-- Dan Rank Sleeve Bar (4th Dan Master) -->
    <g transform="translate(0, 0)">
      <!-- Red Rank Patch -->
      <polygon points="320,344 350,336 339,396 308,406" fill="#d50000" stroke="#800000" stroke-width="1.5"/>
      <!-- Gold Dan Bars -->
      <line x1="324" y1="352" x2="346" y2="346" stroke="#ffd700" stroke-width="3"/>
      <line x1="321" y1="363" x2="343" y2="357" stroke="#ffd700" stroke-width="3"/>
      <line x1="318" y1="374" x2="340" y2="368" stroke="#ffd700" stroke-width="3"/>
      <line x1="315" y1="385" x2="337" y2="379" stroke="#ffd700" stroke-width="3"/>
    </g>
    '''
    elif is_gm:
        dan_rank_bar = '''
    <!-- Grandmaster 10th Dan Sleeve Bar (Red & Gold) -->
    <g transform="translate(0, 0)">
      <!-- Red Rank Patch on Right Tail -->
      <polygon points="318,326 352,316 338,416 304,428" fill="#b71c1c" stroke="#ffd700" stroke-width="2"/>
      <!-- 10 Gold Grandmaster Stripes -->
      <line x1="323" y1="334" x2="347" y2="327" stroke="#ffd700" stroke-width="2.5"/>
      <line x1="321" y1="342" x2="345" y2="335" stroke="#ffd700" stroke-width="2.5"/>
      <line x1="319" y1="350" x2="343" y2="343" stroke="#ffd700" stroke-width="2.5"/>
      <line x1="317" y1="358" x2="341" y2="351" stroke="#ffd700" stroke-width="2.5"/>
      <line x1="315" y1="366" x2="339" y2="359" stroke="#ffd700" stroke-width="2.5"/>
      <line x1="313" y1="374" x2="337" y2="367" stroke="#ffd700" stroke-width="2.5"/>
      <line x1="311" y1="382" x2="335" y2="375" stroke="#ffd700" stroke-width="2.5"/>
      <line x1="309" y1="390" x2="333" y2="383" stroke="#ffd700" stroke-width="2.5"/>
      <line x1="307" y1="398" x2="331" y2="391" stroke="#ffd700" stroke-width="2.5"/>
      <line x1="305" y1="406" x2="329" y2="399" stroke="#ffd700" stroke-width="2.5"/>
    </g>
    '''

    # Knot medallion for Grandmaster
    gm_knot_crest = ""
    if is_gm:
        gm_knot_crest = '''
    <!-- Grandmaster Knot Medallion: Gilded Imperial Dragon Crest with Radiant Ruby -->
    <g transform="translate(256, 212)" filter="url(#gold-shimmer)">
      <!-- Outer Gold Filigree Ring -->
      <circle cx="0" cy="0" r="26" fill="#121212" stroke="#ffd700" stroke-width="3"/>
      <circle cx="0" cy="0" r="22" fill="none" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4,2"/>
      <!-- 8 Golden Sun Teeth -->
      <path d="M 0,-26 L 3,-22 L -3,-22 Z M 0,26 L 3,22 L -3,22 Z M -26,0 L -22,3 L -22,-3 Z M 26,0 L 22,3 L 22,-3 Z" fill="#ffd700"/>
      <!-- Inner Ruby Core Gem -->
      <circle cx="0" cy="0" r="14" fill="#d50000" stroke="#fef08a" stroke-width="2"/>
      <circle cx="-4" cy="-4" r="4" fill="#ffffff" opacity="0.7"/>
    </g>
    '''

    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <defs>
    <!-- Master Filters -->
    <filter id="{bid}-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#000000" flood-opacity="0.8"/>
    </filter>
    <filter id="{bid}-soft-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="0" stdDeviation="10" flood-color="{base_m}" flood-opacity="0.5"/>
    </filter>

    <!-- Belt Gradients -->
    {bg_gradient}

    <linearGradient id="{bid}-loop-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{base_l}"/>
      <stop offset="35%" stop-color="{base_m}"/>
      <stop offset="75%" stop-color="{base_d}"/>
      <stop offset="100%" stop-color="{shadow}"/>
    </linearGradient>

    <linearGradient id="{bid}-knot-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{base_l}"/>
      <stop offset="40%" stop-color="{base_m}"/>
      <stop offset="85%" stop-color="{base_d}"/>
      <stop offset="100%" stop-color="{shadow}"/>
    </linearGradient>

    <linearGradient id="{bid}-ltail-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{base_l}"/>
      <stop offset="30%" stop-color="{base_m}"/>
      <stop offset="75%" stop-color="{base_d}"/>
      <stop offset="100%" stop-color="{shadow}"/>
    </linearGradient>

    <linearGradient id="{bid}-rtail-grad" x1="100%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{base_l}"/>
      <stop offset="30%" stop-color="{base_m}"/>
      <stop offset="75%" stop-color="{base_d}"/>
      <stop offset="100%" stop-color="{shadow}"/>
    </linearGradient>

    {gold_defs}
  </defs>

  <!-- Ambient Radial Glow -->
  <circle cx="256" cy="256" r="230" fill="url(#{bid}-bg)"/>

  {gm_aura}

  <!-- Master Belt Assembly -->
  <g filter="url(#{bid}-shadow)">

    <!-- 1. BACK LOOP (Inside of the Belt Wrap) -->
    <path d="M 100,210 C 100,165 160,140 256,140 C 352,140 412,165 412,210 C 412,225 390,238 360,244
             L 354,215 C 380,205 388,190 388,185 C 388,165 330,152 256,152 C 182,152 124,165 124,185
             C 124,190 132,205 158,215 L 152,244 C 122,238 100,225 100,210 Z"
          fill="{shadow}" stroke="{stroke}" stroke-width="1.5" opacity="0.6"/>

    <!-- 2. FRONT BELT LOOP (Waist Band Wrap) -->
    <path d="M 88,206 C 88,172 150,158 256,158 C 362,158 424,172 424,206 C 424,244 362,258 256,258 C 150,258 88,244 88,206 Z"
          {loop_fill} stroke="{stroke}" stroke-width="2.5"/>

    <!-- Front Loop Highlight & Stitch Tracks -->
    <!-- Top Highlight -->
    <path d="M 104,198 C 120,172 174,162 256,162 C 338,162 392,172 408,198"
          fill="none" stroke="{base_l}" stroke-width="2" opacity="0.8"/>
    <!-- 4 Longitudinal Stitch Lines across the Belt Band -->
    <path d="M 96,192 C 126,170 180,164 256,164 C 332,164 386,170 416,192"
          fill="none" stroke="{stitch}" stroke-width="1.2" stroke-dasharray="7,4" opacity="0.7"/>
    <path d="M 92,202 C 124,180 180,174 256,174 C 332,174 388,180 420,202"
          fill="none" stroke="{stitch}" stroke-width="1.2" stroke-dasharray="7,4" opacity="0.7"/>
    <path d="M 92,212 C 124,232 180,240 256,240 C 332,240 388,232 420,212"
          fill="none" stroke="{stitch}" stroke-width="1.2" stroke-dasharray="7,4" opacity="0.7"/>
    <path d="M 96,222 C 126,242 180,248 256,248 C 332,248 386,242 416,222"
          fill="none" stroke="{stitch}" stroke-width="1.2" stroke-dasharray="7,4" opacity="0.7"/>

    <!-- 3. HANGING BELT TAILS (Descending Ends) -->
    <!-- LEFT TAIL -->
    <g class="belt-left-tail">
      <!-- Main Left Tail Fabric -->
      <path d="M 234,230 C 220,285 192,355 164,430 L 206,446 C 232,374 258,300 268,242 Z"
            {ltail_fill} stroke="{stroke}" stroke-width="2"/>
      <!-- Angled Cut Tip Bottom Hem -->
      <line x1="164" y1="430" x2="206" y2="446" stroke="{base_l}" stroke-width="2.5"/>
      <!-- 4 Longitudinal Stitch Tracks down Left Tail -->
      <path d="M 240,233 C 227,288 200,358 172,433" fill="none" stroke="{stitch}" stroke-width="1.2" stroke-dasharray="7,4" opacity="0.75"/>
      <path d="M 248,236 C 235,291 208,361 182,437" fill="none" stroke="{stitch}" stroke-width="1.2" stroke-dasharray="7,4" opacity="0.75"/>
      <path d="M 256,239 C 243,294 216,364 192,441" fill="none" stroke="{stitch}" stroke-width="1.2" stroke-dasharray="7,4" opacity="0.75"/>
      <path d="M 264,242 C 251,297 224,367 200,444" fill="none" stroke="{stitch}" stroke-width="1.2" stroke-dasharray="7,4" opacity="0.75"/>

      <!-- Dragon Embroidery on Left Tail if enabled -->
      {DRAGON_PATH_LEFT_TAIL if (has_dragon or is_gm) else ""}
    </g>

    <!-- RIGHT TAIL -->
    <g class="belt-right-tail">
      <!-- Main Right Tail Fabric -->
      <path d="M 248,242 C 258,300 284,374 310,446 L 352,430 C 324,355 296,285 282,230 Z"
            {rtail_fill} stroke="{stroke}" stroke-width="2"/>
      <!-- Angled Cut Tip Bottom Hem -->
      <line x1="310" y1="446" x2="352" y2="430" stroke="{base_l}" stroke-width="2.5"/>
      <!-- 4 Longitudinal Stitch Tracks down Right Tail -->
      <path d="M 254,242 C 264,297 291,367 316,444" fill="none" stroke="{stitch}" stroke-width="1.2" stroke-dasharray="7,4" opacity="0.75"/>
      <path d="M 262,239 C 272,294 299,364 324,441" fill="none" stroke="{stitch}" stroke-width="1.2" stroke-dasharray="7,4" opacity="0.75"/>
      <path d="M 270,236 C 280,291 307,361 334,437" fill="none" stroke="{stitch}" stroke-width="1.2" stroke-dasharray="7,4" opacity="0.75"/>
      <path d="M 278,233 C 288,288 315,358 344,433" fill="none" stroke="{stitch}" stroke-width="1.2" stroke-dasharray="7,4" opacity="0.75"/>

      <!-- Dan Rank Sleeve Bar on Right Tail -->
      {dan_rank_bar}

      <!-- Dragon Embroidery on Right Tail if Grandmaster -->
      {DRAGON_PATH_RIGHT_TAIL if is_gm else ""}
    </g>

    <!-- 4. TRADITIONAL MARTIAL ARTS SQUARE KNOT (Musubi) -->
    <!-- Knot Left Fold -->
    <path d="M 204,196 C 220,186 238,190 240,214 C 238,236 218,246 200,234 Z"
          fill="{base_d}" stroke="{stroke}" stroke-width="2"/>
    <!-- Knot Right Fold -->
    <path d="M 308,196 C 292,186 274,190 272,214 C 274,236 294,246 312,234 Z"
          fill="{base_d}" stroke="{stroke}" stroke-width="2"/>

    <!-- Center Cinch Wrap (Vertical Knot Core) -->
    <path d="M 234,178 C 248,172 264,172 278,178 L 284,244 C 268,248 244,248 228,244 Z"
          {knot_fill} stroke="{stroke}" stroke-width="2.5"/>

    <!-- Knot Tension Creases -->
    <path d="M 240,184 C 252,192 260,192 272,184" fill="none" stroke="{shadow}" stroke-width="2" opacity="0.6"/>
    <path d="M 238,236 C 252,230 262,230 274,236" fill="none" stroke="{shadow}" stroke-width="2" opacity="0.6"/>
    <line x1="236" y1="180" x2="280" y2="180" stroke="{base_l}" stroke-width="2" opacity="0.8"/>

    <!-- Grandmaster Knot Medallion -->
    {gm_knot_crest}
  </g>

  <!-- Title & Rank Badge Label at Bottom -->
  <g transform="translate(0, 460)">
    <rect x="136" y="-6" width="240" height="34" rx="17" fill="#111317" stroke="{base_m}" stroke-width="2"/>
    <text x="256" y="16" font-family="'Impact', 'Arial Black', sans-serif" font-size="16" font-weight="900"
          letter-spacing="3" fill="{base_l if bid != 'belt_white' else '#f8f9fa'}" text-anchor="middle">{name}</text>
  </g>
</svg>'''
    return svg


def generate_all_belts():
    print(f"Generating {len(BELT_CONFIGS)} belt icons in {BASE_DIR}...")
    for cfg in BELT_CONFIGS:
        filename = f"{cfg['id']}.svg"
        content = generate_belt_svg(cfg)
        filepath = os.path.join(BASE_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        
        # XML validation
        try:
            ET.fromstring(content)
            print(f"  [OK] {filename} created and validated (valid XML).")
        except ET.ParseError as e:
            print(f"  [ERROR] {filename} XML parse error: {e}")
            raise


if __name__ == "__main__":
    generate_all_belts()
