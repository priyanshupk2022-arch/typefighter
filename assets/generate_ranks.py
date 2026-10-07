"""
generate_ranks.py - Generates DMC-inspired fighting game rank badges:
rank_d.svg, rank_c.svg, rank_b.svg, rank_a.svg, rank_s.svg, rank_ss.svg, rank_sss.svg
"""

import os
import xml.etree.ElementTree as ET

BASE_DIR = r"c:\Users\priya\OneDrive\Documents\Next Toppers\typefighter\assets\icons\ranks"
os.makedirs(BASE_DIR, exist_ok=True)


def get_rank_d_svg():
    """Rank D: Dull / Heavy Cast Iron & Weathered Bronze, bolted plates."""
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <defs>
    <!-- Filters -->
    <filter id="d-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#000000" flood-opacity="0.8"/>
    </filter>
    <filter id="d-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="0" stdDeviation="8" flood-color="#8c7355" flood-opacity="0.5"/>
    </filter>
    <filter id="inner-bevel" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000000" flood-opacity="0.7"/>
    </filter>

    <!-- Gradients -->
    <radialGradient id="d-bg-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#4a3728" stop-opacity="0.6"/>
      <stop offset="60%" stop-color="#1f1a17" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#0b0908" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="iron-rim" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#555d6b"/>
      <stop offset="30%" stop-color="#363c46"/>
      <stop offset="70%" stop-color="#1e2229"/>
      <stop offset="100%" stop-color="#454c59"/>
    </linearGradient>

    <linearGradient id="bronze-plate" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#8a6f4d"/>
      <stop offset="25%" stop-color="#5c4731"/>
      <stop offset="60%" stop-color="#3b2b1d"/>
      <stop offset="100%" stop-color="#241a12"/>
    </linearGradient>

    <linearGradient id="d-letter-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d4b483"/>
      <stop offset="35%" stop-color="#99774d"/>
      <stop offset="70%" stop-color="#5e452b"/>
      <stop offset="100%" stop-color="#3a2715"/>
    </linearGradient>

    <linearGradient id="d-bevel-light" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f0d5a8"/>
      <stop offset="100%" stop-color="#a38257"/>
    </linearGradient>

    <linearGradient id="d-bevel-dark" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#4a341e"/>
      <stop offset="100%" stop-color="#1c1209"/>
    </linearGradient>

    <linearGradient id="rivet-metal" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#828d9f"/>
      <stop offset="50%" stop-color="#3a404c"/>
      <stop offset="100%" stop-color="#15181d"/>
    </linearGradient>
  </defs>

  <!-- Background Ambience -->
  <circle cx="256" cy="256" r="230" fill="url(#d-bg-glow)"/>

  <!-- Outer Heavy Industrial Shield -->
  <g filter="url(#d-shadow)">
    <!-- Base Bracket / Spike Wings -->
    <path d="M 256,38 L 380,88 L 442,190 L 416,340 L 256,470 L 96,340 L 70,190 L 132,88 Z"
          fill="#17191d" stroke="url(#iron-rim)" stroke-width="6" stroke-linejoin="round"/>

    <!-- Outer Iron Rim Facets -->
    <path d="M 256,54 L 366,98 L 420,192 L 398,326 L 256,446 L 114,326 L 92,192 L 146,98 Z"
          fill="url(#iron-rim)" stroke="#111317" stroke-width="2"/>

    <!-- Inner Bronze Armor Plate -->
    <path d="M 256,76 L 350,114 L 396,198 L 376,312 L 256,420 L 136,312 L 116,198 L 162,114 Z"
          fill="url(#bronze-plate)" stroke="#1a140f" stroke-width="4"/>

    <!-- Steel Bevel Inner Edge Lines -->
    <path d="M 256,76 L 256,420 M 116,198 L 396,198"
          stroke="#423323" stroke-width="2" stroke-opacity="0.4"/>
    <path d="M 162,114 L 350,312 M 350,114 L 162,312"
          stroke="#261b11" stroke-width="1.5" stroke-opacity="0.3"/>

    <!-- Corner Bolted Rivets -->
    <g fill="url(#rivet-metal)" stroke="#111317" stroke-width="1.5">
      <circle cx="166" cy="120" r="8"/>
      <circle cx="346" cy="120" r="8"/>
      <circle cx="390" cy="204" r="8"/>
      <circle cx="122" cy="204" r="8"/>
      <circle cx="370" cy="308" r="8"/>
      <circle cx="142" cy="308" r="8"/>
      <circle cx="256" cy="406" r="8"/>
      <circle cx="256" cy="90" r="8"/>
    </g>
    <!-- Rivet highlight glints -->
    <g fill="#9aa5b8" opacity="0.6">
      <circle cx="164" cy="118" r="2.5"/>
      <circle cx="344" cy="118" r="2.5"/>
      <circle cx="388" cy="202" r="2.5"/>
      <circle cx="120" cy="202" r="2.5"/>
      <circle cx="368" cy="306" r="2.5"/>
      <circle cx="140" cy="306" r="2.5"/>
      <circle cx="254" cy="404" r="2.5"/>
      <circle cx="254" cy="88" r="2.5"/>
    </g>

    <!-- Battle Scratch Cuts -->
    <path d="M 140,160 L 190,220 M 145,155 L 180,200" stroke="#120c07" stroke-width="3" opacity="0.7"/>
    <path d="M 141,162 L 191,222 M 146,157 L 181,202" stroke="#7e603e" stroke-width="1" opacity="0.5"/>
    <path d="M 330,260 L 375,290" stroke="#120c07" stroke-width="2.5" opacity="0.7"/>
    <path d="M 331,262 L 376,292" stroke="#7e603e" stroke-width="1" opacity="0.5"/>
  </g>

  <!-- Center Letter 'D' - Chiseled Industrial 3D -->
  <g filter="url(#d-glow)">
    <!-- 3D Extrusion Shadow -->
    <path d="M 172,138 L 275,138 C 365,138 375,210 375,256 C 375,302 365,374 275,374 L 172,374 Z"
          fill="#130d07" transform="translate(6, 10)"/>

    <!-- Main Letter Face -->
    <path d="M 172,138 L 275,138 C 365,138 375,210 375,256 C 375,302 365,374 275,374 L 172,374 Z
             M 226,188 L 268,188 C 315,188 322,224 322,256 C 322,288 315,324 268,324 L 226,324 Z"
          fill="url(#d-letter-grad)" fill-rule="evenodd" stroke="#24160b" stroke-width="3"/>

    <!-- Light Top Bevel -->
    <polygon points="172,138 275,138 268,188 226,188 226,324 172,374" fill="url(#d-bevel-light)" opacity="0.75"/>

    <!-- Dark Bottom Bevel -->
    <polygon points="172,374 275,374 268,324 226,324" fill="url(#d-bevel-dark)" opacity="0.9"/>
    <path d="M 275,374 C 365,374 375,302 375,256 L 322,256 C 322,288 315,324 268,324 Z"
          fill="url(#d-bevel-dark)" opacity="0.85"/>
    <path d="M 275,138 C 365,138 375,210 375,256 L 322,256 C 322,224 315,188 268,188 Z"
          fill="url(#d-bevel-light)" opacity="0.6"/>

    <!-- Chiseled Edge Highlights -->
    <path d="M 172,138 L 275,138 L 322,188 M 172,138 L 172,374"
          stroke="#ffe6b8" stroke-width="2.5" stroke-linecap="round"/>
    <path d="M 226,188 L 268,188" stroke="#ffe6b8" stroke-width="1.5"/>

    <!-- Inner Hole Shadow -->
    <path d="M 226,188 L 226,324 L 268,324 C 315,324 322,288 322,256 C 322,224 315,188 268,188 Z"
          fill="#1c130b" fill-opacity="0.65" stroke="#0e0a05" stroke-width="2"/>
  </g>

  <!-- Rank Label Banner at Bottom -->
  <g transform="translate(0, 420)">
    <polygon points="170,0 342,0 358,30 330,30 256,38 182,30 154,30"
             fill="#181a1f" stroke="#525d6f" stroke-width="2"/>
    <text x="256" y="21" font-family="'Impact', 'Arial Black', sans-serif" font-size="18" font-weight="900"
          letter-spacing="5" fill="#c49b66" text-anchor="middle">RANK D</text>
  </g>
