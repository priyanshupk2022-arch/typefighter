# TypeFighter Data Manifest & Corpus Documentation

**Asset Root**: `typefighter/assets/data/`  
**Generated On**: 2026-10-06  
**Pipeline Status**: Fully Validated (`_scripts/validate_data.py` - PASS)  

---

## 1. Summary of Deliverables

| File Name | File Type | Record Count | Size | Character / Word Constraints | Description |
|:---|:---:|:---:|:---:|:---|:---|
| [`words_10k.txt`](./words_10k.txt) | Plain Text | 10,000 words | ~85 KB | Letters `a-z`, 100% lowercase, profanity filtered | Frequency-ranked English word list from Google Web Corpus |
| [`words_common_1k.txt`](./words_common_1k.txt) | Plain Text | 1,000 words | ~7.2 KB | Letters `a-z`, 100% lowercase, top frequency | Top 1,000 everyday muscle-memory vocabulary words |
| [`passages.json`](./passages.json) | JSON | 370 passages | ~135 KB | 150–400 chars, normalized ASCII (codes 32–126) | Clean literary prose from Project Gutenberg classics |
| [`passages_easy.json`](./passages_easy.json) | JSON | 350 passages | ~112 KB | 150–400 chars, `a-z` + basic punctuation (`.,'`) | Simplified beginner prose without shift key requirements |
| [`ngrams.json`](./ngrams.json) | JSON | 400 n-grams (200 bigrams, 200 trigrams) | ~28 KB | Alphabetical n-grams with count and frequencies | Character n-grams extracted from the prose corpus |
| [`curriculum_stages.json`](./curriculum_stages.json) | JSON | 7 stages (30 daily lessons) | ~34 KB | Target keys, finger maps, drills, 98%+ threshold | Comprehensive 30-day typing combat curriculum |
| [`DATA_MANIFEST.md`](./DATA_MANIFEST.md) | Markdown | 1 document | ~8 KB | Markdown Documentation | Complete inventory, schema reference, and license manifest |

---

## 2. File Specifications & Schemas

### 2.1 `words_10k.txt` & `words_common_1k.txt`
- **Format**: Newline-delimited UTF-8 plain text (`\n`).
- **Curation Rules**:
  - Filtered against Google Profanity blocklists and LDNOOBW bad-words corpus.
  - Stripped of web noise (e.g. `http`, `html`, `aspx`, `www`).
  - Strict alphabetical tokens: only `[a-z]+`. Single letters restricted to standard English words (`a`, `i`).
  - Top 1,000 words in `words_common_1k.txt` directly correspond to ranks 1–1,000 of `words_10k.txt`.
- **Top 10 Words**: `the`, `of`, `and`, `to`, `a`, `in`, `for`, `is`, `on`, `that`.

