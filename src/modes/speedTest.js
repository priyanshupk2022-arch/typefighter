// ============================================================================
// TYPEFIGHTER — MODE 4: SPEED TEST & ACCURACY ANALYZER (1M / 2M / 3M)
// ============================================================================

class SpeedTestMode {
  constructor() {
    this.durationSeconds = 60; // 60, 120, 180
    this.remainingSeconds = 60;
    this.timerInterval = null;
    this.isActive = false;
    this.currentPassage = null;
  }

  start(duration = 60) {
    this.durationSeconds = duration;
    this.remainingSeconds = duration;
    this.isActive = true;

    // Pick literary passage
    if (window.curriculumManager) {
      this.currentPassage = window.curriculumManager.getRandomPassage(false);
    }

    const textToType = this.currentPassage ? this.currentPassage.text : "Discipline is the foundation of flawless typing speed.";

    if (window.combatEngine) {
      window.combatEngine.loadBackground('assets/backgrounds/world1_dojo.jpg');
      // In Speed Test, spawn dummy training wooden dummy or peaceful martial stance
      window.combatEngine.enemies = [];
      window.combatEngine.activeEnemy = null;
    }

    if (window.audioManager) {
      window.audioManager.playMusic('zen');
    }

    if (window.typingEngine) {
      window.typingEngine.resetMetrics();
      window.typingEngine.setTarget(textToType);
      if (window.keyboardGuide) {
        window.keyboardGuide.setTargetKey(window.typingEngine.getCurrentTargetChar());
      }
      if (window.handGuide) {
        window.handGuide.setTargetFinger(window.typingEngine.getCurrentFinger());
      }
    }

    if (window.gameUI) {
      window.gameUI.showNotification(`SPEED TEST (${duration}s)`, `${this.currentPassage ? this.currentPassage.title : 'Literary Benchmark'}`);
    }

    clearInterval(this.timerInterval);
    this.timerInterval = setInterval(() => {
      this.remainingSeconds--;
      if (window.gameUI) {
        window.gameUI.updateSpeedTestTimer(this.remainingSeconds);
      }
      if (this.remainingSeconds <= 0) {
        this.finishTest();
      }
    }, 1000);
  }

  finishTest() {
    this.isActive = false;
    clearInterval(this.timerInterval);

    if (window.audioManager) {
      window.audioManager.playLevelComplete();
    }

    const results = window.typingEngine ? window.typingEngine.getResults() : {};
    results.passageTitle = this.currentPassage ? this.currentPassage.title : 'Speed Benchmark';
    results.passageAuthor = this.currentPassage ? this.currentPassage.author : 'Classic';
    results.isSpeedTest = true;

    if (window.saveManager) {
      window.saveManager.recordSessionStats(
        results.totalKeystrokes,
        results.errorKeystrokes,
        this.durationSeconds,
        results.netWpm,
        results.accuracy
      );
      if (window.calendarTracker) {
        window.calendarTracker.recordDailyPractice();
      }
    }

    if (window.gameUI) {
      window.gameUI.showSpeedTestResultsModal(results);
    }
  }
}

window.speedTestMode = new SpeedTestMode();
