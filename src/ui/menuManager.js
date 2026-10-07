// ============================================================================
// TYPEFIGHTER — MENU, MODALS & PROFILE DASHBOARD MANAGER
// ============================================================================

class MenuManager {
  constructor() {
    this.mainMenuModal = null;
    this.stageSelectModal = null;
    this.pauseModal = null;
    this.victoryModal = null;
    this.gameOverModal = null;
    this.settingsModal = null;
    this.profileModal = null;
  }

  init() {
    this.mainMenuModal = document.getElementById('mainMenuModal');
    this.stageSelectModal = document.getElementById('stageSelectModal');
    this.pauseModal = document.getElementById('pauseModal');
    this.victoryModal = document.getElementById('victoryModal');
    this.gameOverModal = document.getElementById('gameOverModal');
    this.settingsModal = document.getElementById('settingsModal');
    this.profileModal = document.getElementById('profileModal');

    this.bindButtons();
  }

  bindButtons() {
    // Main Menu Buttons
    document.getElementById('btnMenuStory')?.addEventListener('click', () => {
      this.hideAllModals();
      this.openStageSelect();
    });

    document.getElementById('btnMenuEndless')?.addEventListener('click', () => {
      this.hideAllModals();
      if (window.game) window.game.startMode('endless');
    });

    document.getElementById('btnMenuDaily')?.addEventListener('click', () => {
      this.hideAllModals();
      if (window.game) window.game.startMode('daily');
    });

    document.getElementById('btnMenuSpeedTest')?.addEventListener('click', () => {
      this.hideAllModals();
      if (window.game) window.game.startMode('speedtest');
    });

    document.getElementById('btnMenuDojo')?.addEventListener('click', () => {
      this.hideAllModals();
      if (window.game) window.game.startMode('dojo');
    });

    document.getElementById('btnMenuProfile')?.addEventListener('click', () => {
      this.openProfileModal();
    });

    document.getElementById('btnMenuSettings')?.addEventListener('click', () => {
      this.openSettingsModal();
    });

    // Close Modals buttons
    document.querySelectorAll('.btn-close-modal').forEach(btn => {
      btn.addEventListener('click', () => {
        this.hideAllModals();
        this.openMainMenu();
      });
    });

    // Settings Sliders
    this.bindSettingsControls();
  }

  bindSettingsControls() {
    const sMaster = document.getElementById('sliderMasterVol');
    const sSfx = document.getElementById('sliderSfxVol');
    const sMusic = document.getElementById('sliderMusicVol');
    const sKey = document.getElementById('sliderKeyVol');
    const togShake = document.getElementById('toggleScreenShake');
    const togHands = document.getElementById('toggleHandsGuide');

    if (sMaster) {
      sMaster.addEventListener('input', (e) => {
        if (window.audioManager) window.audioManager.masterVolume = parseFloat(e.target.value);
      });
    }
    if (sSfx) {
      sSfx.addEventListener('input', (e) => {
        if (window.audioManager) window.audioManager.sfxVolume = parseFloat(e.target.value);
      });
    }
    if (sMusic) {
      sMusic.addEventListener('input', (e) => {
        if (window.audioManager) window.audioManager.musicVolume = parseFloat(e.target.value);
      });
    }
    if (sKey) {
      sKey.addEventListener('input', (e) => {
        if (window.audioManager) window.audioManager.keyClickVolume = parseFloat(e.target.value);
      });
    }
    if (togShake) {
      togShake.addEventListener('change', (e) => {
        if (window.saveManager) window.saveManager.updateSettings({ screenShake: e.target.checked });
      });
    }
    if (togHands) {
      togHands.addEventListener('change', (e) => {
        const wrap = document.getElementById('pedagogyOverlay');
        if (wrap) wrap.style.display = e.target.checked ? 'flex' : 'none';
        if (window.saveManager) window.saveManager.updateSettings({ showHandGuide: e.target.checked });
      });
    }
  }

  hideAllModals() {
    const modals = [
      this.mainMenuModal, this.stageSelectModal, this.pauseModal,
      this.victoryModal, this.gameOverModal, this.settingsModal, this.profileModal
    ];
    for (const m of modals) {
      if (m) m.classList.add('hidden');
    }
  }

  openMainMenu() {
    this.hideAllModals();
    if (this.mainMenuModal) this.mainMenuModal.classList.remove('hidden');
    if (window.audioManager) window.audioManager.playMusic('menu');
  }

