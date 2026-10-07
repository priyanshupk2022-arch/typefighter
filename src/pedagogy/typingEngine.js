// ============================================================================
// TYPEFIGHTER — STRICT STOP-ON-ERROR MOTOR LEARNING TYPING ENGINE
// ============================================================================

const FINGER_MAP = {
  '`': 'l-pinky', '~': 'l-pinky', '1': 'l-pinky', '!': 'l-pinky',
  'q': 'l-pinky', 'Q': 'l-pinky', 'a': 'l-pinky', 'A': 'l-pinky',
  'z': 'l-pinky', 'Z': 'l-pinky',
  '2': 'l-ring', '@': 'l-ring', 'w': 'l-ring', 'W': 'l-ring',
  's': 'l-ring', 'S': 'l-ring', 'x': 'l-ring', 'X': 'l-ring',
  '3': 'l-middle', '#': 'l-middle', 'e': 'l-middle', 'E': 'l-middle',
  'd': 'l-middle', 'D': 'l-middle', 'c': 'l-middle', 'C': 'l-middle',
  '4': 'l-index', '$': 'l-index', '5': 'l-index', '%': 'l-index',
  'r': 'l-index', 'R': 'l-index', 't': 'l-index', 'T': 'l-index',
  'f': 'l-index', 'F': 'l-index', 'g': 'l-index', 'G': 'l-index',
  'v': 'l-index', 'V': 'l-index', 'b': 'l-index', 'B': 'l-index',
  ' ': 'thumb',
  '6': 'r-index', '^': 'r-index', '7': 'r-index', '&': 'r-index',
  'y': 'r-index', 'Y': 'r-index', 'u': 'r-index', 'U': 'r-index',
  'h': 'r-index', 'H': 'r-index', 'j': 'r-index', 'J': 'r-index',
  'n': 'r-index', 'N': 'r-index', 'm': 'r-index', 'M': 'r-index',
  '8': 'r-middle', '*': 'r-middle', 'i': 'r-middle', 'I': 'r-middle',
  'k': 'r-middle', 'K': 'r-middle', ',': 'r-middle', '<': 'r-middle',
  '9': 'r-ring', '(': 'r-ring', 'o': 'r-ring', 'O': 'r-ring',
  'l': 'r-ring', 'L': 'r-ring', '.': 'r-ring', '>': 'r-ring',
  '0': 'r-pinky', ')': 'r-pinky', '-': 'r-pinky', '_': 'r-pinky',
  '=': 'r-pinky', '+': 'r-pinky', 'p': 'r-pinky', 'P': 'r-pinky',
  '[': 'r-pinky', '{': 'r-pinky', ']': 'r-pinky', '}': 'r-pinky',
  '\\': 'r-pinky', '|': 'r-pinky', ';': 'r-pinky', ':': 'r-pinky',
  "'": 'r-pinky', '"': 'r-pinky', '/': 'r-pinky', '?': 'r-pinky'
};

class TypingEngine {
  constructor() {
    this.targetText = '';
    this.currentIndex = 0;
    this.isActive = false;

    // Metrics
    this.totalKeystrokes = 0;
    this.correctKeystrokes = 0;
    this.errorKeystrokes = 0;
    this.currentStreak = 0;
    this.bestStreak = 0;
    this.startTime = null;
    this.lastKeyTimestamp = null;
    this.keyLatencyMap = new Map();
    this.errorMap = new Map();

    // Callbacks
    this.onCorrectChar = null; // (char, isWordEnd, isTargetComplete)
    this.onErrorChar = null;   // (expectedChar, typedChar)
    this.onMetricsUpdate = null; // (metricsObj)
  }

  setTarget(text) {
    this.targetText = text;
    this.currentIndex = 0;
    if (!this.startTime) {
      this.startTime = performance.now();
    }
  }

  resetMetrics() {
    this.totalKeystrokes = 0;
    this.correctKeystrokes = 0;
    this.errorKeystrokes = 0;
    this.currentStreak = 0;
    this.bestStreak = 0;
    this.startTime = null;
    this.lastKeyTimestamp = null;
    this.keyLatencyMap.clear();
    this.errorMap.clear();
  }

  getCurrentTargetChar() {
    if (this.currentIndex >= this.targetText.length) return null;
    return this.targetText[this.currentIndex];
  }

