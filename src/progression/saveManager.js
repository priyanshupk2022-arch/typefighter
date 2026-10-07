// ============================================================================
// TYPEFIGHTER — 100% OFFLINE PERSISTENCE SAVE MANAGER
// ============================================================================

class SaveManager {
  constructor() {
    this.storageKey = 'typefighter_master_save';
    this.data = this.loadData();
  }

  getDefaultData() {
    return {
      version: 1,
      totalXP: 0,
      unlockedStage: 1, // 1 to 50
      completedStages: [],
      endlessHighWave: 0,
      endlessHighWpm: 0,
      dailyStreakCount: 0,
      lastPracticeDate: null,
      practiceDaysHistory: [], // ['2026-10-06', '2026-10-07']
      settings: {
        masterVolume: 1.0,
        sfxVolume: 0.85,
        musicVolume: 0.65,
        keyClickVolume: 0.75,
        screenShake: true,
        showHandGuide: true,
        showKeyboard: true
      },
      stats: {
        totalKeystrokes: 0,
        totalErrors: 0,
        totalPracticeSeconds: 0,
        peakWpm: 0,
        accuracySum: 0,
        sessionsCount: 0
      }
    };
  }

  loadData() {
    try {
      const raw = localStorage.getItem(this.storageKey);
      if (raw) {
        return { ...this.getDefaultData(), ...JSON.parse(raw) };
      }
    } catch (e) {
      console.warn('[SaveManager] Failed to read localStorage:', e);
    }
    return this.getDefaultData();
  }

  save() {
    try {
      localStorage.setItem(this.storageKey, JSON.stringify(this.data));
    } catch (e) {
      console.warn('[SaveManager] Failed to write localStorage:', e);
    }
  }

  saveXP(xp) {
    this.data.totalXP = xp;
    this.save();
  }

  unlockNextStage(stageId) {
    if (!this.data.completedStages.includes(stageId)) {
      this.data.completedStages.push(stageId);
    }
    if (stageId >= this.data.unlockedStage && this.data.unlockedStage < 50) {
      this.data.unlockedStage = stageId + 1;
    }
    this.save();
  }

  updateEndlessRecord(wave, wpm) {
    if (wave > this.data.endlessHighWave) {
      this.data.endlessHighWave = wave;
    }
    if (wpm > this.data.endlessHighWpm) {
      this.data.endlessHighWpm = wpm;
    }
    this.save();
  }

  recordSessionStats(keystrokes, errors, durationSec, wpm, accuracy) {
    this.data.stats.totalKeystrokes += keystrokes;
    this.data.stats.totalErrors += errors;
    this.data.stats.totalPracticeSeconds += durationSec;
    if (wpm > this.data.stats.peakWpm) {
      this.data.stats.peakWpm = wpm;
    }
    this.data.stats.accuracySum += accuracy;
    this.data.stats.sessionsCount += 1;
    this.save();
  }

  updateSettings(newSettings) {
    this.data.settings = { ...this.data.settings, ...newSettings };
    this.save();
  }
}

window.saveManager = new SaveManager();
