// Keyboard Warrior Stickman - Combat Mechanics & DMC Style Rank Engine
export class ComboEngine {
  constructor(audioSystem, arenaManager) {
    this.audio = audioSystem;
    this.arena = arenaManager;

    // Combo & Style State
    this.hits = 0;
    this.maxHits = 0;
    this.score = 0;
    this.comboTimer = 0;
    this.comboTimeout = 2.8; // Seconds before combo meter drops

    // DMC Style Rank: D -> C -> B -> A -> S -> SS -> SSS
    this.ranks = ['D', 'C', 'B', 'A', 'S', 'SS', 'SSS'];
    this.rankNames = {
      'D': 'DISMAL',
      'C': 'CRAZY',
      'B': 'BADASS',
      'A': 'APOCALYPTIC',
      'S': 'SAVAGE',
      'SS': 'SICK SKILLS',
      'SSS': 'SMOKIN\' SEXY STYLE!'
    };
    this.currentRankIndex = 0;
    this.stylePoints = 0;
    this.styleThreshold = 100;
    this.decayRate = 18; // Points lost per second when idle

    // Rage Mode State
    this.isRageMode = false;
    this.rageTimer = 0;

    // Movement speeds
    this.walkSpeed = 4.0;
  }

  registerHit(type = 'light', hero, enemy) {
    this.hits++;
    if (this.hits > this.maxHits) this.maxHits = this.hits;
    this.comboTimer = this.comboTimeout;

    // Multiplier based on style rank
    const multiplier = 1 + this.currentRankIndex * 0.5;
    const baseScore = type === 'crit' ? 300 : type === 'heavy' ? 150 : 80;
    const addedScore = Math.round(baseScore * multiplier * (this.isRageMode ? 2 : 1));
    this.score += addedScore;

    // Style point addition
    const addedStyle = type === 'crit' ? 35 : type === 'heavy' ? 22 : 12;
    this.addStylePoints(addedStyle);

    // Audio & Screen Juice
    this.audio.playCombatHit(type);
    this.arena.triggerScreenShake(type === 'crit' ? 0.35 : 0.15);

    // Enemy Reaction
    if (enemy) {
      enemy.takeHit(this.isRageMode ? 15 : 8, false);
    }
    if (hero) {
      hero.setPose(type === 'kick' ? 'kick' : 'jab', 0.18);
    }
  }

  registerMiss() {
    // Punish player on typo / miss
    this.comboTimer = 0;
    this.hits = 0;
    this.stylePoints = Math.max(0, this.stylePoints - 40);
    if (this.stylePoints <= 0 && this.currentRankIndex > 0) {
      this.currentRankIndex--;
      this.stylePoints = 50;
    }
    this.audio.playKeyClack(true);
    this.arena.triggerScreenShake(0.2);
  }

  addStylePoints(points) {
    this.stylePoints += points;
    if (this.stylePoints >= this.styleThreshold) {
      if (this.currentRankIndex < this.ranks.length - 1) {
        this.currentRankIndex++;
        this.stylePoints = 25;
        this.audio.playSpecialKey('caps'); // Rank up chime
      } else {
        this.stylePoints = this.styleThreshold;
      }
    }
  }

  triggerAirLauncher(hero, enemy) {
    this.audio.playSpecialKey('space');
    this.arena.triggerScreenShake(0.4);

    if (hero) hero.setPose('launcher', 0.5);
    if (enemy) {
      enemy.launchIntoAir(13.0);
      enemy.takeHit(15, true);
    }
    this.addStylePoints(30);
    this.hits += 2;
    this.score += 500;
  }

  triggerGroundSlam(hero, enemy) {
    if (!enemy || !enemy.isAirborne) {
      // Still execute ground sweep if grounded
      this.audio.playSpecialKey('enter');
      this.arena.triggerScreenShake(0.3);
      if (hero) hero.setPose('kick', 0.4);
      if (enemy) enemy.takeHit(12, false);
      return;
    }

    this.audio.playSpecialKey('enter');
    this.arena.triggerScreenShake(0.65); // Massive screen impact shake!
    if (hero) hero.groundSlam();
    if (enemy) {
      enemy.groundSlam();
      enemy.takeHit(35, false);
    }
    this.addStylePoints(50);
    this.hits += 3;
    this.score += 1000;
  }

  triggerDash(hero, direction = 1) {
    this.audio.playSpecialKey('tab');
    if (hero) {
      hero.x += direction * 0.8;
      hero.setPose('run', 0.25);
    }
  }

  triggerRageMode() {
    this.isRageMode = !this.isRageMode;
    if (this.isRageMode) {
      this.rageTimer = 6.0; // 6 seconds of fury
      this.audio.playSpecialKey('caps');
      this.arena.triggerScreenShake(0.3);
    }
  }

  moveHero(hero, dx, delta) {
    if (!hero) return;
    hero.x += dx * this.walkSpeed * delta;
    hero.x = Math.max(-4.5, Math.min(1.0, hero.x)); // Keep within fighting range
    hero.updatePosition();
  }

  update(delta) {
    // Combo timer decay
    if (this.comboTimer > 0) {
      this.comboTimer -= delta;
      if (this.comboTimer <= 0) {
        this.hits = 0;
      }
    }

    // Style Rank decay when inactive
    if (this.hits === 0 && this.stylePoints > 0) {
      this.stylePoints -= this.decayRate * delta;
      if (this.stylePoints <= 0) {
        if (this.currentRankIndex > 0) {
          this.currentRankIndex--;
          this.stylePoints = 75;
        } else {
          this.stylePoints = 0;
        }
      }
    }

    // Rage Mode timer
    if (this.isRageMode) {
      this.rageTimer -= delta;
      if (this.rageTimer <= 0) {
        this.isRageMode = false;
      }
    }
  }

  getCurrentRank() {
    return this.ranks[this.currentRankIndex];
  }

  getCurrentRankTitle() {
    const rank = this.getCurrentRank();
    return this.rankNames[rank] || rank;
  }

  getRankProgress() {
    return Math.min(1.0, Math.max(0, this.stylePoints / this.styleThreshold));
  }
}