  getCurrentFinger() {
    const char = this.getCurrentTargetChar();
    if (!char) return null;
    return FINGER_MAP[char] || 'l-pinky';
  }

  processKey(typedKey) {
    if (!this.targetText || this.currentIndex >= this.targetText.length) {
      return { status: 'idle' };
    }

    if (!this.startTime) {
      this.startTime = performance.now();
    }

    const now = performance.now();
    if (this.lastKeyTimestamp) {
      const latency = now - this.lastKeyTimestamp;
      const expected = this.targetText[this.currentIndex];
      if (!this.keyLatencyMap.has(expected)) {
        this.keyLatencyMap.set(expected, []);
      }
      this.keyLatencyMap.get(expected).push(latency);
    }
    this.lastKeyTimestamp = now;

    this.totalKeystrokes++;
    const expectedChar = this.targetText[this.currentIndex];

    // Check match
    if (typedKey === expectedChar) {
      this.correctKeystrokes++;
      this.currentStreak++;
      if (this.currentStreak > this.bestStreak) {
        this.bestStreak = this.currentStreak;
      }

      this.currentIndex++;
      const isTargetComplete = this.currentIndex >= this.targetText.length;
      const isWordEnd = isTargetComplete || expectedChar === ' ' || this.targetText[this.currentIndex] === ' ';

      if (this.onCorrectChar) {
        this.onCorrectChar(expectedChar, isWordEnd, isTargetComplete);
      }
      this.emitMetrics();

      return {
        status: 'correct',
        char: expectedChar,
        isWordEnd,
        isComplete: isTargetComplete,
        streak: this.currentStreak
      };
    } else {
      // STRICT STOP-ON-ERROR: Do not advance index!
      this.errorKeystrokes++;
      this.currentStreak = 0;

      // Log error frequency
      const count = this.errorMap.get(expectedChar) || 0;
      this.errorMap.set(expectedChar, count + 1);

      if (this.onErrorChar) {
        this.onErrorChar(expectedChar, typedKey);
      }
      this.emitMetrics();

      return {
        status: 'error',
        expected: expectedChar,
        typed: typedKey,
        streak: 0
      };
    }
  }

  emitMetrics() {
    if (!this.onMetricsUpdate) return;
    const elapsedMinutes = this.startTime ? Math.max(0.01, (performance.now() - this.startTime) / 60000) : 0.01;
    const grossWpm = Math.round((this.totalKeystrokes / 5) / elapsedMinutes);
    const netWpm = Math.max(0, Math.round(((this.correctKeystrokes - this.errorKeystrokes) / 5) / elapsedMinutes));
    const accuracy = this.totalKeystrokes > 0
      ? Math.round((this.correctKeystrokes / this.totalKeystrokes) * 1000) / 10
      : 100.0;

    this.onMetricsUpdate({
      totalKeystrokes: this.totalKeystrokes,
      correctKeystrokes: this.correctKeystrokes,
      errorKeystrokes: this.errorKeystrokes,
      currentStreak: this.currentStreak,
      bestStreak: this.bestStreak,
      grossWpm,
      netWpm,
      accuracy,
      progressRatio: this.targetText.length > 0 ? this.currentIndex / this.targetText.length : 0
    });
  }

  getResults() {
    const elapsedMinutes = this.startTime ? Math.max(0.01, (performance.now() - this.startTime) / 60000) : 0.01;
    const grossWpm = Math.round((this.totalKeystrokes / 5) / elapsedMinutes);
    const netWpm = Math.max(0, Math.round(((this.correctKeystrokes - this.errorKeystrokes) / 5) / elapsedMinutes));
    const accuracy = this.totalKeystrokes > 0
      ? Math.round((this.correctKeystrokes / this.totalKeystrokes) * 1000) / 10
      : 100.0;

    return {
      totalKeystrokes: this.totalKeystrokes,
      correctKeystrokes: this.correctKeystrokes,
      errorKeystrokes: this.errorKeystrokes,
      bestStreak: this.bestStreak,
      grossWpm,
      netWpm,
      accuracy,
      durationSeconds: Math.round(elapsedMinutes * 60),
      errorMap: Object.fromEntries(this.errorMap)
    };
  }
}

window.typingEngine = new TypingEngine();
