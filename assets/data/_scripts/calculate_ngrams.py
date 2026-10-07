"""
calculate_ngrams.py
Calculates the top 200 bigrams and top 200 trigrams from the collected passages (passages.json).
Outputs ngrams.json with ranks, counts, frequencies, and percentages.
"""

import json
import os
import re
from collections import Counter

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def main():
    passages_path = os.path.join(DATA_DIR, "passages.json")
    if not os.path.exists(passages_path):
        raise FileNotFoundError(f"passages.json not found at {passages_path}")

    with open(passages_path, "r", encoding="utf-8") as f:
        passages = json.load(f)

    bigram_counts = Counter()
    trigram_counts = Counter()
    total_words = 0

    for p in passages:
        words = re.findall(r"[a-z]+", p["text"].lower())
        total_words += len(words)
        for w in words:
            for i in range(len(w) - 1):
                bigram_counts[w[i:i+2]] += 1
            for i in range(len(w) - 2):
                trigram_counts[w[i:i+3]] += 1

    total_bigram_occurrences = sum(bigram_counts.values())
    total_trigram_occurrences = sum(trigram_counts.values())

    top_200_bigrams = bigram_counts.most_common(200)
    top_200_trigrams = trigram_counts.most_common(200)

    bigram_list = []
    for rank, (ngram, count) in enumerate(top_200_bigrams, start=1):
        freq = count / total_bigram_occurrences
        bigram_list.append({
            "rank": rank,
            "ngram": ngram,
            "count": count,
            "frequency": round(freq, 6),
            "percentage": round(freq * 100, 4)
        })

    trigram_list = []
    for rank, (ngram, count) in enumerate(top_200_trigrams, start=1):
        freq = count / total_trigram_occurrences
        trigram_list.append({
            "rank": rank,
            "ngram": ngram,
            "count": count,
            "frequency": round(freq, 6),
            "percentage": round(freq * 100, 4)
        })

    output_data = {
        "metadata": {
          "description": "Top 200 bigrams and top 200 trigrams extracted from TypeFighter Project Gutenberg prose passages",
          "total_passages_analyzed": len(passages),
          "total_words_analyzed": total_words,
          "total_bigram_tokens": total_bigram_occurrences,
          "total_trigram_tokens": total_trigram_occurrences,
          "unique_bigrams_total": len(bigram_counts),
          "unique_trigrams_total": len(trigram_counts)
        },
        "bigrams": bigram_list,
        "trigrams": trigram_list
    }

    out_path = os.path.join(DATA_DIR, "ngrams.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2)

    print(f"Successfully calculated n-grams and saved to {out_path}")
    print(f"Top 10 Bigrams: {[b['ngram'] for b in bigram_list[:10]]}")
    print(f"Top 10 Trigrams: {[t['ngram'] for t in trigram_list[:10]]}")

if __name__ == "__main__":
    main()