  openStageSelect() {
    this.hideAllModals();
    if (!this.stageSelectModal) return;

    const grid = document.getElementById('stageGrid');
    if (grid) {
      grid.innerHTML = '';
      const unlocked = (window.saveManager && window.saveManager.data) ? window.saveManager.data.unlockedStage : 1;

      // 5 Worlds x 10 Stages = 50
      for (let s = 1; s <= 50; s++) {
        const btn = document.createElement('button');
        const isUnlocked = s <= unlocked;
        const isBoss = s % 10 === 0;

        btn.className = `stage-node-btn ${isUnlocked ? 'unlocked' : 'locked'} ${isBoss ? 'boss-stage' : ''}`;
        btn.innerHTML = `
          <span class="stage-num">${s}</span>
          <span class="stage-type">${isBoss ? '👑 BOSS' : (s <= 10 ? 'DOJO' : 'BRAWL')}</span>
        `;

        if (isUnlocked) {
          btn.addEventListener('click', () => {
            this.hideAllModals();
            if (window.game) window.game.startStoryStage(s);
          });
        }
        grid.appendChild(btn);
      }
    }
    this.stageSelectModal.classList.remove('hidden');
  }

  openProfileModal() {
    this.hideAllModals();
    if (!this.profileModal) return;

    // Populate Belt Info
    const belt = window.beltSystem ? window.beltSystem.getCurrentBelt() : null;
    const nextBelt = window.beltSystem ? window.beltSystem.getNextBelt() : null;
    const xp = window.beltSystem ? window.beltSystem.totalXP : 0;

    const bNameEl = document.getElementById('profileBeltName');
    const bTitleEl = document.getElementById('profileBeltTitle');
    const bXpEl = document.getElementById('profileXpVal');
    const bIconEl = document.getElementById('profileBeltIcon');
    const bBarEl = document.getElementById('profileBeltBarFill');

    if (bNameEl && belt) bNameEl.textContent = belt.name;
    if (bTitleEl && belt) bTitleEl.textContent = belt.title;
    if (bXpEl) bXpEl.textContent = `${xp.toLocaleString()} XP`;
    if (bIconEl && belt) bIconEl.src = belt.svg;
    if (bBarEl && window.beltSystem) {
      bBarEl.style.width = `${Math.round(window.beltSystem.getProgressToNext() * 100)}%`;
    }

    // Populate 30-Day Calendar Grid
    const calGrid = document.getElementById('calendarDaysGrid');
    if (calGrid && window.calendarTracker) {
      calGrid.innerHTML = '';
      const days = window.calendarTracker.generateCalendarGrid(30);
      for (const d of days) {
        const div = document.createElement('div');
        div.className = `cal-day-box ${d.isCompleted ? 'completed' : ''} ${d.isToday ? 'today' : ''}`;
        div.innerHTML = `
          <span class="d-num">${d.dayNumber}</span>
          <span class="d-mark">${d.isCompleted ? '✓' : '•'}</span>
        `;
        calGrid.appendChild(div);
      }
    }

    this.profileModal.classList.remove('hidden');
  }

  openSettingsModal() {
    this.hideAllModals();
    if (this.settingsModal) this.settingsModal.classList.remove('hidden');
  }

  showVictoryModal(stageNum, results) {
    this.hideAllModals();
    if (!this.victoryModal) return;

    document.getElementById('vicStageTitle').textContent = `STAGE ${stageNum} CLEARED!`;
    document.getElementById('vicWpm').textContent = results.netWpm || 0;
    document.getElementById('vicAccuracy').textContent = `${results.accuracy || 100}%`;
    document.getElementById('vicStreak').textContent = results.bestStreak || 0;

    // 100% Accuracy badge
    const badge = document.getElementById('vicFlawlessBadge');
    if (badge) {
      badge.style.display = (results.accuracy === 100) ? 'inline-block' : 'none';
    }

    this.victoryModal.classList.remove('hidden');
  }

  showGameOverModal(results) {
    this.hideAllModals();
    if (!this.gameOverModal) return;

    document.getElementById('goWpm').textContent = results.netWpm || 0;
    document.getElementById('goAccuracy').textContent = `${results.accuracy || 0}%`;

    this.gameOverModal.classList.remove('hidden');
  }
}

window.menuManager = new MenuManager();
