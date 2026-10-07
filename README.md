# TypeFighter — Stickman Typing Beat 'Em Up 🥋⚡

> **A full-featured offline Windows desktop game that teaches touch typing from absolute zero (0 WPM) to 60+ WPM at 100% accuracy through spectacle fighter combat.**

Inspired by *Devil May Cry*, *Keyboard Warrior Stickman*, and *Street Fighter*, **TypeFighter** transforms typing practice into martial arts beat-'em-up combat. Every correct keystroke executes punches, kicks, and aerial launchers. Every finished word triggers devastating finishers and screen-clearing shockwaves.

---

## 🎮 Core Gameplay & Key Features

### 1. 🥊 2D Procedural Stickman Combat Engine (60 FPS)
- **16-Joint Skeletal Animation Rig**: Procedural Forward Kinematics (FK) system executing martial arts moves (jabs, straights, roundhouses, uppercuts, air juggles, ground slams).
- **5 Distinct Enemy Archetypes**:
  - **Grunts**: Single-letter scouts.
  - **Warriors**: 3–5 letter aggressive brawlers.
  - **Ninjas**: High-speed acrobats with rapid attack timers.
  - **Tanks**: Heavy armored units with endurance words.
  - **Bosses**: Multi-phase encounters with sentence battles and rage mechanics.
- **Combat Juice**: Frame freeze hit-stops on impact, dynamic camera shake, knockback physics, critical hit spark fountains, and ground dust puffs.

### 2. 🧠 Strict Stop-on-Error Pedagogy
- **Zero Bad Muscle Memory Consolidation**: Forward progress halts on typos. The target key never advances until the correct motor trace is executed, eliminating error habituation.
- **Real-Time Telemetry**: Gross WPM, Net WPM, 100% Accuracy enforcement, and per-key latency measurement.
- **Adaptive Weak-Key Trainer**: Automatically detects keys with <85% accuracy and dynamically injects targeted reinforcement drills.

### 3. 🖐️ Interactive Keyboard Overlay & Animated Hand Guides
- **Visual QWERTY Overlay**: Live keyboard with target key glowing and color-coded finger zones.
- **Animated Hand Guide**: Semi-transparent hands with real-time pulsing fingertips indicating the exact finger reach required.

### 4. ⚡ Devil May Cry Style Rank & Dopamine Progression
- **DMC Style Rank System**: `D (Dull)` → `C (Cool)` → `B (Bravo)` → `A (Awesome)` → `S (Stylish!)` → `SS (Super Stylish!!)` → `SSS (SMOKIN' SEXY STYLE!!!)`.
- **Keystroke Streaks**:
  - **15 Clean**: Fire Streak (Flame aura, 1.5x XP).
  - **30 Clean**: Lightning Streak (Electric aura, 2.0x XP).
  - **50 Clean**: Hyper Overdrive (Golden aura, 3.0x XP + screen-clearing special finisher).
- **10 Martial Arts Belts**: White → Yellow → Orange → Green → Blue → Purple → Brown → Red → Black → Grandmaster.
- **30-Day Practice Calendar**: Visual consistency punch-card tracking daily streaks and multiplier rewards.

### 5. 🏆 Five Complete Game Modes
1. **Story Campaign**: 5 Worlds × 10 Stages = 50 levels (Dojo warm-ups, street brawls, and boss encounters on stages 10, 20, 30, 40, 50).
2. **Endless Survival**: Infinite scaling waves with real-time peak WPM leaderboards.
3. **Daily Challenge**: Date-seeded deterministic challenges with streak bonus multipliers.
4. **Speed Test**: 1m / 2m / 3m timed prose tests using Project Gutenberg classics.
5. **Practice Dojo**: Zero-pressure training for home row, top row, bottom row, n-grams, numbers, and custom user text.

### 6. 🔊 Ultra-Low Latency Audio Engine
- Web Audio API buffer engine featuring 592 sound effects: Cherry MX mechanical thocks, heavy combat impacts, feedback jingles, and 6 adaptive music tracks.

---

## 🚀 Quick Start

### Prerequisites
- [Node.js](https://nodejs.org/) (v18+)
- Windows 10/11 (x64 or ARM64)

### 1. Run as Windows Desktop App (Electron)
```bash
npm install
npm start
```

### 2. Run Local Web Preview Server
```bash
npm run serve
```
Open [http://localhost:3000](http://localhost:3000) in your web browser.

### 3. Package Standalone Windows Desktop App (.exe)
```bash
npm run build:app
```
Produces a standalone, portable Windows application in `dist/TypeFighter/TypeFighter.exe`.

### 4. Run Automated Verification Test Suite
```bash
npm test
```
Executes 63 comprehensive integration tests verifying asset manifests, skeletal rig data, curriculum schemas, and typing pedagogy.

---

## 📂 Project Architecture

```
typefighter/
├── build/                 # Application icon assets (icon.ico, icon.png)
├── dist/                  # Packaged desktop application (TypeFighter.exe)
├── scripts/               # Desktop packaging script
├── assets/
│   ├── audio/             # 592 SFX and adaptive music tracks
│   ├── backgrounds/       # 5 World arena backgrounds (Dojo, Street, Factory, Rooftop, Boss Arena)
│   ├── data/              # 30-Day curriculum stages, 10k words, passages, ngrams
│   ├── fonts/             # Chakra Petch, Bebas Neue, JetBrains Mono, Press Start 2P
│   ├── icons/             # 10 Belt SVGs, 7 DMC Rank SVGs, 3 Streak SVGs
│   ├── sprites/           # 16-Joint procedural skeletal stickman rig and animation definitions
│   └── ui/                # Hands guide SVG and keyboard layout
├── src/
│   ├── engine/            # Combat engine, stickman rig renderer, particles, audio manager
│   ├── pedagogy/          # Stop-on-error typing engine, curriculum, keyboard guide, hand guide, adaptive tracker
│   ├── progression/       # DMC style rank, streaks, 10 belts, offline save manager, 30-day calendar
│   ├── modes/             # Story Campaign, Endless, Daily Challenge, Speed Test, Practice Dojo
│   ├── ui/                # HUD overlay, menu manager, modal dialogs
│   └── game.js            # Master 60 FPS runtime orchestrator
├── index.html             # Application viewport shell
├── styles.css             # Cyberpunk/Arcade design system
├── main.js                # Electron main process
├── preload.js             # Electron preload bridge
├── server.js              # Local HTTP preview server
└── package.json           # Scripts and dependencies
```

---

## 📜 License
MIT License. Open source and free for non-commercial and educational use.
