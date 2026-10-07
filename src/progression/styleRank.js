// ============================================================================
// TYPEFIGHTER — DEVIL MAY CRY STYLE RANK ENGINE (D -> SSS)
// ============================================================================

const STYLE_RANKS = [
  { id: 'rank-d', key: 'D', name: 'DULL', minPoints: 0, color: '#8892b0' },
  { id: 'rank-c', key: 'C', name: 'COOL', minPoints: 100, color: '#00f0ff' },
  { id: 'rank-b', key: 'B', name: 'BRAVO', minPoints: 240, color: '#00ff88' },
  { id: 'rank-a', key: 'A', name: 'AWESOME', minPoints: 420, color: '#ffd700' },
  { id: 'rank-s', key: 'S', name: 'STYLISH!', minPoints: 650, color: '#ff9900' },
  { id: 'rank-ss', key: 'SS', name: 'SUPER STYLISH!!', minPoints: 920, color: '#ff3333' },
  { id: 'rank-sss', key: 'SSS', name: "SMOKIN' SEXY STYLE!!!", minPoints: 1250, color: '#ffd700' }
];

class StyleRankManager {
  constructor() {
    this.currentPoints = 0;
    this.currentRankIndex = 0;
    this.decayRate = 18; // points decayed per second of hesitation
    this.lastActionTime = performance.now();
    this.onRankChange = null;
    this.onUpdate = null;
  }

  reset() {
    this.currentPoints = 0;
    this.currentRankIndex = 0;
    this.lastActionTime = performance.now();
    this.emitUpdate();
  }

  addPoints(points, streakMultiplier = 1.0) {
    const gained = points * streakMultiplier;
    this.currentPoints = Math.min(1500, this.currentPoints + gained);
    this.lastActionTime = performance.now();
    this.checkRankTransition();
    this.emitUpdate();
  }

  applyTypoPenalty() {
    // Punish typo by cutting meter by 25%
    this.currentPoints = Math.max(0, this.currentPoints - 150);
    this.checkRankTransition();
    this.emitUpdate();
  }

  update(dt) {
    const now = performance.now();
    // Start decaying after 800ms of inactivity
    if (now - this.lastActionTime > 800 && this.currentPoints > 0) {
      this.currentPoints = Math.max(0, this.currentPoints - this.decayRate * dt);
      this.checkRankTransition();
      this.emitUpdate();
    }
  }

  checkRankTransition() {
    let newIndex = 0;
    for (let i = STYLE_RANKS.length - 1; i >= 0; i--) {
      if (this.currentPoints >= STYLE_RANKS[i].minPoints) {
        newIndex = i;
        break;
      }
    }

    if (newIndex !== this.currentRankIndex) {
      const isUp = newIndex > this.currentRankIndex;
      this.currentRankIndex = newIndex;

      if (this.onRankChange) {
        this.onRankChange(STYLE_RANKS[this.currentRankIndex], isUp);
      }

      if (window.audioManager) {
        if (isUp) window.audioManager.playRankUp();
        window.audioManager.setStyleRankIntensity(this.currentRankIndex);
      }
    }
  }

  getCurrentRank() {
    return STYLE_RANKS[this.currentRankIndex];
  }

  emitUpdate() {
    if (!this.onUpdate) return;
    const current = STYLE_RANKS[this.currentRankIndex];
    const next = STYLE_RANKS[this.currentRankIndex + 1];

    let progressInTier = 1.0;
    if (next) {
      const tierSpan = next.minPoints - current.minPoints;
      progressInTier = Math.min(1.0, Math.max(0, (this.currentPoints - current.minPoints) / tierSpan));
    }

    this.onUpdate({
      rank: current,
      rankIndex: this.currentRankIndex,
      points: Math.round(this.currentPoints),
      tierProgress: progressInTier
    });
  }
}

window.styleRankManager = new StyleRankManager();
