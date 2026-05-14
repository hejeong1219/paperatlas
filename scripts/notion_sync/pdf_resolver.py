#!/usr/bin/env python3
"""DOI-first PDF wrapper for Notion-sync flow.

Wraps scripts/ingest/resolve_pdf.py (which requires PMID via title search)
with a DOI-seeded fallback chain, then KU EZproxy fallback. Returns the
same shape as resolve_and_download() with `tried` listing every attempt.
"""
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
INGEST = REPO / "scripts/ingest"
sys.path.insert(0, str(INGEST))

from resolve_pdf import (  # noqa: E402
    resolve_and_download,
    try_unpaywall,
    try_doi_direct,
    try_elsevier,
    try_springer,
)
from ezproxy_download import (  # noqa: E402
    load_cookies,
    make_opener,
    try_ezproxy_pdf,
)


def resolve_with_doi(ref, out_dir):
    """Resolve PDF for a DOI-only ref (PMID may not exist).

    ref keys (required): slug, title, year, first_author_last, doi
    ref keys (optional): pmcid, journal

    Returns dict shaped like resolve_and_download() output:
      {slug, pmid, pmcid, doi, journal, downloaded, pdf_path, tried, via}
    """
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / (ref["slug"] + ".pdf")

    # 1) Existing resolve_and_download — handles already-on-disk + PMID hit case.
    result = resolve_and_download(ref, out_dir)
    if result.get("downloaded"):
        return result

    # 2) PMID lookup may have failed, but ref["doi"] is known — seed manual chain.
    doi = ref["doi"]
    journal = result.get("journal") or ref.get("journal")
    fallback_chain = [
        ("unpaywall-doi", lambda: try_unpaywall(doi, out_path)),
        ("doi-direct-doi", lambda: try_doi_direct(doi, journal, out_path)),
        ("elsevier-doi", lambda: try_elsevier(doi, out_path)),
        ("springer-doi", lambda: try_springer(doi, out_path)),
    ]
    for name, fn in fallback_chain:
        try:
            ok, msg = fn()
        except Exception as e:
            ok, msg = False, f"exc: {e}"
        result["tried"].append({"src": name, "ok": ok, "msg": msg})
        if ok and out_path.exists() and out_path.stat().st_size > 5000:
            result["downloaded"] = True
            result["pdf_path"] = str(out_path)
            result["via"] = f"{name}: {msg}"
            return result

    # 3) KU EZproxy fallback (if cookies present).
    cookies = REPO / ".cookies/oca.cookies.txt"
    if cookies.exists():
        try:
            opener = make_opener(load_cookies(cookies))
            ok, info = try_ezproxy_pdf(opener, doi, out_path)
        except Exception as e:
            ok, info = False, f"ezproxy exc: {e}"
        result["tried"].append({"src": "ezproxy", "ok": ok, "msg": info})
        if ok and out_path.exists() and out_path.stat().st_size > 5000:
            result["downloaded"] = True
            result["pdf_path"] = str(out_path)
            result["via"] = f"ezproxy: {info}"
    else:
        result["tried"].append({"src": "ezproxy", "ok": False, "msg": "no cookies file"})

    return result


if __name__ == "__main__":
    # Smoke test: usage: pdf_resolver.py <doi> <slug> <first_author_last> <year> <title> <out_dir>
    import json
    if len(sys.argv) != 7:
        print("usage: pdf_resolver.py <doi> <slug> <first_author> <year> <title> <out_dir>",
              file=sys.stderr)
        sys.exit(1)
    ref = {
        "doi": sys.argv[1],
        "slug": sys.argv[2],
        "first_author_last": sys.argv[3],
        "year": int(sys.argv[4]),
        "title": sys.argv[5],
    }
    r = resolve_with_doi(ref, Path(sys.argv[6]))
    json.dump(r, sys.stdout, indent=2, default=str)
    sys.stdout.write("\n")
