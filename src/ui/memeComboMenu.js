// Keyboard Warrior Stickman - Authentic "Meme Combo Maker" & Arena Switcher Menu
export class MemeComboMenu {
  constructor(container, arenaManager, promptManager, audioSystem) {
    this.container = container;
    this.arena = arenaManager;
    this.prompt = promptManager;
    this.audio = audioSystem;
    this.isOpen = false;

    this.createDomElements();
    this.bindEvents();
  }

  createDomElements() {
    this.menuRoot = document.createElement('div');
    this.menuRoot.id = 'meme-combo-menu-wrapper';
    this.menuRoot.innerHTML = `
      <!-- Top Bar Toggle Button -->
      <button id="toggle-menu-btn" title="Open Meme Combo Maker (ESC)">
        <span class="icon">&#9881;</span> MEME COMBO MAKER
      </button>

      <!-- Full Menu Modal Overlay -->
      <div id="meme-menu-modal" class="hidden">
        <div class="modal-card">
          <div class="modal-header">
            <h2>MEME COMBO MAKER</h2>
            <button id="close-menu-btn" class="close-x">&times;</button>
          </div>

          <div class="modal-body">
            <!-- Section 1: Choose Arena -->
            <div class="menu-section">
              <label class="section-title">SELECT ARENA / STAGE</label>
              <div class="arena-grid">
                <button class="arena-btn active" data-arena="desk">
                  <div class="arena-thumb desk-thumb"></div>
                  <span>The Desk Room</span>
                </button>
                <button class="arena-btn" data-arena="crt">
                  <div class="arena-thumb crt-thumb"></div>
                  <span>Retro CRT PC</span>
                </button>
                <button class="arena-btn" data-arena="bliss">
                  <div class="arena-thumb bliss-thumb"></div>
                  <span>Windows XP Bliss</span>
                </button>
                <button class="arena-btn" data-arena="mxpain">
                  <div class="arena-thumb mxpain-thumb"></div>
                  <span>untitled - MXPain</span>
                </button>
                <button class="arena-btn gs-btn" data-arena="greenscreen">
                  <div class="arena-thumb gs-thumb"></div>
                  <span>Green Screen (Rec)</span>
                </button>
              </div>
            </div>

            <!-- Section 2: Custom Meme Phrase -->
            <div class="menu-section">
              <label class="section-title">CUSTOM PROMPT / MEME PHRASE</label>
              <div class="prompt-input-row">
                <input type="text" id="custom-phrase-input" placeholder="Enter your custom sentence or meme..." maxlength="60" value="THIS IS A TYPING GAME." />
                <button id="apply-phrase-btn">APPLY PHRASE</button>
              </div>

              <!-- Quick Preset Meme Phrases -->
              <div class="preset-phrases-list">
                <button class="phrase-tag" data-phrase="THIS IS A TYPING GAME.">Steam Demo</button>
                <button class="phrase-tag" data-phrase="I AM THE STORM THAT IS APPROACHING">Bury The Light</button>
                <button class="phrase-tag" data-phrase="STANDING HERE I REALIZE">Armstrong</button>
                <button class="phrase-tag" data-phrase="RULES OF NATURE">Metal Gear</button>
                <button class="phrase-tag" data-phrase="WHY DO I HEAR BOSS MUSIC">Boss Music</button>
                <button class="phrase-tag" data-phrase="YOU SHALL NOT PASS">Gandalf</button>
                <button class="phrase-tag" data-phrase="SKIBIDI TOILET IN OHIO">Brainrot</button>
              </div>
            </div>

            <!-- Section 3: Audio Settings -->
            <div class="menu-section">
              <label class="section-title">AUDIO & JUICE SETTINGS</label>
              <div class="slider-row">
                <span>Mechanical Keyboard SFX:</span>
                <input type="range" id="vol-sfx" min="0" max="100" value="80" />
              </div>
              <div class="slider-row">
                <span>Music Volume:</span>
                <input type="range" id="vol-music" min="0" max="100" value="50" />
              </div>
            </div>
          </div>

          <div class="modal-footer">
            <span class="tip-text">Tip: Press <b>ESC</b> anytime to resume combat</span>
            <button id="resume-game-btn" class="primary-btn">START FIGHTING</button>
          </div>
        </div>
      </div>
    `;

    this.container.appendChild(this.menuRoot);

    this.modal = document.getElementById('meme-menu-modal');
    this.customInput = document.getElementById('custom-phrase-input');
    this.arenaBtns = this.menuRoot.querySelectorAll('.arena-btn');
    this.phraseTags = this.menuRoot.querySelectorAll('.phrase-tag');
  }

  bindEvents() {
    // Open / Close toggles
    document.getElementById('toggle-menu-btn').addEventListener('click', () => this.toggle());
    document.getElementById('close-menu-btn').addEventListener('click', () => this.close());
    document.getElementById('resume-game-btn').addEventListener('click', () => this.close());

    // ESC key toggle
    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        this.toggle();
      }
    });

    // Arena switcher
    this.arenaBtns.forEach((btn) => {
      btn.addEventListener('click', () => {
        const arenaKey = btn.dataset.arena;
        this.arenaBtns.forEach((b) => b.classList.remove('active'));
        btn.classList.add('active');
        this.arena.switchArena(arenaKey);
      });
    });

    // Custom phrase application
    document.getElementById('apply-phrase-btn').addEventListener('click', () => {
      this.applyPhrase(this.customInput.value);
    });
    this.customInput.addEventListener('keydown', (e) => {
      e.stopPropagation(); // Don't trigger game inputs while typing custom phrase
      if (e.key === 'Enter') {
        this.applyPhrase(this.customInput.value);
      }
    });

    // Preset phrase tags
    this.phraseTags.forEach((tag) => {
      tag.addEventListener('click', () => {
        const phrase = tag.dataset.phrase;
        this.customInput.value = phrase;
        this.applyPhrase(phrase);
      });
    });

    // Audio Sliders
    document.getElementById('vol-sfx').addEventListener('input', (e) => {
      const val = e.target.value / 100;
      if (this.audio.sfxGain) this.audio.sfxGain.gain.value = val;
    });
    document.getElementById('vol-music').addEventListener('input', (e) => {
      const val = e.target.value / 100;
      if (this.audio.musicGain) this.audio.musicGain.gain.value = val;
    });
  }

  applyPhrase(text) {
    if (!text || text.trim() === '') return;
    this.prompt.setCustomPrompt(text);
    this.close();
  }

  toggle() {
    if (this.isOpen) {
      this.close();
    } else {
      this.open();
    }
  }

  open() {
    this.isOpen = true;
    this.modal.classList.remove('hidden');
    this.customInput.focus();
    this.customInput.select();
  }

  close() {
    this.isOpen = false;
    this.modal.classList.add('hidden');
  }
}
