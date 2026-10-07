// ============================================================================
// TYPEFIGHTER — KEYSTROKE FLAME & OVERDRIVE STREAK SYSTEM
// ============================================================================

class StreakSystem {
  constructor() {
    this.currentStreak = 0;
    this.currentTier = 0; // 0=None, 1=Fire (15), 2=Lightning (30), 3=Overdrive (50)
    this.specialMoveReady = false;
    this.onTierChange = null;
    this.onUpdate = null;
  }

  reset() {
    this.currentStreak = 0;
    this.currentTier = 0;
    this.specialMoveReady = false;
    this.emitUpdate();
  }

  addKeystroke() {
    this.currentStreak++;
    const oldTier = this.currentTier;

    if (this.currentStreak >= 50) {
      this.currentTier = 3;
      this.specialMoveReady = true;
    } else if (this.currentStreak >= 30) {
      this.currentTier = 2;
    } else if (this.currentStreak >= 15) {
      this.currentTier = 1;
    } else {
      this.currentTier = 0;
    }

    if (this.currentTier > oldTier) {
      if (this.onTierChange) {
        this.onTierChange(this.currentTier);
      }
      if (window.audioManager) {
        const soundLvl = this.currentTier === 1 ? 15 : (this.currentTier === 2 ? 30 : 50);
        window.audioManager.playStreakSound(soundLvl);
      }
    }

    this.emitUpdate();
  }

  breakStreak() {
    if (this.currentStreak >= 15) {
      // Audio or visual cue on broken high streak
    }
    this.currentStreak = 0;
    this.currentTier = 0;
    this.specialMoveReady = false;
    this.emitUpdate();
  }

  consumeSpecialMove() {
    if (this.specialMoveReady) {
      this.specialMoveReady = false;
      this.emitUpdate();
      return true;
    }
    return false;
  }

  getMultiplier() {
    if (this.currentTier === 1) return 1.5;
    if (this.currentTier === 2) return 2.0;
    if (this.currentTier >= 3) return 3.0;
    return 1.0;
  }

  emitUpdate() {
    if (!this.onUpdate) return;
    this.onUpdate({
      streak: this.currentStreak,
      tier: this.currentTier,
      multiplier: this.getMultiplier(),
      specialMoveReady: this.specialMoveReady
    });
  }
}

window.streakSystem = new StreakSystem();
