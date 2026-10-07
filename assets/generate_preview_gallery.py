"""
generate_preview_gallery.py - Generates an HTML preview page showcasing all 22 TypeFighter SVG assets.
"""

import os

BASE_DIR = r"c:\Users\priya\OneDrive\Documents\Next Toppers\typefighter\assets"
OUTPUT_HTML = os.path.join(BASE_DIR, "preview_gallery.html")

RANKS = ["rank_d.svg", "rank_c.svg", "rank_b.svg", "rank_a.svg", "rank_s.svg", "rank_ss.svg", "rank_sss.svg"]
BELTS = [
    "belt_white.svg", "belt_yellow.svg", "belt_orange.svg", "belt_green.svg", "belt_blue.svg",
    "belt_purple.svg", "belt_brown.svg", "belt_red.svg", "belt_black.svg", "belt_grandmaster.svg"
]
STREAKS = ["streak_fire_15.svg", "streak_lightning_30.svg", "streak_overdrive_50.svg"]


def main():
    html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>TypeFighter Vector Asset Gallery</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: #090d16;
      color: #f1f5f9;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      padding: 40px 24px;
      line-height: 1.5;
    }
    .container { max-width: 1400px; margin: 0 auto; }
    header {
      text-align: center;
      margin-bottom: 50px;
      border-bottom: 1px solid #1e293b;
      padding-bottom: 30px;
    }
    h1 {
      font-size: 42px;
      font-weight: 900;
      letter-spacing: 4px;
      background: linear-gradient(135deg, #f59e0b, #ef4444, #ec4899, #00f0ff);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 10px;
      text-transform: uppercase;
    }
    .subtitle { color: #94a3b8; font-size: 16px; letter-spacing: 1px; }
    section { margin-bottom: 60px; }
    h2 {
      font-size: 24px;
      font-weight: 800;
      letter-spacing: 2px;
      color: #38bdf8;
      border-left: 4px solid #38bdf8;
      padding-left: 14px;
      margin-bottom: 24px;
      text-transform: uppercase;
    }
    .grid {
      display: grid;
      gap: 24px;
    }
    .grid-ranks { grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); }
    .grid-belts { grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); }
    .grid-streaks { grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); }

    .card {
      background: #111827;
      border: 1px solid #1f2937;
      border-radius: 14px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
      transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s;
    }
    .card:hover {
      transform: translateY(-4px);
      border-color: #38bdf8;
      box-shadow: 0 12px 24px rgba(0, 0, 0, 0.6);
    }
    .card img {
      width: 100%;
      max-width: 260px;
      height: auto;
      aspect-ratio: 1 / 1;
      display: block;
      margin-bottom: 14px;
    }
    .card-title {
      font-size: 14px;
      font-weight: 700;
      color: #e2e8f0;
      letter-spacing: 1px;
      text-align: center;
    }
    .card-sub {
      font-size: 12px;
      color: #64748b;
      margin-top: 4px;
    }
    .large-preview {
      background: #0f172a;
      border: 1px solid #1e293b;
      border-radius: 16px;
      padding: 24px;
      overflow-x: auto;
    }
    .large-preview img {
      width: 100%;
      height: auto;
      display: block;
      border-radius: 8px;
    }
    .badge {
      display: inline-block;
      padding: 2px 8px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 700;
      background: #1e293b;
      color: #38bdf8;
      margin-bottom: 8px;
    }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>TypeFighter Vector Assets</h1>
      <p class="subtitle">Complete SVG asset collection for arcade fighting game typing UI</p>
    </header>

    <!-- SECTION 1: RANKS -->
    <section>
      <h2>1. Rank Badges (DMC-Inspired Arcades)</h2>
      <div class="grid grid-ranks">
"""

    for r in RANKS:
        name = r.replace(".svg", "").replace("rank_", "RANK ").upper()
        html += f"""
        <div class="card">
          <span class="badge">BADGE</span>
          <img src="icons/ranks/{r}" alt="{name}">
          <div class="card-title">{name}</div>
          <div class="card-sub">{r}</div>
        </div>
"""

    html += """
      </div>
    </section>

    <!-- SECTION 2: BELTS -->
    <section>
      <h2>2. Martial Arts Belts</h2>
      <div class="grid grid-belts">
"""

    for b in BELTS:
        name = b.replace(".svg", "").replace("belt_", "").upper() + " BELT"
        html += f"""
        <div class="card">
          <span class="badge">OBI ICON</span>
          <img src="icons/belts/{b}" alt="{name}">
          <div class="card-title">{name}</div>
          <div class="card-sub">{b}</div>
        </div>
"""

    html += """
      </div>
    </section>

    <!-- SECTION 3: STREAKS -->
    <section>
      <h2>3. Combo Streak Badges</h2>
      <div class="grid grid-streaks">
"""

    for s in STREAKS:
        name = s.replace(".svg", "").replace("streak_", "").replace("_", " ").upper()
        html += f"""
        <div class="card">
          <span class="badge">STREAK BADGE</span>
          <img src="icons/streaks/{s}" alt="{name}">
          <div class="card-title">{name}</div>
          <div class="card-sub">{s}</div>
        </div>
"""

    html += """
      </div>
    </section>

    <!-- SECTION 4: KEYBOARD LAYOUT -->
    <section>
      <h2>4. Keyboard Layout (Dark Mode / 8 Finger Zones + Home Bumps)</h2>
      <div class="large-preview">
        <img src="ui/keyboard/keyboard_layout.svg" alt="Keyboard Layout">
      </div>
    </section>

    <!-- SECTION 5: HANDS GUIDE -->
    <section>
      <h2>5. Hands Guide Overlay (Transparent Home-Row Posture & Finger IDs)</h2>
      <div class="large-preview">
        <img src="ui/hands/hands_guide.svg" alt="Hands Guide">
      </div>
    </section>
  </div>
</body>
</html>
"""
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Preview gallery generated at: {OUTPUT_HTML}")


if __name__ == "__main__":
    main()
