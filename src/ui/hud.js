// ============================================================================
// TYPEFIGHTER — ARCADE COMBAT HUD & METRICS CONTROLLER
// ============================================================================

class GameHUD {
  constructor() {
    this.heroHpFill = null;
    this.wpmVal = null;
    this.accuracyVal = null;
    this.comboVal = null;
    this.rankLetter = null;
    this.rankName = null;
    this.styleMeterFill = null;
    this.streakBadge = null;
    this.streakCount = null;
    this.stageTitle = null;
    this.targetWordCard = null;
    this.notificationToast = null;
  }

  init() {
    this.heroHpFill = document.getElementById('heroHpFill');
    this.wpmVal = document.getElementById('hudWpmVal');
    this.accuracyVal = document.getElementById('hudAccuracyVal');
    this.comboVal = document.getElementById('hudComboVal');
    this.rankLetter = document.getElementById('hudRankLetter');
    this.rankName = document.getElementById('hudRankName');
    this.styleMeterFill = document.getElementById('hudStyleMeterFill');
    this.streakBadge = document.getElementById('hudStreakBadge');
    this.streakCount = document.getElementById('hudStreakCount');
    this.stageTitle = document.getElementById('hudStageTitle');
    this.targetWordCard = document.getElementById('targetWordCard');
    this.notificationToast = document.getElementById('notificationToast');

    // Hook Style Rank updates
    if (window.styleRankManager) {
      window.styleRankManager.onUpdate = (data) => this.updateStyleRank(data);
    }

    // Hook Streak updates
    if (window.streakSystem) {
      window.streakSystem.onUpdate = (data) => this.updateStreak(data);
    }

    // Hook Typing metrics
    if (window.typingEngine) {
      window.typingEngine.onMetricsUpdate = (data) => this.updateMetrics(data);
    }
  }

  updateHeroHp(hp, maxHp = 100) {
    if (this.heroHpFill) {
      const pct = Math.max(0, Math.min(100, (hp / maxHp) * 100));
      this.heroHpFill.style.width = `${pct}%`;
    }
  }

  updateMetrics(data) {
    if (this.wpmVal) this.wpmVal.textContent = data.netWpm;
    if (this.accuracyVal) this.accuracyVal.textContent = `${data.accuracy}%`;
    if (this.comboVal) this.comboVal.textContent = `${data.currentStreak}x`;
    this.renderTargetPrompt();
  }

  updateStyleRank(data) {
    if (!this.rankLetter || !this.rankName) return;

    this.rankLetter.textContent = data.rank.key;
    this.rankLetter.className = `style-rank-letter ${data.rank.id}`;
    this.rankName.textContent = data.rank.name;

    if (this.styleMeterFill) {
      this.styleMeterFill.style.width = `${Math.round(data.tierProgress * 100)}%`;
    }
  }

  updateStreak(data) {
    if (!this.streakBadge || !this.streakCount) return;

    this.streakCount.textContent = data.streak;
    this.streakBadge.className = 'streak-badge';

    if (data.tier === 1) {
      this.streakBadge.classList.add('fire');
      this.streakBadge.querySelector('.streak-label').textContent = 'FIRE';
    } else if (data.tier === 2) {
      this.streakBadge.classList.add('lightning');
      this.streakBadge.querySelector('.streak-label').textContent = 'LIGHTNING';
    } else if (data.tier >= 3) {
      this.streakBadge.classList.add('overdrive');
      this.streakBadge.querySelector('.streak-label').textContent = 'OVERDRIVE';
    } else {
      this.streakBadge.querySelector('.streak-label').textContent = 'STREAK';
    }
  }

  setStageTitle(text) {
    if (this.stageTitle) {
      this.stageTitle.textContent = text;
    }
  }

  renderTargetPrompt() {
    if (!this.targetWordCard || !window.typingEngine) return;
    const text = window.typingEngine.targetText;
    const curIdx = window.typingEngine.currentIndex;

    this.targetWordCard.innerHTML = '';
    for (let i = 0; i < text.length; i++) {
      const span = document.createElement('span');
      span.className = 'target-char';
      span.textContent = text[i] === ' ' ? '␣' : text[i];

      if (i < curIdx) {
        span.classList.add('typed');
      } else if (i === curIdx) {
        span.classList.add('active');
      } else {
        span.classList.add('pending');
      }
      this.targetWordCard.appendChild(span);
    }
  }

  triggerPromptError() {
    if (!this.targetWordCard) return;
    const activeSpan = this.targetWordCard.querySelector('.target-char.active');
    if (activeSpan) {
      activeSpan.classList.add('error');
      setTimeout(() => activeSpan.classList.remove('error'), 250);
    }
  }

  showNotification(title, subtitle) {
    if (!this.notificationToast) return;
    this.notificationToast.querySelector('.notif-title').textContent = title;
    this.notificationToast.querySelector('.notif-sub').textContent = subtitle;
    this.notificationToast.classList.remove('hidden');

    clearTimeout(this._notifTimeout);
    this._notifTimeout = setTimeout(() => {
      this.notificationToast.classList.add('hidden');
    }, 2800);
  }
}

window.gameHUD = new GameHUD();
