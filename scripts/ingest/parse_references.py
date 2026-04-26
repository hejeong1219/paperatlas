#!/usr/bin/env python3
"""Parse Vancouver-style references from a plain-text manuscript dump."""
import json
import re
import sys
from pathlib import Path


REF_HEADER = re.compile(r"^\s*References\s*$", re.IGNORECASE)
NEXT_SECTION = re.compile(r"^\s*(Figures?|Tables?|Supplementary|Appendix)\s*$", re.IGNORECASE)
REF_START = re.compile(r"^(\d+)\.\s+(.*)$")


def read_refs(text_path: Path):
    lines = text_path.read_text().splitlines()
    in_refs = False
    blocks = []
    current = []
    for line in lines:
        if REF_HEADER.match(line):
            in_refs = True
            continue
        if not in_refs:
            continue
        if NEXT_SECTION.match(line) and current:
            blocks.append(" ".join(current).strip())
            current = []
            break
        m = REF_START.match(line.strip())
        if m:
            if current:
                blocks.append(" ".join(current).strip())
            current = [line.strip()]
        else:
            if line.strip():
                current.append(line.strip())
    if current and in_refs:
        blocks.append(" ".join(current).strip())
    return blocks


YEAR_RE = re.compile(r"\.\s*(19|20)(\d{2})\s*[;:]")
AUTHOR_RE = re.compile(r"^(\d+)\.\s+([^.]+?)\.\s+(.*)$")


def parse_ref(block):
    m = AUTHOR_RE.match(block)
    if not m:
        return None
    num = int(m.group(1))
    authors_raw = m.group(2)
    rest = m.group(3)
    first_author_last = re.split(r",| ", authors_raw.strip())[0].lower()
    first_author_last = re.sub(r"[^a-z]", "", first_author_last) or "unknown"
    ym = YEAR_RE.search(rest)
    year = int(ym.group(1) + ym.group(2)) if ym else 0
    title_match = re.match(r"^([^.]+?)\.", rest)
    title = title_match.group(1).strip() if title_match else rest
    journal_match = re.search(r"\.\s+([^.]+?)\.\s*(?:\d{4})", rest)
    journal = journal_match.group(1).strip() if journal_match else ""
    return {
        "number": num,
        "first_author_last": first_author_last,
        "authors_raw": authors_raw.strip(),
        "year": year,
        "title": title,
        "journal": journal,
        "rest": rest,
        "block": block,
    }


def slug_from_title(title, year, first_author):
    cleaned = re.sub(r"[^a-zA-Z0-9\s-]", "", title.lower())
    words = cleaned.split()
    skipwords = {
        "a", "an", "the", "of", "in", "on", "and", "for", "to", "by", "with",
        "from", "as", "via", "is", "are", "be", "at", "or", "into", "vs",
        "versus", "this", "that", "their", "its", "but",
    }
    words = [w for w in words if w not in skipwords]
    keywords = "-".join(words[:5])
    return f"{first_author}-{year}-{keywords}"


def main():
    sources = {
        "resistance": "/tmp/wiki_work/resistance_manuscript.txt",
        "ptmanchor": "/tmp/wiki_work/ptmanchor_manuscript.txt",
    }
    out = {}
    for name, path in sources.items():
        blocks = read_refs(Path(path))
        parsed = []
        for b in blocks:
            p = parse_ref(b)
            if not p:
                continue
            p["slug"] = slug_from_title(p["title"], p["year"], p["first_author_last"])
            parsed.append(p)
        out[name] = parsed
        print(f"{name}: {len(parsed)} references", file=sys.stderr)
    Path("/tmp/wiki_work/parsed_refs.json").write_text(json.dumps(out, indent=2))
    print("Wrote /tmp/wiki_work/parsed_refs.json", file=sys.stderr)


if __name__ == "__main__":
    main()