</svg>'''


def get_rank_c_svg():
    """Rank C: Cool / Polished Cobalt Steel & Chromium, cyan energy line."""
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <defs>
    <!-- Filters -->
    <filter id="c-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="12" stdDeviation="18" flood-color="#000000" flood-opacity="0.85"/>
    </filter>
    <filter id="c-cyan-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="c-soft-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="0" stdDeviation="12" flood-color="#00d2d3" flood-opacity="0.6"/>
    </filter>

    <!-- Gradients -->
    <radialGradient id="c-bg-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#005b82" stop-opacity="0.6"/>
      <stop offset="60%" stop-color="#061a29" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#02080d" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="chrome-steel" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="25%" stop-color="#a4b0be"/>
      <stop offset="48%" stop-color="#57606f"/>
      <stop offset="52%" stop-color="#2f3542"/>
      <stop offset="75%" stop-color="#747d8c"/>
      <stop offset="100%" stop-color="#ced6e0"/>
    </linearGradient>

    <linearGradient id="cobalt-shield" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1e3799"/>
      <stop offset="35%" stop-color="#0c2461"/>
      <stop offset="75%" stop-color="#0a1936"/>
      <stop offset="100%" stop-color="#050d1e"/>
    </linearGradient>

    <linearGradient id="c-letter-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="30%" stop-color="#dff9fb"/>
      <stop offset="60%" stop-color="#00a8ff"/>
      <stop offset="100%" stop-color="#005b96"/>
    </linearGradient>

    <linearGradient id="cyan-energy-line" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00d2d3" stop-opacity="0"/>
      <stop offset="30%" stop-color="#00d2d3" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#ffffff" stop-opacity="1"/>
      <stop offset="70%" stop-color="#00d2d3" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#00d2d3" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <!-- Ambient Blue Glow -->
  <circle cx="256" cy="256" r="230" fill="url(#c-bg-glow)"/>

  <!-- Winged Cold Steel Crest Shield -->
  <g filter="url(#c-shadow)">
    <!-- Flaring Winglets / Side Blades -->
    <path d="M 256,40 L 330,70 L 440,110 L 470,170 L 430,230 L 460,290 L 390,360 L 256,472
             L 122,360 L 52,290 L 82,230 L 42,170 L 72,110 L 182,70 Z"
          fill="#0a1524" stroke="url(#chrome-steel)" stroke-width="4" stroke-linejoin="round"/>

    <!-- Outer Chrome Wing Chamfers -->
    <path d="M 256,56 L 320,82 L 418,120 L 442,172 L 406,224 L 430,280 L 372,344 L 256,450
             L 140,344 L 82,280 L 106,224 L 70,172 L 94,120 L 192,82 Z"
          fill="url(#chrome-steel)" stroke="#091422" stroke-width="2"/>

    <!-- Inner Cobalt Blue Shield Plate -->
    <path d="M 256,80 L 350,126 L 390,210 L 350,326 L 256,424 L 162,326 L 122,210 L 162,126 Z"
          fill="url(#cobalt-shield)" stroke="#00d2d3" stroke-width="2.5"/>

    <!-- Sharp Bevel Ridges -->
    <line x1="256" y1="80" x2="256" y2="424" stroke="#48dbfb" stroke-width="2" stroke-opacity="0.7"/>
    <line x1="162" y1="126" x2="350" y2="326" stroke="#0abde3" stroke-width="1.5" stroke-opacity="0.3"/>
    <line x1="350" y1="126" x2="162" y2="326" stroke="#0abde3" stroke-width="1.5" stroke-opacity="0.3"/>

    <!-- Cyan Circuit / Energy Chevron Insets -->
    <path d="M 190,140 L 256,180 L 322,140" fill="none" stroke="#00d2d3" stroke-width="3" opacity="0.6"/>
    <path d="M 190,380 L 256,410 L 322,380" fill="none" stroke="#00d2d3" stroke-width="3" opacity="0.6"/>
  </g>

  <!-- Horizontal Neon Cyan Energy Laser Slicing Across -->
  <g filter="url(#c-cyan-glow)">
    <path d="M 30,256 L 482,256" stroke="url(#cyan-energy-line)" stroke-width="4"/>
    <circle cx="256" cy="256" r="3" fill="#ffffff"/>
  </g>

  <!-- Center Letter 'C' - Aerodynamic Chromium Razor -->
  <g filter="url(#c-soft-glow)">
    <!-- 3D Shadow -->
    <path d="M 346,182 C 328,144 294,134 256,134 C 182,134 154,192 154,256 C 154,320 182,378 256,378 C 294,378 328,368 346,330 L 298,312 C 288,326 274,332 256,332 C 206,332 202,290 202,256 C 202,222 206,180 256,180 C 274,180 288,186 298,200 Z"
          fill="#020912" transform="translate(6, 10)"/>

    <!-- Letter Face -->
    <path d="M 346,182 C 328,144 294,134 256,134 C 182,134 154,192 154,256 C 154,320 182,378 256,378 C 294,378 328,368 346,330 L 298,312 C 288,326 274,332 256,332 C 206,332 202,290 202,256 C 202,222 206,180 256,180 C 274,180 288,186 298,200 Z"
          fill="url(#c-letter-grad)" stroke="#002f52" stroke-width="3"/>

    <!-- Sharp Specular Cuts on Outer Curve -->
    <path d="M 346,182 C 328,144 294,134 256,134 C 182,134 154,192 154,256"
          fill="none" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
    <!-- Bottom Inner Rim Shadow -->
    <path d="M 154,256 C 154,320 182,378 256,378 C 294,378 328,368 346,330"
          fill="none" stroke="#003e6b" stroke-width="3"/>

    <!-- Inner Spine Cyan Energy Glint -->
    <path d="M 206,240 C 210,210 230,192 256,192 C 270,192 282,198 290,208"
          fill="none" stroke="#c7f8ff" stroke-width="2.5" opacity="0.9"/>
  </g>

  <!-- Rank Label Banner at Bottom -->
  <g transform="translate(0, 424)">
    <polygon points="166,0 346,0 366,32 334,32 256,40 178,32 146,32"
             fill="#081422" stroke="#00a8ff" stroke-width="2"/>
    <text x="256" y="22" font-family="'Impact', 'Arial Black', sans-serif" font-size="18" font-weight="900"
          letter-spacing="5" fill="#70a1ff" text-anchor="middle">RANK C</text>
  </g>
</svg>'''


