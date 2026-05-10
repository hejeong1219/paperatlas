#!/usr/bin/env python3
"""Fallback PDF downloader for stubs whose KU/DOI flow failed.

Tries, in order:
  1. arxiv_id frontmatter -> https://arxiv.org/pdf/<id>.pdf
  2. url frontmatter (if it ends with .pdf or looks like a publisher PDF)
  3. bioRxiv DOI -> https://www.biorxiv.org/content/<doi>vN.full.pdf for N=1..3
  4. medRxiv DOI -> https://www.medrxiv.org/content/<doi>vN.full.pdf for N=1..3

Reads --include-file (one slug per line) like ku_download.py. Patches the
source page's `pdf_status: pending` to `pdf: "raw/inbox/papers/<slug>.pdf"`
on success. Uses cookies if --cookies provided (helps for paywalled).
"""
import argparse
import http.cookiejar as cj_module
import re
import sys
import urllib.request
from pathlib import Path

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"


def make_opener(cookies_path=None):
    handlers = []
    if cookies_path and Path(cookies_path).exists():
        cj = cj_module.MozillaCookieJar(cookies_path)
        cj.load(ignore_discard=True, ignore_expires=True)
        handlers.append(urllib.request.HTTPCookieProcessor(cj))
    op = urllib.request.build_opener(*handlers)
    op.addheaders = [
        ("User-Agent", UA),
        ("Accept", "application/pdf,*/*"),
    ]
    return op


def fetch(opener, url, timeout=120):
    try:
        with opener.open(url, timeout=timeout) as r:
            return r.read(), r.headers.get("Content-Type", "")
    except Exception as e:
        return None, f"err:{type(e).__name__}:{str(e)[:80]}"


def is_pdf(data):
    return data is not None and len(data) > 5000 and data[:4] == b"%PDF"


def parse_frontmatter_field(text, key):
    m = re.search(rf'^{re.escape(key)}:\s*"?([^"\n]+)"?', text, re.MULTILINE)
    return m.group(1).strip().rstrip('"').strip() if m else None


def candidate_urls(stub_text):
    out = []
    arxiv_id = parse_frontmatter_field(stub_text, "arxiv_id")
    if arxiv_id:
        out.append(("arxiv", f"https://arxiv.org/pdf/{arxiv_id}.pdf"))
    doi = parse_frontmatter_field(stub_text, "doi")
    if doi:
        if doi.startswith("10.1101/"):
            for v in range(1, 4):
                out.append((f"biorxiv-v{v}", f"https://www.biorxiv.org/content/{doi}v{v}.full.pdf"))
        elif doi.startswith("10.64898/"):
            for v in range(1, 4):
                out.append((f"biorxiv64898-v{v}", f"https://www.biorxiv.org/content/{doi}v{v}.full.pdf"))
                out.append((f"medrxiv64898-v{v}", f"https://www.medrxiv.org/content/{doi}v{v}.full.pdf"))
    url = parse_frontmatter_field(stub_text, "url")
    if url and (url.endswith(".pdf") or "/pdf/" in url) and not any(u == url for _, u in out):
        out.append(("frontmatter-url", url))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--include-file", required=True)
    ap.add_argument("--cookies", default=".cookies/oca.cookies.txt")
    args = ap.parse_args()

    slugs = [s.strip() for s in Path(args.include_file).read_text().splitlines() if s.strip() and not s.startswith("#")]
    sources = Path("wiki/sources")
    pdf_dir = Path("raw/inbox/papers")
    pdf_dir.mkdir(parents=True, exist_ok=True)

    opener = make_opener(args.cookies)

    ok = 0
    for slug in slugs:
        md = sources / f"{slug}.md"
        if not md.exists():
            print(f"  SKIP missing stub: {slug}")
            continue
        out_pdf = pdf_dir / f"{slug}.pdf"
        if out_pdf.exists() and out_pdf.stat().st_size > 5000:
            print(f"  HAVE {slug}")
            continue
        text = md.read_text()
        cands = candidate_urls(text)
        if not cands:
            print(f"  NONE no candidate urls: {slug}")
            continue
        success = False
        for label, url in cands:
            data, msg = fetch(opener, url)
            if is_pdf(data):
                out_pdf.write_bytes(data)
                ntext = text.replace("pdf_status: pending",
                                     f'pdf: "raw/inbox/papers/{slug}.pdf"')
                md.write_text(ntext)
                print(f"  OK   [{label}] {slug} ({len(data)//1024}KB)")
                success = True
                ok += 1
                break
        if not success:
            tried = ", ".join(l for l, _ in cands)
            print(f"  PEND {slug}  (tried: {tried})")

    print(f"\nFallback: downloaded {ok}/{len(slugs)} new PDFs")


if __name__ == "__main__":
    main()
