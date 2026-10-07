// ============================================================================
// TYPEFIGHTER — ADAPTIVE WEAK-KEY TRACKER & DRILL GENERATOR
// ============================================================================

class AdaptiveTracker {
  constructor() {
    this.storageKey = 'typefighter_key_stats';
    this.keyStats = this.loadStats();
    this.ngramsData = null;
    this.words10k = [];
  }

  async init() {
    try {
      const [ngRes, wordsRes] = await Promise.all([
        fetch('assets/data/ngrams.json'),
        fetch('assets/data/words_common_1k.txt')
      ]);
      this.ngramsData = await ngRes.json();
      const text = await wordsRes.text();
      this.words10k = text.split('\n').map(w => w.trim().toLowerCase()).filter(w => w.length > 0);
    } catch (e) {
      console.warn('[AdaptiveTracker] Failed to load ngrams or words list:', e);
    }
  }

  loadStats() {
    try {
      const data = localStorage.getItem(this.storageKey);
      return data ? JSON.parse(data) : {};
    } catch (e) {
      return {};
    }
  }

  saveStats() {
    try {
      localStorage.setItem(this.storageKey, JSON.stringify(this.keyStats));
    } catch (e) {}
  }

  recordKey(char, isCorrect) {
    if (!char || char.length !== 1) return;
    const c = char.toLowerCase();
    if (!this.keyStats[c]) {
      this.keyStats[c] = { correct: 0, error: 0, accuracy: 100 };
    }

    if (isCorrect) {
      this.keyStats[c].correct++;
    } else {
      this.keyStats[c].error++;
    }

    const total = this.keyStats[c].correct + this.keyStats[c].error;
    this.keyStats[c].accuracy = total > 0
      ? Math.round((this.keyStats[c].correct / total) * 100)
      : 100;

    this.saveStats();
  }

  getWeakKeys(threshold = 85, minAttempts = 5) {
    const weak = [];
    for (const [key, stat] of Object.entries(this.keyStats)) {
      const total = stat.correct + stat.error;
      if (total >= minAttempts && stat.accuracy < threshold) {
        weak.push({ key, accuracy: stat.accuracy, total });
      }
    }
    return weak.sort((a, b) => a.accuracy - b.accuracy);
  }

  generateReinforcementDrill(count = 6) {
    const weak = this.getWeakKeys();
    if (weak.length === 0 || this.words10k.length === 0) {
      // Default fallback
      return ['focus', 'strike', 'practice', 'accuracy', 'mastery'];
    }

    const targetKeyChars = new Set(weak.map(w => w.key));
    const matchingWords = this.words10k.filter(word => {
      for (const char of word) {
        if (targetKeyChars.has(char)) return true;
      }
      return false;
    });

    // Shuffle and pick
    const shuffled = matchingWords.sort(() => 0.5 - Math.random());
    return shuffled.slice(0, count);
  }
}

window.adaptiveTracker = new AdaptiveTracker();
