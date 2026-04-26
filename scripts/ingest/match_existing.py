#!/usr/bin/env python3
"""Match parsed manuscript references against existing wiki source pages.

Strategy:
- Existing wiki source pages live in wiki/sources/<slug>.md
- We match by first-author last name + year primarily, then by overlapping keywords.
"""
import json
import os
import re
from pathlib import Path


WIKI_SOURCES = Path("wiki/sources")
PARSED = Path("/tmp/wiki_work/parsed_refs.json")


def existing_slugs():
    slugs = []
    for p in sorted(WIKI_SOURCES.glob("*.md")):
        if p.stem == "index":
            continue
        slugs.append(p.stem)
    return slugs


def normalize_slug(s):
    return re.sub(r"[^a-z0-9-]", "", s.lower())


def slug_tokens(s):
    return s.split("-")


def match_ref(ref, existing):
    """Return existing slug if matched else None."""
    fa = ref["first_author_last"]
    yr = str(ref["year"])
    # Build keyword set from title
    title_tokens = re.sub(r"[^a-zA-Z0-9\s]", " ", ref["title"].lower()).split()
    title_tokens = [t for t in title_tokens if len(t) >= 4]
    title_set = set(title_tokens)
    candidates = [s for s in existing if s.startswith(fa + "-" + yr + "-")]
    if not candidates:
        # try suffixed year: e.g., chen-2018 vs chen-2018b — currently no
        return None
    if len(candidates) == 1:
        return candidates[0]
    # Multiple candidates with same author+year: use keyword overlap
    best = None
    best_score = 0
    for c in candidates:
        c_tokens = set(c.split("-")[2:])
        score = len(title_set & c_tokens)
        if score > best_score:
            best_score = score
            best = c
    return best


def main():
    parsed = json.loads(PARSED.read_text())
    existing = existing_slugs()
    print(f"Existing wiki sources: {len(existing)}")
    out = {}
    for topic, refs in parsed.items():
        matched_count = 0
        for r in refs:
            m = match_ref(r, existing)
            r["matched_existing"] = m
            if m:
                matched_count += 1
        out[topic] = refs
        print(f"{topic}: {matched_count}/{len(refs)} already in wiki")
    Path("/tmp/wiki_work/parsed_refs.json").write_text(json.dumps(out, indent=2))
    # write unmatched lists
    for topic, refs in out.items():
        unmatched = [r for r in refs if not r["matched_existing"]]
        Path(f"/tmp/wiki_work/{topic}_unmatched.json").write_text(json.dumps(unmatched, indent=2))
        print(f"  {topic} unmatched: {len(unmatched)} (saved)")


if __name__ == "__main__":
    main()
