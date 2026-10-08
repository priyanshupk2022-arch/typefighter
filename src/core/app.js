// Keyboard Warrior Stickman - Main Application Coordinator & Game Loop
import * as THREE from 'three';
import { audioSystem } from './audioSystem.js';
import { ArenaManager } from '../render/arenas/arenaManager.js';
import { PaperStandee } from '../render/stickman/paperStandee.js';
import { ComboEngine } from '../combat/comboEngine.js';
import { PromptManager } from '../combat/promptManager.js';
import { RetroHud } from '../ui/retroHud.js';
import { MemeComboMenu } from '../ui/memeComboMenu.js';
import { InputManager } from './inputManager.js';

export class App {
  constructor() {
    this.container = document.getElementById('game-container');
    this.clock = new THREE.Clock();

    // 1. Audio System
    this.audio = audioSystem;

    // 2. 3D Arena & Perspective Renderer
    this.arena = new ArenaManager(this.container);

    // 3. 3D Cutout Paper Standees
    this.hero = new PaperStandee(true, this.arena.scene);
    this.enemy = new PaperStandee(false, this.arena.scene);

    // 4. Combat & Style Rank Engine
    this.combo = new ComboEngine(this.audio, this.arena);

    // 5. Floating Prompt Engine
    this.prompt = new PromptManager(() => {
      // Callback on sentence complete
      this.combo.addStylePoints(60);
      this.audio.playSpecialKey('enter');
      this.arena.triggerScreenShake(0.4);
    });

    // 6. Retro Steam HUD
    this.hud = new RetroHud(this.container);
    this.hud.updatePrompt(this.prompt);

    // 7. Meme Combo Maker Menu
    this.menu = new MemeComboMenu(this.container, this.arena, this.prompt, this.audio);

    // 8. Low-Latency Keyboard Input Controller
    this.input = new InputManager(
      this.prompt,
      this.combo,
      this.audio,
      this.hud,
      this.menu,
      this.hero,
      this.enemy
    );

    // Start background music on first user interaction
    const startAudioOnce = () => {
      this.audio.init();
      this.audio.playMusic('assets/audio/music/music_street_combat.ogg');
      window.removeEventListener('keydown', startAudioOnce);
      window.removeEventListener('click', startAudioOnce);
    };
    window.addEventListener('keydown', startAudioOnce, { once: true });
    window.addEventListener('click', startAudioOnce, { once: true });

    // Enemy auto-recovery & behavior loop
    this.enemyRespawnTimer = 0;

    // Launch 60 FPS Render Loop
    this.animate = this.animate.bind(this);
    requestAnimationFrame(this.animate);
  }

  animate() {
    requestAnimationFrame(this.animate);
    const delta = Math.min(this.clock.getDelta(), 0.1); // Clamp to prevent delta spikes

    // Update input (continuous horizontal walk)
    this.input.update(delta);

    // Update combat & prompt timers
    this.combo.update(delta);
    this.prompt.update(delta);

    // Update paper cutout standees
    this.hero.update(delta);
    this.enemy.update(delta);

    // Enemy knockdown recovery
    if (this.enemy.health <= 0) {
      this.enemyRespawnTimer += delta;
      if (this.enemyRespawnTimer > 2.5) {
        this.enemy.health = 100;
        this.enemy.x = 1.8;
        this.enemy.setPose('idle');
        this.enemyRespawnTimer = 0;
      }
    }

    // Update 3D Camera shake & scene
    this.arena.update(delta);

    // Update UI HUD metrics
    this.hud.updateMetrics(this.prompt, this.combo);

    // Render WebGL frame
    this.arena.render();
  }
}

// Auto-boot on DOM ready
window.addEventListener('DOMContentLoaded', () => {
  window.gameApp = new App();
});
