#!/usr/bin/env python3
"""KU campus IP-based PDF download for paywalled papers.

For each pending paper with a DOI, fetch the publisher landing page directly
(via doi.org), parse `citation_pdf_url` (most publishers expose this), and
download the PDF using the user's browser cookies (loaded from cookies.txt).
"""
import argparse
import http.cookiejar as cj_module
import re
import sys
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"


def load_cookies(path):
    cj = cj_module.MozillaCookieJar(str(path))
    cj.load(ignore_discard=True, ignore_expires=True)
    return cj


def make_opener(cj):
    op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    op.addheaders = [
        ("User-Agent", UA),
        ("Accept", "text/html,application/xhtml+xml,application/xml,application/pdf,*/*"),
        ("Accept-Language", "en-US,en;q=0.9,ko;q=0.8"),
    ]
    return op


def fetch(opener, url, timeout=60):
    try:
        with opener.open(url, timeout=timeout) as r:
            return r.read(), r.headers.get("Content-Type", ""), r.url
    except Exception as e:
        return None, str(e)[:200], url


def extract_pdf_urls(html, base_url):
    candidates = []
    # 1. citation_pdf_url meta (most publishers)
    for m in re.finditer(r'<meta\s+[^>]*name="citation_pdf_url"[^>]*content="([^"]+)"', html, re.I):
        candidates.append(m.group(1))
    for m in re.finditer(r'<meta\s+[^>]*content="([^"]+)"[^>]*name="citation_pdf_url"', html, re.I):
        candidates.append(m.group(1))
    # 2. alternate type=application/pdf
    for m in re.finditer(r'<link[^>]+type="application/pdf"[^>]+href="([^"]+)"', html, re.I):
        candidates.append(m.group(1))
    # 3. AACR / Cell Press style
    for m in re.finditer(r'href="(/(?:doi/)?(?:pdf|reader|article-pdf)/[^"]+)"', html):
        candidates.append(m.group(1))
    # 4. ScienceDirect (Cell Press)
    for m in re.finditer(r'data-href="([^"]+\.pdf[^"]*)"', html):
        candidates.append(m.group(1))
    for m in re.finditer(r'href="(https?://[^"]+\.pdf[^"]*)"', html):
        candidates.append(m.group(1))
    # de-dup, normalize
    seen = set(); out = []
    from urllib.parse import urljoin
    for c in candidates:
        if "supplement" in c.lower() or "_supp" in c.lower(): continue
        if c.startswith("//"): c = "https:" + c
        elif not c.startswith("http"):
            c = urljoin(base_url, c)
        if c in seen: continue
        seen.add(c); out.append(c)
    return out


def try_save_pdf(data, out_path):
    if not data or len(data) < 5000: return False
    if data[:4] != b"%PDF": return False
    out_path.write_bytes(data)
    return True


def download_via_doi(opener, doi, out_path):
    if not doi: return False, "no doi"
    url = "https://doi.org/" + urllib.parse.quote(doi, safe="/")
    data, ctype, final_url = fetch(opener, url, timeout=90)
    if data is None:
        return False, f"doi err: {ctype[:60]}"

    # immediate PDF?
    if data[:4] == b"%PDF":
        if try_save_pdf(data, out_path):
            return True, "doi-direct"
        return False, "small pdf"

    try:
        html = data.decode("utf-8", errors="ignore")
    except Exception:
        return False, "decode err"

    pdf_urls = extract_pdf_urls(html, final_url)
    if not pdf_urls:
        return False, f"no pdf url ({len(html)//1000}KB landing)"

    for pdf_url in pdf_urls[:5]:
        d2, ct2, fu2 = fetch(opener, pdf_url, timeout=120)
        if d2 and try_save_pdf(d2, out_path):
            return True, pdf_url[:80]
    return False, f"PDF urls failed (tried {min(5,len(pdf_urls))})"


def parse_pmid_doi(text):
    pmid = doi = None
    m = re.search(r'^pmid:\s*"?(\d+)"?', text, re.MULTILINE)
    if m: pmid = m.group(1)
    m = re.search(r'^doi:\s*"?([^"\n]+)"?', text, re.MULTILINE)
    if m: doi = m.group(1).strip().rstrip('"').strip()
    return pmid, doi


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cookies", default=".cookies/oca.cookies.txt")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    cj = load_cookies(args.cookies)
    print(f"Loaded {sum(1 for _ in cj)} cookies", file=sys.stderr)

    sources = Path("wiki/sources")
    pdf_dir = Path("raw/inbox/papers")
    pdf_dir.mkdir(parents=True, exist_ok=True)

    targets = []
    for f in sorted(sources.glob("*.md")):
        if f.stem == "index": continue
        text = f.read_text()
        if "pdf_status: pending" not in text: continue
        pmid, doi = parse_pmid_doi(text)
        if not doi: continue
        out = pdf_dir / (f.stem + ".pdf")
        if out.exists() and out.stat().st_size > 5000: continue
        targets.append((f, doi, out))
    print(f"Pending pages with DOI: {len(targets)}", file=sys.stderr)
    if args.limit: targets = targets[:args.limit]

    ok = 0
    def worker(item):
        f, doi, out = item
        opener = make_opener(cj)
        return (f, doi, out, *download_via_doi(opener, doi, out))

    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futures = [ex.submit(worker, t) for t in targets]
        for i, fut in enumerate(as_completed(futures)):
            f, doi, out, success, msg = fut.result()
            if success:
                ok += 1
                # patch page
                text = f.read_text()
                if "pdf_status: pending" in text:
                    text = text.replace("pdf_status: pending",
                                        f'pdf: "raw/inbox/papers/{f.stem}.pdf"')
                    f.write_text(text)
            if success or i % 25 == 0:
                tag = "OK " if success else "PEND"
                print(f"  [{i+1}/{len(targets)}] {tag} {f.stem[:48]:50} | {msg[:60]}", file=sys.stderr)

    print(f"\nDownloaded {ok}/{len(targets)} via KU campus access", file=sys.stderr)


if __name__ == "__main__":
    main()
