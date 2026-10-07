// ============================================================================
// TYPEFIGHTER — 60 FPS 2D STICKMAN COMBAT & BEAT 'EM UP ENGINE
// ============================================================================

class CombatEngine {
  constructor() {
    this.canvas = null;
    this.ctx = null;
    this.isActive = false;

    // Background
    this.bgImage = null;
    this.bgLoaded = false;

    // World & Dimensions
    this.worldWidth = 1440;
    this.worldHeight = 900;
    this.groundY = 660;

    // Camera & Juice
    this.cameraX = 0;
    this.screenShake = 0;
    this.hitStopFrames = 0;

    // Entities
    this.hero = null;
    this.enemies = [];
    this.activeEnemy = null; // currently targeted enemy

    // Attack animation cycles
    this.strikeCycle = ['punch_jab', 'punch_straight', 'roundhouse_kick'];
    this.strikeIndex = 0;
    this.finisherMoves = ['uppercut', 'air_juggle', 'ground_slam'];
    this.finisherIndex = 0;

    // Callbacks
    this.onEnemyDefeated = null;
    this.onHeroHit = null;
    this.onWaveClear = null;
    this.onGameOver = null;
  }

  init(canvas) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.resize();
    window.addEventListener('resize', () => this.resize());
    this.resetHero();
  }

  resize() {
    if (!this.canvas) return;
    const dpr = window.devicePixelRatio || 1;
    this.canvas.width = window.innerWidth * dpr;
    this.canvas.height = window.innerHeight * dpr;
    this.ctx.resetTransform();
    this.ctx.scale(dpr, dpr);
    this.worldWidth = window.innerWidth;
    this.worldHeight = window.innerHeight;
    this.groundY = Math.round(window.innerHeight * 0.70);
    if (this.hero) this.hero.groundY = this.groundY;
  }

  loadBackground(imagePath) {
    this.bgLoaded = false;
    this.bgImage = new Image();
    this.bgImage.onload = () => {
      this.bgLoaded = true;
    };
    this.bgImage.src = imagePath;
  }

  resetHero() {
    this.hero = {
      x: 320,
      y: 0,
      groundY: this.groundY,
      facing: 1, // 1 = right
      scale: 1.7,
      hp: 100,
      maxHp: 100,
      currentAnim: 'idle',
      animProgress: 0,
      comboQueue: [],
      theme: (window.stickmanRig && window.stickmanRig.rigData) ? window.stickmanRig.rigData.themes.hero : {
        primary: '#00f0ff', secondary: '#0088ff', glow: 'rgba(0, 240, 255, 0.8)', glowSize: 20
      },
      trails: []
    };
  }

  spawnEnemy(archetype, word, targetX = null) {
    const isBoss = archetype === 'boss';
    const isTank = archetype === 'tank';
    const isNinja = archetype === 'ninja';

    const enemy = {
      id: Math.random().toString(36).substr(2, 9),
      archetype,
      word,
      x: targetX !== null ? targetX : (this.worldWidth + 120 + Math.random() * 200),
      y: 0,
      groundY: this.groundY,
      facing: -1, // facing player (left)
      scale: isBoss ? 2.3 : (isTank ? 2.0 : (isNinja ? 1.5 : 1.65)),
      hp: isBoss ? 400 : (isTank ? 3 : 1),
      maxHp: isBoss ? 400 : (isTank ? 3 : 1),
      speed: isBoss ? 40 : (isNinja ? 110 : (isTank ? 35 : 65)),
      attackDistance: isBoss ? 220 : 170,
      attackTimer: 0,
      attackInterval: isBoss ? 3.5 : (isNinja ? 2.8 : 4.0),
      currentAnim: 'idle',
      animProgress: Math.random() * 20,
      state: 'approaching', // 'approaching', 'striking', 'hit', 'knockback', 'defeated'
      vx: 0,
      vy: 0,
      theme: (window.stickmanRig && window.stickmanRig.rigData) ? 
        (isBoss ? window.stickmanRig.rigData.themes.boss : 
         (isTank ? window.stickmanRig.rigData.themes.enemy_tank : window.stickmanRig.rigData.themes.enemy_red)) : {
        primary: '#ff2244', secondary: '#ff5500', glow: 'rgba(255, 34, 68, 0.85)', glowSize: 18
      },
      trails: []
    };

    this.enemies.push(enemy);
    if (!this.activeEnemy) {
      this.setActiveEnemy(enemy);
    }
    return enemy;
  }

  setActiveEnemy(enemy) {
    this.activeEnemy = enemy;
    if (window.typingEngine && enemy) {
      window.typingEngine.setTarget(enemy.word);
      if (window.keyboardGuide) {
        window.keyboardGuide.setTargetKey(window.typingEngine.getCurrentTargetChar());
      }
      if (window.handGuide) {
        window.handGuide.setTargetFinger(window.typingEngine.getCurrentFinger());
      }
    }
  }

  // --- ACTIONS TRIGGERED BY TYPING ---
  triggerHeroStrike(isWordEnd) {
    if (!this.hero) return;

    if (isWordEnd) {
      // Powerful finisher
      const move = this.finisherMoves[this.finisherIndex % this.finisherMoves.length];
      this.finisherIndex++;
      this.playHeroAnimation(move);

      // Hit stop & screen shake
      this.hitStopFrames = 4;
      this.screenShake = 12;

      // Finish active enemy
      if (this.activeEnemy) {
        const hitX = this.activeEnemy.x;
        const hitY = this.groundY - 80;

        // Particle explosion
        if (window.particleSystem) {
          window.particleSystem.spawnCritBurst(hitX, hitY);
        }

        // Knockback enemy
        this.activeEnemy.state = 'knockback';
        this.activeEnemy.vx = 450 + Math.random() * 200;
        this.activeEnemy.vy = -300 - Math.random() * 150;
        this.activeEnemy.currentAnim = 'knockdown';
        this.activeEnemy.animProgress = 0;

        if (this.onEnemyDefeated) {
          this.onEnemyDefeated(this.activeEnemy);
        }

        // Next enemy in line
        this.enemies = this.enemies.filter(e => e.id !== this.activeEnemy.id);
        const next = this.enemies.find(e => e.state !== 'knockback');
        this.setActiveEnemy(next || null);
      }
    } else {
      // Normal cycling strike
      const move = this.strikeCycle[this.strikeIndex % this.strikeCycle.length];
      this.strikeIndex++;
      this.playHeroAnimation(move);

      this.screenShake = 3;

      if (this.activeEnemy) {
        const hitX = this.activeEnemy.x - 30;
        const hitY = this.groundY - 60;
        if (window.particleSystem) {
          window.particleSystem.spawnHitSparks(hitX, hitY, ['#00f0ff', '#ffffff'], 12, 1.2);
        }
        this.activeEnemy.currentAnim = 'hit_reaction';
        this.activeEnemy.animProgress = 0;
      }
    }
  }

  triggerScreenClearSpecial() {
    this.screenShake = 24;
    this.hitStopFrames = 8;
    this.playHeroAnimation('ground_slam');

    if (window.particleSystem) {
      window.particleSystem.spawnShockwave(this.hero.x, this.groundY, '#ffd700', 350, 8);
      window.particleSystem.spawnCritBurst(this.hero.x + 100, this.groundY - 50);
    }

    if (window.audioManager) {
      window.audioManager.playCrit();
      window.audioManager.playKnockdown();
    }

    // Eliminate all visible enemies
    for (const e of this.enemies) {
      e.state = 'knockback';
      e.vx = 600 + Math.random() * 300;
      e.vy = -400 - Math.random() * 200;
      e.currentAnim = 'knockdown';
      e.animProgress = 0;
      if (this.onEnemyDefeated) {
        this.onEnemyDefeated(e);
      }
    }
    this.enemies = [];
    this.setActiveEnemy(null);
  }

  playHeroAnimation(animName) {
    if (!this.hero) return;
    this.hero.currentAnim = animName;
    this.hero.animProgress = 0;
  }

  // --- UPDATE LOOP ---
  update(dt) {
    if (!this.isActive) return;

    // Hit stop freeze
    if (this.hitStopFrames > 0) {
      this.hitStopFrames--;
      return;
    }

    // Screen shake damping
    if (this.screenShake > 0) {
      this.screenShake = Math.max(0, this.screenShake - 20 * dt);
    }

    // Update Hero
    if (this.hero) {
      const rig = window.stickmanRig;
      if (rig && rig.rigData) {
        const anim = rig.rigData.animations[this.hero.currentAnim];
        if (anim) {
          this.hero.animProgress += 60 * dt;
          if (this.hero.animProgress >= anim.durationFrames) {
            if (anim.loop) {
              this.hero.animProgress = this.hero.animProgress % anim.durationFrames;
            } else {
              this.hero.currentAnim = 'idle';
              this.hero.animProgress = 0;
            }
          }
        }
      }

      // Hero aura particles
      if (window.particleSystem && window.streakSystem) {
        const tier = window.streakSystem.currentTier;
        if (tier > 0) {
          window.particleSystem.spawnAuraEmber(this.hero.x, this.groundY - 60, tier);
        }
      }
    }

    // Update Enemies
    for (let i = this.enemies.length - 1; i >= 0; i--) {
      const e = this.enemies[i];

      if (e.state === 'approaching') {
        const dist = e.x - this.hero.x;
        if (dist > e.attackDistance) {
          e.x -= e.speed * dt;
        } else {
          // In attack range
          e.attackTimer += dt;
          if (e.attackTimer >= e.attackInterval) {
            e.attackTimer = 0;
            // Enemy attacks hero!
            this.enemyStrikeHero(e);
          }
        }
      } else if (e.state === 'knockback') {
        e.x += e.vx * dt;
        e.y += e.vy * dt;
        e.vy += 980 * dt; // gravity

        if (e.y >= 0) {
          e.y = 0;
          e.state = 'defeated';
        }
      }

      // Animation advancement for enemy
      const rig = window.stickmanRig;
      if (rig && rig.rigData) {
        const anim = rig.rigData.animations[e.currentAnim] || rig.rigData.animations.idle;
        if (anim) {
          e.animProgress += 60 * dt;
          if (e.animProgress >= anim.durationFrames) {
            if (anim.loop) {
              e.animProgress = e.animProgress % anim.durationFrames;
            } else {
              e.currentAnim = 'idle';
              e.animProgress = 0;
            }
          }
        }
      }

      // Remove defeated enemies that moved off screen
      if (e.x > this.worldWidth + 300 || e.state === 'defeated') {
        this.enemies.splice(i, 1);
        if (this.activeEnemy && this.activeEnemy.id === e.id) {
          const next = this.enemies.find(en => en.state !== 'knockback' && en.state !== 'defeated');
          this.setActiveEnemy(next || null);
        }
      }
    }

    // Check wave clear
    if (this.enemies.length === 0 && this.onWaveClear) {
      this.onWaveClear();
    }
  }

  enemyStrikeHero(enemy) {
    if (!this.hero) return;
    this.hero.hp = Math.max(0, this.hero.hp - 15);
    this.hero.currentAnim = 'hit_reaction';
    this.hero.animProgress = 0;

    this.screenShake = 15;
    if (window.particleSystem) {
      window.particleSystem.spawnHitSparks(this.hero.x, this.groundY - 70, ['#ff2244', '#ffffff'], 20, 1.5);
    }
    if (window.audioManager) {
      window.audioManager.playPunchHeavy();
    }
    if (window.styleRankManager) {
      window.styleRankManager.applyTypoPenalty();
    }
    if (window.streakSystem) {
      window.streakSystem.breakStreak();
    }

    if (this.onHeroHit) {
      this.onHeroHit(this.hero.hp);
    }

    if (this.hero.hp <= 0 && this.onGameOver) {
      this.hero.currentAnim = 'knockdown';
      this.isActive = false;
      this.onGameOver();
    }
  }

  // --- RENDER 60 FPS ---
  render() {
    if (!this.ctx) return;
    const ctx = this.ctx;
    const rig = window.stickmanRig;

    ctx.save();

    // Camera shake offset
    let shakeX = 0;
    let shakeY = 0;
    if (this.screenShake > 0) {
      shakeX = (Math.random() - 0.5) * this.screenShake;
      shakeY = (Math.random() - 0.5) * this.screenShake;
    }
    ctx.translate(shakeX, shakeY);

    // 1. Draw Background
    if (this.bgLoaded && this.bgImage) {
      ctx.drawImage(this.bgImage, 0, 0, this.worldWidth, this.worldHeight);
      // Dark vignette overlay
      ctx.fillStyle = 'rgba(6, 10, 18, 0.45)';
      ctx.fillRect(0, 0, this.worldWidth, this.worldHeight);
    } else {
      // Gradient background fallback
      const grad = ctx.createLinearGradient(0, 0, 0, this.worldHeight);
      grad.addColorStop(0, '#0a0e1a');
      grad.addColorStop(1, '#151d30');
      ctx.fillStyle = grad;
      ctx.fillRect(0, 0, this.worldWidth, this.worldHeight);
    }

    // 2. Arena Floor Line & Reflection Shadow
    ctx.strokeStyle = 'rgba(0, 240, 255, 0.2)';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(0, this.groundY + 2);
    ctx.lineTo(this.worldWidth, this.groundY + 2);
    ctx.stroke();

    // 3. Draw Hero
    if (this.hero && rig && rig.isLoaded) {
      const pose = rig.sampleAnimation(this.hero.currentAnim, this.hero.animProgress);
      if (pose) {
        const skel = rig.solveSkeleton(pose, this.hero.x, this.groundY, this.hero.scale, this.hero.facing);
        if (skel) {
          const streakTier = window.streakSystem ? window.streakSystem.currentTier : 0;
          rig.drawStickman(ctx, skel, this.hero.theme, 1.0, false, streakTier);
        }
      }
    }

    // 4. Draw Enemies
    for (const enemy of this.enemies) {
      if (rig && rig.isLoaded) {
        const pose = rig.sampleAnimation(enemy.currentAnim, enemy.animProgress);
        if (pose) {
          const skel = rig.solveSkeleton(pose, enemy.x, enemy.groundY + enemy.y, enemy.scale, enemy.facing);
          if (skel) {
            rig.drawStickman(ctx, skel, enemy.theme, 1.0, false, 0);
          }
        }
      }

      // Draw Floating Prompt above Active Enemy
      if (this.activeEnemy && this.activeEnemy.id === enemy.id && enemy.state === 'approaching') {
        this.drawEnemyPrompt(ctx, enemy);
      }
    }

    // 5. Draw Particle VFX
    if (window.particleSystem) {
      window.particleSystem.draw(ctx);
    }

    ctx.restore();
  }

  drawEnemyPrompt(ctx, enemy) {
    const text = enemy.word;
    const typing = window.typingEngine;
    const typedCount = typing ? typing.currentIndex : 0;

    const boxY = enemy.groundY - 140;
    const boxX = enemy.x;

    ctx.save();
    ctx.font = 'bold 24px "JetBrains Mono", monospace';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';

    const textWidth = ctx.measureText(text).width;
    const paddingX = 18;
    const paddingY = 8;

    // Background pill
    ctx.fillStyle = 'rgba(10, 14, 26, 0.9)';
    ctx.strokeStyle = 'rgba(0, 240, 255, 0.6)';
    ctx.lineWidth = 1.5;
    ctx.shadowColor = 'rgba(0, 240, 255, 0.4)';
    ctx.shadowBlur = 10;

    const pillX = boxX - textWidth / 2 - paddingX;
    const pillY = boxY - 16;
    const pillW = textWidth + paddingX * 2;
    const pillH = 32;

    ctx.beginPath();
    ctx.roundRect(pillX, pillY, pillW, pillH, 6);
    ctx.fill();
    ctx.stroke();

    // Render characters
    ctx.shadowBlur = 0;
    let startCharX = boxX - textWidth / 2;

    for (let i = 0; i < text.length; i++) {
      const char = text[i];
      const charWidth = ctx.measureText(char).width;

      if (i < typedCount) {
        ctx.fillStyle = '#00ff88'; // typed green
      } else if (i === typedCount) {
        ctx.fillStyle = '#00f0ff'; // active cyan
      } else {
        ctx.fillStyle = '#94a3b8'; // pending gray
      }

      ctx.fillText(char, startCharX + charWidth / 2, boxY);
      startCharX += charWidth;
    }

    ctx.restore();
  }
}

window.combatEngine = new CombatEngine();
