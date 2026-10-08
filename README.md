# Keyboard Warrior Stickman: Typing Beat 'Em Up 🥋⌨️

> **An authentic 1:1 open-source clone of the Steam beat 'em up phenomenon [Keyboard Warrior Stickman: Typing Beat 'Em Up](https://store.steampowered.com/app/4691530/Keyboard_Warrior_Stickman__Typing_Beat_Em_Up/) (by Good Knight Collective / itch.io Meme Combo Maker).**

Built with **Three.js WebGL 2.5D perspective rendering**, **crumpled notebook paper cutout stickmen standees**, **real-time contact drop shadows**, **low-latency Cherry MX mechanical keyboard audio**, and **Devil May Cry spectacle fighter combat**.

---

## 🎮 Core Gameplay & Authentic Parity Features

### 1. 📜 2.5D Notebook Paper Cutout Standee Engine (60 FPS)
- **Torn & Crumpled Ruled Paper Standees**: Faithful recreation of the viral stickman animation style with transparent chroma-keyed notebook cutouts.
- **Physical Contact Drop Shadows**: Standees project dynamic elliptical contact shadows onto the desk and floor surfaces in true 3D perspective.
- **Airborne Physics & Hit-Stops**: Gravity, air launch arcs, dive slams, and 60 FPS impact frame freezes (*hit-stops*).

### 2. 🏟️ 5 Authentic Arenas / Stages
1. **The Wooden Desk**: Battle directly on the office desk in front of the PC keyboard and mousepad.
2. **Retro CRT Computer**: Authentic beige 90s/2000s PC monitor setup.
3. **Windows XP Bliss**: The legendary rolling green hills and blue sky.
4. **untitled - MXPain**: Classic nostalgic MS Paint canvas window.
5. **Green Screen Studio**: Pure `#00ff00` chroma-key backdrop built for content creators to record TikToks, YouTube Shorts, and viral video memes.

### 3. 🎯 Floating Notebook Prompt with Red Cursor Box
- Prompts float directly above the combat arena on ruled notebook paper.
- **Authentic Red Rectangular Cursor Box**: Highlights the exact active letter to type with a red pulsing neon outline.
- **Real-Time Steam Metrics**: Bottom-left display tracking `[GOOD] / [MISS] / [% ACCURACY] / [TIME]`, plus `000,123` formatted score.

### 4. ⌨️ Physical Spectacle Control Keys
- **Spacebar**: **Air Launcher Kick!** Launches enemy paper standees high into the air for aerial juggle combos.
- **Enter**: **Ground Slam Finisher!** Spikes airborne enemies down into the desk with screen-shattering impact.
- **Tab**: **Dash / Teleport Evasion!** Evasive slide to reposition.
- **Caps Lock**: **Rage Fury Mode!** Red vignette aura, double damage, rapid-fire strikes.
- **WASD / Arrow Keys**: Walk and reposition horizontally across the desk plane.

### 5. ⚡ Devil May Cry Style Rank & Combo Engine
- Real-time DMC Style Rank: `D (DISMAL)` → `C (CRAZY)` → `B (BADASS)` → `A (APOCALYPTIC)` → `S (SAVAGE)` → `SS (SICK SKILLS)` → `SSS (SMOKIN' SEXY STYLE!)`.
- Dynamic Style decay meter and hit counter multiplier.

### 6. 🔊 Ultra-Low Latency Mechanical Keyboard Audio
- Web Audio API buffer engine with randomized Cherry MX switch thocks, error buzzers, combat punch/kick impacts, whooshes, and adaptive background music.

### 7. 🛠️ Meme Combo Maker Menu (ESC / Top Bar)
- Custom sentence input: type or paste custom text/memes.
- One-click arena switcher.
- Instant preset meme phrases (*"THIS IS A TYPING GAME."*, *"I AM THE STORM THAT IS APPROACHING"*, *"STANDING HERE I REALIZE"*, *"RULES OF NATURE"*, *"SKIBIDI TOILET IN OHIO"*).
- Audio and volume sliders.

---

## 🚀 Quick Start

### 1. Run as Windows Desktop App (Electron)
```bash
npm install
npm start
```

### 2. Run in Web Browser
```bash
npm run serve
```
Open your browser at `http://localhost:3000`.

### 3. Run Automated 1:1 Verification Test Suite
```bash
npm test
```

### 4. Build Standalone Desktop Executable (.exe)
```bash
npm run build:app
```
Packages the complete standalone portable executable at:
`dist/TypeFighter/TypeFighter.exe`

---

## 🕹️ Controls

| Key | Action |
| :--- | :--- |
| **A-Z / 0-9 / Symbols** | Type prompt characters & execute light/heavy combat strikes |
| **Spacebar** | Air Launcher Kick *(launches enemy into airborne juggle)* |
| **Enter** | Ground Slam Finisher *(spikes airborne enemy into desk)* |
| **Tab** | Evasive Dash |
| **Caps Lock** | Toggle Rage Fury Mode *(red aura, 2x damage)* |
| **A / D or Left / Right** | Walk / Reposition standee |
| **ESC** | Open / Close Meme Combo Maker & Arena Switcher |
| **F11** | Toggle Fullscreen |

---

## 📄 License
MIT Open Source License. Assets and fan homage inspired by Good Knight Collective's *Keyboard Warrior Stickman*.
