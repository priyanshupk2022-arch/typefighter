"""
validate_data.py
Performs comprehensive automated integrity checks and validation
across all TypeFighter text and curriculum deliverables:
1. words_10k.txt
2. words_common_1k.txt
3. passages.json
4. passages_easy.json
5. ngrams.json
6. curriculum_stages.json
"""

import json
import os
import re

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def validate_words():
    print("--> Validating words_10k.txt and words_common_1k.txt...")
    p10k = os.path.join(DATA_DIR, "words_10k.txt")
    p1k = os.path.join(DATA_DIR, "words_common_1k.txt")

    assert os.path.isfile(p10k), "words_10k.txt missing!"
    assert os.path.isfile(p1k), "words_common_1k.txt missing!"

    with open(p10k, "r", encoding="utf-8") as f:
        words_10k = [line.strip() for line in f if line.strip()]

    with open(p1k, "r", encoding="utf-8") as f:
        words_1k = [line.strip() for line in f if line.strip()]

    assert len(words_10k) == 10000, f"Expected 10,000 words in words_10k.txt, got {len(words_10k)}"
    assert len(words_1k) == 1000, f"Expected 1,000 words in words_common_1k.txt, got {len(words_1k)}"

    # Check words are unique
    assert len(set(words_10k)) == 10000, "Duplicate words detected in words_10k.txt"
    assert len(set(words_1k)) == 1000, "Duplicate words detected in words_common_1k.txt"

    # Check formatting: lowercase letters only
    for w in words_10k:
        assert re.fullmatch(r"[a-z]+", w), f"Invalid non-alpha word in words_10k.txt: {w}"

    for w in words_1k:
        assert re.fullmatch(r"[a-z]+", w), f"Invalid non-alpha word in words_common_1k.txt: {w}"

    # Verify 1k is exact prefix of 10k
    assert words_10k[:1000] == words_1k, "words_common_1k.txt should match the top 1,000 of words_10k.txt"

    print(f"    [PASS] words_10k.txt: 10,000 clean words.")
    print(f"    [PASS] words_common_1k.txt: 1,000 common daily words.")

def validate_passages():
    print("--> Validating passages.json...")
    p_path = os.path.join(DATA_DIR, "passages.json")
    assert os.path.isfile(p_path), "passages.json missing!"

    with open(p_path, "r", encoding="utf-8") as f:
        passages = json.load(f)

    assert isinstance(passages, list), "passages.json must be a JSON array"
    assert len(passages) >= 300, f"Expected >= 300 passages, got {len(passages)}"

    sources = set()
    for idx, p in enumerate(passages):
        assert "id" in p and "source" in p and "text" in p and "length" in p, f"Missing fields in passage {idx}"
        txt = p["text"]
        assert 150 <= len(txt) <= 400, f"Passage {p['id']} length out of bounds (150-400): {len(txt)}"
        assert p["length"] == len(txt), f"Passage {p['id']} length mismatch: recorded {p['length']} vs actual {len(txt)}"
        # Check pure printable ASCII (32-126)
        for ch in txt:
            assert 32 <= ord(ch) <= 126, f"Non-ASCII char {repr(ch)} in passage {p['id']}"
        sources.add(p["source"])

    print(f"    [PASS] passages.json: {len(passages)} passages from sources: {list(sources)}")

def validate_passages_easy():
    print("--> Validating passages_easy.json...")
    pe_path = os.path.join(DATA_DIR, "passages_easy.json")
    assert os.path.isfile(pe_path), "passages_easy.json missing!"

    with open(pe_path, "r", encoding="utf-8") as f:
        easy = json.load(f)

    assert isinstance(easy, list), "passages_easy.json must be a JSON array"
    assert len(easy) >= 300, f"Expected >= 300 easy passages, got {len(easy)}"

    for idx, p in enumerate(easy):
        assert "id" in p and "text" in p and "length" in p, f"Missing fields in easy passage {idx}"
        txt = p["text"]
        assert 150 <= len(txt) <= 400, f"Easy passage {p['id']} length out of bounds (150-400): {len(txt)}"
        # Simplified: lowercase and basic punctuation only: a-z, space, comma, period, apostrophe
        assert re.fullmatch(r"[a-z\s,\.']+", txt), f"Easy passage {p['id']} contains non-easy characters: {txt}"

    print(f"    [PASS] passages_easy.json: {len(easy)} simplified passages.")

def validate_ngrams():
    print("--> Validating ngrams.json...")
    ng_path = os.path.join(DATA_DIR, "ngrams.json")
    assert os.path.isfile(ng_path), "ngrams.json missing!"

    with open(ng_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert "bigrams" in data and "trigrams" in data, "ngrams.json missing bigrams or trigrams"
    bigrams = data["bigrams"]
    trigrams = data["trigrams"]

    assert len(bigrams) == 200, f"Expected 200 bigrams, got {len(bigrams)}"
    assert len(trigrams) == 200, f"Expected 200 trigrams, got {len(trigrams)}"

    # Check ranks and keys
    for i, b in enumerate(bigrams, start=1):
        assert b["rank"] == i, f"Rank mismatch in bigram {b}"
        assert len(b["ngram"]) == 2 and b["ngram"].isalpha() and b["ngram"].islower()
        assert b["count"] > 0
        assert 0 < b["frequency"] <= 1.0

    for i, t in enumerate(trigrams, start=1):
        assert t["rank"] == i, f"Rank mismatch in trigram {t}"
        assert len(t["ngram"]) == 3 and t["ngram"].isalpha() and t["ngram"].islower()
        assert t["count"] > 0
        assert 0 < t["frequency"] <= 1.0

    print(f"    [PASS] ngrams.json: 200 bigrams and 200 trigrams verified.")

def validate_curriculum():
    print("--> Validating curriculum_stages.json...")
    cur_path = os.path.join(DATA_DIR, "curriculum_stages.json")
    assert os.path.isfile(cur_path), "curriculum_stages.json missing!"

    with open(cur_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    stages = data.get("stages", [])
    assert len(stages) == 7, f"Expected 7 stages, got {len(stages)}"

    days_covered = []
    for s in stages:
        assert "stage_number" in s and "name" in s and "target_keys" in s
        assert "finger_assignments" in s
        assert "drill_words" in s and len(s["drill_words"]) >= 10
        assert "practice_phrases" in s and len(s["practice_phrases"]) >= 5
        assert "unlock_accuracy_threshold" in s
        assert s["unlock_accuracy_threshold"] >= 98.0, f"Stage {s['stage_number']} threshold must be >= 98.0%"
        assert "boss_battle" in s
        assert "daily_lessons" in s

        for d in s["daily_lessons"]:
            days_covered.append(d["day"])

    assert len(days_covered) == 30, f"Expected 30 daily lessons, got {len(days_covered)}"
    assert sorted(days_covered) == list(range(1, 31)), "Missing or duplicated days in 30-day curriculum!"

    print(f"    [PASS] curriculum_stages.json: 7 stages and 30 consecutive days verified.")

def main():
    print("========================================")
    print("RUNNING TYPEFIGHTER DATA VALIDATION")
    print("========================================")
    validate_words()
    validate_passages()
    validate_passages_easy()
    validate_ngrams()
    validate_curriculum()
    print("========================================")
    print("ALL 6 DELIVERABLES SUCCESSFULLY VALIDATED!")
    print("========================================")

if __name__ == "__main__":
    main()
