// ============================================================================
// TYPEFIGHTER — INTERACTIVE QWERTY KEYBOARD GUIDE
// ============================================================================

class KeyboardGuide {
  constructor() {
    this.container = null;
    this.keyElements = new Map();
    this.activeTargetKey = null;

    this.rows = [
      [
        { key: '`', label: '~ `', finger: 'f-l-pinky' },
        { key: '1', label: '! 1', finger: 'f-l-pinky' },
        { key: '2', label: '@ 2', finger: 'f-l-ring' },
        { key: '3', label: '# 3', finger: 'f-l-middle' },
        { key: '4', label: '$ 4', finger: 'f-l-index' },
        { key: '5', label: '% 5', finger: 'f-l-index' },
        { key: '6', label: '^ 6', finger: 'f-r-index' },
        { key: '7', label: '& 7', finger: 'f-r-index' },
        { key: '8', label: '* 8', finger: 'f-r-middle' },
        { key: '9', label: '( 9', finger: 'f-r-ring' },
        { key: '0', label: ') 0', finger: 'f-r-pinky' },
        { key: '-', label: '_ -', finger: 'f-r-pinky' },
        { key: '=', label: '+ =', finger: 'f-r-pinky' },
        { key: 'Backspace', label: '⌫ BACK', class: 'kb-wide', finger: 'f-r-pinky' }
      ],
      [
        { key: 'Tab', label: 'TAB', class: 'kb-wide', finger: 'f-l-pinky' },
        { key: 'q', label: 'Q', finger: 'f-l-pinky' },
        { key: 'w', label: 'W', finger: 'f-l-ring' },
        { key: 'e', label: 'E', finger: 'f-l-middle' },
        { key: 'r', label: 'R', finger: 'f-l-index' },
        { key: 't', label: 'T', finger: 'f-l-index' },
        { key: 'y', label: 'Y', finger: 'f-r-index' },
        { key: 'u', label: 'U', finger: 'f-r-index' },
        { key: 'i', label: 'I', finger: 'f-r-middle' },
        { key: 'o', label: 'O', finger: 'f-r-ring' },
        { key: 'p', label: 'P', finger: 'f-r-pinky' },
        { key: '[', label: '{ [', finger: 'f-r-pinky' },
        { key: ']', label: '} ]', finger: 'f-r-pinky' },
        { key: '\\', label: '| \\', finger: 'f-r-pinky' }
      ],
      [
        { key: 'CapsLock', label: 'CAPS', class: 'kb-wide', finger: 'f-l-pinky' },
        { key: 'a', label: 'A', finger: 'f-l-pinky' },
        { key: 's', label: 'S', finger: 'f-l-ring' },
        { key: 'd', label: 'D', finger: 'f-l-middle' },
        { key: 'f', label: 'F', finger: 'f-l-index' },
        { key: 'g', label: 'G', finger: 'f-l-index' },
        { key: 'h', label: 'H', finger: 'f-r-index' },
        { key: 'j', label: 'J', finger: 'f-r-index' },
        { key: 'k', label: 'K', finger: 'f-r-middle' },
        { key: 'l', label: 'L', finger: 'f-r-ring' },
        { key: ';', label: ': ;', finger: 'f-r-pinky' },
        { key: "'", label: '" \'', finger: 'f-r-pinky' },
        { key: 'Enter', label: 'ENTER ↵', class: 'kb-wide', finger: 'f-r-pinky' }
      ],
      [
        { key: 'Shift', label: 'SHIFT ⇧', class: 'kb-extrawide', finger: 'f-l-pinky' },
        { key: 'z', label: 'Z', finger: 'f-l-pinky' },
        { key: 'x', label: 'X', finger: 'f-l-ring' },
        { key: 'c', label: 'C', finger: 'f-l-middle' },
        { key: 'v', label: 'V', finger: 'f-l-index' },
        { key: 'b', label: 'B', finger: 'f-l-index' },
        { key: 'n', label: 'N', finger: 'f-r-index' },
        { key: 'm', label: 'M', finger: 'f-r-index' },
        { key: ',', label: '< ,', finger: 'f-r-middle' },
        { key: '.', label: '> .', finger: 'f-r-ring' },
        { key: '/', label: '? /', finger: 'f-r-pinky' },
        { key: 'ShiftRight', label: 'SHIFT ⇧', class: 'kb-extrawide', finger: 'f-r-pinky' }
      ],
      [
        { key: 'Control', label: 'CTRL', finger: 'f-l-pinky' },
        { key: 'Alt', label: 'ALT', finger: 'f-thumb' },
        { key: ' ', label: 'SPACEBAR', class: 'kb-space', finger: 'f-thumb' },
        { key: 'AltGraph', label: 'ALT', finger: 'f-thumb' },
        { key: 'ControlRight', label: 'CTRL', finger: 'f-r-pinky' }
      ]
    ];
  }

  mount(containerElement) {
    this.container = containerElement;
    this.container.innerHTML = '';
    this.keyElements.clear();

    for (const row of this.rows) {
      const rowDiv = document.createElement('div');
      rowDiv.className = 'kb-row';

      for (const k of row) {
        const keyDiv = document.createElement('div');
        keyDiv.className = `kb-key ${k.class || ''} ${k.finger || ''}`;
        keyDiv.textContent = k.label;
        keyDiv.dataset.key = k.key.toLowerCase();

        this.keyElements.set(k.key.toLowerCase(), keyDiv);
        rowDiv.appendChild(keyDiv);
      }
      this.container.appendChild(rowDiv);
    }
  }

  setTargetKey(char) {
    if (this.activeTargetKey) {
      const oldEl = this.keyElements.get(this.activeTargetKey);
      if (oldEl) oldEl.classList.remove('target');
    }

    if (!char) {
      this.activeTargetKey = null;
      return;
    }

    const keyLookup = char.toLowerCase();
    this.activeTargetKey = keyLookup;
    const targetEl = this.keyElements.get(keyLookup);
    if (targetEl) {
      targetEl.classList.add('target');
    }
  }

  triggerKeyPress(key) {
    const el = this.keyElements.get(key.toLowerCase());
    if (el) {
      el.classList.add('pressed');
      setTimeout(() => el.classList.remove('pressed'), 80);
    }
  }
}

window.keyboardGuide = new KeyboardGuide();
