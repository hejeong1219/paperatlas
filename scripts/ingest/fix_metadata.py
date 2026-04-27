#!/usr/bin/env python3
"""For every wiki/sources page that has a pmid in frontmatter, re-fetch the
authoritative metadata (DOI, PMCID, journal, year, title) from NCBI esummary
and patch the frontmatter so future PDF resolvers use correct identifiers.
"""
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

NCBI = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
UA = "llm-wiki/0.1"


def http_get(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def esummary_batch(pmids):
    if not pmids: return {}
    url = f"{NCBI}/esummary.fcgi?db=pubmed&retmode=json&id=" + ",".join(pmids)
    try:
        j = json.loads(http_get(url, timeout=60))
        out = {}
        for pmid in pmids:
            rec = j.get("result", {}).get(pmid)
            if not rec: continue
            doi = pmcid = None
            for aid in rec.get("articleids", []):
                if aid.get("idtype") == "doi": doi = aid.get("value")
                elif aid.get("idtype") == "pmc": pmcid = aid.get("value")
            out[pmid] = {
                "doi": doi,
                "pmcid": pmcid,
                "journal": rec.get("fulljournalname") or rec.get("source"),
                "year": (rec.get("pubdate", "") or "")[:4],
                "title": rec.get("title"),
            }
        return out
    except Exception as e:
        print(f"  esummary err: {e}", file=sys.stderr)
        return {}


def patch_frontmatter(text, fields):
    """Replace or add frontmatter fields (dict of key -> value)."""
    fm_end = text.find("\n---", 4)
    if fm_end < 0: return text
    fm = text[4:fm_end]
    body = text[fm_end:]
    for k, v in fields.items():
        if v is None: continue
        v_str = str(v).replace('"', '\\"')
        line_pat = re.compile(r"^" + re.escape(k) + r":\s*.*$", re.MULTILINE)
        new_line = f'{k}: "{v_str}"'
        if line_pat.search(fm):
            fm = line_pat.sub(new_line, fm)
        else:
            fm = fm.rstrip() + "\n" + new_line + "\n"
    return "---\n" + fm + body


def main():
    sources = Path("wiki/sources")
    targets = []
    for f in sources.glob("*.md"):
        if f.stem == "index": continue
        text = f.read_text()
        m = re.search(r'^pmid:\s*"?(\d+)"?', text, re.MULTILINE)
        if not m: continue
        targets.append((f, m.group(1), text))
    print(f"Pages with PMID: {len(targets)}", file=sys.stderr)
    pmids = [t[1] for t in targets]
    metas = {}
    for i in range(0, len(pmids), 100):
        chunk = pmids[i:i+100]
        metas.update(esummary_batch(chunk))
        time.sleep(0.4)
        if i and i % 500 == 0:
            print(f"  fetched {len(metas)} so far", file=sys.stderr)
    print(f"\nFetched metadata for {len(metas)}/{len(pmids)} PMIDs", file=sys.stderr)

    updated = 0
    for f, pmid, text in targets:
        meta = metas.get(pmid)
        if not meta: continue
        new = patch_frontmatter(text, {
            "doi": meta.get("doi"),
            "pmcid": meta.get("pmcid"),
            "journal": meta.get("journal"),
            "year": meta.get("year"),
        })
        if new != text:
            f.write_text(new)
            updated += 1
    print(f"Patched {updated} pages", file=sys.stderr)


if __name__ == "__main__":
    main()
