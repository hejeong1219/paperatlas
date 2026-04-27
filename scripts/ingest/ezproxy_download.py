#!/usr/bin/env python3
"""Use Korea Univ EZproxy + browser cookies to fetch paywalled PDFs.

For each pending paper with a DOI, try:
  1. EZproxy URL = https://oca.korea.ac.kr/link.n2s?url=https://doi.org/{DOI}
  2. Follow redirects under cookie session.
  3. If response is PDF, save it.
  4. Otherwise parse landing page for citation_pdf_url meta tag, fetch that.
"""
import argparse
import http.cookiejar as cj_module
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
EZPROXY = "https://oca.korea.ac.kr/link.n2s?url="


def load_cookies(path):
    cj = cj_module.MozillaCookieJar(str(path))
    cj.load(ignore_discard=True, ignore_expires=True)
    return cj


def make_opener(cj):
    handler = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(handler)
    opener.addheaders = [
        ("User-Agent", UA),
        ("Accept", "text/html,application/xhtml+xml,application/xml,application/pdf,*/*"),
        ("Accept-Language", "en-US,en;q=0.9,ko;q=0.8"),
    ]
    return opener


def fetch(opener, url, timeout=60):
    try:
        with opener.open(url, timeout=timeout) as r:
            data = r.read()
            ctype = r.headers.get("Content-Type", "")
            return data, ctype, r.url
    except Exception as e:
        return None, str(e), url


def try_ezproxy_pdf(opener, doi, out_path):
    if not doi:
        return False, "no doi"
    ez_url = EZPROXY + urllib.parse.quote("https://doi.org/" + doi, safe=":/?&=#@")
    data, ctype, final_url = fetch(opener, ez_url, timeout=90)
    if data is None:
        return False, f"ezproxy fetch err: {ctype[:80]}"

    # if direct PDF
    if data[:4] == b"%PDF" and len(data) > 5000:
        out_path.write_bytes(data)
        return True, ez_url

    # parse HTML for citation_pdf_url
    try:
        html = data.decode("utf-8", errors="ignore")
    except Exception:
        return False, "decode err"

    candidates = []
    for pat in [
        r'<meta\s+name="citation_pdf_url"\s+content="([^"]+)"',
        r'<link\s+rel="alternate"[^>]*type="application/pdf"[^>]*href="([^"]+)"',
        r'<a[^>]+class="[^"]*(?:pdf|download)[^"]*"[^>]+href="([^"]+\.pdf[^"]*)"',
        r'href="(https?://[^"]+\.pdf[^"]*)"',
        r'href="(/[^"]+\.pdf[^"]*)"',
    ]:
        for m in re.finditer(pat, html, re.IGNORECASE):
            url = m.group(1)
            if "supplement" in url.lower() or "supp" in url.lower(): continue
            candidates.append(url)
    # also AACR / Cell Press patterns
    for m in re.finditer(r'href="([^"]+pdf-?(?:url|download)[^"]*)"', html, re.IGNORECASE):
        candidates.append(m.group(1))

    seen = set()
    candidates = [c for c in candidates if not (c in seen or seen.add(c))]

    for cand in candidates[:8]:
        if not cand.startswith("http"):
            if cand.startswith("//"):
                cand = "https:" + cand
            else:
                # absolute path -> use final_url's host
                from urllib.parse import urljoin
                cand = urljoin(final_url, cand)
        # if not already EZproxied and is paywalled domain, wrap with EZproxy
        if "oca.korea.ac.kr" not in cand and any(d in cand for d in (
            "aacrjournals.org", "sciencedirect.com", "cell.com",
            "wiley.com", "academic.oup.com", "nature.com",
            "ahajournals.org", "annualreviews.org", "rupress.org",
            "ascopubs.org", "jci.org", "biomedcentral.com",
        )):
            wrapped = EZPROXY + urllib.parse.quote(cand, safe=":/?&=#@")
        else:
            wrapped = cand
        d2, ct2, _ = fetch(opener, wrapped, timeout=90)
        if d2 and d2[:4] == b"%PDF" and len(d2) > 5000:
            out_path.write_bytes(d2)
            return True, wrapped
    return False, f"no PDF on landing page ({len(candidates)} candidates tried)"


def parse_pmid_doi(text):
    pmid = None
    doi = None
    m = re.search(r'^pmid:\s*"?(\d+)"?', text, re.MULTILINE)
    if m: pmid = m.group(1)
    m = re.search(r'^doi:\s*"?([^"\n]+)"?', text, re.MULTILINE)
    if m: doi = m.group(1).strip().rstrip('"').strip()
    return pmid, doi


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cookies", default=".cookies/oca.cookies.txt")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--limit", type=int, default=0, help="0 = no limit")
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
    if args.limit:
        targets = targets[:args.limit]

    ok = 0
    def worker(item):
        f, doi, out = item
        opener = make_opener(cj)
        success, msg = try_ezproxy_pdf(opener, doi, out)
        return f, doi, success, msg

    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futures = [ex.submit(worker, t) for t in targets]
        for i, fut in enumerate(as_completed(futures)):
            f, doi, success, msg = fut.result()
            if success: ok += 1
            if i % 10 == 0 or success:
                tag = "OK " if success else "PEND"
                print(f"  [{i+1}/{len(targets)}] {tag} {f.stem[:48]:50} | {msg[:60]}", file=sys.stderr)
            # update page if downloaded
            if success:
                text = f.read_text()
                if "pdf_status: pending" in text:
                    text = text.replace("pdf_status: pending",
                                        f'pdf: "raw/inbox/papers/{f.stem}.pdf"')
                    f.write_text(text)

    print(f"\nDownloaded {ok}/{len(targets)} via EZproxy+cookies", file=sys.stderr)


if __name__ == "__main__":
    main()
