#!/usr/bin/env python3
"""Classify legacy source pages (no topic field) into one or more of the three
topics by keyword matching against title + body, then add a topic field to the
frontmatter so update_anchor_links picks them up.

A page can belong to multiple topics — for those, we duplicate-assign by adding
both topic tags + anchor links.
"""
import re
from pathlib import Path

SOURCES = Path("wiki/sources")

KW = {
    "ptmanchor": [
        r"\bphospho\w*\b", r"\bkinase\w*\b", r"\bproteogenom\w*\b",
        r"\bproteom\w*\b", r"\bptm\b", r"\bpost-translational\b",
        r"\bcptac\b", r"\bsignal\w* network\b", r"\bsignaling pathway\b",
        r"\bphosphosite\b",
    ],
    "bcell-neoantigen": [
        r"\bneoantigen\w*\b", r"\bneoepitope\w*\b",
        r"\bb cell\b", r"\bb-cell\b",
        r"\btertiary lymphoid\b", r"\btls\b",
        r"\bimmunopeptidom\w*\b", r"\bvaccine\b",
        r"\bhla\b.*\bpresentation\b",
        r"\bantibody response\b", r"\btcr\b.*\bneoantigen\b",
    ],
    "resistance": [
        r"\bresistance\b", r"\bimmune evasion\b", r"\bimmune escape\b",
        r"\bcheckpoint\b", r"\bhla loss\b", r"\bb2m\b", r"\bjak\b",
        r"\bkras\b", r"\begfr\b", r"\besr1\b", r"\bparp\b",
        r"\bcheckpoint inhibitor\b", r"\bpd-?1\b", r"\bpd-?l1\b",
        r"\btgf\W*beta\b", r"\bcar.t\b", r"\bbispecific\b",
        r"\bantibody.drug conjugate\b", r"\badc\b", r"\bantiandrogen\b",
        r"\bcd?k\d*\b inhibitor\b",
    ],
}


def parse_fm(text):
    if not text.startswith("---"):
        return None, None, text
    end = text.find("\n---", 4)
    if end < 0:
        return None, None, text
    return text[4:end], text[:end+4], text[end+4:]


def classify(text):
    body = text.lower()
    matched = []
    for topic, patterns in KW.items():
        for p in patterns:
            if re.search(p, body):
                matched.append(topic)
                break
    return matched


def main():
    updated = 0
    for f in sorted(SOURCES.glob("*.md")):
        if f.stem == "index": continue
        text = f.read_text()
        fm, fm_block, body = parse_fm(text)
        if fm is None: continue
        if re.search(r"^topic:\s*\S+", fm, re.MULTILINE):
            continue  # already classified
        topics = classify(text)
        if not topics:
            continue
        # Use the first matched topic as primary, store all matched in tags
        primary = topics[0]
        new_lines = []
        for line in fm.split("\n"):
            new_lines.append(line)
        # Insert topic field
        new_lines.append(f"topic: {primary}")
        if len(topics) > 1:
            new_lines.append(f"extra_topics:")
            for t in topics[1:]:
                new_lines.append(f"  - \"{t}\"")
        new_fm = "\n".join(new_lines)
        new_text = "---\n" + new_fm + "\n---\n" + body.lstrip("\n")
        f.write_text(new_text)
        updated += 1
        if updated <= 5:
            print(f"  classified {f.stem}: {topics}")
    print(f"Updated {updated} legacy pages")

if __name__ == "__main__":
    main()