def get_rank_b_svg():
    """Rank B: Bravo / Gilded Brass, Amber Gold Battle Crest with Dual Wings."""
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <defs>
    <!-- Filters -->
    <filter id="b-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="12" stdDeviation="18" flood-color="#000000" flood-opacity="0.85"/>
    </filter>
    <filter id="b-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="0" stdDeviation="14" flood-color="#f59e0b" flood-opacity="0.6"/>
    </filter>

    <!-- Gradients -->
    <radialGradient id="b-bg-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#b45309" stop-opacity="0.5"/>
      <stop offset="50%" stop-color="#78350f" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#0a0502" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="brass-gold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="20%" stop-color="#facc15"/>
      <stop offset="45%" stop-color="#d97706"/>
      <stop offset="70%" stop-color="#92400e"/>
      <stop offset="100%" stop-color="#fde047"/>
    </linearGradient>

    <linearGradient id="amber-core" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#78350f"/>
      <stop offset="30%" stop-color="#451a03"/>
      <stop offset="75%" stop-color="#270e02"/>
      <stop offset="100%" stop-color="#120601"/>
    </linearGradient>

    <linearGradient id="b-letter-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="25%" stop-color="#fde047"/>
      <stop offset="55%" stop-color="#f59e0b"/>
      <stop offset="85%" stop-color="#b45309"/>
      <stop offset="100%" stop-color="#78350f"/>
    </linearGradient>

    <linearGradient id="b-top-bevel" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fffbeb"/>
      <stop offset="100%" stop-color="#f59e0b"/>
    </linearGradient>
  </defs>

  <!-- Ambient Amber Glow -->
  <circle cx="256" cy="256" r="230" fill="url(#b-bg-glow)"/>

  <!-- Tiered Battle Crest Shield -->
  <g filter="url(#b-shadow)">
    <!-- Sweeping Wing Tips -->
    <path d="M 256,36 L 340,60 L 420,78 L 472,142 L 440,210 L 480,270 L 430,340 L 370,380 L 256,478
             L 142,380 L 82,340 L 32,270 L 72,210 L 40,142 L 92,78 L 172,60 Z"
          fill="#170c04" stroke="url(#brass-gold)" stroke-width="5" stroke-linejoin="round"/>

    <!-- Gilded Outer Trim -->
    <path d="M 256,52 L 330,74 L 400,90 L 446,146 L 418,206 L 452,260 L 408,324 L 356,360 L 256,454
             L 156,360 L 104,324 L 60,260 L 94,206 L 66,146 L 112,90 L 182,74 Z"
          fill="url(#brass-gold)" stroke="#2b1404" stroke-width="2"/>

    <!-- Inner Dark Amber Shield Plate -->
    <path d="M 256,76 L 350,110 L 396,180 L 366,310 L 256,420 L 146,310 L 116,180 L 162,110 Z"
          fill="url(#amber-core)" stroke="#f59e0b" stroke-width="3"/>

    <!-- Engraved Gold Sunburst Rays -->
    <g stroke="#f59e0b" stroke-width="1.5" opacity="0.35">
      <line x1="256" y1="256" x2="256" y2="82"/>
      <line x1="256" y1="256" x2="350" y2="114"/>
      <line x1="256" y1="256" x2="394" y2="182"/>
      <line x1="256" y1="256" x2="364" y2="308"/>
      <line x1="256" y1="256" x2="256" y2="416"/>
      <line x1="256" y1="256" x2="148" y2="308"/>
      <line x1="256" y1="256" x2="118" y2="182"/>
      <line x1="256" y1="256" x2="162" y2="114"/>
    </g>

    <!-- Golden Ornamental Brackets -->
    <polygon points="256,86 270,104 256,122 242,104" fill="#fde047" stroke="#78350f" stroke-width="1.5"/>
    <polygon points="124,180 142,180 133,198" fill="#fde047" stroke="#78350f" stroke-width="1.5"/>
    <polygon points="388,180 370,180 379,198" fill="#fde047" stroke="#78350f" stroke-width="1.5"/>
  </g>

  <!-- Center Letter 'B' - Sculpted Fighting Game Brass -->
  <g filter="url(#b-glow)">
    <!-- 3D Base Shadow -->
    <path d="M 174,136 L 282,136 C 336,136 348,172 334,210 C 358,230 358,276 322,374 L 174,374 Z"
          fill="#0f0501" transform="translate(6, 10)"/>

    <!-- Letter B Body -->
    <path d="M 174,136 L 284,136 C 334,136 346,172 332,210 C 358,232 358,280 322,374 L 174,374 Z
             M 226,182 L 276,182 C 298,182 300,222 278,222 L 226,222 Z
             M 226,260 L 280,260 C 304,260 306,328 280,328 L 226,328 Z"
          fill="url(#b-letter-grad)" fill-rule="evenodd" stroke="#451a03" stroke-width="3"/>

    <!-- Beveled Light Facets on Top Edges -->
    <polygon points="174,136 284,136 276,182 226,182 226,222 174,232" fill="url(#b-top-bevel)" opacity="0.8"/>
    <polygon points="174,250 280,260 280,280 226,280 174,290" fill="#fde047" opacity="0.6"/>

    <!-- Specular Highlight Cuts -->
    <line x1="174" y1="136" x2="284" y2="136" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>
    <line x1="174" y1="136" x2="174" y2="374" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>
    <path d="M 284,136 C 334,136 346,172 332,210" fill="none" stroke="#fffbeb" stroke-width="2.5"/>

    <!-- Inner Counters Depth -->
    <rect x="226" y="182" width="50" height="40" rx="4" fill="#1c0a02" opacity="0.6"/>
    <rect x="226" y="260" width="54" height="68" rx="4" fill="#1c0a02" opacity="0.6"/>
  </g>

  <!-- Rank Label Banner at Bottom -->
  <g transform="translate(0, 424)">
    <polygon points="166,0 346,0 366,32 334,32 256,40 178,32 146,32"
             fill="#220e03" stroke="#f59e0b" stroke-width="2"/>
    <text x="256" y="22" font-family="'Impact', 'Arial Black', sans-serif" font-size="18" font-weight="900"
          letter-spacing="5" fill="#fde047" text-anchor="middle">RANK B</text>
  </g>
