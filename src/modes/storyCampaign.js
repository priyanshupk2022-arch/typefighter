// ============================================================================
// TYPEFIGHTER — MODE 1: STORY CAMPAIGN (50 STAGES ACROSS 5 WORLDS)
// ============================================================================

class StoryCampaignMode {
  constructor() {
    this.currentWorld = 1;
    this.currentStage = 1;
    this.stageData = null;
    this.phase = 'idle'; // 'warmup', 'brawl', 'boss', 'cleared'
    this.warmupIndex = 0;
    this.warmupList = [];
    this.brawlQueue = [];
    this.enemiesDefeatedInStage = 0;
  }

  startStage(stageNumber) {
    this.currentStage = stageNumber;
    this.currentWorld = Math.min(5, Math.floor((stageNumber - 1) / 10) + 1);
    const stageInWorld = ((stageNumber - 1) % 10) + 1;

    this.stageData = window.curriculumManager.getStageData(this.currentWorld, stageInWorld);
    this.enemiesDefeatedInStage = 0;

    // Load world background and music
    if (window.combatEngine && this.stageData.world) {
      window.combatEngine.loadBackground(this.stageData.world.background);
    }
    if (window.audioManager && this.stageData.world) {
      window.audioManager.playMusic(this.stageData.world.music);
    }

    if (this.stageData.isBoss) {
      this.startBossPhase();
    } else {
      this.startWarmupPhase();
    }
  }

  startWarmupPhase() {
    this.phase = 'warmup';
    this.warmupIndex = 0;
    const keys = this.stageData.warmupKeys;
    // Generate 5 warm-up repetitive patterns for muscle memory
    this.warmupList = [
      keys.join(''),
      keys.slice().reverse().join(''),
      keys.map(k => k + k).join(' '),
      keys.join(' ')
    ];

    // Show Warmup HUD Banner
    if (window.gameUI) {
      window.gameUI.showNotification(`STAGE ${this.currentStage}: DOJO WARM-UP`, `Anchor finger placement for: ${keys.join(' ').toUpperCase()}`);
    }

    this.nextWarmupItem();
  }

  nextWarmupItem() {
    if (this.warmupIndex >= this.warmupList.length) {
      // Warm-up complete -> Proceed to Brawl
      this.startBrawlPhase();
      return;
    }

    const item = this.warmupList[this.warmupIndex];
    this.warmupIndex++;

    if (window.typingEngine) {
      window.typingEngine.setTarget(item);
      if (window.keyboardGuide) {
        window.keyboardGuide.setTargetKey(window.typingEngine.getCurrentTargetChar());
      }
      if (window.handGuide) {
        window.handGuide.setTargetFinger(window.typingEngine.getCurrentFinger());
      }
    }
  }

  startBrawlPhase() {
    this.phase = 'brawl';
    if (window.gameUI) {
      window.gameUI.showNotification(`STREET BRAWL!`, `Defeat the incoming enemy waves!`);
    }

    // Prepare queue of 8-12 enemies
    this.brawlQueue = [...this.stageData.enemyWords];
    this.spawnNextBrawlEnemy();
  }

  spawnNextBrawlEnemy() {
    if (this.brawlQueue.length === 0) {
      // Stage Cleared!
      this.stageCleared();
      return;
    }

    const word = this.brawlQueue.shift();
    const archetype = word.length <= 2 ? 'grunt' : (word.length <= 5 ? 'warrior' : 'ninja');
    window.combatEngine.spawnEnemy(archetype, word);
  }

  startBossPhase() {
    this.phase = 'boss';
    const boss = this.stageData.bossConfig;
    if (window.gameUI) {
      window.gameUI.showNotification(`BOSS BATTLE!`, `${boss.name} — ${boss.title}`);
    }
    if (window.audioManager) {
      window.audioManager.playMusic('boss');
    }

    this.brawlQueue = [...boss.sentences];
    window.combatEngine.spawnEnemy('boss', this.brawlQueue.shift());
  }

  onEnemyDefeated(enemy) {
    this.enemiesDefeatedInStage++;
    // Award XP
    if (window.beltSystem) {
      const streakMult = window.streakSystem ? window.streakSystem.getMultiplier() : 1.0;
      window.beltSystem.addXP(enemy.archetype === 'boss' ? 500 : 35, streakMult);
    }

    if (this.phase === 'brawl') {
      setTimeout(() => this.spawnNextBrawlEnemy(), 400);
    } else if (this.phase === 'boss') {
      if (this.brawlQueue.length > 0) {
        setTimeout(() => {
          window.combatEngine.spawnEnemy('boss', this.brawlQueue.shift());
        }, 600);
      } else {
        this.stageCleared();
      }
    }
  }

  stageCleared() {
    this.phase = 'cleared';
    if (window.audioManager) {
      window.audioManager.playLevelComplete();
    }
    if (window.saveManager) {
      window.saveManager.unlockNextStage(this.currentStage);
      if (window.calendarTracker) {
        window.calendarTracker.recordDailyPractice();
      }
    }

    const results = window.typingEngine ? window.typingEngine.getResults() : {};
    if (window.gameUI) {
      window.gameUI.showStageVictoryModal(this.currentStage, results);
    }
  }
}

window.storyCampaignMode = new StoryCampaignMode();
