// ============================================================================
// TYPEFIGHTER — 10 MARTIAL ARTS BELTS & XP PROGRESSION SYSTEM
// ============================================================================

const BELTS = [
  { id: 'white', name: 'White Belt', title: 'Beginner Initiate', minXP: 0, svg: 'assets/icons/belts/belt_white.svg', color: '#f8fafc' },
  { id: 'yellow', name: 'Yellow Belt', title: 'Home Row Adept', minXP: 1000, svg: 'assets/icons/belts/belt_yellow.svg', color: '#facc15' },
  { id: 'orange', name: 'Orange Belt', title: 'Top Row Striker', minXP: 2500, svg: 'assets/icons/belts/belt_orange.svg', color: '#fb923c' },
  { id: 'green', name: 'Green Belt', title: 'Bottom Row Defender', minXP: 5000, svg: 'assets/icons/belts/belt_green.svg', color: '#4ade80' },
  { id: 'blue', name: 'Blue Belt', title: 'Rhythm Warrior', minXP: 9000, svg: 'assets/icons/belts/belt_blue.svg', color: '#38bdf8' },
  { id: 'purple', name: 'Purple Belt', title: 'Combo Master', minXP: 15000, svg: 'assets/icons/belts/belt_purple.svg', color: '#c084fc' },
  { id: 'brown', name: 'Brown Belt', title: 'Shift Specialist', minXP: 23000, svg: 'assets/icons/belts/belt_brown.svg', color: '#b45309' },
  { id: 'red', name: 'Red Belt', title: 'Apex Brawler', minXP: 34000, svg: 'assets/icons/belts/belt_red.svg', color: '#f87171' },
  { id: 'black', name: 'Black Belt', title: 'Touch Typing Virtuoso', minXP: 50000, svg: 'assets/icons/belts/belt_black.svg', color: '#1e293b' },
  { id: 'grandmaster', name: 'Grandmaster Belt', title: 'Legendary Senshi', minXP: 75000, svg: 'assets/icons/belts/belt_grandmaster.svg', color: '#eab308' }
];

class BeltSystem {
  constructor() {
    this.totalXP = 0;
    this.currentBeltIndex = 0;
    this.onBeltUp = null;
    this.onXPChange = null;
  }

  init(savedXP = 0) {
    this.totalXP = savedXP;
    this.recalculateBelt();
  }

  addXP(amount, multiplier = 1.0) {
    const gained = Math.round(amount * multiplier);
    this.totalXP += gained;
    const oldIndex = this.currentBeltIndex;
    this.recalculateBelt();

    if (this.currentBeltIndex > oldIndex) {
      if (this.onBeltUp) {
        this.onBeltUp(BELTS[this.currentBeltIndex]);
      }
      if (window.audioManager) {
        window.audioManager.playLevelComplete();
      }
    }

    if (this.onXPChange) {
      this.onXPChange({
        gained,
        totalXP: this.totalXP,
        belt: BELTS[this.currentBeltIndex]
      });
    }

    if (window.saveManager) {
      window.saveManager.saveXP(this.totalXP);
    }
    return gained;
  }

  recalculateBelt() {
    let index = 0;
    for (let i = BELTS.length - 1; i >= 0; i--) {
      if (this.totalXP >= BELTS[i].minXP) {
        index = i;
        break;
      }
    }
    this.currentBeltIndex = index;
  }

  getCurrentBelt() {
    return BELTS[this.currentBeltIndex];
  }

  getNextBelt() {
    return BELTS[this.currentBeltIndex + 1] || null;
  }

  getProgressToNext() {
    const cur = this.getCurrentBelt();
    const next = this.getNextBelt();
    if (!next) return 1.0;
    const span = next.minXP - cur.minXP;
    return Math.min(1.0, Math.max(0, (this.totalXP - cur.minXP) / span));
  }
}

window.beltSystem = new BeltSystem();