</svg>'''


def get_rank_a_svg():
    """Rank A: Awesome / Crimson Ruby & Gilded Demon Razor Wings."""
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <defs>
    <!-- Filters -->
    <filter id="a-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="14" stdDeviation="20" flood-color="#000000" flood-opacity="0.9"/>
    </filter>
    <filter id="a-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="#ef4444" flood-opacity="0.75"/>
    </filter>
    <filter id="a-fire-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="10" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <!-- Gradients -->
    <radialGradient id="a-bg-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#dc2626" stop-opacity="0.6"/>
      <stop offset="45%" stop-color="#991b1b" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#0e0202" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="ruby-gold-rim" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="25%" stop-color="#e11d48"/>
      <stop offset="50%" stop-color="#9f1239"/>
      <stop offset="75%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#ffe4e6"/>
    </linearGradient>

    <linearGradient id="crimson-core" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#881337"/>
      <stop offset="40%" stop-color="#4c0519"/>
      <stop offset="80%" stop-color="#2a020d"/>
      <stop offset="100%" stop-color="#140106"/>
    </linearGradient>

    <linearGradient id="a-letter-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="20%" stop-color="#fecdd3"/>
      <stop offset="45%" stop-color="#f43f5e"/>
      <stop offset="75%" stop-color="#be123c"/>
      <stop offset="100%" stop-color="#881337"/>
    </linearGradient>

    <linearGradient id="a-gold-trim" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#fde047"/>
      <stop offset="50%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#fef08a"/>
    </linearGradient>
  </defs>

  <!-- Ambient Crimson Inferno Glow -->
  <circle cx="256" cy="256" r="235" fill="url(#a-bg-glow)"/>

  <!-- Aggressive Demon Blade Spiked Crest -->
  <g filter="url(#a-shadow)">
    <!-- Razor Spikes Silhouette -->
    <path d="M 256,22 L 286,60 L 350,50 L 410,92 L 486,138 L 444,204 L 492,274 L 434,346 L 376,392 L 256,488
             L 136,392 L 78,346 L 20,274 L 68,204 L 26,138 L 102,92 L 162,50 L 226,60 Z"
          fill="#1c0409" stroke="url(#ruby-gold-rim)" stroke-width="5" stroke-linejoin="round"/>

    <!-- Outer Crimson Plate -->
    <path d="M 256,42 L 280,74 L 336,66 L 390,104 L 458,146 L 424,202 L 464,264 L 412,330 L 362,372 L 256,462
             L 150,372 L 100,330 L 48,264 L 88,202 L 54,146 L 122,104 L 176,66 L 232,74 Z"
          fill="url(#ruby-gold-rim)" stroke="#4c0519" stroke-width="2"/>

    <!-- Inner Ruby Heart Shield -->
    <path d="M 256,76 L 350,116 L 398,194 L 366,322 L 256,428 L 146,322 L 114,194 L 162,116 Z"
          fill="url(#crimson-core)" stroke="#f43f5e" stroke-width="3"/>

    <!-- Golden Spiked Battle Horns on Crest Top -->
    <polygon points="256,44 268,76 256,92 244,76" fill="#fde047" stroke="#881337" stroke-width="1.5"/>
    <polygon points="200,64 220,86 206,96" fill="#fde047" stroke="#881337" stroke-width="1.5"/>
    <polygon points="312,64 292,86 306,96" fill="#fde047" stroke="#881337" stroke-width="1.5"/>

    <!-- Glowing Ruby Facet Lines -->
    <line x1="256" y1="76" x2="256" y2="428" stroke="#ff4d4d" stroke-width="2" stroke-opacity="0.6"/>
    <line x1="162" y1="116" x2="366" y2="322" stroke="#ff4d4d" stroke-width="1.5" stroke-opacity="0.4"/>
    <line x1="350" y1="116" x2="146" y2="322" stroke="#ff4d4d" stroke-width="1.5" stroke-opacity="0.4"/>

    <!-- Floating Fiery Ember Particles -->
    <g fill="#fde047" opacity="0.8">
      <circle cx="106" cy="160" r="3"/>
      <circle cx="140" cy="98" r="2.5"/>
      <circle cx="380" cy="110" r="3"/>
      <circle cx="410" cy="180" r="2"/>
      <circle cx="370" cy="350" r="2.5"/>
      <circle cx="130" cy="360" r="3"/>
    </g>
  </g>

  <!-- Center Letter 'A' - Aggressive Dagger-Apex Blade -->
  <g filter="url(#a-glow)">
    <!-- 3D Cast Shadow -->
    <path d="M 256,118 L 364,374 L 306,374 L 282,316 L 230,316 L 206,374 L 148,374 Z
             M 256,184 L 274,272 L 238,272 Z"
          fill="#0c0103" transform="translate(6, 12)"/>

    <!-- Main Letter Face -->
    <path d="M 256,118 L 364,374 L 306,374 L 282,316 L 230,316 L 206,374 L 148,374 Z
             M 256,184 L 274,272 L 238,272 Z"
          fill="url(#a-letter-grad)" fill-rule="evenodd" stroke="#4c0519" stroke-width="3.5"/>

    <!-- Razor Blade Left Ridge -->
    <polygon points="256,118 256,184 238,272 230,316 206,374 148,374"
             fill="#ffffff" opacity="0.35"/>

    <!-- Razor Blade Right Ridge -->
    <polygon points="256,118 364,374 306,374 282,316 274,272 256,184"
             fill="#7f1d1d" opacity="0.6"/>

    <!-- Glowing Apex Specular Cut -->
    <polygon points="256,118 266,150 256,160 246,150" fill="#ffffff"/>
    <line x1="256" y1="118" x2="148" y2="374" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>
    <line x1="230" y1="316" x2="282" y2="316" stroke="#fecdd3" stroke-width="2.5"/>

    <!-- Inner Triangle Ruby Core -->
    <polygon points="256,184 274,272 238,272" fill="#2a020a" stroke="#fb7185" stroke-width="1.5"/>
  </g>

  <!-- Rank Label Banner at Bottom -->
  <g transform="translate(0, 428)">
    <polygon points="166,0 346,0 370,32 334,32 256,42 178,32 142,32"
             fill="#3b0713" stroke="#f43f5e" stroke-width="2.5"/>
    <text x="256" y="22" font-family="'Impact', 'Arial Black', sans-serif" font-size="18" font-weight="900"
          letter-spacing="5" fill="#fecdd3" text-anchor="middle">RANK A</text>
  </g>
</svg>'''


