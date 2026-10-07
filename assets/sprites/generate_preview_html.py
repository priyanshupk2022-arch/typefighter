import json

def generate_preview_html():
    with open(r"c:\Users\priya\OneDrive\Documents\Next Toppers\typefighter\assets\sprites\stickman_rig.json", "r", encoding="utf-8") as f:
        rig_json_content = f.read()

    html_code = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TypeFighter - Procedural Stickman Rig & Animation Demo</title>
  <style>
    :root {{
      --bg-dark: #0a0c14;
      --panel-bg: rgba(16, 20, 32, 0.85);
      --panel-border: rgba(0, 240, 255, 0.25);
      --cyan: #00f0ff;
      --cyan-glow: rgba(0, 240, 255, 0.4);
      --red: #ff2244;
      --green: #00ff66;
      --boss: #ff0055;
      --text: #e2e8f0;
      --text-muted: #94a3b8;
      --font-mono: 'JetBrains Mono', 'Fira Code', monospace;
      --font-display: 'Bebas Neue', 'Chakra Petch', sans-serif;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      user-select: none;
    }}

    body {{
      background: var(--bg-dark);
      background-image: 
        radial-gradient(circle at 50% 10%, rgba(0, 240, 255, 0.08) 0%, transparent 60%),
        radial-gradient(circle at 80% 90%, rgba(255, 34, 68, 0.05) 0%, transparent 50%),
        linear-gradient(to bottom, #08090f 0%, #0d111a 100%);
      color: var(--text);
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }}

    header {{
      background: rgba(10, 12, 20, 0.9);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--panel-border);
      padding: 12px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      z-index: 10;
    }}

    .logo-badge {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .logo-badge h1 {{
      font-size: 24px;
      letter-spacing: 2px;
      text-transform: uppercase;
      font-weight: 900;
      background: linear-gradient(90deg, #00f0ff, #fff, #ff2244);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      text-shadow: 0 0 20px rgba(0, 240, 255, 0.4);
    }}

    .logo-badge .tag {{
      background: rgba(0, 240, 255, 0.15);
      border: 1px solid var(--cyan);
      color: var(--cyan);
      font-size: 11px;
      font-family: var(--font-mono);
      padding: 2px 8px;
      border-radius: 4px;
      letter-spacing: 1px;
    }}

    .header-stats {{
      display: flex;
      gap: 20px;
      font-family: var(--font-mono);
      font-size: 12px;
      color: var(--text-muted);
    }}

    .header-stats span strong {{
      color: var(--cyan);
    }}

    main {{
      display: grid;
      grid-template-columns: 1fr 380px;
      gap: 16px;
      padding: 16px;
      flex: 1;
      max-width: 1700px;
      margin: 0 auto;
      width: 100%;
    }}

    @media (max-width: 1100px) {{
      main {{
        grid-template-columns: 1fr;
      }}
    }}

    /* Canvas Stage Container */
    .viewport-card {{
      background: var(--panel-bg);
      border: 1px solid var(--panel-border);
      border-radius: 12px;
      display: flex;
      flex-direction: column;
      position: relative;
      overflow: hidden;
      box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.05);
    }}

    .viewport-canvas-wrap {{
      flex: 1;
      position: relative;
      min-height: 520px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: #06080e;
      overflow: hidden;
    }}

    canvas#fighterCanvas {{
      display: block;
      width: 100%;
      height: 100%;
      object-fit: contain;
    }}

    /* Overlay HUD inside canvas */
    .canvas-hud-top {{
      position: absolute;
      top: 14px;
      left: 16px;
      right: 16px;
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      pointer-events: none;
    }}

    .anim-title-pill {{
      background: rgba(0, 0, 0, 0.7);
      backdrop-filter: blur(8px);
      border: 1px solid var(--cyan-glow);
      border-radius: 8px;
      padding: 8px 14px;
      display: flex;
      flex-direction: column;
      gap: 2px;
    }}

    .anim-title-pill .anim-name {{
      font-size: 16px;
      font-weight: 800;
      color: #fff;
      letter-spacing: 0.5px;
    }}

    .anim-title-pill .anim-sub {{
      font-size: 11px;
      font-family: var(--font-mono);
      color: var(--cyan);
    }}

    .theme-active-pill {{
      background: rgba(0, 0, 0, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.2);
      border-radius: 8px;
      padding: 6px 12px;
      font-family: var(--font-mono);
      font-size: 11px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .theme-dot {{
      width: 10px;
      height: 10px;
      border-radius: 50%;
      display: inline-block;
      box-shadow: 0 0 8px currentColor;
    }}

    /* Canvas Bottom Timeline Controls */
    .timeline-bar {{
      background: rgba(8, 10, 18, 0.95);
      border-top: 1px solid var(--panel-border);
      padding: 10px 16px;
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .btn-icon {{
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: var(--text);
      width: 34px;
      height: 34px;
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.15s ease;
      font-size: 14px;
    }}

    .btn-icon:hover {{
      background: rgba(0, 240, 255, 0.2);
      border-color: var(--cyan);
      color: var(--cyan);
      transform: translateY(-1px);
    }}

    .btn-icon:active {{
      transform: translateY(1px);
    }}

    .timeline-slider-wrap {{
      flex: 1;
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .timeline-slider-wrap input[type="range"] {{
      flex: 1;
      height: 6px;
      -webkit-appearance: none;
      background: #1e293b;
      border-radius: 3px;
      outline: none;
      cursor: pointer;
    }}

    .timeline-slider-wrap input[type="range"]::-webkit-slider-thumb {{
      -webkit-appearance: none;
      width: 14px;
      height: 14px;
      border-radius: 50%;
      background: var(--cyan);
      box-shadow: 0 0 10px var(--cyan);
      cursor: pointer;
    }}

    .frame-badge {{
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--text-muted);
      min-width: 70px;
      text-align: right;
    }}

    /* Side Control Panel */
    .controls-panel {{
      background: var(--panel-bg);
      border: 1px solid var(--panel-border);
      border-radius: 12px;
      display: flex;
      flex-direction: column;
      gap: 16px;
      padding: 18px;
      overflow-y: auto;
      max-height: calc(100vh - 100px);
    }}

    .section-title {{
      font-size: 12px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 1.5px;
      color: var(--cyan);
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 8px;
      border-bottom: 1px solid rgba(0, 240, 255, 0.15);
      padding-bottom: 4px;
    }}

    /* Martial Arts Move Buttons */
    .moves-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 8px;
    }}

    .btn-move {{
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 8px;
      padding: 9px 10px;
      text-align: left;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
      gap: 3px;
      position: relative;
      overflow: hidden;
    }}

    .btn-move::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 3px;
      height: 100%;
      background: transparent;
      transition: background 0.2s;
    }}

    .btn-move:hover {{
      background: rgba(0, 240, 255, 0.1);
      border-color: rgba(0, 240, 255, 0.4);
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(0, 240, 255, 0.15);
    }}

    .btn-move:active {{
      transform: translateY(0);
    }}

    .btn-move.active {{
      background: rgba(0, 240, 255, 0.18);
      border-color: var(--cyan);
      box-shadow: 0 0 16px rgba(0, 240, 255, 0.25);
    }}

    .btn-move.active::before {{
      background: var(--cyan);
    }}

    .btn-move .move-num {{
      font-family: var(--font-mono);
      font-size: 9px;
      color: var(--text-muted);
      letter-spacing: 0.5px;
    }}

    .btn-move .move-name {{
      font-size: 12px;
      font-weight: 700;
      color: #fff;
    }}

    .btn-move .move-badge {{
      font-size: 9px;
      font-family: var(--font-mono);
      color: var(--cyan);
    }}

    /* Combo Sequencer Row */
    .combo-row {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 6px;
    }}

    .btn-combo {{
      background: linear-gradient(135deg, rgba(255, 34, 68, 0.15), rgba(0, 240, 255, 0.15));
      border: 1px solid rgba(255, 34, 68, 0.35);
      border-radius: 6px;
      padding: 8px 6px;
      color: #fff;
      font-size: 11px;
      font-weight: 700;
      cursor: pointer;
      text-align: center;
      transition: all 0.2s ease;
    }}

    .btn-combo:hover {{
      border-color: #ff2244;
      background: linear-gradient(135deg, rgba(255, 34, 68, 0.3), rgba(0, 240, 255, 0.3));
      box-shadow: 0 0 14px rgba(255, 34, 68, 0.3);
      transform: translateY(-1px);
    }}

    /* Themes Selection */
    .themes-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 8px;
    }}

    .btn-theme {{
      display: flex;
      align-items: center;
      gap: 8px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 6px;
      padding: 8px 10px;
      cursor: pointer;
      font-size: 11px;
      font-weight: 600;
      color: var(--text);
      transition: all 0.15s ease;
    }}

    .btn-theme:hover {{
      background: rgba(255, 255, 255, 0.09);
      border-color: rgba(255, 255, 255, 0.3);
    }}

    .btn-theme.active {{
      border-color: #fff;
      background: rgba(255, 255, 255, 0.14);
      box-shadow: 0 0 10px rgba(255, 255, 255, 0.15);
    }}

    .btn-theme .t-color {{
      width: 12px;
      height: 12px;
      border-radius: 50%;
      flex-shrink: 0;
    }}

    /* Toggles Grid */
    .toggles-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 6px;
    }}

    .toggle-chip {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 6px;
      padding: 6px 10px;
      font-size: 11px;
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.15s ease;
    }}

    .toggle-chip:hover {{
      border-color: rgba(255, 255, 255, 0.2);
      color: var(--text);
    }}

    .toggle-chip.active {{
      border-color: var(--cyan);
      color: var(--cyan);
      background: rgba(0, 240, 255, 0.1);
    }}

    /* Speed and Scale Sliders */
    .param-row {{
      display: flex;
      flex-direction: column;
      gap: 4px;
      margin-bottom: 6px;
    }}

    .param-header {{
      display: flex;
      justify-content: space-between;
      font-size: 11px;
      color: var(--text-muted);
      font-family: var(--font-mono);
    }}

    .param-slider {{
      width: 100%;
      height: 4px;
      -webkit-appearance: none;
      background: #1e293b;
      border-radius: 2px;
      outline: none;
    }}

    .param-slider::-webkit-slider-thumb {{
      -webkit-appearance: none;
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: var(--cyan);
      cursor: pointer;
    }}

    /* Inspector / Telemetry details */
    .telemetry-box {{
      background: rgba(0, 0, 0, 0.4);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 6px;
      padding: 8px;
      font-family: var(--font-mono);
      font-size: 10px;
      line-height: 1.5;
      color: var(--text-muted);
      max-height: 130px;
      overflow-y: auto;
    }}

    .telemetry-box span {{
      color: var(--cyan);
    }}

    /* Footer */
    footer {{
      padding: 10px 24px;
      border-top: 1px solid rgba(255, 255, 255, 0.05);
      text-align: center;
      font-size: 11px;
      color: #64748b;
      font-family: var(--font-mono);
    }}
  </style>
