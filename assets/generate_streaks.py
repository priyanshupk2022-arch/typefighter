"""
generate_streaks.py - Generates fighting game combo streak badges:
streak_fire_15.svg, streak_lightning_30.svg, streak_overdrive_50.svg
"""

import os
import xml.etree.ElementTree as ET

BASE_DIR = r"c:\Users\priya\OneDrive\Documents\Next Toppers\typefighter\assets\icons\streaks"
os.makedirs(BASE_DIR, exist_ok=True)


def get_streak_fire_15_svg():
    """15 Streak: Flames Aura Icon / Fiery Combustion Fighting Crest."""
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <defs>
    <!-- Filters -->
    <filter id="fire-heavy-shadow" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="16" stdDeviation="22" flood-color="#000000" flood-opacity="0.95"/>
    </filter>
    <filter id="flame-blur-glow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="8" result="blur1"/>
      <feGaussianBlur stdDeviation="18" result="blur2"/>
      <feMerge>
        <feMergeNode in="blur2"/>
        <feMergeNode in="blur1"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="ember-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="4" result="glow"/>
      <feMerge>
        <feMergeNode in="glow"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <!-- Gradients -->
    <radialGradient id="fire-thermal-core" cx="50%" cy="55%" r="55%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="1"/>
      <stop offset="20%" stop-color="#fde047" stop-opacity="0.9"/>
      <stop offset="45%" stop-color="#f97316" stop-opacity="0.7"/>
      <stop offset="70%" stop-color="#dc2626" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#140202" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="outer-flame" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#7f1d1d"/>
      <stop offset="35%" stop-color="#b91c1c"/>
      <stop offset="70%" stop-color="#dc2626"/>
      <stop offset="100%" stop-color="#f97316"/>
    </linearGradient>

    <linearGradient id="mid-flame" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#ea580c"/>
      <stop offset="40%" stop-color="#f97316"/>
      <stop offset="75%" stop-color="#fb923c"/>
      <stop offset="100%" stop-color="#fde047"/>
    </linearGradient>

    <linearGradient id="core-flame" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#facc15"/>
      <stop offset="50%" stop-color="#fef08a"/>
      <stop offset="90%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#ffffff"/>
    </linearGradient>

    <linearGradient id="obsidian-badge" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3f1303"/>
      <stop offset="30%" stop-color="#1c0702"/>
      <stop offset="70%" stop-color="#0a0201"/>
      <stop offset="100%" stop-color="#2a0802"/>
    </linearGradient>

    <linearGradient id="fire-gold-bevel" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="25%" stop-color="#fde047"/>
      <stop offset="60%" stop-color="#f97316"/>
      <stop offset="100%" stop-color="#7c2d12"/>
    </linearGradient>
  </defs>

  <!-- Thermal Glow Base -->
  <circle cx="256" cy="270" r="236" fill="url(#fire-thermal-core)"/>

  <!-- LAYER 1: OUTER ROARING INFERNO TONGUES -->
  <g filter="url(#flame-blur-glow)">
    <path d="M 256,22 C 290,70 334,95 350,140 C 370,120 405,150 420,195 C 445,170 465,220 460,270
             C 480,310 460,370 425,410 C 385,455 325,480 256,488 C 187,480 127,455 87,410
             C 52,370 32,310 52,270 C 47,220 67,170 92,195 C 107,150 142,120 162,140
             C 178,95 222,70 256,22 Z"
          fill="url(#outer-flame)" opacity="0.95"/>
  </g>

  <!-- LAYER 2: MID INTENSE FLAME TONGUES -->
  <g filter="url(#ember-glow)">
    <path d="M 256,54 C 282,98 322,125 334,168 C 354,152 384,178 396,218 C 418,198 436,240 430,285
             C 446,322 428,370 398,405 C 362,442 312,464 256,470 C 200,464 150,442 114,405
             C 84,370 66,322 82,285 C 76,240 94,198 116,218 C 128,178 158,152 178,168
             C 190,125 230,98 256,54 Z"
          fill="url(#mid-flame)"/>
  </g>

  <!-- LAYER 3: CORE SUN-GOLD FLAME TONGUES -->
  <g>
    <path d="M 256,95 C 275,134 305,160 314,196 C 330,182 355,205 364,240 C 380,222 396,260 388,300
             C 400,332 382,372 356,400 C 326,430 292,444 256,448 C 220,444 186,430 156,400
             C 130,372 112,332 124,300 C 116,260 132,222 148,240 C 157,205 182,182 198,196
             C 207,160 237,134 256,95 Z"
          fill="url(#core-flame)"/>
  </g>

  <!-- LAYER 4: WHITE-HOT PLASMA HEART -->
  <g>
    <path d="M 256,150 C 270,182 292,204 298,232 C 310,220 328,240 334,268 C 346,255 356,285 348,318
             C 356,344 338,374 316,394 C 292,416 274,424 256,426 C 238,424 220,416 196,394
             C 174,374 156,344 164,318 C 156,285 166,255 178,268 C 184,240 202,220 214,232
             C 220,204 242,182 256,150 Z"
          fill="#ffffff" opacity="0.95"/>
  </g>

  <!-- FLOATING FIERY EMBERS & SPARKS -->
  <g fill="#fde047" filter="url(#ember-glow)">
    <circle cx="210" cy="80" r="4.5"/>
    <circle cx="310" cy="90" r="3.5"/>
    <circle cx="370" cy="130" r="5"/>
    <circle cx="140" cy="140" r="4"/>
    <circle cx="440" cy="220" r="3.5"/>
    <circle cx="70" cy="230" r="4"/>
    <circle cx="450" cy="330" r="3"/>
    <circle cx="60" cy="340" r="4.5"/>
    <circle cx="256" cy="35" r="5"/>
    <circle cx="280" cy="60" r="3"/>
    <circle cx="170" cy="110" r="3"/>
    <circle cx="340" cy="110" r="4"/>
  </g>

  <!-- COMBAT BADGE PLAQUE: OBSIDIAN & GOLDEN FLAME -->
  <g filter="url(#fire-heavy-shadow)" transform="translate(0, 40)">
    <!-- Shield Backing Plaque -->
    <polygon points="256,220 376,244 394,324 256,378 118,324 136,244"
             fill="url(#obsidian-badge)" stroke="url(#fire-gold-bevel)" stroke-width="4"/>

    <!-- Inner Rim Inset -->
    <polygon points="256,236 360,256 376,316 256,362 136,316 152,256"
             fill="#140301" stroke="#ea580c" stroke-width="2"/>

    <!-- Fiery Chevron Brackets -->
    <path d="M 164,264 L 256,290 L 348,264" fill="none" stroke="#fde047" stroke-width="2" opacity="0.5"/>
    <path d="M 152,310 L 256,346 L 360,310" fill="none" stroke="#fde047" stroke-width="2" opacity="0.5"/>

    <!-- NUMBER "15" IN CHISELED FIGHTING 3D TYPOGRAPHY -->
    <g transform="translate(256, 304)">
      <!-- 3D Shadow -->
      <text x="4" y="16" font-family="'Impact', 'Arial Black', sans-serif" font-size="74" font-weight="900"
            fill="#050100" text-anchor="middle" letter-spacing="2">15</text>
      <!-- Face -->
      <text x="0" y="12" font-family="'Impact', 'Arial Black', sans-serif" font-size="74" font-weight="900"
            fill="url(#fire-gold-bevel)" stroke="#450a0a" stroke-width="3" text-anchor="middle" letter-spacing="2">15</text>
      <!-- Specular Highlight Cut -->
      <text x="0" y="12" font-family="'Impact', 'Arial Black', sans-serif" font-size="74" font-weight="900"
            fill="none" stroke="#ffffff" stroke-width="1.5" stroke-dasharray="8,12" text-anchor="middle" letter-spacing="2">15</text>
    </g>

    <!-- Subtitle Banner -->
    <g transform="translate(0, 372)">
      <polygon points="174,0 338,0 354,26 322,26 256,34 190,26 158,26"
               fill="#1a0401" stroke="#f97316" stroke-width="2"/>
      <text x="256" y="18" font-family="'Impact', 'Arial Black', sans-serif" font-size="14" font-weight="900"
            letter-spacing="4" fill="#fde047" text-anchor="middle">FIRE STREAK</text>
    </g>
  </g>