def get_rank_s_svg():
    """Rank S: Stylish / DMC Royal Gold & Scarlet Crest, Neon Cyan Lightning."""
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <defs>
    <!-- Filters -->
    <filter id="s-shadow" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="14" stdDeviation="22" flood-color="#000000" flood-opacity="0.9"/>
    </filter>
    <filter id="s-gold-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="#f59e0b" flood-opacity="0.8"/>
    </filter>
    <filter id="lightning-glow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="6" result="blur1"/>
      <feGaussianBlur stdDeviation="14" result="blur2"/>
      <feMerge>
        <feMergeNode in="blur2"/>
        <feMergeNode in="blur1"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="flame-aura-filter" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <!-- Gradients -->
    <radialGradient id="s-bg-vortex" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.7"/>
      <stop offset="35%" stop-color="#ef4444" stop-opacity="0.45"/>
      <stop offset="70%" stop-color="#7f1d1d" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#0b0303" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="s-gold-armor" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="20%" stop-color="#fef08a"/>
      <stop offset="45%" stop-color="#f59e0b"/>
      <stop offset="70%" stop-color="#b45309"/>
      <stop offset="90%" stop-color="#78350f"/>
      <stop offset="100%" stop-color="#fde047"/>
    </linearGradient>

    <linearGradient id="s-flame-plate" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#b91c1c"/>
      <stop offset="35%" stop-color="#7f1d1d"/>
      <stop offset="70%" stop-color="#450a0a"/>
      <stop offset="100%" stop-color="#1c0303"/>
    </linearGradient>

    <linearGradient id="s-letter-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="20%" stop-color="#fef08a"/>
      <stop offset="45%" stop-color="#f59e0b"/>
      <stop offset="75%" stop-color="#dc2626"/>
      <stop offset="100%" stop-color="#7f1d1d"/>
    </linearGradient>

    <linearGradient id="lightning-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e0ffff"/>
      <stop offset="50%" stop-color="#00ffff"/>
      <stop offset="100%" stop-color="#0099ff"/>
    </linearGradient>
  </defs>

  <!-- Blazing Vortex Ambient Core -->
  <circle cx="256" cy="256" r="240" fill="url(#s-bg-vortex)"/>

  <!-- Flaming Outer Silhouette Tongues -->
  <g filter="url(#flame-aura-filter)" opacity="0.85">
    <path d="M 256,12 C 280,45 310,35 330,70 C 350,60 380,85 395,115 C 430,110 460,150 465,190 C 490,230 480,280 460,320
             C 475,360 440,400 410,425 C 380,460 320,475 256,500 C 192,475 132,460 102,425 C 72,400 37,360 52,320
             C 32,280 22,230 47,190 C 52,150 82,110 117,115 C 132,85 162,60 182,70 C 202,35 232,45 256,12 Z"
          fill="#f97316" opacity="0.35"/>
    <path d="M 256,26 C 275,55 300,48 318,80 C 340,75 365,96 380,125 C 410,122 435,158 440,195 C 460,230 450,270 435,305
             C 448,340 420,375 395,398 C 365,430 310,448 256,470 C 202,448 147,430 117,398 C 92,375 64,340 77,305
             C 62,270 52,230 72,195 C 77,158 102,122 132,125 C 147,96 172,75 194,80 C 212,48 237,55 256,26 Z"
          fill="#ef4444" opacity="0.5"/>
  </g>

  <!-- Royal Golden Crest Shield -->
  <g filter="url(#s-shadow)">
    <!-- Flared Phoenix Razor Wings -->
    <path d="M 256,38 L 334,60 L 416,74 L 486,134 L 452,204 L 498,272 L 440,344 L 382,388 L 256,482
             L 130,388 L 72,344 L 14,272 L 60,204 L 26,134 L 96,74 L 178,60 Z"
          fill="#1c0702" stroke="url(#s-gold-armor)" stroke-width="6" stroke-linejoin="round"/>

    <!-- Layered Beveled Gold Plate -->
    <path d="M 256,54 L 324,74 L 398,88 L 456,142 L 426,202 L 466,262 L 416,328 L 366,368 L 256,454
             L 146,368 L 96,328 L 46,262 L 86,202 L 56,142 L 114,88 L 188,74 Z"
          fill="url(#s-gold-armor)" stroke="#3f1303" stroke-width="2"/>

    <!-- Inner Molten Scarlet Battle Plate -->
    <path d="M 256,78 L 352,116 L 398,190 L 366,316 L 256,420 L 146,316 L 114,190 L 160,116 Z"
          fill="url(#s-flame-plate)" stroke="#f59e0b" stroke-width="3.5"/>

    <!-- Crowned Tri-Spike at Crest Apex -->
    <polygon points="256,38 274,74 256,92 238,74" fill="#fde047" stroke="#78350f" stroke-width="1.5"/>
    <polygon points="194,56 216,84 200,94" fill="#fde047" stroke="#78350f" stroke-width="1.5"/>
    <polygon points="318,56 296,84 312,94" fill="#fde047" stroke="#78350f" stroke-width="1.5"/>

    <!-- Intricate Filigree Engravings -->
    <path d="M 170,130 C 210,140 230,160 256,160 C 282,160 302,140 342,130"
          fill="none" stroke="#fde047" stroke-width="2" opacity="0.6"/>
    <path d="M 170,370 C 210,360 230,340 256,340 C 282,340 302,360 342,370"
          fill="none" stroke="#fde047" stroke-width="2" opacity="0.6"/>
  </g>

  <!-- Crackling Neon Cyan Lightning Arcs -->
  <g filter="url(#lightning-glow)">
    <!-- Primary Bolt (Diagonal Across Crest) -->
    <path d="M 80,100 L 170,160 L 150,185 L 230,225 L 205,250 L 320,295 L 300,325 L 430,410"
          fill="none" stroke="#ffffff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="miter"/>
    <path d="M 80,100 L 170,160 L 150,185 L 230,225 L 205,250 L 320,295 L 300,325 L 430,410"
          fill="none" stroke="#00ffff" stroke-width="8" stroke-linecap="round" stroke-linejoin="miter" opacity="0.6"/>

    <!-- Secondary Branch Bolt -->
    <path d="M 420,80 L 350,140 L 365,160 L 290,210 L 310,230 L 220,330 L 235,350 L 140,430"
          fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round"/>
    <path d="M 420,80 L 350,140 L 365,160 L 290,210 L 310,230 L 220,330 L 235,350 L 140,430"
          fill="none" stroke="#00ffff" stroke-width="6" stroke-linecap="round" opacity="0.5"/>

    <!-- Sparks & Discharge Nodes -->
    <circle cx="170" cy="160" r="4" fill="#ffffff"/>
    <circle cx="320" cy="295" r="4" fill="#ffffff"/>
    <circle cx="350" cy="140" r="3.5" fill="#ffffff"/>
    <circle cx="220" cy="330" r="3.5" fill="#ffffff"/>
  </g>

  <!-- Center Letter 'S' - Iconic DMC Fighting Serif Letter -->
  <g filter="url(#s-gold-glow)">
    <!-- 3D Heavy Drop Shadow -->
    <path d="M 338,154 L 338,198 C 314,180 286,170 256,170 C 220,170 206,186 206,204 C 206,224 224,236 264,248
             C 324,266 350,290 350,330 C 350,378 308,400 254,400 C 212,400 174,386 148,362 L 148,316
             C 176,342 212,356 252,356 C 290,356 304,340 304,322 C 304,302 284,290 246,278
             C 188,260 162,236 162,198 C 162,152 204,126 256,126 C 292,126 322,136 338,154 Z"
          fill="#100301" transform="translate(6, 12)"/>

    <!-- Main Sculpted Body -->
    <path d="M 338,154 L 338,198 C 314,180 286,170 256,170 C 220,170 206,186 206,204 C 206,224 224,236 264,248
             C 324,266 350,290 350,330 C 350,378 308,400 254,400 C 212,400 174,386 148,362 L 148,316
             C 176,342 212,356 252,356 C 290,356 304,340 304,322 C 304,302 284,290 246,278
             C 188,260 162,236 162,198 C 162,152 204,126 256,126 C 292,126 322,136 338,154 Z"
          fill="url(#s-letter-grad)" stroke="#450a0a" stroke-width="4"/>

    <!-- Specular Blade Bevel Highlights -->
    <path d="M 338,154 C 322,136 292,126 256,126 C 204,126 162,152 162,198 C 162,236 188,260 246,278"
          fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>
    <path d="M 264,248 C 324,266 350,290 350,330 C 350,378 308,400 254,400"
          fill="none" stroke="#fde047" stroke-width="3" stroke-linecap="round"/>

    <!-- Upper & Lower Terminal Flairs -->
    <polygon points="338,154 354,166 338,198" fill="#fde047"/>
    <polygon points="148,362 132,350 148,316" fill="#fde047"/>
  </g>

  <!-- Rank Label Banner at Bottom -->
  <g transform="translate(0, 428)">
    <polygon points="160,0 352,0 376,32 338,32 256,42 174,32 136,32"
             fill="#2a0802" stroke="#f59e0b" stroke-width="2.5"/>
    <text x="256" y="22" font-family="'Impact', 'Arial Black', sans-serif" font-size="20" font-weight="900"
          letter-spacing="6" fill="#fef08a" text-anchor="middle">RANK S</text>
  </g>
