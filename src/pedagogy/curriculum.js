// ============================================================================
// TYPEFIGHTER — 50-STAGE STORY CURRICULUM & WORLD ENGINE
// ============================================================================

class CurriculumManager {
  constructor() {
    this.rawCurriculum = null;
    this.passages = [];
    this.passagesEasy = [];
    this.isLoaded = false;

    this.worlds = [
      {
        id: 1,
        name: "World 1: The Sacred Dojo",
        themeName: "Home Row Mastery",
        keys: "ASDF JKL;",
        background: "assets/backgrounds/world1_dojo.jpg",
        music: "dojo",
        enemyTheme: "enemy_red"
      },
      {
        id: 2,
        name: "World 2: Neon Street Brawl",
        themeName: "Top Row Reaches",
        keys: "QWERT YUIOP",
        background: "assets/backgrounds/world2_street.jpg",
        music: "combat",
        enemyTheme: "enemy_red"
      },
      {
        id: 3,
        name: "World 3: Cyber Factory",
        themeName: "Bottom Row Defense",
        keys: "ZXCVB NM,./",
        background: "assets/backgrounds/world3_factory.jpg",
        music: "combat",
        enemyTheme: "enemy_tank"
      },
      {
        id: 4,
        name: "World 4: Skyscraper Rooftop",
        themeName: "Numbers & Shift Punctuation",
        keys: "1234567890 !@#$%",
        background: "assets/backgrounds/world4_rooftop.jpg",
        music: "combat",
        enemyTheme: "enemy_red"
      },
      {
        id: 5,
        name: "World 5: Grandmaster Apex Arena",
        themeName: "Flawless Combat Mastery",
        keys: "Full Keyboard Literary Mastery",
        background: "assets/backgrounds/world5_boss_arena.jpg",
        music: "boss",
        enemyTheme: "boss"
      }
    ];
  }

  async init() {
    try {
      const [curRes, passRes, passEasyRes] = await Promise.all([
        fetch('assets/data/curriculum_stages.json'),
        fetch('assets/data/passages.json'),
        fetch('assets/data/passages_easy.json')
      ]);

      this.rawCurriculum = await curRes.json();
      this.passages = await passRes.json();
      this.passagesEasy = await passEasyRes.json();
      this.isLoaded = true;
      console.log('[CurriculumManager] Curriculum loaded (50 stages, passages ready).');
    } catch (e) {
      console.warn('[CurriculumManager] Failed to load curriculum assets:', e);
    }
  }

