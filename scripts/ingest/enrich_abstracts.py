#!/usr/bin/env python3
"""For source pages whose body still has 'Abstract pending', fetch the
PubMed abstract via efetch and replace the placeholder."""
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

NCBI = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
UA = "Mozilla/5.0 llm-wiki/0.1"

PLACEHOLDER = "_Abstract pending — see source PDF or external link for full content._"


def http_get(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def fetch_abstract(pmid):
    url = f"{NCBI}/efetch.fcgi?db=pubmed&id={pmid}&retmode=xml"
    try:
        data = http_get(url, timeout=30)
        root = ET.fromstring(data)
        art = root.find(".//PubmedArticle")
        if art is None:
            return None
        parts = []
        for ab in art.findall(".//Abstract/AbstractText"):
            label = ab.attrib.get("Label")
            text = "".join(ab.itertext()).strip()
            if not text:
                continue
            parts.append(f"**{label}**: {text}" if label else text)
        return "\n\n".join(parts).strip() or None
    except Exception:
        return None


def parse_pmid_from_page(text):
    m = re.search(r"^pmid:\s*\"?(\d+)\"?", text, re.MULTILINE)
    if m: return m.group(1)
    m = re.search(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d+)", text)
    if m: return m.group(1)
    return None


def main():
    sources = Path("wiki/sources")
    targets = []
    for f in sources.glob("*.md"):
        if f.stem == "index": continue
        text = f.read_text()
        if PLACEHOLDER not in text:
            continue
        pmid = parse_pmid_from_page(text)
        if not pmid:
            continue
        targets.append((f, pmid, text))
    print(f"Pages eligible for abstract enrichment: {len(targets)}", file=sys.stderr)
    updated = 0
    for i, (f, pmid, text) in enumerate(targets):
        if i and i % 20 == 0:
            print(f"  [{i}/{len(targets)}] updated={updated}", file=sys.stderr)
        abstract = fetch_abstract(pmid)
        if not abstract:
            time.sleep(0.3)
            continue
        new_text = text.replace(PLACEHOLDER, abstract)
        if new_text != text:
            f.write_text(new_text)
            updated += 1
        time.sleep(0.2)
    print(f"\nEnriched {updated}/{len(targets)} pages", file=sys.stderr)


if __name__ == "__main__":
    main()