</svg>'''


def get_rank_ss_svg():
    """Rank SS: Showtime / Twin S, Dual Chromatic Lightning (Cyan + Magenta), Quad Wings."""
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <defs>
    <!-- Filters -->
    <filter id="ss-shadow" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="16" stdDeviation="24" flood-color="#000000" flood-opacity="0.95"/>
    </filter>
    <filter id="ss-magenta-glow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="8" result="blur1"/>
      <feGaussianBlur stdDeviation="16" result="blur2"/>
      <feMerge>
        <feMergeNode in="blur2"/>
        <feMergeNode in="blur1"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="ss-cyan-glow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="8" result="blur1"/>
      <feGaussianBlur stdDeviation="16" result="blur2"/>
      <feMerge>
        <feMergeNode in="blur2"/>
        <feMergeNode in="blur1"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="ss-gold-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="#f59e0b" flood-opacity="0.85"/>
    </filter>

    <!-- Gradients -->
    <radialGradient id="ss-cosmic-bg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#7c3aed" stop-opacity="0.7"/>
      <stop offset="40%" stop-color="#be185d" stop-opacity="0.5"/>
      <stop offset="75%" stop-color="#1e1b4b" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#030209" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="ss-gold-rim" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="20%" stop-color="#fef08a"/>
      <stop offset="45%" stop-color="#f59e0b"/>
      <stop offset="75%" stop-color="#d97706"/>
      <stop offset="90%" stop-color="#78350f"/>
      <stop offset="100%" stop-color="#ffffff"/>
    </linearGradient>

    <linearGradient id="ss-dark-core" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#4c0519"/>
      <stop offset="40%" stop-color="#2e1065"/>
      <stop offset="80%" stop-color="#0f0728"/>
      <stop offset="100%" stop-color="#050212"/>
    </linearGradient>

    <linearGradient id="s1-gold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="25%" stop-color="#fde047"/>
      <stop offset="60%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>

    <linearGradient id="s2-gold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="25%" stop-color="#fef08a"/>
      <stop offset="55%" stop-color="#fbbf24"/>
      <stop offset="85%" stop-color="#ea580c"/>
      <stop offset="100%" stop-color="#991b1b"/>
    </linearGradient>
  </defs>

  <!-- Cosmic Nebula Ambient Core -->
  <circle cx="256" cy="256" r="242" fill="url(#ss-cosmic-bg)"/>

  <!-- Starburst Energy Rays in Background -->
  <g stroke="#ec4899" stroke-width="1.5" opacity="0.4">
    <line x1="256" y1="256" x2="30" y2="30"/>
    <line x1="256" y1="256" x2="482" y2="30"/>
    <line x1="256" y1="256" x2="482" y2="482"/>
    <line x1="256" y1="256" x2="30" y2="482"/>
    <line x1="256" y1="256" x2="256" y2="10"/>
    <line x1="256" y1="256" x2="256" y2="502"/>
  </g>

  <!-- Quad-Wing Imperial Battle Crest -->
  <g filter="url(#ss-shadow)">
    <!-- Outer Wing Extensions -->
    <path d="M 256,26 L 334,50 L 426,62 L 496,124 L 460,192 L 508,256 L 460,320 L 496,388 L 426,450 L 334,462 L 256,494
             L 178,462 L 86,450 L 16,388 L 52,320 L 4,256 L 52,192 L 16,124 L 86,62 L 178,50 Z"
          fill="#110519" stroke="url(#ss-gold-rim)" stroke-width="6" stroke-linejoin="round"/>

    <!-- Layered Beveled Facets -->
    <path d="M 256,44 L 324,66 L 406,78 L 468,134 L 436,192 L 476,256 L 436,320 L 468,378 L 406,434 L 324,446 L 256,472
             L 188,446 L 106,434 L 44,378 L 76,320 L 36,256 L 76,192 L 44,134 L 106,78 L 188,66 Z"
          fill="url(#ss-gold-rim)" stroke="#2e1065" stroke-width="2"/>

    <!-- Inner Dark Amethyst Plate -->
    <path d="M 256,68 L 360,108 L 410,186 L 380,326 L 256,438 L 132,326 L 102,186 L 152,108 Z"
          fill="url(#ss-dark-core)" stroke="#f59e0b" stroke-width="3.5"/>

    <!-- Gilded Crown Crest Horns -->
    <polygon points="256,26 276,64 256,84 236,64" fill="#ffffff" stroke="#b45309" stroke-width="1.5"/>
    <polygon points="186,44 208,74 192,86" fill="#fde047" stroke="#b45309" stroke-width="1.5"/>
    <polygon points="326,44 304,74 320,86" fill="#fde047" stroke="#b45309" stroke-width="1.5"/>
  </g>

  <!-- Cyan Plasma Lightning (Left-to-Right Strike) -->
  <g filter="url(#ss-cyan-glow)">
    <path d="M 30,120 L 120,180 L 100,205 L 190,250 L 165,275 L 290,320 L 265,348 L 430,440"
          fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>
    <path d="M 30,120 L 120,180 L 100,205 L 190,250 L 165,275 L 290,320 L 265,348 L 430,440"
          fill="none" stroke="#00f0ff" stroke-width="8" stroke-linecap="round" opacity="0.6"/>
  </g>

  <!-- Magenta Plasma Lightning (Right-to-Left Strike) -->
  <g filter="url(#ss-magenta-glow)">
    <path d="M 480,120 L 390,180 L 410,205 L 320,250 L 345,275 L 220,320 L 245,348 L 80,440"
          fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>
    <path d="M 480,120 L 390,180 L 410,205 L 320,250 L 345,275 L 220,320 L 245,348 L 80,440"
          fill="none" stroke="#ff007f" stroke-width="8" stroke-linecap="round" opacity="0.6"/>
  </g>

  <!-- Twin "SS" Letters in Staggered 3D Arcade Hierarchy -->
  <!-- Letter 1 (Left / Back S) -->
  <g transform="translate(-46, -10)" filter="url(#ss-gold-glow)">
    <!-- 3D Shadow -->
    <path d="M 284,166 L 284,204 C 264,188 238,180 214,180 C 182,180 170,194 170,210 C 170,226 186,236 220,248
             C 272,264 294,286 294,320 C 294,360 258,380 210,380 C 174,380 142,368 120,346 L 120,306
             C 144,328 174,342 208,342 C 240,342 254,328 254,314 C 254,296 236,286 204,274
             C 154,258 132,238 132,204 C 132,164 168,142 214,142 C 246,142 270,150 284,166 Z"
          fill="#0c0214" transform="translate(6, 12)"/>
    <!-- Body -->
    <path d="M 284,166 L 284,204 C 264,188 238,180 214,180 C 182,180 170,194 170,210 C 170,226 186,236 220,248
             C 272,264 294,286 294,320 C 294,360 258,380 210,380 C 174,380 142,368 120,346 L 120,306
             C 144,328 174,342 208,342 C 240,342 254,328 254,314 C 254,296 236,286 204,274
             C 154,258 132,238 132,204 C 132,164 168,142 214,142 C 246,142 270,150 284,166 Z"
          fill="url(#s1-gold)" stroke="#3b0764" stroke-width="3"/>
    <!-- Specular highlight -->
    <path d="M 284,166 C 270,150 246,142 214,142 C 168,142 132,164 132,204"
          fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>
  </g>

  <!-- Letter 2 (Right / Front S - Slightly Larger & Overlapping) -->
  <g transform="translate(46, 10)" filter="url(#ss-gold-glow)">
    <!-- 3D Shadow -->
    <path d="M 292,160 L 292,200 C 270,184 244,174 218,174 C 184,174 172,188 172,206 C 172,224 188,236 224,248
             C 280,266 304,288 304,324 C 304,366 266,386 216,386 C 178,386 144,372 120,350 L 120,308
             C 146,332 178,346 214,346 C 250,346 264,332 264,316 C 264,296 244,286 210,274
             C 156,258 132,236 132,200 C 132,158 170,134 218,134 C 252,134 278,144 292,160 Z"
          fill="#100302" transform="translate(6, 12)"/>
    <!-- Body -->
    <path d="M 292,160 L 292,200 C 270,184 244,174 218,174 C 184,174 172,188 172,206 C 172,224 188,236 224,248
             C 280,266 304,288 304,324 C 304,366 266,386 216,386 C 178,386 144,372 120,350 L 120,308
             C 146,332 178,346 214,346 C 250,346 264,332 264,316 C 264,296 244,286 210,274
             C 156,258 132,236 132,200 C 132,158 170,134 218,134 C 252,134 278,144 292,160 Z"
          fill="url(#s2-gold)" stroke="#7f1d1d" stroke-width="3.5"/>
    <!-- Specular highlight -->
    <path d="M 292,160 C 278,144 252,134 218,134 C 170,134 132,158 132,200"
          fill="none" stroke="#ffffff" stroke-width="3.5" stroke-linecap="round"/>
    <path d="M 224,248 C 280,266 304,288 304,324 C 304,366 266,386 216,386"
          fill="none" stroke="#fef08a" stroke-width="3" stroke-linecap="round"/>
  </g>

  <!-- Rank Label Banner at Bottom -->
  <g transform="translate(0, 432)">
    <polygon points="154,0 358,0 384,32 344,32 256,44 168,32 128,32"
             fill="#1e0524" stroke="#ec4899" stroke-width="2.5"/>
    <text x="256" y="23" font-family="'Impact', 'Arial Black', sans-serif" font-size="20" font-weight="900"
          letter-spacing="6" fill="#fef08a" text-anchor="middle">RANK SS</text>
  </g>
</svg>'''


