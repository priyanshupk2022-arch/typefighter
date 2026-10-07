"""
process_passages.py
Extracts, cleans, normalizes, and filters public-domain prose from Project Gutenberg:
- Aesop's Fables
- The Adventures of Sherlock Holmes
- The Art of War (Sun Tzu's actual treatise)
- Grimm's Fairy Tales

Produces:
1. passages.json (300+ clean public-domain prose passages, 150-400 chars, normalized ASCII)
2. passages_easy.json (300+ simplified passages, lowercase + basic punctuation, short words)
"""

import json
import os
import re
import unicodedata

RAW_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "_raw"))
DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def read_book(filename):
    path = os.path.join(RAW_DIR, filename)
    with open(path, "rb") as f:
        raw = f.read().decode("utf-8", errors="ignore")
    # Normalize newline variations
    text = raw.replace("\r\r\n", "\n").replace("\r\n", "\n").replace("\r", "\n")
    return text

def strip_gutenberg_markers(text):
    start_match = re.search(r"\*\*\* START OF THE PROJECT GUTENBERG EBOOK[^\n]*\*\*\*", text)
    end_match = re.search(r"\*\*\* END OF THE PROJECT GUTENBERG EBOOK", text)
    start_pos = start_match.end() if start_match else 0
    end_pos = end_match.start() if end_match else len(text)
    return text[start_pos:end_pos].strip()

def clean_to_ascii(text):
    # Strip bracketed comments like [illustration...] or [note...]
    text = re.sub(r"\[[^\]]*\]", "", text)
    # Remove italics underscores
    text = text.replace("_", "")
    # Map special quotes and dashes before NFKD
    text = text.replace("“", '"').replace("”", '"')
    text = text.replace("‘", "'").replace("’", "'")
    text = text.replace("`", "'")
    text = text.replace("—", " -- ").replace("–", " - ")
    text = text.replace("…", "...")
    # Sun Tzu spelling
    text = text.replace("Sun Tzŭ", "Sun Tzu").replace("Sun Tzu", "Sun Tzu")
    # NFKD decomposition to strip accents
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    # Replace tabs and newlines with space
    text = re.sub(r"\s+", " ", text).strip()
    return text

def is_noise(p):
    # Exclude headers, Roman numerals, Gutenberg terms, transcriber notes
    upper_chars = sum(1 for c in p if c.isupper())
    if len(p) > 0 and (upper_chars / len(p)) > 0.35:
        return True
    noise_keywords = [
        "PROJECT GUTENBERG", "TRANSCRIPTION", "TRANSCRIBER", "ILLUSTRATION",
        "TABLE OF CONTENTS", "CHAPTER", "ADVENTURE I", "ADVENTURE V",
        "ADVENTURE X", "FABLE ", "SCENE ", "ACT ", "FOOTNOTE",
        "Gutenberg", "gutenberg.org", "eBook", "http", "www."
    ]
    for kw in noise_keywords:
        if kw in p or kw.lower() in p.lower():
            return True
    # Must start with letter or standard quote
    if not re.match(r"^[\"\'A-Z]", p):
        return True
    # Must end with terminal punctuation
    if not re.search(r"[\.!\?][\"\'\)]?$", p):
        return True
    # No brackets or braces
    if any(c in p for c in "[]{}<>_~`\\|^"):
        return True
    return False

def clean_passage_text(p):
    # Remove leading fable titles like "THE FOX AND THE GRAPES. "
    p = re.sub(r"^[A-Z\s,;'\-]{4,40}\.\s+", "", p)
    # Fix any double dashes to spaced dash or comma
    p = re.sub(r"\s*--\s*", ", ", p)
    p = re.sub(r"\s+-\s+", " - ", p)
    # Fix quotes spacing
    p = re.sub(r'\s+"', ' "', p)
    p = re.sub(r'"\s+', '" ', p)
    p = re.sub(r"\s+", " ", p).strip()
    return p

def extract_aesop_passages(text):
    body = strip_gutenberg_markers(text)
    paras = re.split(r"\n\n+", body)
    passages = []
    current_title = "Aesop's Fables"
    
    for raw_p in paras:
        p = clean_to_ascii(raw_p)
        if not p:
            continue
        if len(p) < 50 and not p.endswith((".", "!", "?")) and not is_noise(p):
            current_title = p.strip()
            continue
        p = clean_passage_text(p)
        if is_noise(p):
            continue
        if 150 <= len(p) <= 400:
            passages.append({
                "source": "Aesop's Fables",
                "author": "Aesop",
                "title": current_title,
                "category": "Fable",
                "text": p
            })
    return passages