  getStageData(worldNum, stageNumInWorld) {
    // 5 Worlds x 10 Stages = 50 total stages
    const globalStageId = (worldNum - 1) * 10 + stageNumInWorld;
    const isBoss = stageNumInWorld === 10;
    const world = this.worlds[worldNum - 1] || this.worlds[0];

    // Build stage-specific enemy waves and warm-up prompts
    let warmupKeys = [];
    let enemyWords = [];
    let bossConfig = null;

    if (worldNum === 1) {
      // Home row progression
      if (stageNumInWorld <= 3) {
        warmupKeys = ['f', 'j', 'd', 'k'];
        enemyWords = ['f', 'j', 'fj', 'jf', 'd', 'k', 'dk', 'kd', 'all', 'fall', 'ask', 'fad'];
      } else if (stageNumInWorld <= 6) {
        warmupKeys = ['s', 'l', 'a', ';'];
        enemyWords = ['as', 'sad', 'lad', 'lass', 'flask', 'falls', 'salad', 'dad', 'adds'];
      } else if (stageNumInWorld <= 9) {
        warmupKeys = ['a', 's', 'd', 'f', 'j', 'k', 'l', ';'];
        enemyWords = ['a sad lad', 'all lads fall', 'dad asks all', 'flask falls', 'add a salad'];
      } else {
        // Stage 10 Boss
        bossConfig = {
          name: "Stone Sentry Golem",
          title: "Guardian of the Home Row",
          hp: 400,
          sentences: [
            "all lads fall as a lad asks",
            "a sad lad asks all as a flask falls",
            "dad adds a salad as a lad falls",
            "alas a sad lass falls as dad asks"
          ]
        };
      }
    } else if (worldNum === 2) {
      // Top row progression
      if (stageNumInWorld <= 3) {
        warmupKeys = ['r', 'u', 'e', 'i'];
        enemyWords = ['red', 'run', 'fire', 'true', 'ride', 'free', 'wire', 'tire'];
      } else if (stageNumInWorld <= 6) {
        warmupKeys = ['w', 'o', 'q', 'p'];
        enemyWords = ['power', 'point', 'quick', 'proud', 'quiet', 'wrap', 'drop', 'trip'];
      } else if (stageNumInWorld <= 9) {
        warmupKeys = ['t', 'y', 'e', 'u', 'i', 'o', 'p'];
        enemyWords = ['strike fast', 'power attack', 'pure focus', 'swift punch', 'iron will'];
      } else {
        // Stage 20 Boss
        bossConfig = {
          name: "Shadow Blade Ronin",
          title: "Master of High Strikes",
          hp: 550,
          sentences: [
            "quick strikes pierce through the dark street",
            "speed without accuracy is fatal defeat",
            "focus your power into every single blow",
            "the true warrior never hesitates to strike"
          ]
        };
      }
    } else if (worldNum === 3) {
      // Bottom row progression
      if (stageNumInWorld <= 5) {
        warmupKeys = ['v', 'm', 'c', ','];
        enemyWords = ['combat', 'move', 'claim', 'climb', 'vivid', 'metal', 'valve', 'matrix'];
      } else if (stageNumInWorld <= 9) {
        warmupKeys = ['x', 'b', 'n', '.', '/'];
        enemyWords = ['boxer', 'break', 'block', 'brave', 'nexus', 'noble', 'blitz', 'parry'];
      } else {
        // Stage 30 Boss
        bossConfig = {
          name: "Cyber Mech Titan",
          title: "Heavy Armor Behemoth",
          hp: 750,
          sentences: [
            "heavy armor breaks under continuous blows",
            "rhythm and balance overcome raw brute force",
            "strike the weak joints with laser precision",
            "shatter the mechanical titan into scrap metal"
          ]
        };
      }
    } else if (worldNum === 4) {
      // Numbers & Shift symbols
      if (stageNumInWorld <= 5) {
        warmupKeys = ['1', '2', '3', '4', '5'];
        enemyWords = ['Strike #1', 'Combo 2x', 'Wave 3', 'Code 404', 'Level 5', 'Rank 100'];
      } else if (stageNumInWorld <= 9) {
        warmupKeys = ['!', '@', '#', '$', '%', '&'];
        enemyWords = ['Power!', 'Watch out!', 'Double strike!', 'Super combo!', 'Overdrive!'];
      } else {
        // Stage 40 Boss
        bossConfig = {
          name: "Apex Cyber Ninja",
          title: "Grand Infiltrator",
          hp: 950,
          sentences: [
            "Shift your balance! Speed reaches 100% capacity!",
            "Can you match the lightning rhythm of the storm?",
            "Every keystroke must land with absolute 100% accuracy!",
            "Break the barrier and ascend to the rooftop pinnacle!"
          ]
        };
      }
    } else {
      // World 5: Final Master Arena
      if (stageNumInWorld <= 9) {
        const samplePassage = this.passages[Math.floor(Math.random() * this.passages.length)];
        enemyWords = samplePassage ? samplePassage.text.split(' ').slice(0, 8) : ['master', 'champion', 'perfection', 'grandmaster'];
      } else {
        // Stage 50 Final Boss
        bossConfig = {
          name: "Grandmaster Sensei",
          title: "Supreme Typing Beat 'Em Up Deity",
          hp: 1400,
          sentences: [
            "You have traveled from the humble dojo to the apex summit.",
            "A true typist does not look at the keys; fingers find truth.",
            "Fluid as water, devastating as thunder, unbroken in spirit.",
            "Show me the culmination of thirty days of relentless practice!"
          ]
        };
      }
    }

    return {
      globalStageId,
      worldNum,
      stageNumInWorld,
      world,
      isBoss,
      warmupKeys,
      enemyWords: enemyWords.length > 0 ? enemyWords : ['strike', 'kick', 'punch', 'block'],
      bossConfig
    };
  }

  getRandomPassage(isEasy = false) {
    const list = isEasy ? this.passagesEasy : this.passages;
    if (!list || list.length === 0) {
      return {
        title: "The Art of Mastery",
        author: "Sensei",
        text: "True mastery of the keyboard is achieved not by haste, but by flawless precision and relaxed posture."
      };
    }
    return list[Math.floor(Math.random() * list.length)];
  }
}

window.curriculumManager = new CurriculumManager();
