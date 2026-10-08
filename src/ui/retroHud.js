// Keyboard Warrior Stickman - Retro Steam Game HUD & Floating 3D/2.5D Prompt Overlay
export class RetroHud {
  constructor(container) {
    this.container = container;
    this.createDomElements();
  }

  createDomElements() {
    this.hudRoot = document.createElement('div');
    this.hudRoot.id = 'retro-hud-overlay';
    this.hudRoot.innerHTML = `
      <!-- Top / Center Floating In-Arena Prompt -->
      <div id="floating-prompt-container">
        <div id="floating-prompt-paper">
          <div id="prompt-text-display"></div>
        </div>
      </div>

      <!-- Combo & DMC Style Rank Widget (Right Side) -->
      <div id="style-rank-widget">
        <div id="combo-counter-text" class="hidden">0 HITS!</div>
        <div id="rank-badge-letter">D</div>
        <div id="rank-title-text">DISMAL</div>
        <div id="rank-meter-track">
          <div id="rank-meter-fill"></div>
        </div>
      </div>

      <!-- Bottom-Left Steam Authentic HUD -->
      <div id="steam-bottom-hud">
        <div id="steam-hud-metrics">
          <span class="hud-item"><span id="hud-good-count" class="val">0</span> <span class="lbl">GOOD</span></span>
          <span class="hud-sep">/</span>
          <span class="hud-item"><span id="hud-miss-count" class="val">0</span> <span class="lbl">MISS</span></span>
          <span class="hud-sep">/</span>
          <span class="hud-item"><span id="hud-accuracy-val" class="val">100</span><span class="lbl">%</span></span>
          <span class="hud-sep">/</span>
          <span class="hud-item"><span id="hud-time-val" class="val">0:00</span></span>
        </div>
        <div id="steam-score-counter">000,000</div>
        <div id="steam-progress-track">
          <div id="steam-progress-fill"></div>
        </div>
      </div>

      <!-- Bottom-Center Physical Keybind Reminder Bar -->
      <div id="keybind-guide-bar">
        <span class="k-chip"><kbd>SPACE</kbd> AIR LAUNCH</span>
        <span class="k-chip"><kbd>ENTER</kbd> GROUND SLAM</span>
        <span class="k-chip"><kbd>TAB</kbd> DASH</span>
        <span class="k-chip"><kbd>CAPS</kbd> RAGE FURY</span>
        <span class="k-chip"><kbd>WASD</kbd> MOVE</span>
      </div>

      <!-- Red Screen Flash on Miss / Error -->
      <div id="screen-miss-flash"></div>
      <!-- Rage Mode Red Aura Vignette -->
      <div id="rage-aura-vignette"></div>
    `;

    this.container.appendChild(this.hudRoot);

    // Cache elements for 60 FPS performance
    this.promptDisplay = document.getElementById('prompt-text-display');
    this.goodEl = document.getElementById('hud-good-count');
    this.missEl = document.getElementById('hud-miss-count');
    this.accEl = document.getElementById('hud-accuracy-val');
    this.timeEl = document.getElementById('hud-time-val');
    this.scoreEl = document.getElementById('steam-score-counter');
    this.progressFill = document.getElementById('steam-progress-fill');

    this.comboText = document.getElementById('combo-counter-text');
    this.rankLetter = document.getElementById('rank-badge-letter');
    this.rankTitle = document.getElementById('rank-title-text');
    this.rankFill = document.getElementById('rank-meter-fill');

    this.flashEl = document.getElementById('screen-miss-flash');
    this.rageEl = document.getElementById('rage-aura-vignette');
  }

  updatePrompt(promptManager) {
    const text = promptManager.currentText;
    const activeIdx = promptManager.charIndex;

    let html = '';
    for (let i = 0; i < text.length; i++) {
      const char = text[i];
      const displayChar = char === ' ' ? '&nbsp;' : char;

      if (i < activeIdx) {
        // Already completed
        html += `<span class="char char-done">${displayChar}</span>`;
      } else if (i === activeIdx) {
        // Active target with STEAM RED CURSOR BOX!
        html += `<span class="char char-active"><span class="red-cursor-box">${displayChar}</span></span>`;
      } else {
        // Pending
        html += `<span class="char char-pending">${displayChar}</span>`;
      }
    }
    this.promptDisplay.innerHTML = html;
  }

  updateMetrics(promptManager, comboEngine) {
    // Bottom-Left Steam HUD
    this.goodEl.textContent = promptManager.goodCount;
    this.missEl.textContent = promptManager.missCount;
    this.accEl.textContent = promptManager.getAccuracy();
    this.timeEl.textContent = promptManager.getElapsedFormatted();

    // 6-digit score formatting: e.g. 000,123
    const scoreNum = comboEngine.score;
    const formattedScore = scoreNum.toLocaleString('en-US').padStart(7, '0');
    this.scoreEl.textContent = formattedScore;

    // Sentence Progress Bar
    const progress = promptManager.getProgress() * 100;
    this.progressFill.style.width = `${progress}%`;

    // Combo Counter
    if (comboEngine.hits > 1) {
      this.comboText.classList.remove('hidden');
      this.comboText.textContent = `${comboEngine.hits} HITS!`;
    } else {
      this.comboText.classList.add('hidden');
    }

    // DMC Style Rank
    const rank = comboEngine.getCurrentRank();
    this.rankLetter.textContent = rank;
    this.rankLetter.setAttribute('data-rank', rank);
    this.rankTitle.textContent = comboEngine.getCurrentRankTitle();
    this.rankFill.style.width = `${comboEngine.getRankProgress() * 100}%`;

    // Rage Aura
    if (comboEngine.isRageMode) {
      this.rageEl.style.opacity = '1';
    } else {
      this.rageEl.style.opacity = '0';
    }
  }

  flashError() {
    this.flashEl.classList.remove('flash-active');
    void this.flashEl.offsetWidth; // Trigger reflow
    this.flashEl.classList.add('flash-active');
  }
}