def extract_sherlock_passages(text):
    body = strip_gutenberg_markers(text)
    paras = re.split(r"\n\n+", body)
    passages = []
    current_adventure = "The Adventures of Sherlock Holmes"
    
    for raw_p in paras:
        p = clean_to_ascii(raw_p)
        if not p:
            continue
        if p.startswith("ADVENTURE ") or p.startswith("THE ADVENTURE OF"):
            current_adventure = p
            continue
        p = clean_passage_text(p)
        if is_noise(p):
            continue
        if 150 <= len(p) <= 400:
            passages.append({
                "source": "The Adventures of Sherlock Holmes",
                "author": "Arthur Conan Doyle",
                "title": current_adventure,
                "category": "Mystery / Detective",
                "text": p
            })
    return passages

def extract_art_of_war_passages(text):
    body = strip_gutenberg_markers(text)
    # Start at the actual treatise
    pos = body.find("Chapter I. LAYING PLANS")
    if pos != -1:
        body = body[pos:]
    paras = re.split(r"\n\n+", body)
    passages = []
    current_chapter = "The Art of War"
    
    chapter_names = {
        "I": "Laying Plans", "II": "Waging War", "III": "Attack by Stratagem",
        "IV": "Tactical Dispositions", "V": "Energy", "VI": "Weak Points and Strong",
        "VII": "Maneuvering", "VIII": "Variation in Tactics", "IX": "The Army on the March",
        "X": "Terrain", "XI": "The Nine Situations", "XII": "The Attack by Fire",
        "XIII": "The Use of Spies"
    }

    for raw_p in paras:
        p = clean_to_ascii(raw_p)
        if not p:
            continue
        chap_match = re.match(r"^Chapter\s+([IVXLCDM]+)\.?\s*(.*)", p, re.IGNORECASE)
        if chap_match:
            cnum = chap_match.group(1).upper()
            cname = chapter_names.get(cnum, chap_match.group(2).title() or f"Chapter {cnum}")
            current_chapter = f"Chapter {cnum}: {cname}"
            continue
        # Strip leading numbers e.g. "1. Sun Tzu said:"
        p = re.sub(r"^\d+\.\s*", "", p)
        p = clean_passage_text(p)
        if is_noise(p):
            continue
        # Exclude translator commentators
        if re.match(r"^(Tu Mu|Wang Hsi|Chang Yu|Li Ch'uan|Mei Yao-ch'en|Ho Shih|Chia Lin)\s+", p):
            continue
        if 150 <= len(p) <= 400:
            passages.append({
                "source": "The Art of War",
                "author": "Sun Tzu",
                "title": current_chapter,
                "category": "Strategy / Philosophy",
                "text": p
            })
    return passages

def extract_grimm_passages(text):
    body = strip_gutenberg_markers(text)
    paras = re.split(r"\n\n+", body)
    passages = []
    current_tale = "Grimm's Fairy Tales"
    
    for raw_p in paras:
        p = clean_to_ascii(raw_p)
        if not p:
            continue
        if len(p) < 45 and not p.endswith((".", "!", "?")) and not is_noise(p):
            current_tale = p.strip().strip("'\"")
            continue
        p = clean_passage_text(p)
        if is_noise(p):
            continue
        if 150 <= len(p) <= 400:
            passages.append({
                "source": "Grimm's Fairy Tales",
                "author": "Brothers Grimm",
                "title": current_tale,
                "category": "Fairy Tale",
                "text": p
            })
    return passages

