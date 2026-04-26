#!/usr/bin/env python3
"""Add Connections links from each topic anchor + topic-hub page to all
source pages tagged with that topic.

Reads wiki/sources/*.md, picks up frontmatter `topic:` field, and inserts a
"Linked Sources" section with bullet list at the bottom of the anchor and
topic-hub pages.
"""
import re
from pathlib import Path

SOURCES_DIR = Path("wiki/sources")

TOPIC_TO_PAGES = {
    "ptmanchor": [
        Path("wiki/analyses/ptmanchor-manuscript-anchor.md"),
        Path("wiki/topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md"),
    ],
    "resistance": [
        Path("wiki/analyses/cancer-resistance-manuscript-anchor.md"),
        Path("wiki/topics/immunotherapy-resistance-and-immune-evasion.md"),
    ],
    "bcell-neoantigen": [
        Path("wiki/analyses/b-cell-neoantigen-proposal-anchor.md"),
        Path("wiki/topics/b-cell-neoantigen-human-cancer.md"),
    ],
}


def parse_frontmatter(text):
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 4)
    if end < 0:
        return {}, text
    fm = text[4:end]
    body = text[end + 4 :]
    out = {}
    for line in fm.split("\n"):
        m = re.match(r"^([a-zA-Z_]+)\s*:\s*(.+)$", line)
        if m:
            k = m.group(1)
            v = m.group(2).strip().strip('"').strip("'")
            out[k] = v
    return out, body


def collect_sources_by_topic():
    by_topic = {}
    for f in sorted(SOURCES_DIR.glob("*.md")):
        if f.stem == "index": continue
        fm, _ = parse_frontmatter(f.read_text())
        topic = fm.get("topic")
        title = fm.get("title", f.stem)
        if not topic: continue
        by_topic.setdefault(topic, []).append((f.stem, title))
    return by_topic


def upsert_section(text, header, items):
    """Replace or append a '## {header}' section with a bullet list of items.
    items is list of (slug, title)."""
    bullets = [f"- [{title}](../sources/{slug}.md)" for slug, title in items]
    section = f"## {header}\n\n" + "\n".join(bullets) + "\n"
    pat = re.compile(r"\n## " + re.escape(header) + r"\n.*?(?=\n## |\Z)", re.DOTALL)
    if pat.search(text):
        return pat.sub("\n" + section, text)
    return text.rstrip() + "\n\n" + section


def main():
    by_topic = collect_sources_by_topic()
    for topic, items in by_topic.items():
        print(f"{topic}: {len(items)} sources")
        for page in TOPIC_TO_PAGES.get(topic, []):
            if not page.exists(): continue
            text = page.read_text()
            new_text = upsert_section(text, "Linked Sources", sorted(items, key=lambda x: x[1]))
            if new_text != text:
                page.write_text(new_text)
                print(f"  updated {page}")


if __name__ == "__main__":
    main()
