// ============================================================================
// TYPEFIGHTER — MASTER GAME ORCHESTRATOR & 60 FPS RUNTIME LOOP
// ============================================================================

class TypeFighterGame {
  constructor() {
    this.currentMode = 'menu'; // 'story', 'endless', 'daily', 'speedtest', 'dojo', 'menu'
    this.lastTime = performance.now();
    this.isPaused = false;
    this.isInitialized = false;
  }

  async init() {
    console.log('[TypeFighter] Booting game engine...');

    // 1. Initialize Subsystems in Parallel
    const canvas = document.getElementById('gameCanvas');
    window.combatEngine.init(canvas);

    await Promise.all([
      window.stickmanRig.init(),
      window.curriculumManager.init(),
      window.adaptiveTracker.init()
    ]);

    // 2. Initialize Guides and UI
    const kbContainer = document.getElementById('keyboardWrap');
    if (kbContainer) window.keyboardGuide.mount(kbContainer);

    const handsContainer = document.getElementById('handGuideWrap');
    if (handsContainer) await window.handGuide.mount(handsContainer);

    window.gameHUD.init();
    window.menuManager.init();

    // 3. Load Saved Progression
    const savedXP = window.saveManager ? window.saveManager.data.totalXP : 0;
    window.beltSystem.init(savedXP);

    // 4. Hook Typing Engine Callbacks
    this.hookTypingEngine();

    // 5. Hook Combat Engine Callbacks
    this.hookCombatEngine();

    // 6. Bind Global Keyboard Listener
    this.bindKeyboardInput();

    // 7. Start 60 FPS Game Loop
    this.isInitialized = true;
    requestAnimationFrame((now) => this.gameLoop(now));

    // Show Main Menu by default
    window.menuManager.openMainMenu();
  }

  hookTypingEngine() {
    const te = window.typingEngine;
    if (!te) return;

    te.onCorrectChar = (char, isWordEnd, isTargetComplete) => {
      // 1. Play tactile mechanical click
      if (window.audioManager) {
        window.audioManager.playKeyClick(char === ' ', isWordEnd);
      }

      // 2. Trigger combat animations
      if (this.currentMode === 'story' && window.storyCampaignMode.phase === 'warmup') {
        // In Dojo warm-up
        if (isTargetComplete) {
          window.storyCampaignMode.nextWarmupItem();
        }
      } else if (this.currentMode === 'dojo') {
        if (isTargetComplete) {
          window.practiceDojoMode.onItemComplete();
        }
      } else {
        // Combat modes
        if (window.streakSystem && window.streakSystem.specialMoveReady && isWordEnd) {
          window.streakSystem.consumeSpecialMove();
          window.combatEngine.triggerScreenClearSpecial();
        } else {
          window.combatEngine.triggerHeroStrike(isWordEnd);
        }
      }

      // 3. Add streak & Style points
      if (window.streakSystem) window.streakSystem.addKeystroke();
      if (window.styleRankManager) {
        const streakMult = window.streakSystem ? window.streakSystem.getMultiplier() : 1.0;
        window.styleRankManager.addPoints(isWordEnd ? 50 : 15, streakMult);
      }

      // 4. Record Key Accuracy in Adaptive Tracker
      if (window.adaptiveTracker) {
        window.adaptiveTracker.recordKey(char, true);
      }

      // 5. Update Guides
      const nextChar = te.getCurrentTargetChar();
      if (window.keyboardGuide) window.keyboardGuide.setTargetKey(nextChar);
      if (window.handGuide) window.handGuide.setTargetFinger(te.getCurrentFinger());
    };

    te.onErrorChar = (expectedChar, typedChar) => {
      // 1. Play subtle error buzzer
      if (window.audioManager) window.audioManager.playKeyError();

      // 2. Shake prompt in red
      if (window.gameHUD) window.gameHUD.triggerPromptError();

      // 3. Penalize streak & Style Rank
      if (window.streakSystem) window.streakSystem.breakStreak();
      if (window.styleRankManager) window.styleRankManager.applyTypoPenalty();

      // 4. Record Error in Adaptive Tracker
      if (window.adaptiveTracker) {
        window.adaptiveTracker.recordKey(expectedChar, false);
      }
    };
  }