def simplify_to_easy(text):
    """
    Transforms text to simplified easy passage:
    - Lowercase only
    - Basic punctuation only: comma, period, apostrophe for contraction
    - Remove numbers, quotes, dashes, semicolons, colons, brackets
    - Clean up duplicate spaces and punctuation
    """
    t = text.lower()
    t = t.replace("`", "'").replace('"', '')
    # Replace colons, semicolons, exclamation, question marks with periods or commas
    t = re.sub(r"[;:]", ",", t)
    t = re.sub(r"[!\?]", ".", t)
    t = re.sub(r"[\-\(\)\[\]\{\}]", " ", t)
    # Strip any characters that are not a-z, space, comma, period, apostrophe
    t = re.sub(r"[^a-z\s,\.']", "", t)
    # Clean multiple spaces and multiple punctuation
    t = re.sub(r"\s+", " ", t)
    t = re.sub(r",+", ",", t)
    t = re.sub(r"\.+", ".", t)
    t = re.sub(r",\s*\.", ".", t)
    t = re.sub(r"\.\s*,", ".", t)
    # Ensure spaces after punctuation
    t = re.sub(r",(?=[a-z])", ", ", t)
    t = re.sub(r"\.(?=[a-z])", ". ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t

def pick_diverse(lst, target_n):
    seen_texts = set()
    picked = []
    for item in lst:
        txt = item["text"]
        if not (150 <= len(txt) <= 400):
            continue
        if txt in seen_texts:
            continue
        # Verify strict ASCII printable (32 to 126)
        if any(ord(c) < 32 or ord(c) > 126 for c in txt):
            continue
        seen_texts.add(txt)
        picked.append(item)
        if len(picked) >= target_n:
            break
    return picked

def main():
    print("Reading and parsing raw texts...")
    aesop_text = read_book("aesop.txt")
    sherlock_text = read_book("sherlock.txt")
    art_of_war_text = read_book("art_of_war.txt")
    grimm_text = read_book("grimm.txt")

    aesop_passages = extract_aesop_passages(aesop_text)
    sherlock_passages = extract_sherlock_passages(sherlock_text)
    art_war_passages = extract_art_of_war_passages(art_of_war_text)
    grimm_passages = extract_grimm_passages(grimm_text)

    print(f"Extracted candidates:")
    print(f" - Aesop: {len(aesop_passages)}")
    print(f" - Sherlock: {len(sherlock_passages)}")
    print(f" - Art of War: {len(art_war_passages)}")
    print(f" - Grimm: {len(grimm_passages)}")

    # Pick 90 Aesop, 100 Sherlock, 85 Art of War, 95 Grimm = 370 total
    p_aesop = pick_diverse(aesop_passages, 90)
    p_sherlock = pick_diverse(sherlock_passages, 100)
    p_art_war = pick_diverse(art_war_passages, 85)
    p_grimm = pick_diverse(grimm_passages, 95)

    all_raw_selected = p_aesop + p_sherlock + p_art_war + p_grimm

    # 1. Build passages.json
    final_passages = []
    for idx, item in enumerate(all_raw_selected, start=1):
        txt = item["text"]
        words = txt.split()
        entry = {
            "id": f"passage_{idx:03d}",
            "source": item["source"],
            "author": item["author"],
            "title": item["title"],
            "category": item["category"],
            "text": txt,
            "length": len(txt),
            "word_count": len(words)
        }
        final_passages.append(entry)

    out_passages_path = os.path.join(DATA_DIR, "passages.json")
    with open(out_passages_path, "w", encoding="utf-8") as f:
        json.dump(final_passages, f, indent=2, ensure_ascii=True)
    print(f"Successfully saved {len(final_passages)} passages to {out_passages_path}")

    # 2. Build passages_easy.json
    all_pool = aesop_passages + sherlock_passages + art_war_passages + grimm_passages
    seen_easy = set()
    easy_passages = []

    for item in all_pool:
        easy_text = simplify_to_easy(item["text"])
        if not (150 <= len(easy_text) <= 400):
            continue
        if easy_text in seen_easy:
            continue
        # Verify characters: strictly lowercase and basic punctuation
        if not re.fullmatch(r"[a-z\s,\.']+", easy_text):
            continue
        if not easy_text.endswith("."):
            easy_text += "."
            if len(easy_text) > 400:
                continue
        words = easy_text.split()
        if not words:
            continue
        avg_wlen = sum(len(w.strip(".,'")) for w in words) / len(words)
        if avg_wlen > 5.5:
            continue
        seen_easy.add(easy_text)
        easy_passages.append({
            "id": f"easy_{len(easy_passages)+1:03d}",
            "source": item["source"],
            "title": item["title"],
            "category": item["category"],
            "text": easy_text,
            "length": len(easy_text),
            "word_count": len(words),
            "avg_word_length": round(avg_wlen, 2)
        })
        if len(easy_passages) >= 350:
            break

    out_easy_path = os.path.join(DATA_DIR, "passages_easy.json")
    with open(out_easy_path, "w", encoding="utf-8") as f:
        json.dump(easy_passages, f, indent=2, ensure_ascii=True)
    print(f"Successfully saved {len(easy_passages)} easy passages to {out_easy_path}")

if __name__ == "__main__":
    main()
