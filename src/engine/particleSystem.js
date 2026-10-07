// ============================================================================
// TYPEFIGHTER — 60 FPS PARTICLE VFX & COMBAT JUICE ENGINE
// ============================================================================

class ParticleSystem {
  constructor() {
    this.particles = [];
    this.shockwaves = [];
  }

  update(dt) {
    // 1. Update Particles
    for (let i = this.particles.length - 1; i >= 0; i--) {
      const p = this.particles[i];
      p.x += p.vx * dt * 60;
      p.y += p.vy * dt * 60;
      if (p.gravity) p.vy += p.gravity * dt * 60;
      p.alpha -= p.decay * dt * 60;

      if (p.alpha <= 0) {
        this.particles.splice(i, 1);
      }
    }

    // 2. Update Shockwaves
    for (let i = this.shockwaves.length - 1; i >= 0; i--) {
      const sw = this.shockwaves[i];
      sw.radius += sw.growSpeed * dt * 60;
      sw.alpha = Math.max(0, 1 - (sw.radius / sw.maxRadius));

      if (sw.radius >= sw.maxRadius || sw.alpha <= 0) {
        this.shockwaves.splice(i, 1);
      }
    }
  }

  draw(ctx) {
    ctx.save();

    // Draw Shockwaves
    for (const sw of this.shockwaves) {
      ctx.save();
      ctx.globalAlpha = sw.alpha;
      ctx.lineWidth = sw.lineWidth || 3;
      ctx.strokeStyle = sw.color;
      ctx.shadowColor = sw.color;
      ctx.shadowBlur = 15;
      ctx.beginPath();
      ctx.arc(sw.x, sw.y, sw.radius, 0, Math.PI * 2);
      ctx.stroke();
      ctx.restore();
    }

    // Draw Particles
    for (const p of this.particles) {
      ctx.save();
      ctx.globalAlpha = p.alpha;
      ctx.fillStyle = p.color;
      ctx.shadowColor = p.color;
      ctx.shadowBlur = p.glow ? 12 : 0;

      ctx.beginPath();
      ctx.arc(p.x, p.y, Math.max(0.5, p.size), 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();
    }

    ctx.restore();
  }

  // --- SPAWNERS ---
  spawnHitSparks(x, y, colors = ['#00f0ff', '#ffffff', '#7df9ff'], count = 18, speedMult = 1.0) {
    for (let i = 0; i < count; i++) {
      const angle = Math.random() * Math.PI * 2;
      const spd = (3.5 + Math.random() * 8.5) * speedMult;
      this.particles.push({
        x,
        y,
        vx: Math.cos(angle) * spd,
        vy: Math.sin(angle) * spd,
        color: colors[Math.floor(Math.random() * colors.length)],
        size: 2.0 + Math.random() * 3.5,
        alpha: 1.0,
        decay: 0.025 + Math.random() * 0.035,
        gravity: 0.16,
        glow: true
      });
    }
  }

  spawnShockwave(x, y, color = '#00f0ff', maxRadius = 70, lineWidth = 4) {
    this.shockwaves.push({
      x,
      y,
      radius: 6,
      maxRadius,
      color,
      lineWidth,
      alpha: 1.0,
      growSpeed: maxRadius / 10
    });
  }

  spawnDust(x, y, count = 8) {
    for (let i = 0; i < count; i++) {
      const angle = Math.PI + (Math.random() - 0.5) * 1.2;
      const spd = 1.0 + Math.random() * 3.0;
      this.particles.push({
        x: x + (Math.random() - 0.5) * 20,
        y: y + (Math.random() - 0.5) * 5,
        vx: Math.cos(angle) * spd,
        vy: -0.5 - Math.random() * 1.5,
        color: 'rgba(180, 195, 220, 0.6)',
        size: 3 + Math.random() * 4,
        alpha: 0.7,
        decay: 0.03 + Math.random() * 0.02,
        gravity: -0.02,
        glow: false
      });
    }
  }

  spawnAuraEmber(x, y, streakLevel) {
    if (streakLevel === 1) {
      // Fire ember
      this.particles.push({
        x: x + (Math.random() - 0.5) * 35,
        y: y + Math.random() * 40 - 20,
        vx: (Math.random() - 0.5) * 1.5,
        vy: -2.5 - Math.random() * 3.0,
        color: Math.random() > 0.4 ? '#ff5500' : '#ffcc00',
        size: 2.5 + Math.random() * 3,
        alpha: 0.9,
        decay: 0.035,
        gravity: -0.05,
        glow: true
      });
    } else if (streakLevel === 2) {
      // Lightning spark
      this.particles.push({
        x: x + (Math.random() - 0.5) * 45,
        y: y + Math.random() * 50 - 25,
        vx: (Math.random() - 0.5) * 4.0,
        vy: (Math.random() - 0.5) * 4.0,
        color: Math.random() > 0.3 ? '#00f0ff' : '#ffffff',
        size: 1.5 + Math.random() * 2.5,
        alpha: 1.0,
        decay: 0.06,
        gravity: 0,
        glow: true
      });
    } else if (streakLevel >= 3) {
      // Golden Overdrive sparkles
      this.particles.push({
        x: x + (Math.random() - 0.5) * 55,
        y: y + Math.random() * 60 - 30,
        vx: (Math.random() - 0.5) * 2.5,
        vy: -3.0 - Math.random() * 4.0,
        color: Math.random() > 0.3 ? '#ffd700' : '#ffffff',
        size: 3.0 + Math.random() * 3.5,
        alpha: 1.0,
        decay: 0.028,
        gravity: -0.06,
        glow: true
      });
    }
  }

  spawnCritBurst(x, y) {
    this.spawnShockwave(x, y, '#ffd700', 120, 6);
    this.spawnShockwave(x, y, '#ff0055', 90, 4);
    this.spawnHitSparks(x, y, ['#ffd700', '#ff0055', '#00f0ff', '#ffffff'], 45, 1.6);
  }
}

window.particleSystem = new ParticleSystem();
