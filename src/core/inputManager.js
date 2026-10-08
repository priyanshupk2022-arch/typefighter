// Keyboard Warrior Stickman - Low-Latency Input Manager & Special Keys Controller
export class InputManager {
  constructor(promptManager, comboEngine, audioSystem, retroHud, memeMenu, hero, enemy) {
    this.prompt = promptManager;
    this.combo = comboEngine;
    this.audio = audioSystem;
    this.hud = retroHud;
    this.menu = memeMenu;
    this.hero = hero;
    this.enemy = enemy;

    // Held key state for continuous movement
    this.keysHeld = {
      left: false,
      right: false
    };

    this.bindKeyboard();
  }

  setFighters(hero, enemy) {
    this.hero = hero;
    this.enemy = enemy;
  }

  bindKeyboard() {
    window.addEventListener('keydown', (e) => this.onKeyDown(e));
    window.addEventListener('keyup', (e) => this.onKeyUp(e));
  }

  onKeyDown(e) {
    // If the custom phrase menu modal is open, let user type into input freely
    if (this.menu && this.menu.isOpen) {
      return;
    }

    const key = e.key;

    // Movement key interception
    if (key === 'ArrowLeft' || key === 'a' || key === 'A') {
      this.keysHeld.left = true;
      return;
    }
    if (key === 'ArrowRight' || key === 'd' || key === 'D') {
      this.keysHeld.right = true;
      return;
    }

    // Special spectacle keys
    if (e.code === 'Tab') {
      e.preventDefault(); // Don't lose focus
      this.combo.triggerDash(this.hero, 1);
      return;
    }

    if (e.code === 'CapsLock') {
      e.preventDefault();
      this.combo.triggerRageMode();
      return;
    }

    if (e.code === 'Enter') {
      e.preventDefault();
      this.combo.triggerGroundSlam(this.hero, this.enemy);
      return;
    }

    if (e.code === 'Space') {
      e.preventDefault();
      const targetChar = this.prompt.getCurrentChar();
      if (targetChar === ' ') {
        // Space advances the prompt!
        this.audio.playKeyClack(false);
        const result = this.prompt.handleKeyPress(' ');
        this.combo.registerHit('heavy', this.hero, this.enemy);
        this.hud.updatePrompt(this.prompt);
      } else {
        // Space launches enemy into air!
        this.combo.triggerAirLauncher(this.hero, this.enemy);
      }
      return;
    }

    // Normal typing character handling (single printable character)
    if (key.length === 1 && !e.ctrlKey && !e.metaKey && !e.altKey) {
      e.preventDefault();
      const result = this.prompt.handleKeyPress(key);

      if (result.status === 'good' || result.status === 'sentence_complete') {
        this.audio.playKeyClack(false);
        const hitType = result.status === 'sentence_complete' ? 'crit' : 'light';
        this.combo.registerHit(hitType, this.hero, this.enemy);
        this.hud.updatePrompt(this.prompt);
      } else if (result.status === 'miss') {
        this.combo.registerMiss();
        this.hud.flashError();
      }
    }
  }

  onKeyUp(e) {
    const key = e.key;
    if (key === 'ArrowLeft' || key === 'a' || key === 'A') {
      this.keysHeld.left = false;
    }
    if (key === 'ArrowRight' || key === 'd' || key === 'D') {
      this.keysHeld.right = false;
    }
  }

  update(delta) {
    if (this.keysHeld.left) {
      this.combo.moveHero(this.hero, -1, delta);
    } else if (this.keysHeld.right) {
      this.combo.moveHero(this.hero, 1, delta);
    }
  }
}