</svg>'''


def get_streak_lightning_30_svg():
    """30 Streak: Electric Lightning Badge / High-Voltage Plasma Storm Crest."""
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <defs>
    <!-- Filters -->
    <filter id="light-heavy-shadow" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="16" stdDeviation="24" flood-color="#000000" flood-opacity="0.95"/>
    </filter>
    <filter id="neon-electric-glow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="6" result="blur1"/>
      <feGaussianBlur stdDeviation="16" result="blur2"/>
      <feMerge>
        <feMergeNode in="blur2"/>
        <feMergeNode in="blur1"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="purple-plasma-glow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="12" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <!-- Gradients -->
    <radialGradient id="electric-field-core" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.95"/>
      <stop offset="25%" stop-color="#00f0ff" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#3b82f6" stop-opacity="0.5"/>
      <stop offset="75%" stop-color="#6b21a8" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#04020a" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="titanium-hex" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="20%" stop-color="#7dd3fc"/>
      <stop offset="45%" stop-color="#0284c7"/>
      <stop offset="70%" stop-color="#0f172a"/>
      <stop offset="90%" stop-color="#1e1b4b"/>
      <stop offset="100%" stop-color="#00f0ff"/>
    </linearGradient>

    <linearGradient id="voltage-30-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="25%" stop-color="#cffafe"/>
      <stop offset="55%" stop-color="#00f0ff"/>
      <stop offset="85%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#1e3a8a"/>
    </linearGradient>

    <linearGradient id="cyan-bolt-line" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="40%" stop-color="#e0ffff"/>
      <stop offset="70%" stop-color="#00f0ff"/>
      <stop offset="100%" stop-color="#0099ff"/>
    </linearGradient>
  </defs>

  <!-- Ambient Electromagnetic Plasma Field -->
  <circle cx="256" cy="256" r="238" fill="url(#electric-field-core)"/>

  <!-- Rotating Ion Ring Background -->
  <g stroke="#00f0ff" stroke-width="1.5" opacity="0.35">
    <circle cx="256" cy="256" r="210" fill="none" stroke-dasharray="12,8"/>
    <circle cx="256" cy="256" r="180" fill="none" stroke-dasharray="24,12"/>
    <circle cx="256" cy="256" r="150" fill="none" stroke-dasharray="6,6"/>
  </g>

  <!-- HIGH-VOLTAGE CRACKLING LIGHTNING BOLTS (BURSTING IN 6 DIRECTIONS) -->
  <g filter="url(#neon-electric-glow)">
    <!-- Bolt 1: Top-Right Diagonal -->
    <path d="M 256,220 L 290,170 L 275,155 L 340,110 L 325,95 L 420,40"
          fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>
    <path d="M 256,220 L 290,170 L 275,155 L 340,110 L 325,95 L 420,40"
          fill="none" stroke="#00f0ff" stroke-width="7" stroke-linecap="round" opacity="0.6"/>

    <!-- Bolt 2: Top-Left Diagonal -->
    <path d="M 256,220 L 220,170 L 235,155 L 170,110 L 185,95 L 90,40"
          fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>
    <path d="M 256,220 L 220,170 L 235,155 L 170,110 L 185,95 L 90,40"
          fill="none" stroke="#00f0ff" stroke-width="7" stroke-linecap="round" opacity="0.6"/>

    <!-- Bolt 3: Right Horizontal Sweep -->
    <path d="M 280,256 L 330,235 L 320,250 L 400,230 L 390,245 L 485,240"
          fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>
    <path d="M 280,256 L 330,235 L 320,250 L 400,230 L 390,245 L 485,240"
          fill="none" stroke="#00f0ff" stroke-width="7" stroke-linecap="round" opacity="0.6"/>

    <!-- Bolt 4: Left Horizontal Sweep -->
    <path d="M 232,256 L 182,235 L 192,250 L 112,230 L 122,245 L 27,240"
          fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>
    <path d="M 232,256 L 182,235 L 192,250 L 112,230 L 122,245 L 27,240"
          fill="none" stroke="#00f0ff" stroke-width="7" stroke-linecap="round" opacity="0.6"/>

    <!-- Bolt 5: Bottom-Right Diagonal -->
    <path d="M 265,290 L 305,340 L 290,355 L 360,400 L 345,415 L 430,475"
          fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>
    <path d="M 265,290 L 305,340 L 290,355 L 360,400 L 345,415 L 430,475"
          fill="none" stroke="#00f0ff" stroke-width="7" stroke-linecap="round" opacity="0.6"/>

    <!-- Bolt 6: Bottom-Left Diagonal -->
    <path d="M 247,290 L 207,340 L 222,355 L 152,400 L 167,415 L 82,475"
          fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>
    <path d="M 247,290 L 207,340 L 222,355 L 152,400 L 167,415 L 82,475"
          fill="none" stroke="#00f0ff" stroke-width="7" stroke-linecap="round" opacity="0.6"/>

    <!-- Spark Arc Nodes -->
    <circle cx="290" cy="170" r="4.5" fill="#ffffff"/>
    <circle cx="220" cy="170" r="4.5" fill="#ffffff"/>
    <circle cx="330" cy="235" r="4" fill="#ffffff"/>
    <circle cx="182" cy="235" r="4" fill="#ffffff"/>
    <circle cx="305" cy="340" r="4" fill="#ffffff"/>
    <circle cx="207" cy="340" r="4" fill="#ffffff"/>
  </g>

  <!-- IONIZED TITANIUM HEXAGONAL CREST SHIELD -->
  <g filter="url(#light-heavy-shadow)">
    <!-- Outer Beveled Hexagon Armor -->
    <polygon points="256,48 436,152 436,360 256,464 76,360 76,152"
             fill="#080c18" stroke="url(#titanium-hex)" stroke-width="7" stroke-linejoin="round"/>

    <!-- Layered Inset Facet -->
    <polygon points="256,68 418,162 418,350 256,444 94,350 94,162"
             fill="url(#titanium-hex)" stroke="#021024" stroke-width="2"/>

    <!-- Inner Dark Ion Chamber -->
    <polygon points="256,92 396,174 396,338 256,420 116,338 116,174"
             fill="#040714" stroke="#00f0ff" stroke-width="3"/>

    <!-- Neon Circuit Tracks in Armor Plate -->
    <g stroke="#00f0ff" stroke-width="2" opacity="0.6">
      <line x1="256" y1="92" x2="256" y2="150"/>
      <line x1="256" y1="360" x2="256" y2="420"/>
      <line x1="116" y1="174" x2="166" y2="204"/>
      <line x1="396" y1="174" x2="346" y2="204"/>
      <line x1="116" y1="338" x2="166" y2="308"/>
      <line x1="396" y1="338" x2="346" y2="308"/>
    </g>

    <!-- Center Plasma Reactor Core -->
    <circle cx="256" cy="256" r="92" fill="#03081c" stroke="#38bdf8" stroke-width="3"/>
    <circle cx="256" cy="256" r="82" fill="none" stroke="#a855f7" stroke-width="2" stroke-dasharray="14,6"/>
    <circle cx="256" cy="256" r="68" fill="url(#electric-field-core)" opacity="0.8"/>
  </g>

  <!-- NUMBER "30" IN HIGH-VOLTAGE 3D COMBAT NUMERALS -->
  <g filter="url(#neon-electric-glow)" transform="translate(256, 280)">
    <!-- 3D Shadow -->
    <text x="4" y="6" font-family="'Impact', 'Arial Black', sans-serif" font-size="82" font-weight="900"
          fill="#01040a" text-anchor="middle" letter-spacing="2">30</text>
    <!-- Face -->
    <text x="0" y="0" font-family="'Impact', 'Arial Black', sans-serif" font-size="82" font-weight="900"
          fill="url(#voltage-30-grad)" stroke="#082f49" stroke-width="3" text-anchor="middle" letter-spacing="2">30</text>
    <!-- Lightning Glint on Digits -->
    <text x="0" y="0" font-family="'Impact', 'Arial Black', sans-serif" font-size="82" font-weight="900"
          fill="none" stroke="#ffffff" stroke-width="1.8" stroke-dasharray="10,14" text-anchor="middle" letter-spacing="2">30</text>
  </g>

  <!-- Subtitle Banner at Bottom -->
  <g transform="translate(0, 420)">
    <polygon points="160,0 352,0 376,28 338,28 256,36 174,28 136,28"
             fill="#020713" stroke="#00f0ff" stroke-width="2.5"/>
    <text x="256" y="19" font-family="'Impact', 'Arial Black', sans-serif" font-size="14" font-weight="900"
          letter-spacing="4" fill="#cffafe" text-anchor="middle">LIGHTNING 30</text>
  </g>
</svg>'''


