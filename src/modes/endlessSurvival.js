// ============================================================================
// TYPEFIGHTER — MODE 2: ENDLESS SURVIVAL
// ============================================================================

class EndlessSurvivalMode {
  constructor() {
    this.currentWave = 1;
    this.totalDefeated = 0;
    this.peakWpm = 0;
    this.isActive = false;
    this.wordsPool = [];
  }

  start() {
    this.currentWave = 1;
    this.totalDefeated = 0;
    this.peakWpm = 0;
    this.isActive = true;

    if (window.adaptiveTracker && window.adaptiveTracker.words10k.length > 0) {
      this.wordsPool = window.adaptiveTracker.words10k;
    } else {
      this.wordsPool = ['strike', 'speed', 'thunder', 'flame', 'dragon', 'fist', 'shadow', 'blade'];
    }

    if (window.combatEngine) {
      window.combatEngine.loadBackground('assets/backgrounds/world2_street.jpg');
    }
    if (window.audioManager) {
      window.audioManager.playMusic('combat');
    }

    this.spawnWave();
  }

  spawnWave() {
    if (!this.isActive) return;

    if (window.gameUI) {
      window.gameUI.showNotification(`WAVE ${this.currentWave}`, `Survival pace increasing!`);
    }

    // Number of enemies in wave scales with wave number
    const enemyCount = Math.min(6, 2 + Math.floor(this.currentWave / 2));
    for (let i = 0; i < enemyCount; i++) {
      const word = this.getRandomWordForWave(this.currentWave);
      const archetype = this.getArchetypeForWave(this.currentWave);
      setTimeout(() => {
        if (this.isActive && window.combatEngine) {
          window.combatEngine.spawnEnemy(archetype, word);
        }
      }, i * 700);
    }
  }

  getRandomWordForWave(wave) {
    const minLen = Math.min(8, 3 + Math.floor(wave / 4));
    const maxLen = minLen + 3;
    const filtered = this.wordsPool.filter(w => w.length >= minLen && w.length <= maxLen);
    if (filtered.length > 0) {
      return filtered[Math.floor(Math.random() * filtered.length)];
    }
    return 'strike';
  }

  getArchetypeForWave(wave) {
    if (wave % 5 === 0) return 'boss';
    if (wave > 3 && Math.random() > 0.6) return 'tank';
    if (wave > 2 && Math.random() > 0.5) return 'ninja';
    return 'warrior';
  }

  onEnemyDefeated(enemy) {
    if (!this.isActive) return;
    this.totalDefeated++;

    if (window.typingEngine) {
      const stats = window.typingEngine.getResults();
      if (stats.netWpm > this.peakWpm) {
        this.peakWpm = stats.netWpm;
      }
    }

    // Award XP
    if (window.beltSystem) {
      const streakMult = window.streakSystem ? window.streakSystem.getMultiplier() : 1.0;
      window.beltSystem.addXP(40 + this.currentWave * 5, streakMult);
    }

    // If no more active enemies, next wave
    if (window.combatEngine && window.combatEngine.enemies.length === 0) {
      this.currentWave++;
      if (window.saveManager) {
        window.saveManager.updateEndlessRecord(this.currentWave, this.peakWpm);
      }
      setTimeout(() => this.spawnWave(), 1000);
    }
  }

  onGameOver() {
    this.isActive = false;
    if (window.saveManager) {
      window.saveManager.updateEndlessRecord(this.currentWave, this.peakWpm);
    }
    const results = window.typingEngine ? window.typingEngine.getResults() : {};
    results.waveReached = this.currentWave;
    results.totalDefeated = this.totalDefeated;
    if (window.gameUI) {
      window.gameUI.showGameOverModal(results);
    }
  }
}

window.endlessSurvivalMode = new EndlessSurvivalMode();