  hookCombatEngine() {
    const ce = window.combatEngine;
    if (!ce) return;

    ce.onEnemyDefeated = (enemy) => {
      if (this.currentMode === 'story') {
        window.storyCampaignMode.onEnemyDefeated(enemy);
      } else if (this.currentMode === 'endless') {
        window.endlessSurvivalMode.onEnemyDefeated(enemy);
      } else if (this.currentMode === 'daily') {
        window.dailyChallengeMode.onEnemyDefeated(enemy);
      }
    };

    ce.onHeroHit = (hp) => {
      if (window.gameHUD) window.gameHUD.updateHeroHp(hp);
    };

    ce.onGameOver = () => {
      if (this.currentMode === 'endless') {
        window.endlessSurvivalMode.onGameOver();
      } else {
        const results = window.typingEngine ? window.typingEngine.getResults() : {};
        window.menuManager.showGameOverModal(results);
      }
    };
  }

  bindKeyboardInput() {
    window.addEventListener('keydown', (e) => {
      // Ignore functional controls like F11, F12, Escape
      if (e.key === 'F11' || e.key === 'F12') return;

      if (e.key === 'Escape') {
        // Toggle pause / menu
        window.menuManager.openMainMenu();
        return;
      }

      // If any menu modal is open, ignore game typing
      const activeModal = document.querySelector('.modal-overlay:not(.hidden)');
      if (activeModal) return;

      // Prevent scrolling / navigation on space or backspace
      if (e.key === ' ' || e.key === 'Backspace' || e.key === 'Tab') {
        e.preventDefault();
      }

      if (e.key.length === 1 || e.key === 'Enter') {
        if (window.audioManager) window.audioManager.init(); // unlock audio on first stroke
        if (window.keyboardGuide) window.keyboardGuide.triggerKeyPress(e.key);
        if (window.typingEngine) window.typingEngine.processKey(e.key);
      }
    });
  }

  startStoryStage(stageNumber) {
    this.currentMode = 'story';
    window.combatEngine.resetHero();
    window.combatEngine.isActive = true;
    window.storyCampaignMode.startStage(stageNumber);
  }

  startMode(modeName) {
    this.currentMode = modeName;
    window.combatEngine.resetHero();
    window.combatEngine.isActive = true;

    if (modeName === 'endless') {
      window.endlessSurvivalMode.start();
    } else if (modeName === 'daily') {
      window.dailyChallengeMode.start();
    } else if (modeName === 'speedtest') {
      window.speedTestMode.start(60);
    } else if (modeName === 'dojo') {
      window.practiceDojoMode.start('home');
    }
  }

  // --- 60 FPS MAIN RENDER LOOP ---
  gameLoop(now) {
    requestAnimationFrame((n) => this.gameLoop(n));

    const dt = Math.min(0.1, (now - this.lastTime) / 1000);
    this.lastTime = now;

    if (this.isPaused) return;

    // 1. Update Engine Subsystems
    if (window.combatEngine) window.combatEngine.update(dt);
    if (window.particleSystem) window.particleSystem.update(dt);
    if (window.styleRankManager) window.styleRankManager.update(dt);

    // 2. Render 60 FPS Canvas
    if (window.combatEngine) window.combatEngine.render();
  }
}

window.game = new TypeFighterGame();

// Global UI helper for modals
window.gameUI = {
  showNotification: (title, sub) => window.gameHUD?.showNotification(title, sub),
  showStageVictoryModal: (stage, res) => window.menuManager?.showVictoryModal(stage, res),
  showGameOverModal: (res) => window.menuManager?.showGameOverModal(res),
  updateSpeedTestTimer: (sec) => {
    const min = Math.floor(sec / 60);
    const s = sec % 60;
    const badge = document.getElementById('hudStageTitle');
    if (badge) badge.textContent = `TIME: ${min}:${s < 10 ? '0' : ''}${s}`;
  },
  showSpeedTestResultsModal: (res) => window.menuManager?.showVictoryModal('SPEED TEST', res)
};

// Start application when DOM is ready
window.addEventListener('DOMContentLoaded', () => {
  window.game.init();
});
