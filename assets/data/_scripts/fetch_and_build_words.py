"""
fetch_and_build_words.py
Downloads frequency word lists and profanity blocklists,
filters profanity, adult terms, and web junk tokens, and produces:
- words_10k.txt (top 10,000 clean, family-friendly lowercase English words)
- words_common_1k.txt (top 1,000 daily English words for instant muscle memory)
"""

import os
import re
import urllib.request

RAW_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "_raw"))
DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

os.makedirs(RAW_DIR, exist_ok=True)

URL_20K = "https://raw.githubusercontent.com/first20hours/google-10000-english/master/20k.txt"
URL_10K = "https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english.txt"
URL_10K_NO_SWEARS = "https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-no-swears.txt"
URL_LDNOOBW = "https://raw.githubusercontent.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/master/en"

def read_or_fetch(url, local_path):
    if os.path.exists(local_path) and os.path.getsize(local_path) > 0:
        print(f"Reading cached {local_path}")
        with open(local_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    print(f"Fetching {url} -> {local_path}")
    headers = {"User-Agent": "TypeFighter-DataCollector/1.0"}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as resp:
        content = resp.read().decode("utf-8", errors="ignore")
    with open(local_path, "w", encoding="utf-8") as f:
        f.write(content)
    return content

def main():
    raw_20k_path = os.path.join(RAW_DIR, "google_20k.txt")
    raw_10k_path = os.path.join(RAW_DIR, "google_10k.txt")
    raw_10k_ns_path = os.path.join(RAW_DIR, "google_10k_no_swears.txt")
    raw_ldnoobw_path = os.path.join(RAW_DIR, "ldnoobw_bad_words.txt")

    content_20k = read_or_fetch(URL_20K, raw_20k_path)
    content_10k = read_or_fetch(URL_10K, raw_10k_path)
    content_10k_ns = read_or_fetch(URL_10K_NO_SWEARS, raw_10k_ns_path)
    content_ldnoobw = read_or_fetch(URL_LDNOOBW, raw_ldnoobw_path)

    # 1. Base google swears
    google_swears = set(content_10k.lower().splitlines()) - set(content_10k_ns.lower().splitlines())

    # 2. LDNOOBW list
    ldnoobw_swears = {line.strip().lower() for line in content_ldnoobw.splitlines() if line.strip()}

    # 3. Comprehensive curated list of explicit profanity, slurs, sexual/adult content, and crude web slang
    curated_bad = {
        "anal", "anus", "arse", "ass", "asshole", "bastard", "bitch", "bitches", "bitchy", "blowjob",
        "bollock", "bollocks", "boob", "boobs", "booty", "bugger", "bullshit", "butt", "butts",
        "clit", "clitoris", "cock", "cocks", "crap", "crappy", "cunt", "cunts", "damn", "damned",
        "dick", "dicks", "dildo", "dildos", "dyke", "ejaculat", "erect", "erection", "erotic", "erotica",
        "erotik", "escort", "escorts", "fag", "faggot", "fags", "fetish", "foreskin", "fuck", "fucked",
        "fucker", "fuckers", "fucking", "fucks", "gangbang", "gay", "goddamn", "gook", "handjob",
        "hardcore", "hentai", "homo", "horny", "incest", "intercourse", "jerk", "jerking", "jism", "jizz",
        "kike", "labia", "lesbian", "lesbians", "lust", "masturbat", "masturbation", "milf", "nazi",
        "nazis", "negro", "nigga", "nigger", "niggers", "nipple", "nipples", "nude", "nudes", "nudity",
        "orgasm", "orgasms", "orgy", "orgies", "penis", "penises", "piss", "pissed", "pisses", "poop",
        "porn", "porno", "pornography", "prick", "prostitute", "prostitution", "pussy", "pussies",
        "queer", "rape", "raped", "raper", "rapes", "raping", "rapist", "rectum", "scrotum", "semen",
        "sex", "sexual", "sexuality", "sexually", "sexy", "shemale", "shit", "shits", "shitty",
        "skank", "slut", "sluts", "smegma", "snuff", "sodomy", "spic", "spunk", "stripper", "strippers",
        "testicle", "testicles", "threesome", "tit", "tits", "titties", "tosser", "tranny", "twat",
        "urethra", "vagina", "vaginal", "vaginas", "viagra", "vulva", "wank", "wanker", "whore", "whores",
        "xxx"
    }

    # Combined blockset
    blockset = set()
    for s in (google_swears | ldnoobw_swears | curated_bad):
        s_clean = s.strip().lower()
        if s_clean:
            blockset.add(s_clean)

    # Web/noise tokens that aren't good typing practice words
    noise_tokens = {
        "http", "https", "www", "html", "htm", "php", "asp", "aspx", "jsp", "css",
        "xml", "sql", "pdf", "jpg", "jpeg", "png", "gif", "svg", "exe", "zip", "rar",
        "com", "org", "net", "edu", "gov", "mil", "int", "biz", "info", "href", "src",
        "var", "url", "utf", "rss", "isbn", "faq", "jpg", "doc", "docx", "xls", "xlsx"
    }

    # Common valid two-letter English words (whitelisted)
    valid_2_letter = {
        "am", "an", "as", "at", "be", "by", "do", "go", "he", "hi", "if", "in", "is",
        "it", "me", "my", "no", "of", "on", "or", "ox", "so", "to", "up", "us", "we"
    }

    def is_blocked(w):
        if w in blockset or w in noise_tokens:
            return True
        if len(w) == 2 and w not in valid_2_letter:
            return True
        # Check stem triggers for severe roots
        severe_stems = ["fuck", "shit", "porn", "nigger", "cunt", "dildo", "bitch", "nude", "eroti", "fetish"]
        for stem in severe_stems:
            if stem in w:
                return True
        return False

    raw_words = [line.strip().lower() for line in content_20k.splitlines() if line.strip()]

    clean_words = []
    seen = set()

    for w in raw_words:
        # Letters only
        if not re.fullmatch(r"[a-z]+", w):
            continue
        # Length check: 1 letter only 'a' or 'i', maximum length 25
        if len(w) == 1 and w not in ("a", "i"):
            continue
        if len(w) > 25:
            continue
        if is_blocked(w):
            continue
        if w not in seen:
            seen.add(w)
            clean_words.append(w)

    print(f"Total clean candidates available: {len(clean_words)}")
    if len(clean_words) < 10000:
        raise ValueError(f"Not enough clean words! Only {len(clean_words)} found.")

    # 1. words_10k.txt: exactly top 10,000 words
    top_10k = clean_words[:10000]
    out_10k_path = os.path.join(DATA_DIR, "words_10k.txt")
    with open(out_10k_path, "w", encoding="utf-8") as f:
        f.write("\n".join(top_10k) + "\n")
    print(f"Successfully saved {len(top_10k)} words to {out_10k_path}")

    # 2. words_common_1k.txt: exactly top 1,000 words
    top_1k = clean_words[:1000]
    out_1k_path = os.path.join(DATA_DIR, "words_common_1k.txt")
    with open(out_1k_path, "w", encoding="utf-8") as f:
        f.write("\n".join(top_1k) + "\n")
    print(f"Successfully saved {len(top_1k)} words to {out_1k_path}")

    # Verification checks
    assert len(top_10k) == 10000, f"Expected 10000 words, got {len(top_10k)}"
    assert len(top_1k) == 1000, f"Expected 1000 words, got {len(top_1k)}"
    for w in top_10k:
        assert w.islower() and w.isalpha(), f"Invalid word: {w}"
    print("All validation assertions passed!")

if __name__ == "__main__":
    main()
