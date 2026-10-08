// Keyboard Warrior Stickman - Floating Typing Prompt & Real-Time Red Cursor Engine
export class PromptManager {
  constructor(onSentenceComplete) {
    this.onSentenceComplete = onSentenceComplete;

    // Authentic library of Steam demo & Internet meme prompts
    this.defaultPrompts = [
      'THIS IS A TYPING GAME.',
      'MEME COMBO MAKER',
      'I AM THE STORM THAT IS APPROACHING',
      'STANDING HERE I REALIZE',
      'RULES OF NATURE',
      'WHY DO I HEAR BOSS MUSIC',
      'YOU SHALL NOT PASS',
      'KEYBOARD WARRIOR UNLEASHED',
      'MAXIMUM OVERDRIVE ACTIVATED',
      'SKIBIDI TOILET IN OHIO',
      'IT IS OVER NINE THOUSAND',
      'NEVER GONNA GIVE YOU UP',
      'UNLIMITED BLADE WORKS',
      'SHOW ME A GOOD TIME JACK'
    ];

    this.promptIndex = 0;
    this.currentText = this.defaultPrompts[0];
    this.charIndex = 0;

    // Performance metrics (matching Steam HUD: GOOD / MISS / % / TIME)
    this.goodCount = 0;
    this.missCount = 0;
    this.startTime = Date.now();
    this.elapsedSeconds = 0;
  }

  setCustomPrompt(text) {
    if (!text || text.trim() === '') return;
    this.currentText = text.trim().toUpperCase();
    this.charIndex = 0;
  }

  reset() {
    this.charIndex = 0;
    this.goodCount = 0;
    this.missCount = 0;
    this.startTime = Date.now();
    this.elapsedSeconds = 0;
  }

  getCurrentChar() {
    if (this.charIndex >= this.currentText.length) return null;
    return this.currentText[this.charIndex];
  }

  handleKeyPress(key) {
    const targetChar = this.getCurrentChar();
    if (!targetChar) return { status: 'completed' };

    const inputChar = key.toUpperCase();

    if (inputChar === targetChar) {
      // Correct keystroke!
      this.goodCount++;
      this.charIndex++;

      const isFinished = this.charIndex >= this.currentText.length;
      if (isFinished) {
        if (this.onSentenceComplete) this.onSentenceComplete();
        this.nextPrompt();
        return { status: 'sentence_complete', targetChar };
      }

      return { status: 'good', targetChar };
    } else {
      // Typo / Miss!
      this.missCount++;
      return { status: 'miss', expected: targetChar, actual: inputChar };
    }
  }

  nextPrompt() {
    this.promptIndex = (this.promptIndex + 1) % this.defaultPrompts.length;
    this.currentText = this.defaultPrompts[this.promptIndex];
    this.charIndex = 0;
  }

  getAccuracy() {
    const total = this.goodCount + this.missCount;
    if (total === 0) return 100;
    return Math.round((this.goodCount / total) * 100);
  }

  getElapsedFormatted() {
    const mins = Math.floor(this.elapsedSeconds / 60);
    const secs = Math.floor(this.elapsedSeconds % 60);
    return `${mins}:${secs.toString().padStart(2, '0')}`;
  }

  getWPM() {
    const minutes = Math.max(1 / 60, this.elapsedSeconds / 60);
    const words = this.goodCount / 5;
    return Math.round(words / minutes);
  }

  getProgress() {
    if (!this.currentText || this.currentText.length === 0) return 0;
    return this.charIndex / this.currentText.length;
  }

  update(delta) {
    this.elapsedSeconds = (Date.now() - this.startTime) / 1000;
  }
}
