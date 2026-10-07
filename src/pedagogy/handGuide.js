// ============================================================================
// TYPEFIGHTER — DYNAMIC ANIMATED HAND GUIDE
// ============================================================================

class HandGuide {
  constructor() {
    this.container = null;
    this.svgElement = null;
    this.currentFingerId = null;

    this.fingerIdMapping = {
      'l-pinky': 'finger-left-pinky',
      'l-ring': 'finger-left-ring',
      'l-middle': 'finger-left-middle',
      'l-index': 'finger-left-index',
      'thumb': 'finger-left-thumb',
      'r-index': 'finger-right-index',
      'r-middle': 'finger-right-middle',
      'r-ring': 'finger-right-ring',
      'r-pinky': 'finger-right-pinky'
    };
  }

  async mount(containerElement) {
    this.container = containerElement;
    try {
      const res = await fetch('assets/ui/hands/hands_guide.svg');
      const svgText = await res.text();
      this.container.innerHTML = svgText;
      this.svgElement = this.container.querySelector('svg');
      if (this.svgElement) {
        this.svgElement.style.width = '100%';
        this.svgElement.style.height = '100%';
        this.injectPulseStyles();
      }
    } catch (err) {
      console.warn('[HandGuide] Failed to load hands_guide.svg:', err);
    }
  }

  injectPulseStyles() {
    const style = document.createElement('style');
    style.textContent = `
      .finger-group {
        transition: transform 0.15s cubic-bezier(0.175, 0.885, 0.32, 1.275), filter 0.15s;
        transform-origin: center;
      }
      .finger-group.active-pulse {
        filter: drop-shadow(0 0 12px #00f0ff) drop-shadow(0 0 24px #00f0ff);
        transform: translateY(-8px) scale(1.04);
      }
      .finger-group.active-pulse path {
        stroke: #ffffff !important;
        stroke-width: 3.5px !important;
      }
    `;
    if (this.svgElement) {
      this.svgElement.appendChild(style);
    }
  }

  setTargetFinger(fingerCode) {
    if (!this.svgElement) return;

    // Remove active pulse from old
    if (this.currentFingerId) {
      const oldEl = this.svgElement.getElementById(this.currentFingerId);
      if (oldEl) oldEl.classList.remove('active-pulse');
      if (this.currentFingerId === 'finger-left-thumb') {
        const rThumb = this.svgElement.getElementById('finger-right-thumb');
        if (rThumb) rThumb.classList.remove('active-pulse');
      }
    }

    if (!fingerCode) {
      this.currentFingerId = null;
      return;
    }

    const svgId = this.fingerIdMapping[fingerCode];
    if (svgId) {
      this.currentFingerId = svgId;
      const el = this.svgElement.getElementById(svgId);
      if (el) el.classList.add('active-pulse');
      if (svgId === 'finger-left-thumb') {
        const rThumb = this.svgElement.getElementById('finger-right-thumb');
        if (rThumb) rThumb.classList.add('active-pulse');
      }
    }
  }
}

window.handGuide = new HandGuide();