def get_streak_overdrive_50_svg():
    """50 Streak: Golden Celestial Warrior Badge / Transcendent Overdrive Fighting Crest."""
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <defs>
    <!-- Filters -->
    <filter id="od-heavy-shadow" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="16" stdDeviation="26" flood-color="#000000" flood-opacity="0.95"/>
    </filter>
    <filter id="solar-corona-glow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="16" result="blur1"/>
      <feGaussianBlur stdDeviation="30" result="blur2"/>
      <feMerge>
        <feMergeNode in="blur2"/>
        <feMergeNode in="blur1"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="diamond-gem-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="8" result="glow"/>
      <feMerge>
        <feMergeNode in="glow"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <!-- Gradients -->
    <radialGradient id="od-solar-mandala" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="1"/>
      <stop offset="20%" stop-color="#fef08a" stop-opacity="0.95"/>
      <stop offset="45%" stop-color="#f59e0b" stop-opacity="0.75"/>
      <stop offset="70%" stop-color="#d97706" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#050201" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="celestial-gold-wing" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="15%" stop-color="#fffbeb"/>
      <stop offset="35%" stop-color="#fef08a"/>
      <stop offset="60%" stop-color="#f59e0b"/>
      <stop offset="85%" stop-color="#b45309"/>
      <stop offset="100%" stop-color="#78350f"/>
    </linearGradient>

    <linearGradient id="od-crimson-velvet" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#881337"/>
      <stop offset="35%" stop-color="#4c0519"/>
      <stop offset="75%" stop-color="#1e0208"/>
      <stop offset="100%" stop-color="#080002"/>
    </linearGradient>

    <linearGradient id="od-num-50" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="25%" stop-color="#fffbeb"/>
      <stop offset="50%" stop-color="#fde047"/>
      <stop offset="75%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>

    <radialGradient id="od-core-jewel" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="30%" stop-color="#67e8f9"/>
      <stop offset="70%" stop-color="#06b6d4"/>
      <stop offset="100%" stop-color="#0e7490"/>
    </radialGradient>
  </defs>

  <!-- Ambient Radiant Solar Mandala Core -->
  <circle cx="256" cy="256" r="242" fill="url(#od-solar-mandala)"/>

  <!-- SACRED SOLAR MANDALA RAYS (16 Radiant Rays) -->
  <g stroke="#fde047" stroke-width="2" opacity="0.4">
    <line x1="256" y1="256" x2="256" y2="12"/>
    <line x1="256" y1="256" x2="256" y2="500"/>
    <line x1="256" y1="256" x2="12" y2="256"/>
    <line x1="256" y1="256" x2="500" y2="256"/>
    <line x1="256" y1="256" x2="84" y2="84"/>
    <line x1="256" y1="256" x2="428" y2="428"/>
    <line x1="256" y1="256" x2="428" y2="84"/>
    <line x1="256" y1="256" x2="84" y2="428"/>
    <circle cx="256" cy="256" r="218" fill="none" stroke-dasharray="14,8"/>
    <circle cx="256" cy="256" r="190" fill="none" stroke-dasharray="8,6"/>
  </g>

  <!-- CELESTIAL WARRIOR GOLDEN WINGS (SWEEPING OUTWARD) -->
  <g filter="url(#od-heavy-shadow)">
    <!-- LEFT WING FEATHER BLADES -->
    <g class="celestial-left-wing">
      <!-- Feather Tier 1 (Outermost Top Blade) -->
      <path d="M 230,190 C 180,140 110,110 24,96 C 60,140 110,190 200,225 Z"
            fill="url(#celestial-gold-wing)" stroke="#78350f" stroke-width="2"/>
      <!-- Feather Tier 2 -->
      <path d="M 220,215 C 160,175 90,165 14,160 C 60,195 120,235 195,255 Z"
            fill="url(#celestial-gold-wing)" stroke="#78350f" stroke-width="2"/>
      <!-- Feather Tier 3 -->
      <path d="M 215,245 C 150,215 80,220 20,230 C 70,255 130,280 195,290 Z"
            fill="url(#celestial-gold-wing)" stroke="#78350f" stroke-width="2"/>
      <!-- Feather Tier 4 -->
      <path d="M 210,275 C 150,260 90,280 40,305 C 90,320 145,325 200,320 Z"
            fill="url(#celestial-gold-wing)" stroke="#78350f" stroke-width="2"/>
      <!-- Feather Tier 5 (Lowest Inner Blade) -->
      <path d="M 215,310 C 165,315 115,340 76,375 C 120,365 170,355 220,345 Z"
            fill="url(#celestial-gold-wing)" stroke="#78350f" stroke-width="2"/>
    </g>

    <!-- RIGHT WING FEATHER BLADES -->
    <g class="celestial-right-wing">
      <!-- Feather Tier 1 (Outermost Top Blade) -->
      <path d="M 282,190 C 332,140 402,110 488,96 C 452,140 402,190 312,225 Z"
            fill="url(#celestial-gold-wing)" stroke="#78350f" stroke-width="2"/>
      <!-- Feather Tier 2 -->
      <path d="M 292,215 C 352,175 422,165 498,160 C 452,195 392,235 317,255 Z"
            fill="url(#celestial-gold-wing)" stroke="#78350f" stroke-width="2"/>
      <!-- Feather Tier 3 -->
      <path d="M 297,245 C 362,215 432,220 492,230 C 442,255 382,280 317,290 Z"
            fill="url(#celestial-gold-wing)" stroke="#78350f" stroke-width="2"/>
      <!-- Feather Tier 4 -->
      <path d="M 302,275 C 362,260 422,280 472,305 C 422,320 367,325 312,320 Z"
            fill="url(#celestial-gold-wing)" stroke="#78350f" stroke-width="2"/>
      <!-- Feather Tier 5 (Lowest Inner Blade) -->
      <path d="M 297,310 C 347,315 397,340 436,375 C 392,365 342,355 292,345 Z"
            fill="url(#celestial-gold-wing)" stroke="#78350f" stroke-width="2"/>
    </g>

    <!-- CROSSED CELESTIAL BATTLE SWORDS BEHIND CREST -->
    <!-- Sword 1: Top-Left to Bottom-Right -->
    <path d="M 100,50 L 115,40 L 412,462 L 397,472 Z" fill="#ffffff" stroke="#b45309" stroke-width="2"/>
    <polygon points="100,50 90,30 115,40" fill="#fde047"/>
    <!-- Sword 2: Top-Right to Bottom-Left -->
    <path d="M 412,50 L 397,40 L 100,462 L 115,472 Z" fill="#ffffff" stroke="#b45309" stroke-width="2"/>
    <polygon points="412,50 422,30 397,40" fill="#fde047"/>
  </g>

  <!-- GILDED WARRIOR HEART CREST & CELESTIAL CROWN -->
  <g filter="url(#od-heavy-shadow)">
    <!-- Main Imperial Armor Shield -->
    <path d="M 256,66 L 360,116 L 392,204 L 358,340 L 256,444 L 154,340 L 120,204 L 152,116 Z"
          fill="#170402" stroke="url(#celestial-gold-wing)" stroke-width="6" stroke-linejoin="round"/>

    <!-- Inner Velvet Armor Plate -->
    <path d="M 256,86 L 344,128 L 372,206 L 342,326 L 256,420 L 170,326 L 140,206 L 168,128 Z"
          fill="url(#od-crimson-velvet)" stroke="#f59e0b" stroke-width="3"/>

    <!-- Celestial Crown Apex Spikes -->
    <polygon points="256,46 272,86 256,104 240,86" fill="#ffffff" stroke="#b45309" stroke-width="2"/>
    <polygon points="196,70 218,98 202,110" fill="#fde047" stroke="#b45309" stroke-width="1.5"/>
    <polygon points="316,70 294,98 310,110" fill="#fde047" stroke="#b45309" stroke-width="1.5"/>

    <!-- Radiant Diamond Core Overdrive Gem -->
    <g transform="translate(256, 175)" filter="url(#diamond-gem-glow)">
      <!-- Gilded Setting Ring -->
      <polygon points="0,-24 18,-18 24,0 18,18 0,24 -18,18 -24,0 -18,-18"
               fill="#fde047" stroke="#b45309" stroke-width="2"/>
      <!-- Cyan Core Gem Facet -->
      <polygon points="0,-18 13,-13 18,0 13,13 0,18 -13,13 -18,0 -13,-13"
               fill="url(#od-core-jewel)" stroke="#ffffff" stroke-width="1.5"/>
      <circle cx="-4" cy="-5" r="3.5" fill="#ffffff" opacity="0.8"/>
    </g>
  </g>

  <!-- NUMBER "50" IN SCULPTED 3D CELESTIAL GOLD -->
  <g filter="url(#solar-corona-glow)" transform="translate(256, 308)">
    <!-- 3D Shadow -->
    <text x="5" y="10" font-family="'Impact', 'Arial Black', sans-serif" font-size="88" font-weight="900"
          fill="#100301" text-anchor="middle" letter-spacing="2">50</text>
    <!-- Face -->
    <text x="0" y="0" font-family="'Impact', 'Arial Black', sans-serif" font-size="88" font-weight="900"
          fill="url(#od-num-50)" stroke="#451a03" stroke-width="3.5" text-anchor="middle" letter-spacing="2">50</text>
    <!-- Specular Star Cut -->
    <text x="0" y="0" font-family="'Impact', 'Arial Black', sans-serif" font-size="88" font-weight="900"
          fill="none" stroke="#ffffff" stroke-width="2" stroke-dasharray="10,16" text-anchor="middle" letter-spacing="2">50</text>
  </g>

  <!-- IMPERIAL OVERDRIVE BANNER RIBBON -->
  <g transform="translate(0, 426)" filter="url(#od-heavy-shadow)">
    <polygon points="144,0 368,0 398,34 354,34 256,46 158,34 114,34"
             fill="#2b0704" stroke="url(#celestial-gold-wing)" stroke-width="3"/>
    <text x="256" y="23" font-family="'Impact', 'Arial Black', sans-serif" font-size="18" font-weight="900"
          letter-spacing="6" fill="#fef08a" text-anchor="middle">OVERDRIVE</text>
  </g>
</svg>'''


def generate_all_streaks():
    streaks = [
        ("streak_fire_15.svg", get_streak_fire_15_svg()),
        ("streak_lightning_30.svg", get_streak_lightning_30_svg()),
        ("streak_overdrive_50.svg", get_streak_overdrive_50_svg()),
    ]
    
    print(f"Generating {len(streaks)} streak badges in {BASE_DIR}...")
    for filename, content in streaks:
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
    generate_all_streaks()