</head>
<body>

  <header>
    <div class="logo-badge">
      <h1>TypeFighter</h1>
      <span class="tag">PROCEDURAL SKELETON RIG v1.0</span>
    </div>
    <div class="header-stats">
      <span>FPS: <strong id="fpsVal">60.0</strong></span>
      <span>JOINTS: <strong>16 RIGGED</strong></span>
      <span>POSES: <strong>10 KEYFRAMED</strong></span>
      <span>RENDER: <strong>CANVAS 2D 60FPS</strong></span>
    </div>
  </header>

  <main>
    <!-- Viewport Area -->
    <div class="viewport-card">
      <div class="viewport-canvas-wrap" id="canvasWrap">
        <canvas id="fighterCanvas"></canvas>

        <div class="canvas-hud-top">
          <div class="anim-title-pill">
            <span class="anim-name" id="hudAnimTitle">Combat Idle</span>
            <span class="anim-sub" id="hudAnimCategory">STANCE &bull; 60 FRAMES &bull; LOOPING</span>
          </div>

          <div class="theme-active-pill" id="hudThemeBadge">
            <span class="theme-dot" id="hudThemeDot" style="background:#00f0ff; color:#00f0ff;"></span>
            <span id="hudThemeName">Hero Cyan Glow</span>
          </div>
        </div>
      </div>

      <!-- Bottom Playback Timeline -->
      <div class="timeline-bar">
        <button class="btn-icon" id="btnPlayPause" title="Play/Pause">⏸</button>
        <button class="btn-icon" id="btnPrevFrame" title="Previous Frame">⏮</button>
        <button class="btn-icon" id="btnNextFrame" title="Next Frame">⏭</button>
        <button class="btn-icon" id="btnFlip" title="Flip Direction (Facing Left/Right)">⇄</button>
        
        <div class="timeline-slider-wrap">
          <input type="range" id="frameScrubber" min="0" max="60" value="0" step="1">
          <div class="frame-badge"><span id="curFrameNum">0</span> / <span id="maxFrameNum">60</span> F</div>
        </div>

        <button class="btn-icon" id="btnAudioToggle" title="Audio Sound FX (Web Audio Synth)">🔊</button>
      </div>
    </div>

    <!-- Controls Panel -->
    <div class="controls-panel">
      <!-- 1. Martial Arts Moves Grid -->
      <div>
        <div class="section-title">Martial Arts Moves</div>
        <div class="moves-grid" id="movesContainer">
          <!-- Dynamically populated buttons -->
        </div>
      </div>

      <!-- 2. Combos -->
      <div>
        <div class="section-title">Combo Chains & Showcase</div>
        <div class="combo-row">
          <button class="btn-combo" id="btnComboBnB">⚡ 3-Hit Strike</button>
          <button class="btn-combo" id="btnComboAir">🌪 Aerial Launch</button>
          <button class="btn-combo" id="btnShowcase">▶ All Moves</button>
        </div>
      </div>

      <!-- 3. Themes -->
      <div>
        <div class="section-title">Color Themes</div>
        <div class="themes-grid" id="themesContainer">
          <!-- Theme buttons -->
        </div>
      </div>

      <!-- 4. Visual FX & Skeleton Toggles -->
      <div>
        <div class="section-title">Visual FX & Overlays</div>
        <div class="toggles-grid">
          <div class="toggle-chip active" id="togTrails"><span>Motion Trails</span><span class="tog-st">ON</span></div>
          <div class="toggle-chip active" id="togSparks"><span>Hit Sparks</span><span class="tog-st">ON</span></div>
          <div class="toggle-chip active" id="togAura"><span>Radiant Aura</span><span class="tog-st">ON</span></div>
          <div class="toggle-chip active" id="togShockwave"><span>Shockwaves</span><span class="tog-st">ON</span></div>
          <div class="toggle-chip" id="togSkeleton"><span>Bone Hierarchy</span><span class="tog-st">OFF</span></div>
          <div class="toggle-chip" id="togJointLabels"><span>Joint Markers</span><span class="tog-st">OFF</span></div>
        </div>
      </div>

      <!-- 5. Speed & Zoom Tuning -->
      <div>
        <div class="section-title">Playback Tuning</div>
        <div class="param-row">
          <div class="param-header">
            <span>PLAYBACK SPEED</span>
            <span id="speedVal">1.0x</span>
          </div>
          <input type="range" class="param-slider" id="speedSlider" min="0.1" max="2.0" step="0.05" value="1.0">
        </div>

        <div class="param-row">
          <div class="param-header">
            <span>SCALE ZOOM</span>
            <span id="scaleVal">1.75x</span>
          </div>
          <input type="range" class="param-slider" id="scaleSlider" min="1.0" max="2.8" step="0.05" value="1.75">
        </div>
      </div>

      <!-- 6. Rig Inspector / Telemetry -->
      <div>
        <div class="section-title">Rig Telemetry & Joint Angles</div>
        <div class="telemetry-box" id="telemetryBox">
          Loading skeletal telemetry...
        </div>
      </div>
    </div>
  </main>

  <footer>
    TypeFighter &copy; 2026 &bull; Procedural Skeletal Animation Rig &bull; High-DPI Canvas 60 FPS
  </footer>

  <!-- Embedded Rig JSON for standalone offline file:// execution -->
  <script id="embedded-rig-data" type="application/json">
{rig_json_content}
  </script>

  <script>
    (function() {{
      // --- AUDIO SYNTHESIS ENGINE (Web Audio API) ---
      let audioCtx = null;
      let soundEnabled = true;

      function initAudio() {{
        if (!audioCtx) {{
          const AudioContextClass = window.AudioContext || window.webkitAudioContext;
          if (AudioContextClass) audioCtx = new AudioContextClass();
        }}
        if (audioCtx && audioCtx.state === 'suspended') {{
          audioCtx.resume();
        }}
      }}

      function playWhoosh(speed = 1.0) {{
        if (!soundEnabled || !audioCtx) return;
        try {{
          const osc = audioCtx.createOscillator();
          const gain = audioCtx.createGain();
          const filter = audioCtx.createBiquadFilter();

          osc.type = 'sine';
          osc.frequency.setValueAtTime(320 * speed, audioCtx.currentTime);
          osc.frequency.exponentialRampToValueAtTime(100, audioCtx.currentTime + 0.12);

          filter.type = 'lowpass';
          filter.frequency.setValueAtTime(800, audioCtx.currentTime);

          gain.gain.setValueAtTime(0.2, audioCtx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.12);

          osc.connect(filter);
          filter.connect(gain);
          gain.connect(audioCtx.destination);

          osc.start();
          osc.stop(audioCtx.currentTime + 0.13);
        }} catch(e) {{}}
      }}

      function playHitImpact(power = 1.0) {{
        if (!soundEnabled || !audioCtx) return;
        try {{
          // Noise burst
          const bufferSize = audioCtx.sampleRate * 0.08;
          const buffer = audioCtx.createBuffer(1, bufferSize, audioCtx.sampleRate);
          const data = buffer.getChannelData(0);
          for (let i = 0; i < bufferSize; i++) {{
            data[i] = (Math.random() * 2 - 1) * Math.exp(-i / (bufferSize * 0.25));
          }}
          const noise = audioCtx.createBufferSource();
          noise.buffer = buffer;

          const filter = audioCtx.createBiquadFilter();
          filter.type = 'bandpass';
          filter.frequency.setValueAtTime(450 * power, audioCtx.currentTime);

          const gain = audioCtx.createGain();
          gain.gain.setValueAtTime(0.35 * power, audioCtx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.15);

          // Sub thud
          const osc = audioCtx.createOscillator();
          const oscGain = audioCtx.createGain();
          osc.frequency.setValueAtTime(180, audioCtx.currentTime);
          osc.frequency.exponentialRampToValueAtTime(35, audioCtx.currentTime + 0.18);
          oscGain.gain.setValueAtTime(0.4 * power, audioCtx.currentTime);
          oscGain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.18);

          noise.connect(filter);
          filter.connect(gain);
          gain.connect(audioCtx.destination);

          osc.connect(oscGain);
          oscGain.connect(audioCtx.destination);

          noise.start();
          osc.start();
          noise.stop(audioCtx.currentTime + 0.16);
          osc.stop(audioCtx.currentTime + 0.2);
        }} catch(e) {{}}
      }}

      function playSlamSound() {{
        if (!soundEnabled || !audioCtx) return;
        try {{
          const osc = audioCtx.createOscillator();
          const gain = audioCtx.createGain();
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(120, audioCtx.currentTime);
          osc.frequency.exponentialRampToValueAtTime(25, audioCtx.currentTime + 0.35);

          gain.gain.setValueAtTime(0.5, audioCtx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.35);

          osc.connect(gain);
          gain.connect(audioCtx.destination);
          osc.start();
          osc.stop(audioCtx.currentTime + 0.36);
        }} catch(e) {{}}
      }}

      // --- SKELETON & RIG DATA LOADER ---
      let rigData = null;
      try {{
        const el = document.getElementById('embedded-rig-data');
        if (el) rigData = JSON.parse(el.textContent);
      }} catch(err) {{
        console.warn("Failed to parse embedded rig data:", err);
      }}

      // Async fetch attempt if available
      fetch('stickman_rig.json')
        .then(res => res.json())
        .then(data => {{
          rigData = data;
          initApp();
        }})
        .catch(err => {{
          console.log("Local fetch not available (running in file:// mode or embedded), using embedded rig data.");
          initApp();
        }});

      function initApp() {{
        if (!rigData) {{
          alert("Error: stickman_rig.json could not be loaded.");
          return;
        }}
        setupEngine();
      }}

      function setupEngine() {{
        const canvas = document.getElementById('fighterCanvas');
        const ctx = canvas.getContext('2d');
        const wrap = document.getElementById('canvasWrap');

        // State
        let currentThemeId = 'hero';
        let currentAnimName = 'idle';
        let isPlaying = true;
        let animProgress = 0; // in frames (float)
        let playbackSpeed = 1.0;
        let modelScale = 1.75;
        let facingDirection = 1; // 1 = right, -1 = left
        let screenShake = 0;

        // Visual Toggles
        const toggles = {{
          trails: true,
          sparks: true,
          aura: true,
          shockwave: true,
          skeleton: false,
          jointLabels: false
        }};

        // Particle System & Trails Buffer
        const particles = [];
        const shockwaves = [];
        const trailsHistory = []; // queue of previous skeleton poses
        const MAX_TRAILS = 12;

        // Combos queue
        let comboQueue = [];
        let comboTimer = 0;

        // Resize Canvas with Retina DPI
        function resize() {{
          const rect = wrap.getBoundingClientRect();
          const dpr = window.devicePixelRatio || 1;
          canvas.width = rect.width * dpr;
          canvas.height = rect.height * dpr;
          ctx.resetTransform();
          ctx.scale(dpr, dpr);
        }}
        window.addEventListener('resize', resize);
        resize();

        // Populate Moves Grid
        const movesContainer = document.getElementById('movesContainer');
        movesContainer.innerHTML = '';
        const animList = Object.keys(rigData.animations);

        animList.forEach((key, idx) => {{
          const anim = rigData.animations[key];
          const btn = document.createElement('button');
          btn.className = `btn-move ${{key === currentAnimName ? 'active' : ''}}`;
          btn.id = `btn_anim_${{key}}`;
          btn.innerHTML = `
            <span class="move-num">0${{idx + 1}} &bull; ${{anim.category || 'MOVE'}}</span>
            <span class="move-name">${{anim.displayName || key}}</span>
            <span class="move-badge">${{anim.durationFrames}}F (${{Math.round(anim.durationSeconds * 1000)}}ms)</span>
          `;
          btn.addEventListener('click', () => {{
            initAudio();
            switchAnimation(key);
          }});
          movesContainer.appendChild(btn);
        }});

        // Populate Themes Grid
        const themesContainer = document.getElementById('themesContainer');
        themesContainer.innerHTML = '';
        Object.keys(rigData.themes).forEach(tKey => {{
          const th = rigData.themes[tKey];
          const btn = document.createElement('button');
          btn.className = `btn-theme ${{tKey === currentThemeId ? 'active' : ''}}`;
          btn.id = `theme_${{tKey}}`;
          btn.innerHTML = `
            <span class="t-color" style="background:${{th.primary}}; box-shadow: 0 0 8px ${{th.primary}};"></span>
            <span>${{th.name}}</span>
          `;
          btn.addEventListener('click', () => {{
            setTheme(tKey);
          }});
          themesContainer.appendChild(btn);
        }});

        function setTheme(themeId) {{
          currentThemeId = themeId;
          const th = rigData.themes[themeId];
          document.querySelectorAll('.btn-theme').forEach(b => b.classList.remove('active'));
          const activeBtn = document.getElementById(`theme_${{themeId}}`);
          if (activeBtn) activeBtn.classList.add('active');

          document.getElementById('hudThemeName').textContent = th.name;
          const dot = document.getElementById('hudThemeDot');
          dot.style.background = th.primary;
          dot.style.color = th.primary;
        }}

        function switchAnimation(animKey, isComboStep = false) {{
          if (!rigData.animations[animKey]) return;
          if (!isComboStep) comboQueue = [];

          currentAnimName = animKey;
          animProgress = 0;
          isPlaying = true;
          document.getElementById('btnPlayPause').textContent = '⏸';

          const anim = rigData.animations[animKey];
          document.querySelectorAll('.btn-move').forEach(b => b.classList.remove('active'));
          const btn = document.getElementById(`btn_anim_${{animKey}}`);
          if (btn) btn.classList.add('active');

          // Update HUD
          document.getElementById('hudAnimTitle').textContent = anim.displayName || animKey;
          document.getElementById('hudAnimCategory').textContent = 
            `${{anim.category || 'ACTION'}} • ${{anim.durationFrames}} FRAMES • ${{anim.loop ? 'LOOPING' : 'ONESHOT'}}`;

          // Update timeline scrubber max
          const scrubber = document.getElementById('frameScrubber');
          scrubber.max = anim.durationFrames;
          scrubber.value = 0;
          document.getElementById('maxFrameNum').textContent = anim.durationFrames;
          document.getElementById('curFrameNum').textContent = '0';

          playWhoosh(1.1);
        }}

        // Setup Combos
        document.getElementById('btnComboBnB').addEventListener('click', () => {{
          initAudio();
          comboQueue = ['punch_jab', 'punch_straight', 'uppercut'];
          playNextCombo();
        }});

        document.getElementById('btnComboAir').addEventListener('click', () => {{
          initAudio();
          comboQueue = ['uppercut', 'air_juggle', 'ground_slam'];
          playNextCombo();
        }});

        document.getElementById('btnShowcase').addEventListener('click', () => {{
          initAudio();
          comboQueue = [
            'idle', 'punch_jab', 'punch_straight', 'roundhouse_kick',
            'uppercut', 'air_juggle', 'ground_slam', 'hit_reaction',
            'knockdown', 'victory_pose'
          ];
          playNextCombo();
        }});

        function playNextCombo() {{
          if (comboQueue.length > 0) {{
            const next = comboQueue.shift();
            switchAnimation(next, true);
          }}
        }}

        // Timeline and playback UI hooks
        const playBtn = document.getElementById('btnPlayPause');
        playBtn.addEventListener('click', () => {{
          isPlaying = !isPlaying;
          playBtn.textContent = isPlaying ? '⏸' : '▶';
        }});

        document.getElementById('btnPrevFrame').addEventListener('click', () => {{
          isPlaying = false;
          playBtn.textContent = '▶';
          const anim = rigData.animations[currentAnimName];
          animProgress = Math.max(0, animProgress - 1);
          document.getElementById('frameScrubber').value = Math.floor(animProgress);
        }});

        document.getElementById('btnNextFrame').addEventListener('click', () => {{
          isPlaying = false;
          playBtn.textContent = '▶';
          const anim = rigData.animations[currentAnimName];
          animProgress = Math.min(anim.durationFrames, animProgress + 1);
          document.getElementById('frameScrubber').value = Math.floor(animProgress);
        }});

        document.getElementById('btnFlip').addEventListener('click', () => {{
          facingDirection *= -1;
        }});

        const scrubber = document.getElementById('frameScrubber');
        scrubber.addEventListener('input', (e) => {{
          isPlaying = false;
          playBtn.textContent = '▶';
          animProgress = parseFloat(e.target.value);
        }});

        document.getElementById('btnAudioToggle').addEventListener('click', (e) => {{
          initAudio();
          soundEnabled = !soundEnabled;
          e.target.textContent = soundEnabled ? '🔊' : '🔇';
        }});

        // Setup Toggles
        function setupToggle(id, key) {{
          const el = document.getElementById(id);
          el.addEventListener('click', () => {{
            toggles[key] = !toggles[key];
            el.classList.toggle('active', toggles[key]);
            el.querySelector('.tog-st').textContent = toggles[key] ? 'ON' : 'OFF';
          }});
        }}
        setupToggle('togTrails', 'trails');
        setupToggle('togSparks', 'sparks');
        setupToggle('togAura', 'aura');
        setupToggle('togShockwave', 'shockwave');
        setupToggle('togSkeleton', 'skeleton');
        setupToggle('togJointLabels', 'jointLabels');

        // Slider controls
        const speedSlider = document.getElementById('speedSlider');
        speedSlider.addEventListener('input', (e) => {{
          playbackSpeed = parseFloat(e.target.value);
          document.getElementById('speedVal').textContent = playbackSpeed.toFixed(2) + 'x';
        }});

        const scaleSlider = document.getElementById('scaleSlider');
        scaleSlider.addEventListener('input', (e) => {{
          modelScale = parseFloat(e.target.value);
          document.getElementById('scaleVal').textContent = modelScale.toFixed(2) + 'x';
        }});

        // --- PARTICLE EMITTER ---
        function spawnHitSparks(x, y, theme, count = 20, speedMult = 1.0) {{
          if (!toggles.sparks) return;
          const colors = theme.sparkColors || [theme.primary, '#ffffff'];
          for (let i = 0; i < count; i++) {{
            const angle = Math.random() * Math.PI * 2;
            const spd = (3 + Math.random() * 8) * speedMult;
            particles.push({{
              x: x,
              y: y,
              vx: Math.cos(angle) * spd,
              vy: Math.sin(angle) * spd,
              color: colors[Math.floor(Math.random() * colors.length)],
              size: 2 + Math.random() * 3,
              alpha: 1.0,
              decay: 0.025 + Math.random() * 0.035,
              gravity: 0.18
            }});
          }}
        }}

        function spawnShockwave(x, y, theme, maxR = 60) {{
          if (!toggles.shockwave) return;
          shockwaves.push({{
            x: x,
            y: y,
            radius: 5,
            maxRadius: maxR,
            color: theme.impactRingColor || theme.primary,
            alpha: 1.0,
            growSpeed: maxR / 12
          }});
        }}

        // --- KEYFRAME INTERPOLATION ---
        function lerp(a, b, t) {{
          return a + (b - a) * t;
        }}

        function lerpAngle(a, b, t) {{
          let diff = (b - a) % 360;
          if (diff < -180) diff += 360;
          if (diff > 180) diff -= 360;
          return a + diff * t;
        }}

        function sampleAnimation(anim, frame) {{
          const kfs = anim.keyframes;
          if (!kfs || kfs.length === 0) return null;

          if (kfs.length === 1 || frame <= kfs[0].frame) return kfs[0];
          if (frame >= kfs[kfs.length - 1].frame) return kfs[kfs.length - 1];

          // Find surrounding keyframes
          let kfA = kfs[0];
          let kfB = kfs[kfs.length - 1];
          for (let i = 0; i < kfs.length - 1; i++) {{
            if (frame >= kfs[i].frame && frame <= kfs[i + 1].frame) {{
              kfA = kfs[i];
              kfB = kfs[i + 1];
              break;
            }}
          }}

          const span = kfB.frame - kfA.frame;
          const t = span === 0 ? 0 : (frame - kfA.frame) / span;

          // Smooth cosine easing between keyframes
          const easeT = (1 - Math.cos(t * Math.PI)) / 2;

          // Interpolate root offset
          const rootOffset = {{
            x: lerp(kfA.rootOffset.x, kfB.rootOffset.x, easeT),
            y: lerp(kfA.rootOffset.y, kfB.rootOffset.y, easeT),
            rotation: lerpAngle(kfA.rootOffset.rotation || 0, kfB.rootOffset.rotation || 0, easeT)
          }};

          // Interpolate all joint angles
          const angles = {{}};
          for (const jKey of Object.keys(kfA.angles)) {{
            const valA = kfA.angles[jKey];
            const valB = (kfB.angles && kfB.angles[jKey] !== undefined) ? kfB.angles[jKey] : valA;
            angles[jKey] = lerpAngle(valA, valB, easeT);
          }}

          return {{
            rootOffset,
            angles,
            fx: (t > 0.4 && t < 0.6) ? kfB.fx : kfA.fx,
            rawT: t
          }};
        }}

        // --- FORWARD KINEMATICS SOLVER ---
        function solveSkeleton(pose, originX, groundY, scale, facing) {{
          const dims = rigData.dimensions;
          const rootOffset = pose.rootOffset;
          const angles = pose.angles;

          const rootX = originX + (rootOffset.x * scale * facing);
          const rootY = groundY + (rootOffset.y * scale);
          const rootRot = (rootOffset.rotation || 0) * (Math.PI / 180) * facing;

          // Torso (0 deg = straight up, canvas -Math.PI / 2)
          const torsoAngle = (-Math.PI / 2) + (angles.torso * (Math.PI / 180) * facing) + rootRot;
          const torsoEndX = rootX + Math.cos(torsoAngle) * (dims.torsoLength * scale);
          const torsoEndY = rootY + Math.sin(torsoAngle) * (dims.torsoLength * scale);

          // Neck
          const neckAngle = torsoAngle + (angles.neck * (Math.PI / 180) * facing);
          const neckEndX = torsoEndX + Math.cos(neckAngle) * (dims.neckLength * scale);
          const neckEndY = torsoEndY + Math.sin(neckAngle) * (dims.neckLength * scale);

          // Head
          const headAngle = neckAngle + (angles.head * (Math.PI / 180) * facing);
          const headRad = dims.headRadius * scale;
          const headCenterX = neckEndX + Math.cos(headAngle) * headRad;
          const headCenterY = neckEndY + Math.sin(headAngle) * headRad;

          // Torso normal for shoulder / hip width offsets
          const torsoNormX = -Math.sin(torsoAngle);
          const torsoNormY = Math.cos(torsoAngle);

          // Shoulder attachment points
          const shoulderHeightFactor = 0.86;
          const shoulderLateral = dims.shoulderWidth * 0.5 * scale * facing;

          const lShoulderX = rootX + Math.cos(torsoAngle) * (dims.torsoLength * scale * shoulderHeightFactor) - torsoNormX * shoulderLateral;
          const lShoulderY = rootY + Math.sin(torsoAngle) * (dims.torsoLength * scale * shoulderHeightFactor) - torsoNormY * shoulderLateral;

          const rShoulderX = rootX + Math.cos(torsoAngle) * (dims.torsoLength * scale * shoulderHeightFactor) + torsoNormX * shoulderLateral;
          const rShoulderY = rootY + Math.sin(torsoAngle) * (dims.torsoLength * scale * shoulderHeightFactor) + torsoNormY * shoulderLateral;

          // Left Arm (0 deg = downward, positive swings forward towards opponent)
          const lShoulderWorldAngle = (Math.PI / 2) - (angles.leftShoulder * (Math.PI / 180) * facing);
          const lElbowX = lShoulderX + Math.cos(lShoulderWorldAngle) * (dims.upperArmLength * scale);
          const lElbowY = lShoulderY + Math.sin(lShoulderWorldAngle) * (dims.upperArmLength * scale);

          const lElbowWorldAngle = lShoulderWorldAngle - (angles.leftElbow * (Math.PI / 180) * facing);
          const lHandX = lElbowX + Math.cos(lElbowWorldAngle) * (dims.forearmLength * scale);
          const lHandY = lElbowY + Math.sin(lElbowWorldAngle) * (dims.forearmLength * scale);

          // Right Arm
          const rShoulderWorldAngle = (Math.PI / 2) - (angles.rightShoulder * (Math.PI / 180) * facing);
          const rElbowX = rShoulderX + Math.cos(rShoulderWorldAngle) * (dims.upperArmLength * scale);
          const rElbowY = rShoulderY + Math.sin(rShoulderWorldAngle) * (dims.upperArmLength * scale);

          const rElbowWorldAngle = rShoulderWorldAngle - (angles.rightElbow * (Math.PI / 180) * facing);
          const rHandX = rElbowX + Math.cos(rElbowWorldAngle) * (dims.forearmLength * scale);
          const rHandY = rElbowY + Math.sin(rElbowWorldAngle) * (dims.forearmLength * scale);

          // Hips / Pelvis attachment points
          const hipLateral = dims.hipWidth * 0.5 * scale * facing;
          const lHipX = rootX - torsoNormX * hipLateral;
          const lHipY = rootY - torsoNormY * hipLateral;

          const rHipX = rootX + torsoNormX * hipLateral;
          const rHipY = rootY + torsoNormY * hipLateral;

          // Left Leg (0 deg = straight down, positive kicks forward)
          const lHipWorldAngle = (Math.PI / 2) - (angles.leftHip * (Math.PI / 180) * facing);
          const lKneeX = lHipX + Math.cos(lHipWorldAngle) * (dims.thighLength * scale);
          const lKneeY = lHipY + Math.sin(lHipWorldAngle) * (dims.thighLength * scale);

          const lKneeWorldAngle = lHipWorldAngle + (angles.leftKnee * (Math.PI / 180) * facing);
          const lFootX = lKneeX + Math.cos(lKneeWorldAngle) * (dims.shinLength * scale);
          const lFootY = lKneeY + Math.sin(lKneeWorldAngle) * (dims.shinLength * scale);

          const lFootTipAngle = lKneeWorldAngle - (Math.PI / 2) + (angles.leftFoot * (Math.PI / 180) * facing);
          const lToeX = lFootX + Math.cos(lFootTipAngle) * (dims.footLength * scale);
          const lToeY = lFootY + Math.sin(lFootTipAngle) * (dims.footLength * scale);

          // Right Leg
          const rHipWorldAngle = (Math.PI / 2) - (angles.rightHip * (Math.PI / 180) * facing);
          const rKneeX = rHipX + Math.cos(rHipWorldAngle) * (dims.thighLength * scale);
          const rKneeY = rHipY + Math.sin(rHipWorldAngle) * (dims.thighLength * scale);

          const rKneeWorldAngle = rHipWorldAngle + (angles.rightKnee * (Math.PI / 180) * facing);
          const rFootX = rKneeX + Math.cos(rKneeWorldAngle) * (dims.shinLength * scale);
          const rFootY = rKneeY + Math.sin(rKneeWorldAngle) * (dims.shinLength * scale);

          const rFootTipAngle = rKneeWorldAngle - (Math.PI / 2) + (angles.rightFoot * (Math.PI / 180) * facing);
          const rToeX = rFootX + Math.cos(rFootTipAngle) * (dims.footLength * scale);
          const rToeY = rFootY + Math.sin(rFootTipAngle) * (dims.footLength * scale);

          return {{
            root: {{ x: rootX, y: rootY }},
            torsoEnd: {{ x: torsoEndX, y: torsoEndY }},
            neckEnd: {{ x: neckEndX, y: neckEndY }},
            head: {{ x: headCenterX, y: headCenterY, radius: headRad, angle: headAngle }},
            leftShoulder: {{ x: lShoulderX, y: lShoulderY }},
            leftElbow: {{ x: lElbowX, y: lElbowY }},
            leftHand: {{ x: lHandX, y: lHandY }},
            rightShoulder: {{ x: rShoulderX, y: rShoulderY }},
            rightElbow: {{ x: rElbowX, y: rElbowY }},
            rightHand: {{ x: rHandX, y: rHandY }},
            leftHip: {{ x: lHipX, y: lHipY }},
            leftKnee: {{ x: lKneeX, y: lKneeY }},
            leftFoot: {{ x: lFootX, y: lFootY }},
            leftToe: {{ x: lToeX, y: lToeY }},
            rightHip: {{ x: rHipX, y: rHipY }},
            rightKnee: {{ x: rKneeX, y: rKneeY }},
            rightFoot: {{ x: rFootX, y: rFootY }},
            rightToe: {{ x: rToeX, y: rToeY }},
            facing: facing,
            scale: scale
          }};
        }}

        // --- RENDER SKELETON ---
        function drawStickman(ctx, skel, theme, alpha = 1.0, isTrail = false) {{
          ctx.save();
          ctx.globalAlpha = alpha;

          const lw = (theme.lineWidth || 5) * (skel.scale / 1.75);
          ctx.lineWidth = lw;
          ctx.lineCap = 'round';
          ctx.lineJoin = 'round';

          if (!isTrail) {{
            ctx.shadowColor = theme.glow;
            ctx.shadowBlur = theme.glowSize || 18;
          }} else {{
            ctx.shadowBlur = 0;
          }}

          ctx.strokeStyle = isTrail ? (theme.trailColor || theme.primary) : theme.primary;

          // Helper to draw bone
          function drawBone(p1, p2, widthMult = 1.0) {{
            ctx.beginPath();
            ctx.lineWidth = lw * widthMult;
            ctx.moveTo(p1.x, p1.y);
            ctx.lineTo(p2.x, p2.y);
            ctx.stroke();
          }}

          // Helper to draw joint cap
          function drawJoint(p, radMult = 0.9) {{
            if (isTrail) return;
            ctx.save();
            ctx.fillStyle = theme.jointFill || '#ffffff';
            ctx.beginPath();
            ctx.arc(p.x, p.y, (lw * 0.55) * radMult, 0, Math.PI * 2);
            ctx.fill();
            ctx.restore();
          }}

          // 1. Rear Leg (Right Leg)
          ctx.strokeStyle = isTrail ? (theme.trailColor || theme.primary) : (theme.secondary || theme.primary);
          drawBone(skel.rightHip, skel.rightKnee, 0.95);
          drawBone(skel.rightKnee, skel.rightFoot, 0.9);
          drawBone(skel.rightFoot, skel.rightToe, 0.7);
          drawJoint(skel.rightHip);
          drawJoint(skel.rightKnee);
          drawJoint(skel.rightFoot);

          // 2. Rear Arm (Right Arm)
          drawBone(skel.rightShoulder, skel.rightElbow, 0.9);
          drawBone(skel.rightElbow, skel.rightHand, 0.85);
          drawJoint(skel.rightShoulder);
          drawJoint(skel.rightElbow);
          drawJoint(skel.rightHand, 1.2);

          // 3. Torso & Pelvis
          ctx.strokeStyle = isTrail ? (theme.trailColor || theme.primary) : theme.primary;
          drawBone(skel.root, skel.torsoEnd, 1.15);
          drawBone(skel.torsoEnd, skel.neckEnd, 0.85);
          drawJoint(skel.root, 1.1);
          drawJoint(skel.torsoEnd);

          // 4. Head & Visor
          ctx.save();
          // Head fill circle
          ctx.fillStyle = theme.headFill || '#001a2c';
          ctx.strokeStyle = isTrail ? (theme.trailColor || theme.primary) : theme.primary;
          ctx.lineWidth = lw * 0.9;
          ctx.beginPath();
          ctx.arc(skel.head.x, skel.head.y, skel.head.radius, 0, Math.PI * 2);
          ctx.fill();
          ctx.stroke();

          // Ninja Headband / Eye Visor slit
          if (!isTrail) {{
            ctx.save();
            ctx.fillStyle = theme.eyeColor || '#ffffff';
            ctx.shadowColor = theme.eyeColor || '#ffffff';
            ctx.shadowBlur = 10;
            const eyeDist = skel.head.radius * 0.35;
            const eyeW = skel.head.radius * 0.7;
            const eyeH = skel.head.radius * 0.22;
            const eyeX = skel.head.x + Math.cos(skel.head.angle) * eyeDist * skel.facing;
            const eyeY = skel.head.y + Math.sin(skel.head.angle) * eyeDist;

            ctx.translate(eyeX, eyeY);
            ctx.rotate(skel.head.angle);
            ctx.fillRect(0, -eyeH * 0.5, eyeW * skel.facing, eyeH);

            // Trailing Headband Ribbons (flowing backward)
            ctx.strokeStyle = theme.primary;
            ctx.lineWidth = lw * 0.4;
            ctx.beginPath();
            const ribbonOriginX = -skel.head.radius * 0.9 * skel.facing;
            const ribbonOriginY = 0;
            ctx.moveTo(ribbonOriginX, ribbonOriginY);
            ctx.quadraticCurveTo(ribbonOriginX - 14 * skel.facing, ribbonOriginY + 6, ribbonOriginX - 24 * skel.facing, ribbonOriginY + 12);
            ctx.stroke();
            ctx.restore();
          }}
          ctx.restore();

          // 5. Lead Leg (Left Leg)
          ctx.strokeStyle = isTrail ? (theme.trailColor || theme.primary) : theme.primary;
          drawBone(skel.leftHip, skel.leftKnee, 1.05);
          drawBone(skel.leftKnee, skel.leftFoot, 1.0);
          drawBone(skel.leftFoot, skel.leftToe, 0.75);
          drawJoint(skel.leftHip);
          drawJoint(skel.leftKnee);
          drawJoint(skel.leftFoot);

          // 6. Lead Arm (Left Arm)
          drawBone(skel.leftShoulder, skel.leftElbow, 1.0);
          drawBone(skel.leftElbow, skel.leftHand, 0.95);
          drawJoint(skel.leftShoulder);
          drawJoint(skel.leftElbow);
          drawJoint(skel.leftHand, 1.3);

          // 7. Wireframe & Joint Marker Debug Overlay
          if (toggles.skeleton && !isTrail) {{
            ctx.save();
            ctx.strokeStyle = 'rgba(255, 255, 255, 0.4)';
            ctx.lineWidth = 1;
            ctx.setLineDash([3, 3]);
            ctx.strokeRect(skel.root.x - 20, skel.root.y - 40, 40, 80);
            ctx.restore();
          }}

          if (toggles.jointLabels && !isTrail) {{
            ctx.save();
            ctx.font = '9px monospace';
            ctx.fillStyle = '#00f0ff';
            ctx.fillText('HIPS', skel.root.x + 8, skel.root.y);
            ctx.fillText('HEAD', skel.head.x + 14, skel.head.y);
            ctx.fillText('L-HAND', skel.leftHand.x + 8, skel.leftHand.y);
            ctx.fillText('R-HAND', skel.rightHand.x + 8, skel.rightHand.y);
            ctx.fillText('L-FOOT', skel.leftFoot.x + 8, skel.leftFoot.y);
            ctx.fillText('R-FOOT', skel.rightFoot.x + 8, skel.rightFoot.y);
            ctx.restore();
          }}

          ctx.restore();
        }}

        // --- SWOOSH MOTION ARCS ---
        function drawSwooshArc(ctx, skel, theme, type) {{
          ctx.save();
          ctx.shadowBlur = 24;
          ctx.shadowColor = theme.primary;
          ctx.strokeStyle = theme.primary;
          ctx.lineCap = 'round';

          if (type === 'roundhouse_arc') {{
            // Circular sweeping arc around waist/foot
            const arcR = 55 * (skel.scale / 1.75);
            ctx.beginPath();
            ctx.lineWidth = 9 * (skel.scale / 1.75);
            ctx.arc(skel.root.x, skel.root.y - 10, arcR, -0.6 * Math.PI, 0.4 * Math.PI, false);
            const grad = ctx.createLinearGradient(skel.root.x - arcR, skel.root.y, skel.rightFoot.x, skel.rightFoot.y);
            grad.addColorStop(0, 'rgba(0,0,0,0)');
            grad.addColorStop(0.7, theme.primary);
            grad.addColorStop(1, '#ffffff');
            ctx.strokeStyle = grad;
            ctx.stroke();
          }} else if (type === 'uppercut_vertical') {{
            // Vertical rising blade arc
            ctx.beginPath();
            ctx.lineWidth = 8 * (skel.scale / 1.75);
            ctx.moveTo(skel.rightHand.x - 10 * skel.facing, skel.rightHand.y + 70);
            ctx.quadraticCurveTo(skel.rightHand.x, skel.rightHand.y + 20, skel.rightHand.x, skel.rightHand.y);
            ctx.stroke();
          }} else if (type === 'axe_slam') {{
            // Vertical downward crescent
            ctx.beginPath();
            ctx.lineWidth = 12 * (skel.scale / 1.75);
            ctx.moveTo(skel.rightFoot.x - 20 * skel.facing, skel.rightFoot.y - 80);
            ctx.quadraticCurveTo(skel.rightFoot.x, skel.rightFoot.y - 30, skel.rightFoot.x, skel.rightFoot.y);
            ctx.stroke();
          }} else if (type === 'jab' || type === 'cross') {{
            // Horizontal bullet streak
            const pt = type === 'jab' ? skel.leftHand : skel.rightHand;
            ctx.beginPath();
            ctx.lineWidth = 6 * (skel.scale / 1.75);
            ctx.moveTo(pt.x - 45 * skel.facing, pt.y);
            ctx.lineTo(pt.x + 8 * skel.facing, pt.y);
            ctx.stroke();
          }}
          ctx.restore();
        }}

        // --- GROUND & SHADOW RENDERING ---
        function drawEnvironment(ctx, originX, groundY, skel, theme) {{
          // Dojo Canvas Floor Grid
          ctx.save();
          ctx.strokeStyle = 'rgba(0, 240, 255, 0.08)';
          ctx.lineWidth = 1;

          // Grid lines
          const gridStep = 40;
          for (let x = 0; x < canvas.width; x += gridStep) {{
            ctx.beginPath();
            ctx.moveTo(x, groundY);
            ctx.lineTo(x + (x - originX) * 0.8, canvas.height);
            ctx.stroke();
          }}
          for (let y = groundY; y < canvas.height; y += 22) {{
            ctx.beginPath();
            ctx.moveTo(0, y);
            ctx.lineTo(canvas.width, y);
            ctx.stroke();
          }}

          // Floor Boundary Line
          ctx.beginPath();
          ctx.strokeStyle = 'rgba(0, 240, 255, 0.3)';
          ctx.lineWidth = 2;
          ctx.shadowColor = 'rgba(0, 240, 255, 0.5)';
          ctx.shadowBlur = 8;
          ctx.moveTo(0, groundY);
          ctx.lineTo(canvas.width, groundY);
          ctx.stroke();

          // Dynamic Ground Contact Shadow
          if (skel) {{
            const shadowX = skel.root.x;
            const heightAboveGround = Math.max(0, groundY - skel.root.y + 40);
            const shadowScale = Math.max(0.2, 1.0 - heightAboveGround / 220);
            const shadowAlpha = Math.max(0.1, 0.6 - heightAboveGround / 240);

            ctx.save();
            ctx.fillStyle = `rgba(0, 0, 0, ${{shadowAlpha}})`;
            ctx.beginPath();
            ctx.ellipse(shadowX, groundY + 4, 38 * shadowScale * (skel.scale / 1.75), 10 * shadowScale, 0, 0, Math.PI * 2);
            ctx.fill();

            // Neon ring under feet
            ctx.strokeStyle = theme.glow;
            ctx.lineWidth = 1.5;
            ctx.globalAlpha = shadowAlpha * 0.6;
            ctx.stroke();
            ctx.restore();
          }}
          ctx.restore();
        }}

        // --- VICTORY AURA PULSE ---
        let auraPulseTimer = 0;
        function drawVictoryAura(ctx, skel, theme) {{
          if (!toggles.aura) return;
          auraPulseTimer += 0.05;
          const pulse = 1.0 + Math.sin(auraPulseTimer * 3) * 0.15;
          const auraRadius = (65 + Math.sin(auraPulseTimer * 4) * 10) * (skel.scale / 1.75);

          ctx.save();
          ctx.globalCompositeOperation = 'screen';
          const grad = ctx.createRadialGradient(
            skel.root.x, skel.root.y - 25, 10,
            skel.root.x, skel.root.y - 25, auraRadius * pulse
          );
          grad.addColorStop(0, theme.auraColor || 'rgba(0, 240, 255, 0.4)');
          grad.addColorStop(0.5, 'rgba(0, 240, 255, 0.15)');
          grad.addColorStop(1, 'rgba(0, 240, 255, 0)');

          ctx.fillStyle = grad;
          ctx.beginPath();
          ctx.arc(skel.root.x, skel.root.y - 25, auraRadius * pulse, 0, Math.PI * 2);
          ctx.fill();

          // Rising energy sparklets
          if (Math.random() < 0.4) {{
            particles.push({{
              x: skel.root.x + (Math.random() * 80 - 40),
              y: skel.root.y + 20,
              vx: (Math.random() - 0.5) * 1.5,
              vy: -2.5 - Math.random() * 3,
              color: '#ffffff',
              size: 2 + Math.random() * 2,
              alpha: 0.9,
              decay: 0.02,
              gravity: -0.05
            }});
          }}
          ctx.restore();
        }}

        // --- MAIN 60 FPS ANIMATION LOOP ---
        let lastTimestamp = performance.now();
        let frameCount = 0;
        let fpsTimer = performance.now();

        function renderLoop(now) {{
          requestAnimationFrame(renderLoop);

          // Delta calculation
          const dt = Math.min(0.1, (now - lastTimestamp) / 1000);
          lastTimestamp = now;

          // FPS measurement
          frameCount++;
          if (now - fpsTimer >= 500) {{
            const currentFps = Math.round((frameCount * 1000) / (now - fpsTimer));
            document.getElementById('fpsVal').textContent = currentFps.toFixed(1);
            frameCount = 0;
            fpsTimer = now;
          }}

          const activeTheme = rigData.themes[currentThemeId];
          const activeAnim = rigData.animations[currentAnimName];

          // Advance animation progress
          let justTriggeredHit = false;
          if (isPlaying && activeAnim) {{
            const prevFrameInt = Math.floor(animProgress);
            animProgress += 60 * dt * playbackSpeed;

            // Check hit frames
            const curFrameInt = Math.floor(animProgress);
            if (activeAnim.hitFrames) {{
              for (const hf of activeAnim.hitFrames) {{
                if (prevFrameInt < hf && curFrameInt >= hf) {{
                  justTriggeredHit = true;
                }}
              }}
            }}

            if (animProgress >= activeAnim.durationFrames) {{
              if (activeAnim.loop) {{
                animProgress = animProgress % activeAnim.durationFrames;
              }} else {{
                animProgress = activeAnim.durationFrames;
                if (comboQueue.length > 0) {{
                  playNextCombo();
                }} else {{
                  // Default return smoothly to idle
                  switchAnimation('idle');
                }}
              }}
            }}

            // Sync timeline UI
            document.getElementById('frameScrubber').value = Math.floor(animProgress);
            document.getElementById('curFrameNum').textContent = Math.floor(animProgress);
          }}

          // Clear Canvas
          ctx.clearRect(0, 0, canvas.width, canvas.height);

          // Screen shake handling
          ctx.save();
          if (screenShake > 0) {{
            const shakeX = (Math.random() - 0.5) * screenShake;
            const shakeY = (Math.random() - 0.5) * screenShake;
            ctx.translate(shakeX, shakeY);
            screenShake *= 0.88;
            if (screenShake < 0.2) screenShake = 0;
          }}

          const groundY = (canvas.height / (window.devicePixelRatio || 1)) * 0.72;
          const originX = (canvas.width / (window.devicePixelRatio || 1)) * 0.5;

          // Sample current pose & solve skeleton
          const currentPose = sampleAnimation(activeAnim, animProgress);
          let currentSkel = null;

          if (currentPose) {{
            currentSkel = solveSkeleton(currentPose, originX, groundY, modelScale, facingDirection);

            // Record trails history
            if (toggles.trails) {{
              trailsHistory.push({{
                skel: currentSkel,
                alpha: 0.35,
                timestamp: now
              }});
              if (trailsHistory.length > MAX_TRAILS) {{
                trailsHistory.shift();
              }}
            }}

            // Hit trigger particle / sound spawn
            if (justTriggeredHit) {{
              const fx = currentPose.fx || {{}};
              screenShake = fx.screenShake || 4;

              // Identify striking joint position
              let hitPt = currentSkel.leftHand;
              if (fx.joint === 'rightHand') hitPt = currentSkel.rightHand;
              else if (fx.joint === 'rightFoot') hitPt = currentSkel.rightFoot;
              else if (fx.joint === 'leftFoot') hitPt = currentSkel.leftFoot;
              else if (fx.joint === 'torso') hitPt = currentSkel.root;

              spawnHitSparks(hitPt.x, hitPt.y, activeTheme, 22 * (fx.sparkSize || 1.0));
              spawnShockwave(hitPt.x, hitPt.y, activeTheme, 65 * (fx.sparkSize || 1.0));

              if (fx.groundShockwave) {{
                spawnShockwave(hitPt.x, groundY, activeTheme, 110);
                playSlamSound();
              }} else {{
                playHitImpact(fx.sparkSize || 1.0);
              }}
            }}
          }}

          // Draw Ground & Environment
          drawEnvironment(ctx, originX, groundY, currentSkel, activeTheme);

          // Draw Motion Trails (fading historic poses)
          if (toggles.trails && trailsHistory.length > 1) {{
            ctx.save();
            ctx.globalCompositeOperation = 'lighter';
            trailsHistory.forEach((item, index) => {{
              const fadeRatio = (index + 1) / trailsHistory.length;
              const trailAlpha = fadeRatio * 0.22;
              drawStickman(ctx, item.skel, activeTheme, trailAlpha, true);
            }});
            ctx.restore();
          }}

          // Draw Victory Radiant Aura
          if (currentAnimName === 'victory_pose' && currentSkel) {{
            drawVictoryAura(ctx, currentSkel, activeTheme);
          }}

          // Draw Active Stickman
          if (currentSkel) {{
            drawStickman(ctx, currentSkel, activeTheme, 1.0, false);

            // Draw Swoosh Arcs if active
            const fx = currentPose.fx || {{}};
            if (fx.swoosh) {{
              drawSwooshArc(ctx, currentSkel, activeTheme, fx.swoosh);
            }}
          }}

          // Draw Shockwaves
          for (let i = shockwaves.length - 1; i >= 0; i--) {{
            const sw = shockwaves[i];
            sw.radius += sw.growSpeed;
            sw.alpha -= 0.055;
            if (sw.alpha <= 0 || sw.radius >= sw.maxRadius) {{
              shockwaves.splice(i, 1);
              continue;
            }}
            ctx.save();
            ctx.strokeStyle = sw.color;
            ctx.globalAlpha = sw.alpha;
            ctx.lineWidth = 3;
            ctx.shadowColor = sw.color;
            ctx.shadowBlur = 10;
            ctx.beginPath();
            ctx.arc(sw.x, sw.y, sw.radius, 0, Math.PI * 2);
            ctx.stroke();
            ctx.restore();
          }}

          // Draw & Update Hit Spark Particles
          for (let i = particles.length - 1; i >= 0; i--) {{
            const p = particles[i];
            p.x += p.vx;
            p.y += p.vy;
            p.vy += p.gravity;
            p.alpha -= p.decay;

            if (p.alpha <= 0) {{
              particles.splice(i, 1);
              continue;
            }}

            ctx.save();
            ctx.fillStyle = p.color;
            ctx.globalAlpha = p.alpha;
            ctx.shadowColor = p.color;
            ctx.shadowBlur = 6;
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
            ctx.fill();
            ctx.restore();
          }}

          ctx.restore(); // restore screen shake

          // Update Telemetry Display
          if (currentPose) {{
            const ang = currentPose.angles;
            const tele = document.getElementById('telemetryBox');
            tele.innerHTML = `
              <div>ANIM: <span>${{activeAnim.displayName}}</span> [Frame ${{Math.floor(animProgress)}}/${{activeAnim.durationFrames}}]</div>
              <div>ROOT POS: X: <span>${{Math.round(currentPose.rootOffset.x)}}</span> | Y: <span>${{Math.round(currentPose.rootOffset.y)}}</span> | ROT: <span>${{Math.round(currentPose.rootOffset.rotation || 0)}}&deg;</span></div>
              <div>TORSO: <span>${{Math.round(ang.torso)}}&deg;</span> | NECK: <span>${{Math.round(ang.neck)}}&deg;</span> | HEAD: <span>${{Math.round(ang.head)}}&deg;</span></div>
              <div>L-ARM: Sh <span>${{Math.round(ang.leftShoulder)}}&deg;</span> &bull; El <span>${{Math.round(ang.leftElbow)}}&deg;</span> &bull; Hd <span>${{Math.round(ang.leftHand)}}&deg;</span></div>
              <div>R-ARM: Sh <span>${{Math.round(ang.rightShoulder)}}&deg;</span> &bull; El <span>${{Math.round(ang.rightElbow)}}&deg;</span> &bull; Hd <span>${{Math.round(ang.rightHand)}}&deg;</span></div>
              <div>L-LEG: Hp <span>${{Math.round(ang.leftHip)}}&deg;</span> &bull; Kn <span>${{Math.round(ang.leftKnee)}}&deg;</span> &bull; Ft <span>${{Math.round(ang.leftFoot)}}&deg;</span></div>
              <div>R-LEG: Hp <span>${{Math.round(ang.rightHip)}}&deg;</span> &bull; Kn <span>${{Math.round(ang.rightKnee)}}&deg;</span> &bull; Ft <span>${{Math.round(ang.rightFoot)}}&deg;</span></div>
              <div>PARTICLES: <span>${{particles.length}}</span> | SHOCKWAVES: <span>${{shockwaves.length}}</span></div>
            `;
          }}
        }}

        requestAnimationFrame(renderLoop);
      }}
    }})();
  </script>
</body>
</html>
"""
    out_html = r"c:\Users\priya\OneDrive\Documents\Next Toppers\typefighter\assets\sprites\stickman_preview.html"
    with open(out_html, "w", encoding="utf-8") as f:
        f.write(html_code)
    print(f"Successfully generated {out_html} (size: {len(html_code)} bytes).")

if __name__ == "__main__":
    generate_preview_html()