def get_rank_sss_svg():
    """Rank SSS: Smoking Sexy Style / The Ultimate God-Tier Fighting Game Badge! Crowned, Inferno, Triple Lightning."""
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <defs>
    <!-- Filters -->
    <filter id="sss-god-shadow" x="-40%" y="-40%" width="180%" height="180%">
      <feDropShadow dx="0" dy="16" stdDeviation="28" flood-color="#000000" flood-opacity="0.95"/>
    </filter>
    <filter id="sss-corona" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="20" result="blur1"/>
      <feGaussianBlur stdDeviation="35" result="blur2"/>
      <feMerge>
        <feMergeNode in="blur2"/>
        <feMergeNode in="blur1"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="sss-lightning-arc" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="6" result="glow"/>
      <feMerge>
        <feMergeNode in="glow"/>
        <feMergeNode in="glow"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <!-- Gradients -->
    <radialGradient id="sss-solar-core" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="1"/>
      <stop offset="25%" stop-color="#fef08a" stop-opacity="0.9"/>
      <stop offset="50%" stop-color="#f59e0b" stop-opacity="0.75"/>
      <stop offset="75%" stop-color="#dc2626" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#050101" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="sss-crown-gold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="15%" stop-color="#fef08a"/>
      <stop offset="40%" stop-color="#f59e0b"/>
      <stop offset="65%" stop-color="#d97706"/>
      <stop offset="85%" stop-color="#78350f"/>
      <stop offset="100%" stop-color="#ffffff"/>
    </linearGradient>

    <linearGradient id="sss-abyss-plate" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#831843"/>
      <stop offset="30%" stop-color="#4c0519"/>
      <stop offset="70%" stop-color="#1e0208"/>
      <stop offset="100%" stop-color="#080002"/>
    </linearGradient>

    <linearGradient id="sss-letter-front" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="20%" stop-color="#fffbeb"/>
      <stop offset="40%" stop-color="#fde047"/>
      <stop offset="70%" stop-color="#f59e0b"/>
      <stop offset="90%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#7f1d1d"/>
    </linearGradient>

    <linearGradient id="sss-letter-side" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="30%" stop-color="#fef08a"/>
      <stop offset="65%" stop-color="#ea580c"/>
      <stop offset="100%" stop-color="#991b1b"/>
    </linearGradient>
  </defs>

  <!-- God-Tier Radiant Solar Corona -->
  <circle cx="256" cy="256" r="248" fill="url(#sss-solar-core)"/>

  <!-- Rotating Starburst Spikes / Sun Rays -->
  <g stroke="#fde047" stroke-width="2" opacity="0.45">
    <line x1="256" y1="256" x2="256" y2="4"/>
    <line x1="256" y1="256" x2="256" y2="508"/>
    <line x1="256" y1="256" x2="4" y2="256"/>
    <line x1="256" y1="256" x2="508" y2="256"/>
    <line x1="256" y1="256" x2="78" y2="78"/>
    <line x1="256" y1="256" x2="434" y2="434"/>
    <line x1="256" y1="256" x2="434" y2="78"/>
    <line x1="256" y1="256" x2="78" y2="434"/>
    <line x1="256" y1="256" x2="160" y2="30"/>
    <line x1="256" y1="256" x2="352" y2="482"/>
    <line x1="256" y1="256" x2="352" y2="30"/>
    <line x1="256" y1="256" x2="160" y2="482"/>
  </g>

  <!-- Raging Inferno Flame Silhouette Ring -->
  <g fill="#ea580c" opacity="0.45">
    <path d="M 256,6 C 290,40 330,30 354,72 C 380,60 416,92 432,130 C 470,120 500,165 504,210 C 530,255 515,310 490,355
             C 505,400 465,445 428,472 C 390,510 325,520 256,540 C 187,520 122,510 84,472 C 47,445 7,400 22,355
             C -3,310 -18,255 8,210 C 12,165 42,120 80,130 C 96,92 132,60 158,72 C 182,30 222,40 256,6 Z"/>
  </g>
  <g fill="#facc15" opacity="0.3">
    <path d="M 256,20 C 285,50 320,42 340,80 C 364,70 396,98 410,132 C 445,124 472,162 475,204 C 500,244 485,294 465,335
             C 478,375 442,415 410,438 C 375,472 315,482 256,500 C 197,482 137,472 102,438 C 70,415 34,375 47,335
             C 27,294 12,244 37,204 C 40,162 67,124 102,132 C 116,98 148,70 172,80 C 192,42 227,50 256,20 Z"/>
  </g>

  <!-- Imperial Golden Crown & Battle Crest -->
  <g filter="url(#sss-god-shadow)">
    <!-- Sweeping Celestial Phoenix Wings -->
    <path d="M 256,22 L 340,46 L 436,58 L 510,122 L 470,192 L 518,256 L 470,320 L 510,390 L 436,454 L 340,466 L 256,500
             L 172,466 L 76,454 L 2,390 L 42,320 L -6,256 L 42,192 L 2,122 L 76,58 L 172,46 Z"
          fill="#1c0307" stroke="url(#sss-crown-gold)" stroke-width="7" stroke-linejoin="round"/>

    <!-- Layered Beveled Wings -->
    <path d="M 256,38 L 330,60 L 416,72 L 480,130 L 446,192 L 486,256 L 446,320 L 480,382 L 416,438 L 330,450 L 256,478
             L 182,450 L 96,438 L 32,382 L 66,320 L 26,256 L 66,192 L 32,130 L 96,72 L 182,60 Z"
          fill="url(#sss-crown-gold)" stroke="#500724" stroke-width="2.5"/>

    <!-- Inner Imperial Crimson Shield Plate -->
    <path d="M 256,64 L 366,104 L 420,186 L 388,332 L 256,448 L 124,332 L 92,186 L 146,104 Z"
          fill="url(#sss-abyss-plate)" stroke="#f59e0b" stroke-width="4"/>

    <!-- Imperial Crown Atop Badge -->
    <g transform="translate(0, -6)">
      <!-- Crown Base -->
      <path d="M 194,56 L 318,56 L 334,80 L 178,80 Z" fill="#b45309" stroke="#fde047" stroke-width="2"/>
      <!-- Crown 5-Spikes -->
      <polygon points="256,12 268,56 244,56" fill="#ffffff" stroke="#d97706" stroke-width="2"/>
      <polygon points="214,24 230,56 202,56" fill="#fde047" stroke="#d97706" stroke-width="2"/>
      <polygon points="298,24 310,56 282,56" fill="#fde047" stroke="#d97706" stroke-width="2"/>
      <polygon points="178,40 196,56 172,56" fill="#f59e0b" stroke="#78350f" stroke-width="1.5"/>
      <polygon points="334,40 340,56 316,56" fill="#f59e0b" stroke="#78350f" stroke-width="1.5"/>
      <!-- Jewels on Crown -->
      <circle cx="256" cy="68" r="5" fill="#ef4444" stroke="#ffffff" stroke-width="1.5"/>
      <circle cx="216" cy="68" r="4" fill="#00f0ff" stroke="#ffffff" stroke-width="1"/>
      <circle cx="296" cy="68" r="4" fill="#00f0ff" stroke="#ffffff" stroke-width="1"/>
    </g>
  </g>

  <!-- Triple High-Voltage Lightning Bolts (Blinding Electric Storm) -->
  <g filter="url(#sss-lightning-arc)">
    <!-- Lightning Bolt 1 (Left Arc) -->
    <path d="M 20,80 L 110,150 L 90,175 L 180,220 L 155,248 L 260,295 L 240,325 L 360,420"
          fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>
    <path d="M 20,80 L 110,150 L 90,175 L 180,220 L 155,248 L 260,295 L 240,325 L 360,420"
          fill="none" stroke="#00ffff" stroke-width="7" stroke-linecap="round" opacity="0.6"/>

    <!-- Lightning Bolt 2 (Right Arc) -->
    <path d="M 490,80 L 400,150 L 420,175 L 330,220 L 355,248 L 250,295 L 270,325 L 150,420"
          fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>
    <path d="M 490,80 L 400,150 L 420,175 L 330,220 L 355,248 L 250,295 L 270,325 L 150,420"
          fill="none" stroke="#ff00ff" stroke-width="7" stroke-linecap="round" opacity="0.6"/>

    <!-- Lightning Bolt 3 (Vertical Ground Strike) -->
    <path d="M 256,80 L 240,150 L 270,185 L 245,260 L 275,320 L 256,440"
          fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round"/>
    <path d="M 256,80 L 240,150 L 270,185 L 245,260 L 275,320 L 256,440"
          fill="none" stroke="#fde047" stroke-width="6" stroke-linecap="round" opacity="0.5"/>
  </g>

  <!-- TRIPLE "SSS" LETTERS IN DYNAMIC STAGGERED FORMATION -->
  <!-- Letter 1 (Left S - Slightly Behind) -->
  <g transform="translate(-82, -4) scale(0.92) transform-origin(200 260)" filter="url(#sss-corona)">
    <!-- Shadow -->
    <path d="M 264,170 L 264,204 C 246,190 224,182 202,182 C 172,182 160,194 160,208 C 160,222 174,232 206,244
             C 256,260 276,280 276,312 C 276,350 242,370 198,370 C 164,370 134,358 114,338 L 114,302
             C 136,322 164,334 196,334 C 226,334 238,322 238,308 C 238,292 222,282 192,270
             C 144,256 124,236 124,204 C 124,168 158,146 202,146 C 232,146 252,154 264,170 Z"
          fill="#1c0205" transform="translate(6, 10)"/>
    <!-- Body -->
    <path d="M 264,170 L 264,204 C 246,190 224,182 202,182 C 172,182 160,194 160,208 C 160,222 174,232 206,244
             C 256,260 276,280 276,312 C 276,350 242,370 198,370 C 164,370 134,358 114,338 L 114,302
             C 136,322 164,334 196,334 C 226,334 238,322 238,308 C 238,292 222,282 192,270
             C 144,256 124,236 124,204 C 124,168 158,146 202,146 C 232,146 252,154 264,170 Z"
          fill="url(#sss-letter-side)" stroke="#7f1d1d" stroke-width="3"/>
    <path d="M 264,170 C 252,154 232,146 202,146 C 158,146 124,168 124,204"
          fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round"/>
  </g>

  <!-- Letter 3 (Right S - Slightly Behind) -->
  <g transform="translate(82, 16) scale(0.92) transform-origin(312 260)" filter="url(#sss-corona)">
    <!-- Shadow -->
    <path d="M 264,170 L 264,204 C 246,190 224,182 202,182 C 172,182 160,194 160,208 C 160,222 174,232 206,244
             C 256,260 276,280 276,312 C 276,350 242,370 198,370 C 164,370 134,358 114,338 L 114,302
             C 136,322 164,334 196,334 C 226,334 238,322 238,308 C 238,292 222,282 192,270
             C 144,256 124,236 124,204 C 124,168 158,146 202,146 C 232,146 252,154 264,170 Z"
          fill="#1c0205" transform="translate(6, 10)"/>
    <!-- Body -->
    <path d="M 264,170 L 264,204 C 246,190 224,182 202,182 C 172,182 160,194 160,208 C 160,222 174,232 206,244
             C 256,260 276,280 276,312 C 276,350 242,370 198,370 C 164,370 134,358 114,338 L 114,302
             C 136,322 164,334 196,334 C 226,334 238,322 238,308 C 238,292 222,282 192,270
             C 144,256 124,236 124,204 C 124,168 158,146 202,146 C 232,146 252,154 264,170 Z"
          fill="url(#sss-letter-side)" stroke="#7f1d1d" stroke-width="3"/>
    <path d="M 264,170 C 252,154 232,146 202,146 C 158,146 124,168 124,204"
          fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round"/>
  </g>

  <!-- Letter 2 (Center S - Forefront, Majestic, Radiant) -->
  <g transform="translate(0, 6) scale(1.08) transform-origin(256 260)" filter="url(#sss-corona)">
    <!-- Shadow -->
    <path d="M 326,156 L 326,196 C 304,180 278,170 252,170 C 218,170 206,184 206,202 C 206,220 222,232 258,244
             C 314,262 338,284 338,320 C 338,362 300,382 250,382 C 212,382 178,368 154,346 L 154,304
             C 180,328 212,342 248,342 C 284,342 298,328 298,312 C 298,292 278,282 244,270
             C 190,254 166,232 166,196 C 166,154 204,130 252,130 C 286,130 312,140 326,156 Z"
          fill="#100103" transform="translate(6, 12)"/>
    <!-- Body -->
    <path d="M 326,156 L 326,196 C 304,180 278,170 252,170 C 218,170 206,184 206,202 C 206,220 222,232 258,244
             C 314,262 338,284 338,320 C 338,362 300,382 250,382 C 212,382 178,368 154,346 L 154,304
             C 180,328 212,342 248,342 C 284,342 298,328 298,312 C 298,292 278,282 244,270
             C 190,254 166,232 166,196 C 166,154 204,130 252,130 C 286,130 312,140 326,156 Z"
          fill="url(#sss-letter-front)" stroke="#450a0a" stroke-width="4"/>
    <!-- Specular Blade Bevel Highlights -->
    <path d="M 326,156 C 312,140 286,130 252,130 C 204,130 166,154 166,196 C 166,232 190,254 244,270"
          fill="none" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
    <path d="M 258,244 C 314,262 338,284 338,320 C 338,362 300,382 250,382"
          fill="none" stroke="#fef08a" stroke-width="3" stroke-linecap="round"/>
    <!-- Specular Star Flare at S Apex -->
    <g transform="translate(326, 156)">
      <circle cx="0" cy="0" r="4" fill="#ffffff"/>
      <line x1="-12" y1="0" x2="12" y2="0" stroke="#ffffff" stroke-width="2"/>
      <line x1="0" y1="-12" x2="0" y2="12" stroke="#ffffff" stroke-width="2"/>
    </g>
  </g>

  <!-- Rank Label Banner at Bottom -->
  <g transform="translate(0, 436)">
    <polygon points="144,0 368,0 396,34 354,34 256,46 158,34 116,34"
             fill="#240307" stroke="#f59e0b" stroke-width="3"/>
    <text x="256" y="24" font-family="'Impact', 'Arial Black', sans-serif" font-size="20" font-weight="900"
          letter-spacing="6" fill="#fef08a" text-anchor="middle">RANK SSS</text>
  </g>
</svg>'''


def generate_all_ranks():
    ranks = [
        ("rank_d.svg", get_rank_d_svg()),
        ("rank_c.svg", get_rank_c_svg()),
        ("rank_b.svg", get_rank_b_svg()),
        ("rank_a.svg", get_rank_a_svg()),
        ("rank_s.svg", get_rank_s_svg()),
        ("rank_ss.svg", get_rank_ss_svg()),
        ("rank_sss.svg", get_rank_sss_svg()),
    ]
    
    print(f"Generating {len(ranks)} rank badges in {BASE_DIR}...")
    for filename, content in ranks:
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
    generate_all_ranks()
