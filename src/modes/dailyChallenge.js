// ============================================================================
// TYPEFIGHTER — MODE 3: DAILY CHALLENGE (DETERMINISTIC DATE SEED)
// ============================================================================

class DailyChallengeMode {
  constructor() {
    this.isActive = false;
    this.challengeWords = [];
    this.currentIndex = 0;
  }

  // Deterministic Pseudo-Random Number Generator based on date string
  getDateSeed() {
    const today = new Date().toISOString().slice(0, 10); // YYYY-MM-DD
    let hash = 0;
    for (let i = 0; i < today.length; i++) {
      hash = (hash << 5) - hash + today.charCodeAt(i);
      hash |= 0;
    }
    return Math.abs(hash);
  }

  start() {
    this.isActive = true;
    this.currentIndex = 0;

    const seed = this.getDateSeed();
    const wordPool = (window.adaptiveTracker && window.adaptiveTracker.words10k.length > 0)
      ? window.adaptiveTracker.words10k
      : ['discipline', 'precision', 'balance', 'accuracy', 'focus', 'strength', 'champion', 'perfection', 'grandmaster', 'victory'];

    // Pick 12 deterministic words
    this.challengeWords = [];
    for (let i = 0; i < 12; i++) {
      const idx = (seed * (i + 1) * 31 + 17) % wordPool.length;
      this.challengeWords.push(wordPool[idx]);
    }

    if (window.combatEngine) {
      window.combatEngine.loadBackground('assets/backgrounds/world4_rooftop.jpg');
    }
    if (window.audioManager) {
      window.audioManager.playMusic('combat');
    }
    if (window.gameUI) {
      const streakInfo = window.calendarTracker ? window.calendarTracker.getStreakInfo() : { streakDays: 0 };
      window.gameUI.showNotification(`DAILY CHALLENGE`, `Daily Streak: ${streakInfo.streakDays} Days (${(1 + streakInfo.streakDays * 0.1).toFixed(1)}x XP Bonus)`);
    }

    this.spawnNext();
  }

  spawnNext() {
    if (!this.isActive) return;
    if (this.currentIndex >= this.challengeWords.length) {
      this.challengeComplete();
      return;
    }

    const word = this.challengeWords[this.currentIndex];
    this.currentIndex++;
    const archetype = this.currentIndex === this.challengeWords.length ? 'boss' : (word.length > 7 ? 'tank' : 'warrior');
    window.combatEngine.spawnEnemy(archetype, word);
  }

  onEnemyDefeated(enemy) {
    if (!this.isActive) return;

    if (window.beltSystem) {
      const streakDays = window.calendarTracker ? window.calendarTracker.getStreakInfo().streakDays : 0;
      const dailyBonus = 1.0 + streakDays * 0.1;
      window.beltSystem.addXP(60, dailyBonus);
    }

    setTimeout(() => this.spawnNext(), 400);
  }

  challengeComplete() {
    this.isActive = false;
    if (window.calendarTracker) {
      window.calendarTracker.recordDailyPractice();
    }
    if (window.audioManager) {
      window.audioManager.playLevelComplete();
    }
    const results = window.typingEngine ? window.typingEngine.getResults() : {};
    results.isDailyChallenge = true;
    if (window.gameUI) {
      window.gameUI.showStageVictoryModal(999, results);
    }
  }
}

window.dailyChallengeMode = new DailyChallengeMode();
