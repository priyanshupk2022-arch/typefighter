// ============================================================================
// TYPEFIGHTER — LOW LATENCY WEB AUDIO ENGINE
// ============================================================================

class AudioManager {
  constructor() {
    this.ctx = null;
    this.buffers = new Map();
    this.currentMusicNode = null;
    this.currentMusicGain = null;
    this.currentTrackName = null;
    this.musicFilterNode = null;

    // Master volume levels
    this.masterVolume = 1.0;
    this.sfxVolume = 0.85;
    this.musicVolume = 0.65;
    this.keyClickVolume = 0.75;
    this.isMuted = false;

    // Sound pools
    this.thockFiles = [
      'assets/audio/sfx/keys/thock_01.ogg',
      'assets/audio/sfx/keys/thock_02.ogg',
      'assets/audio/sfx/keys/thock_03.ogg',
      'assets/audio/sfx/keys/thock_04.ogg',
      'assets/audio/sfx/keys/thock_05.ogg'
    ];

    this.punchLightFiles = [
      'assets/audio/sfx/combat/hit_punch_light_01.ogg',
      'assets/audio/sfx/combat/hit_punch_light_02.ogg'
    ];

    this.punchHeavyFiles = [
      'assets/audio/sfx/combat/hit_punch_heavy_01.ogg',
      'assets/audio/sfx/combat/hit_punch_heavy_02.ogg',
      'assets/audio/sfx/combat/hit_punch_heavy_03.ogg'
    ];

    this.kickFiles = [
      'assets/audio/sfx/combat/hit_kick_01.ogg',
      'assets/audio/sfx/combat/hit_kick_heavy_01.ogg'
    ];

    this.musicTracks = {
      menu: 'assets/audio/music/music_main_menu.ogg',
      dojo: 'assets/audio/music/music_calm_dojo_focus.ogg',
      combat: 'assets/audio/music/music_street_combat.ogg',
      boss: 'assets/audio/music/music_boss_battle.ogg',
      heavyBoss: 'assets/audio/music/music_boss_heavy.ogg',
      zen: 'assets/audio/music/music_zen_wisdom.ogg'
    };
  }

  init() {
    if (!this.ctx) {
      const AudioContextClass = window.AudioContext || window.webkitAudioContext;
      if (AudioContextClass) {
        this.ctx = new AudioContextClass();
      }
    }
    if (this.ctx && this.ctx.state === 'suspended') {
      this.ctx.resume();
    }
    this.preloadKeyBuffers();
  }

  async loadBuffer(url) {
    if (this.buffers.has(url)) return this.buffers.get(url);
    if (!this.ctx) return null;

    try {
      const res = await fetch(url);
      const arrayBuffer = await res.arrayBuffer();
      const audioBuffer = await this.ctx.decodeAudioData(arrayBuffer);
      this.buffers.set(url, audioBuffer);
      return audioBuffer;
    } catch (err) {
      console.warn(`[AudioManager] Failed to load ${url}:`, err);
      return null;
    }
  }

  async preloadKeyBuffers() {
    const list = [
      ...this.thockFiles,
      'assets/audio/sfx/keys/spacebar_down.ogg',
      'assets/audio/sfx/keys/error_buzz_soft.ogg',
      'assets/audio/sfx/keys/key_enter_slam.ogg',
      ...this.punchLightFiles,
      ...this.punchHeavyFiles,
      ...this.kickFiles,
      'assets/audio/sfx/combat/combat_knockdown_01.ogg',
      'assets/audio/sfx/combat/impact_crit_01.ogg',
      'assets/audio/sfx/combat/combat_parry_01.ogg',
      'assets/audio/sfx/feedback/streak_flame_ignite.ogg',
      'assets/audio/sfx/feedback/streak_power_surge.ogg',
      'assets/audio/sfx/feedback/streak_hyper_boost.ogg',
      'assets/audio/sfx/feedback/accuracy_100_fanfare.ogg',
      'assets/audio/sfx/feedback/rank_up_fanfare.ogg',
      'assets/audio/sfx/feedback/level_up_jingle.ogg'
    ];

    for (const url of list) {
      this.loadBuffer(url); // fire in parallel background
    }
  }

  playBuffer(buffer, volume = 1.0, pitch = 1.0) {
    if (!this.ctx || !buffer || this.isMuted) return;

    try {
      const source = this.ctx.createBufferSource();
      const gain = this.ctx.createGain();

      source.buffer = buffer;
      source.playbackRate.value = pitch;
      gain.gain.value = volume * this.masterVolume;

      source.connect(gain);
      gain.connect(this.ctx.destination);
      source.start(0);
    } catch (e) {
      console.warn('[AudioManager] playBuffer error', e);
    }
  }

