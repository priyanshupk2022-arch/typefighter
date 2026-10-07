// ============================================================================
// TYPEFIGHTER — MODE 5: PRACTICE DOJO (TARGETED DRILLS & CUSTOM TEXT)
// ============================================================================

class PracticeDojoMode {
  constructor() {
    this.isActive = false;
    this.currentCategory = 'home';
    this.drillList = [];
    this.drillIndex = 0;
  }

  start(category = 'home', customText = null) {
    this.isActive = true;
    this.currentCategory = category;
    this.drillIndex = 0;

    if (customText) {
      this.drillList = [customText];
    } else {
      this.drillList = this.generateDrillItems(category);
    }

    if (window.combatEngine) {
      window.combatEngine.loadBackground('assets/backgrounds/world1_dojo.jpg');
      window.combatEngine.enemies = [];
      window.combatEngine.activeEnemy = null;
    }

    if (window.audioManager) {
      window.audioManager.playMusic('dojo');
    }

    if (window.gameUI) {
      window.gameUI.showNotification(`PRACTICE DOJO`, `Drill: ${category.toUpperCase()} — Zero Pressure Training`);
    }

    this.loadCurrentDrillItem();
  }

  generateDrillItems(category) {
    if (category === 'home') {
      return [
        'fff jjj ddd kkk sss lll aaa ;;;',
        'asdf jkl; asdf jkl; fdsa ;lkj',
        'all lads fall as a lad asks dad',
        'a sad salad falls as all lads ask'
      ];
    } else if (category === 'top') {
      return [
        'qqq www eee rrr ttt yyy uuu iii ooo ppp',
        'qwert yuiop poiuy trewq',
        'power quick true proud write quiet pure',
        'quick strikes write true power on wire'
      ];
    } else if (category === 'bottom') {
      return [
        'zzz xxx ccc vvv bbb nnn mmm ,,, ... ///',
        'zxcvb nm,./ /.,mn bvcxz',
        'combat matrix metal boxer block nexus',
        'brave moves climb metal matrix with balance'
      ];
    } else if (category === 'ngrams') {
      return [
        'th he in er an re nd at on en ed to',
        'the and ing ion tio ent for nde has nce',
        'the true warrior that has the power'
      ];
    } else if (category === 'weak') {
      if (window.adaptiveTracker) {
        return [window.adaptiveTracker.generateReinforcementDrill(8).join(' ')];
      }
      return ['practice focus discipline accuracy precision'];
    } else {
      return ['12345 67890 !@#$% ^&*()'];
    }
  }

  loadCurrentDrillItem() {
    if (this.drillIndex >= this.drillList.length) {
      this.drillIndex = 0; // loop or complete
    }

    const text = this.drillList[this.drillIndex];
    if (window.typingEngine) {
      window.typingEngine.setTarget(text);
      if (window.keyboardGuide) {
        window.keyboardGuide.setTargetKey(window.typingEngine.getCurrentTargetChar());
      }
      if (window.handGuide) {
        window.handGuide.setTargetFinger(window.typingEngine.getCurrentFinger());
      }
    }
  }

  onItemComplete() {
    this.drillIndex++;
    if (window.audioManager) {
      window.audioManager.playLevelComplete();
    }
    if (window.beltSystem) {
      window.beltSystem.addXP(25);
    }
    if (window.calendarTracker) {
      window.calendarTracker.recordDailyPractice();
    }
    setTimeout(() => this.loadCurrentDrillItem(), 400);
  }
}

window.practiceDojoMode = new PracticeDojoMode();