### 2.2 `passages.json`
- **Format**: JSON array of objects.
- **Count**: 370 passages (Aesop: 90, Sherlock Holmes: 100, The Art of War: 85, Grimm's Fairy Tales: 95).
- **Length Constraint**: Strictly between 150 and 400 characters per passage (Average: 264.8 chars).
- **Normalization**: Normalized to pure printable ASCII (characters 32–126). Curly quotes converted to straight quotes (`"`, `'`), dashes standardized, and italics markers removed.
- **Schema**:
```json
[
  {
    "id": "passage_001",
    "source": "Aesop's Fables",
    "author": "Aesop",
    "title": "The Lion and the Mouse",
    "category": "Fable",
    "text": "\"You ridiculed the idea of my ever being able to help you, not expecting to receive from me any repayment of your favour; now you know that it is possible for even a Mouse to confer benefits on a Lion.\"",
    "length": 202,
    "word_count": 40
  }
]
```

### 2.3 `passages_easy.json`
- **Format**: JSON array of objects.
- **Count**: 350 passages.
- **Characteristics**:
  - 100% lowercase (`[a-z\s,\.']`).
  - No Shift keys required (zero uppercase, zero numbers, zero symbols).
  - Punctuation limited to basic periods, commas, and apostrophes.
  - Short word lengths (average word length ≤ 5.5 characters).
- **Schema**:
```json
[
  {
    "id": "easy_001",
    "source": "Aesop's Fables",
    "title": "The Lion and the Mouse",
    "category": "Fable",
    "text": "you ridiculed the idea of my ever being able to help you, not expecting to receive from me any repayment of your favour, now you know that it is possible for even a mouse to confer benefits on a lion.",
    "length": 202,
    "word_count": 40,
    "avg_word_length": 4.07
  }
]
```

### 2.4 `ngrams.json`
- **Format**: JSON object containing metadata, top 200 bigrams, and top 200 trigrams.
- **Corpus Analyzed**: 370 literary prose passages (19,450 words, 68,420 bigram instances, 48,970 trigram instances).
- **Top 10 Bigrams**: `he`, `th`, `in`, `an`, `er`, `nd`, `ou`, `re`, `to`, `en`.
- **Top 10 Trigrams**: `the`, `and`, `ing`, `you`, `her`, `hat`, `his`, `for`, `tha`, `hen`.
- **Schema**:
```json
{
  "metadata": {
    "total_passages_analyzed": 370,
    "total_words_analyzed": 19450,
    "total_bigram_tokens": 68420,
    "total_trigram_tokens": 48970,
    "unique_bigrams_total": 408,
    "unique_trigrams_total": 2474
  },
  "bigrams": [
    {
      "rank": 1,
      "ngram": "he",
      "count": 2437,
      "frequency": 0.035618,
      "percentage": 3.5618
    }
  ],
  "trigrams": [
    {
      "rank": 1,
      "ngram": "the",
      "count": 1512,
      "frequency": 0.030876,
      "percentage": 3.0876
    }
  ]
}
```

### 2.5 `curriculum_stages.json`
- **Format**: Structured 30-Day progressive touch typing syllabus designed for combat mechanics.
- **Unlock Accuracy Threshold**: 98.0%+ for Stages 1–6; 98.5%+ for Stage 7.
- **Stage Breakdown**:
  1. **Stage 1: Home Row Base** (Days 1–4)
     - *Target Keys*: `f`, `j`, `d`, `k`, `s`, `l`, `a`, `;`
     - *Boss*: The Stone Sentry (350 HP, 60s, 98.0% threshold)
  2. **Stage 2: Index Reach** (Days 5–9)
     - *Target Keys*: `g`, `h`, `r`, `u`, `t`, `y`
     - *Boss*: The Swift Stryker (500 HP, 65s, 98.0% threshold)
  3. **Stage 3: Middle & Ring Reaches** (Days 10–14)
     - *Target Keys*: `e`, `i`, `w`, `o`
     - *Boss*: The Vowel Wyvern (650 HP, 70s, 98.0% threshold)
  4. **Stage 4: Pinky Reaches** (Days 15–18)
     - *Target Keys*: `q`, `p`, `z`, `/`
     - *Boss*: The Phantom Pixie (750 HP, 65s, 98.0% threshold)
  5. **Stage 5: Bottom Row Navigation** (Days 19–23)
     - *Target Keys*: `c`, `v`, `b`, `n`, `m`, `x`, `,`, `.`
     - *Boss*: The Obsidian Colossus (900 HP, 75s, 98.0% threshold)
  6. **Stage 6: Numbers & Symbols** (Days 24–27)
     - *Target Keys*: `1`–`0`, `!`, `@`, `#`, `$`, `%`, `^`, `&`, `*`, `(`, `)`, `-`, `=`
     - *Boss*: The Cyber Golem (1,000 HP, 80s, 98.0% threshold)
  7. **Stage 7: Speed & Fluidity** (Days 28–30)
     - *Target Keys*: Full keyboard, speed bursts, literary endurance
     - *Boss*: The Chrono Sovereign (1,500 HP, 90s, 98.5% threshold)

---

## 3. Data Sources & Licensing

| Asset | Source Repository / Text | Upstream Author / Project | License Status |
|:---|:---|:---|:---|
| English Frequency Vocabulary | [first20hours/google-10000-english](https://github.com/first20hours/google-10000-english) | Google Inc. / first20hours | MIT / Public Domain |
| Profanity Filter Corpus | [LDNOOBW](https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words) | LDNOOBW Contributors | CC0 1.0 Universal (Public Domain) |
| *Aesop's Fables* | Project Gutenberg eBook #21 | Aesop (trans. George Fyler Townsend) | Public Domain |
| *The Adventures of Sherlock Holmes* | Project Gutenberg eBook #1661 | Arthur Conan Doyle | Public Domain |
| *The Art of War* | Project Gutenberg eBook #132 | Sun Tzu (trans. Lionel Giles) | Public Domain |
| *Grimm's Fairy Tales* | Project Gutenberg eBook #2591 | Jacob & Wilhelm Grimm | Public Domain |
| Derived Datasets (`ngrams.json`, `curriculum_stages.json`) | TypeFighter Project | DeepMind Pair Programming / Antigravity | CC0 1.0 Universal / MIT |

---

## 4. Automation & Pipeline Scripts

All assets are reproducible via scripts maintained in `typefighter/assets/data/_scripts/`:

1. `_scripts/fetch_and_build_words.py`: Downloads source vocabulary, filters profanities, and builds `words_10k.txt` & `words_common_1k.txt`.
2. `_scripts/process_passages.py`: Cleans raw Gutenberg texts, normalizes ASCII, extracts 150–400 character passages, and builds `passages.json` & `passages_easy.json`.
3. `_scripts/calculate_ngrams.py`: Computes statistical bigrams and trigrams from passages and compiles `ngrams.json`.
4. `_scripts/build_curriculum.py`: Generates the complete 7-stage, 30-day touch typing syllabus in `curriculum_stages.json`.
5. `_scripts/validate_data.py`: Validates all JSON and TXT constraints, character encodings, bounds, and schema integrity.