  // --- MECHANICAL KEYBOARD CLICKS ---
  playKeyClick(isSpace = false, isEnter = false) {
    this.init();
    if (this.isMuted) return;

    let url;
    if (isSpace) {
      url = 'assets/audio/sfx/keys/spacebar_down.ogg';
    } else if (isEnter) {
      url = 'assets/audio/sfx/keys/key_enter_slam.ogg';
    } else {
      url = this.thockFiles[Math.floor(Math.random() * this.thockFiles.length)];
    }

    const buf = this.buffers.get(url);
    const pitch = 0.94 + Math.random() * 0.12; // subtle tactile pitch randomized
    const vol = this.keyClickVolume * (isEnter ? 1.0 : 0.85);

    if (buf) {
      this.playBuffer(buf, vol, pitch);
    } else {
      // Procedural fallback
      this.synthKeyClick(pitch, vol);
      this.loadBuffer(url);
    }
  }

  playKeyError() {
    this.init();
    if (this.isMuted) return;
    const url = 'assets/audio/sfx/keys/error_buzz_soft.ogg';
    const buf = this.buffers.get(url);
    if (buf) {
      this.playBuffer(buf, this.sfxVolume * 0.8, 1.0);
    } else {
      this.synthErrorBuzzer();
      this.loadBuffer(url);
    }
  }

  // --- COMBAT IMPACT SFX ---
  playPunchLight() {
    this.init();
    const url = this.punchLightFiles[Math.floor(Math.random() * this.punchLightFiles.length)];
    const buf = this.buffers.get(url);
    const pitch = 0.96 + Math.random() * 0.08;
    if (buf) {
      this.playBuffer(buf, this.sfxVolume * 0.75, pitch);
    } else {
      this.synthPunch(0.8);
      this.loadBuffer(url);
    }
  }

  playPunchHeavy() {
    this.init();
    const url = this.punchHeavyFiles[Math.floor(Math.random() * this.punchHeavyFiles.length)];
    const buf = this.buffers.get(url);
    const pitch = 0.92 + Math.random() * 0.1;
    if (buf) {
      this.playBuffer(buf, this.sfxVolume * 0.95, pitch);
    } else {
      this.synthPunch(1.3);
      this.loadBuffer(url);
    }
  }

  playKick() {
    this.init();
    const url = this.kickFiles[Math.floor(Math.random() * this.kickFiles.length)];
    const buf = this.buffers.get(url);
    const pitch = 0.94 + Math.random() * 0.1;
    if (buf) {
      this.playBuffer(buf, this.sfxVolume * 0.9, pitch);
    } else {
      this.synthPunch(1.1);
      this.loadBuffer(url);
    }
  }

  playKnockdown() {
    this.init();
    const url = 'assets/audio/sfx/combat/combat_knockdown_01.ogg';
    const buf = this.buffers.get(url);
    if (buf) {
      this.playBuffer(buf, this.sfxVolume * 1.0, 0.95);
    } else {
      this.synthSlam();
      this.loadBuffer(url);
    }
  }

  playCrit() {
    this.init();
    const url = 'assets/audio/sfx/combat/impact_crit_01.ogg';
    const buf = this.buffers.get(url);
    if (buf) {
      this.playBuffer(buf, this.sfxVolume * 1.05, 1.0);
    }
  }

  // --- STREAKS & FANFARES ---
  playStreakSound(level) {
    this.init();
    let url;
    if (level === 15) url = 'assets/audio/sfx/feedback/streak_flame_ignite.ogg';
    else if (level === 30) url = 'assets/audio/sfx/feedback/streak_power_surge.ogg';
    else if (level >= 50) url = 'assets/audio/sfx/feedback/streak_hyper_boost.ogg';

    if (url) {
      const buf = this.buffers.get(url);
      if (buf) this.playBuffer(buf, this.sfxVolume * 1.0, 1.0);
      else this.loadBuffer(url);
    }
  }

  playRankUp() {
    this.init();
    const url = 'assets/audio/sfx/feedback/rank_up_fanfare.ogg';
    const buf = this.buffers.get(url);
    if (buf) this.playBuffer(buf, this.sfxVolume * 0.9, 1.0);
    else this.loadBuffer(url);
  }

  playAccuracyFanfare() {
    this.init();
    const url = 'assets/audio/sfx/feedback/accuracy_100_fanfare.ogg';
    const buf = this.buffers.get(url);
    if (buf) this.playBuffer(buf, this.sfxVolume * 1.0, 1.0);
    else this.loadBuffer(url);
  }

