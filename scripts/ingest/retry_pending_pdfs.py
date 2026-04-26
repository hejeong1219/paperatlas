#!/usr/bin/env python3
"""Look at all wiki/sources/*.md with pdf_status: pending and retry PDF download."""
import json
import re
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, "scripts/ingest")
from resolve_pdf import resolve_and_download

def parse_fm(text):
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 4)
    if end < 0: return {}
    out = {}
    for line in text[4:end].split("\n"):
        m = re.match(r"^([a-zA-Z_]+)\s*:\s*(.+)$", line.strip())
        if m: out[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return out

def main():
    sources = Path("wiki/sources")
    pdf_dir = Path("raw/inbox/papers")
    pending = []
    for f in sources.glob("*.md"):
        if f.stem == "index": continue
        text = f.read_text()
        if "pdf_status: pending" not in text: continue
        fm = parse_fm(text)
        ref = {
            "slug": f.stem,
            "title": fm.get("title", f.stem),
            "year": int(fm.get("year") or 0),
            "first_author_last": "",
            "authors_raw": fm.get("authors", ""),
            "doi": fm.get("doi"), "pmid": fm.get("pmid"), "pmcid": fm.get("pmcid"),
        }
        # Extract from slug if year missing
        m = re.match(r"^([a-z]+)-(\d{4})-", f.stem)
        if m:
            ref["first_author_last"] = m.group(1)
            ref["year"] = int(m.group(2))
        # Extract title from heading if missing
        if ref["title"] == f.stem:
            m2 = re.search(r"^# (.+)$", text, re.MULTILINE)
            if m2: ref["title"] = m2.group(1).strip()
        pending.append((f, ref))
    print(f"Pending: {len(pending)}", file=sys.stderr)
    
    ok = 0
    def _retry(item):
        f, ref = item
        try:
            return f, ref, resolve_and_download(ref, pdf_dir)
        except Exception as e:
            return f, ref, {"slug": ref["slug"], "downloaded": False, "exc": str(e)}
    
    with ThreadPoolExecutor(max_workers=8) as ex:
        futures = {ex.submit(_retry, item): item for item in pending}
        for i, fut in enumerate(as_completed(futures)):
            f, ref, res = fut.result()
            if res.get("downloaded"):
                ok += 1
                # Update page: replace pdf_status: pending with pdf: path
                text = f.read_text()
                text = text.replace("pdf_status: pending",
                                    f'pdf: "raw/inbox/papers/{ref["slug"]}.pdf"')
                f.write_text(text)
            if i % 20 == 0:
                print(f"  [{i+1}/{len(pending)}] downloaded={ok}", file=sys.stderr)
    print(f"Total downloaded: {ok}/{len(pending)}", file=sys.stderr)

if __name__ == "__main__":
    main()