  playLevelComplete() {
    this.init();
    const url = 'assets/audio/sfx/feedback/level_up_jingle.ogg';
    const buf = this.buffers.get(url);
    if (buf) this.playBuffer(buf, this.sfxVolume * 1.0, 1.0);
    else this.loadBuffer(url);
  }

  // --- DYNAMIC MUSIC CONTROLLER ---
  async playMusic(trackKey) {
    this.init();
    if (!this.ctx || this.currentTrackName === trackKey) return;

    const url = this.musicTracks[trackKey];
    if (!url) return;

    const oldNode = this.currentMusicNode;
    const oldGain = this.currentMusicGain;

    // Cross-fade out old track
    if (oldGain) {
      try {
        oldGain.gain.setValueAtTime(oldGain.gain.value, this.ctx.currentTime);
        oldGain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.8);
        setTimeout(() => {
          try { oldNode.stop(); oldNode.disconnect(); } catch (e) {}
        }, 900);
      } catch (e) {}
    }

    this.currentTrackName = trackKey;
    const buf = await this.loadBuffer(url);
    if (!buf || this.currentTrackName !== trackKey) return;

    const source = this.ctx.createBufferSource();
    source.buffer = buf;
    source.loop = true;

    // Create dynamic lowpass filter for style rank intensity
    const filter = this.ctx.createBiquadFilter();
    filter.type = 'lowpass';
    filter.frequency.setValueAtTime(20000, this.ctx.currentTime);
    this.musicFilterNode = filter;

    const gain = this.ctx.createGain();
    gain.gain.setValueAtTime(0.001, this.ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(
      Math.max(0.01, this.musicVolume * this.masterVolume),
      this.ctx.currentTime + 1.2
    );

    source.connect(filter);
    filter.connect(gain);
    gain.connect(this.ctx.destination);

    source.start(0);
    this.currentMusicNode = source;
    this.currentMusicGain = gain;
  }

  // Scale music intensity with Devil May Cry rank (rankIndex 0 to 6)
  setStyleRankIntensity(rankIndex) {
    if (!this.ctx || !this.currentMusicNode) return;
    try {
      // High ranks slightly boost tempo/pitch and volume
      const speed = 1.0 + rankIndex * 0.018; // D=1.0x -> SSS=~1.11x
      this.currentMusicNode.playbackRate.setTargetAtTime(speed, this.ctx.currentTime, 0.4);

      if (this.currentMusicGain) {
        const boost = 1.0 + rankIndex * 0.04;
        const targetVol = this.musicVolume * this.masterVolume * boost;
        this.currentMusicGain.gain.setTargetAtTime(targetVol, this.ctx.currentTime, 0.3);
      }
    } catch (e) {}
  }

  // --- PROCEDURAL SYNTHESIS FALLBACKS ---
  synthKeyClick(pitch = 1.0, vol = 0.5) {
    if (!this.ctx) return;
    try {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(240 * pitch, this.ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(80, this.ctx.currentTime + 0.04);

      gain.gain.setValueAtTime(vol * 0.3 * this.masterVolume, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.045);

      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start();
      osc.stop(this.ctx.currentTime + 0.05);
    } catch (e) {}
  }

  synthErrorBuzzer() {
    if (!this.ctx) return;
    try {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(140, this.ctx.currentTime);
      gain.gain.setValueAtTime(0.25 * this.masterVolume, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.12);

      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start();
      osc.stop(this.ctx.currentTime + 0.13);
    } catch (e) {}
  }

  synthPunch(power = 1.0) {
    if (!this.ctx) return;
    try {
      const bufferSize = Math.floor(this.ctx.sampleRate * 0.07);
      const buffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
      const data = buffer.getChannelData(0);
      for (let i = 0; i < bufferSize; i++) {
        data[i] = (Math.random() * 2 - 1) * Math.exp(-i / (bufferSize * 0.2));
      }
      const noise = this.ctx.createBufferSource();
      noise.buffer = buffer;

      const filter = this.ctx.createBiquadFilter();
      filter.type = 'bandpass';
      filter.frequency.setValueAtTime(400 * power, this.ctx.currentTime);

      const gain = this.ctx.createGain();
      gain.gain.setValueAtTime(0.35 * power * this.masterVolume, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.12);

      noise.connect(filter);
      filter.connect(gain);
      gain.connect(this.ctx.destination);
      noise.start();
    } catch (e) {}
  }

  synthSlam() {
    if (!this.ctx) return;
    try {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(120, this.ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(25, this.ctx.currentTime + 0.35);

      gain.gain.setValueAtTime(0.5 * this.masterVolume, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.35);

      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start();
      osc.stop(this.ctx.currentTime + 0.36);
    } catch (e) {}
  }
}

// Export singleton
window.audioManager = new AudioManager();
