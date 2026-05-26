#!/usr/bin/env python3
"""Bulk-ingest 100 local PDFs for drug-response proteomics/phosphoproteomics.

This is an auditable batch ingest, not a claim of manual full-text deep reading.
It extracts local PDF text, scores relevance, updates source pages with a
batch-ingest status section, and writes a durable 100-row tracking page.
"""
from __future__ import annotations

import datetime as dt
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE_DIR = ROOT / "wiki/sources"
PDF_DIR = ROOT / "raw/inbox/papers"
OUT_PAGE = ROOT / "wiki/analyses/drug-response-phospho-global-100-bulk-ingest.md"
INDEX = ROOT / "wiki/_meta/index.md"
LOG = ROOT / "wiki/_meta/log.md"


TERMS = {
    "strong": [
        "phosphoproteom", "proteogenom", "global proteom", "proteomic",
        "phosphosite", "phosphopeptide", "kinase", "ksea", "ptm",
    ],
    "response": [
        "drug response", "drug resistance", "treatment response",
        "therapy resistance", "chemoresistance", "resistance",
        "sensitivity", "responder", "non-responder", "nonresponder",
        "inhibitor", "chemotherapy", "immunotherapy", "targeted therapy",
        "osimertinib", "sunitinib", "cisplatin", "paclitaxel",
        "cdk", "kras", "egfr", "parp", "aurkb", "mtor",
    ],
    "human_cancer": [
        "cancer", "tumor", "tumour", "carcinoma", "glioblastoma",
        "leukemia", "lymphoma", "melanoma", "sarcoma", "patient",
        "patients", "cohort", "organoid",
    ],
}

LOW_PRIORITY = [
    "review", "perspective", "database", "web-based", "protocol",
    "computational methods", "machine learning", "deep learning",
    "non-cancer", "mouse", "feline",
]


def parse_frontmatter(text: str) -> tuple[dict[str, str], str, str]:
    if not text.startswith("---"):
        return {}, "", text
    end = text.find("\n---", 4)
    if end < 0:
        return {}, "", text
    raw = text[: end + 4]
    body = text[end + 5 :]
    fm: dict[str, str] = {}
    for line in raw.splitlines()[1:]:
        m = re.match(r"^([A-Za-z0-9_]+):\s*(.+?)\s*$", line)
        if m:
            fm[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return fm, raw, body


def pdf_from_fm(fm: dict[str, str], slug: str) -> Path | None:
    raw = fm.get("pdf")
    if raw:
        p = ROOT / raw
        if p.exists() and p.suffix.lower() == ".pdf" and p.stat().st_size > 5000:
            return p
    p = PDF_DIR / f"{slug}.pdf"
    if p.exists() and p.stat().st_size > 5000:
        return p
    return None


def extract_pdf_text(pdf: Path) -> str:
    res = subprocess.run(
        ["pdftotext", "-f", "1", "-l", "5", "-layout", str(pdf), "-"],
        capture_output=True,
        text=True,
        timeout=12,
    )
    return res.stdout or ""


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def hit_count(hay: str, terms: list[str]) -> int:
    h = hay.lower()
    return sum(h.count(t.lower()) for t in terms)


def first_sentences(text: str, terms: list[str], limit: int = 5) -> list[str]:
    text = clean(text[:45000])
    sents = re.split(r"(?<=[.!?])\s+", text)
    out: list[str] = []
    seen: set[str] = set()
    for sent in sents:
        low = sent.lower()
        if any(t.lower() in low for t in terms):
            sent = sent.strip()
            if len(sent) > 330:
                sent = sent[:327] + "..."
            key = sent[:80]
            if key not in seen and len(sent) > 40:
                out.append(sent)
                seen.add(key)
        if len(out) >= limit:
            break
    return out


def score_page(slug: str, fm: dict[str, str], page_text: str, pdf_text: str) -> int:
    title = fm.get("title", slug)
    journal = fm.get("journal", "")
    combined = " ".join([title, journal, page_text[:8000], pdf_text[:30000]]).lower()
    score = 0
    score += hit_count(combined, TERMS["strong"]) * 8
    score += hit_count(combined, TERMS["response"]) * 5
    score += hit_count(combined, TERMS["human_cancer"]) * 3
    if "nature" in journal.lower() or "science" in journal.lower() or "cell" in journal.lower():
        score += 30
    if "cancer discovery" in journal.lower() or "cancer cell" in journal.lower():
        score += 25
    if "proteogenomic" in title.lower() or "phosphoproteomic" in title.lower():
        score += 40
    if any(x in combined for x in LOW_PRIORITY):
        score -= 20
    if "wrong-pdf" in page_text:
        score -= 1000
    return score


def replace_or_insert_section(page_text: str, section: str) -> str:
    heading = "## Batch PDF Ingest Status"
    pat = re.compile(rf"\n{re.escape(heading)}\n.*?(?=\n## |\Z)", re.S)
    if pat.search(page_text):
        return pat.sub("\n" + section.rstrip() + "\n", page_text)
    marker = "\n## Key Points\n"
    if marker in page_text:
        return page_text.replace(marker, "\n" + section.rstrip() + "\n\n## Key Points\n", 1)
    return page_text.rstrip() + "\n\n" + section.rstrip() + "\n"


def ensure_fm_status(page_text: str, status: str) -> str:
    fm, raw, body = parse_frontmatter(page_text)
    if not raw:
        return page_text
    if "batch_ingest_status:" in raw:
        raw2 = re.sub(r"batch_ingest_status:.*", f"batch_ingest_status: {status}", raw)
    else:
        raw2 = raw.replace("\n---", f"\nbatch_ingest_status: {status}\n---", 1)
    if "batch_ingested_on:" in raw2:
        raw2 = re.sub(r"batch_ingested_on:.*", f"batch_ingested_on: {TODAY}", raw2)
    else:
        raw2 = raw2.replace("\n---", f"\nbatch_ingested_on: {TODAY}\n---", 1)
    return raw2 + "\n" + body


def make_section(pdf: Path, pdf_text: str, snippets: list[str]) -> str:
    char_count = len(pdf_text)
    status = "pdf-text-extracted"
    lines = [
        "## Batch PDF Ingest Status",
        "",
        f"- Status: `{status}` on {TODAY}.",
        f"- Local PDF: `{pdf.relative_to(ROOT)}`.",
        f"- Extracted text length: {char_count:,} characters.",
        "- Scope note: automated local-PDF text ingest for the 100-paper drug-response/phospho-global batch; not yet a manual full-text deep-dive.",
        "- Evidence boundary: downstream scientific claims should use this page only after source-specific Key Points are manually promoted or rechecked against the local PDF.",
        "- High-signal PDF snippets:",
    ]
    if snippets:
        lines.extend(f"  - {s}" for s in snippets)
    else:
        lines.append("  - No concise response/proteomics sentence was confidently extracted from the main PDF text.")
    return "\n".join(lines)


def update_index() -> None:
    link = "- [Drug Response Phospho-Global 100-PDF Bulk Ingest](../analyses/drug-response-phospho-global-100-bulk-ingest.md) - Batch tracker for 100 local PDFs selected for global proteome/phosphoproteome anticancer response and resistance ingest."
    text = INDEX.read_text()
    if "drug-response-phospho-global-100-bulk-ingest.md" not in text:
        text = text.replace("## Analyses\n", "## Analyses\n\n" + link + "\n", 1)
        INDEX.write_text(text)


def update_log(n: int, new_downloads: int) -> None:
    entry = f"""
## [{TODAY}] ingest | drug-response phospho-global 100-PDF batch

- Retried pending PDF downloads before bulk ingest; additional scripted downloads were limited by paywall/PMC challenge behavior ({new_downloads} newly resolved in this pass).
- Selected {n} local PDFs for the drug-response/global-proteome/phosphoproteome corpus and added `Batch PDF Ingest Status` sections with extracted-text provenance to each source page.
- Created `wiki/analyses/drug-response-phospho-global-100-bulk-ingest.md` as the durable 100-row batch tracker.
- These rows are `pdf-text-extracted`, not automatically `full-text-read`; manual deep-dive promotion remains required before using detailed scientific claims in synthesis.
"""
    LOG.write_text(LOG.read_text().rstrip() + "\n\n" + entry.strip() + "\n")


TODAY = dt.date.today().isoformat()


def main() -> None:
    prescored = []
    for page in SOURCE_DIR.glob("*.md"):
        if page.stem == "index":
            continue
        text = page.read_text()
        fm, _, _ = parse_frontmatter(text)
        pdf = pdf_from_fm(fm, page.stem)
        if not pdf:
            continue
        title = fm.get("title", page.stem)
        journal = fm.get("journal", "")
        combined = " ".join([page.stem, title, journal, text[:12000]]).lower()
        pre = 0
        pre += hit_count(combined, TERMS["strong"]) * 10
        pre += hit_count(combined, TERMS["response"]) * 7
        pre += hit_count(combined, TERMS["human_cancer"]) * 3
        if "proteogenomic" in title.lower() or "phosphoproteomic" in title.lower():
            pre += 50
        if "drug-response-phospho-global-100-corpus-queue" in text:
            pre += 30
        if any(x in combined for x in LOW_PRIORITY):
            pre -= 15
        if "wrong-pdf" in text:
            pre -= 1000
        if pre <= 0:
            continue
        prescored.append((pre, page, fm, pdf, text))

    prescored.sort(key=lambda x: x[0], reverse=True)

    candidates = []
    print(f"Prescored local-PDF pages: {len(prescored)}", file=sys.stderr)
    for i, (pre, page, fm, pdf, page_text) in enumerate(prescored[:110], start=1):
        if i == 1 or i % 10 == 0:
            print(f"  extracting {i}/110: {page.stem}", file=sys.stderr)
        try:
            pdf_text = extract_pdf_text(pdf)
        except Exception:
            continue
        if len(pdf_text.strip()) < 1000:
            continue
        score = pre + score_page(page.stem, fm, page_text, pdf_text)
        candidates.append((score, page, fm, pdf, pdf_text))

    candidates.sort(key=lambda x: x[0], reverse=True)
    selected = candidates[:100]

    rows = []
    for rank, (score, page, fm, pdf, pdf_text) in enumerate(selected, start=1):
        snippets = first_sentences(
            pdf_text,
            TERMS["strong"] + TERMS["response"],
            limit=5,
        )
        section = make_section(pdf, pdf_text, snippets)
        updated = ensure_fm_status(page.read_text(), "pdf-text-extracted")
        updated = replace_or_insert_section(updated, section)
        page.write_text(updated)
        rows.append({
            "rank": rank,
            "score": score,
            "slug": page.stem,
            "title": fm.get("title", page.stem),
            "year": fm.get("year", ""),
            "journal": fm.get("journal", ""),
            "pdf": str(pdf.relative_to(ROOT)),
            "chars": len(pdf_text),
        })

    lines = [
        "---",
        'title: "Drug Response Phospho-Global 100-PDF Bulk Ingest"',
        "tags:",
        "  - drug-response",
        "  - phosphoproteomics",
        "  - global-proteomics",
        "  - batch-ingest",
        "---",
        "",
        "# Drug Response Phospho-Global 100-PDF Bulk Ingest",
        "",
        f"Created on {TODAY}. This page tracks 100 local PDFs selected for the anticancer drug-response, resistance, global proteome, phosphoproteome, and kinase-signaling corpus.",
        "",
        "## Key Points",
        "",
        "- Status `pdf-text-extracted` means the local PDF was opened with `pdftotext`, source pages were marked with extracted-text provenance, and high-signal snippets were stored.",
        "- This is not the same as `full-text-read`; detailed scientific claims still require source-specific manual deep-dive before synthesis.",
        "- Wrong-PDF pages were excluded by score penalty.",
        "- The batch uses local PDFs only; web pages were not used as scientific evidence.",
        "",
        "## 100-PDF Table",
        "",
        "| # | Source | Year | Journal | Score | Extracted chars | Local PDF |",
        "| --- | --- | --- | --- | ---: | ---: | --- |",
    ]
    for row in rows:
        lines.append(
            f"| {row['rank']} | [{row['slug']}](../sources/{row['slug']}.md) | {row['year']} | {row['journal']} | {row['score']} | {row['chars']} | `{row['pdf']}` |"
        )
    lines.extend([
        "",
        "## Connections",
        "",
        "- [Drug Response Phospho-Global Proteomics Corpus Queue](drug-response-phospho-global-100-corpus-queue.md)",
        "- [Drug Response Proof-of-Concept with Global Proteome, Phosphoproteome, and Somatic SNV](drug-response-poc-global-phospho-somatic-snv.md)",
        "- [Cancer Multiomics Literature Monitor](../topics/cancer-multiomics-literature.md)",
        "- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)",
    ])
    OUT_PAGE.write_text("\n".join(lines) + "\n")
    update_index()
    update_log(len(rows), 1)
    print(f"Selected and batch-ingested {len(rows)} PDFs")
    print(OUT_PAGE)


if __name__ == "__main__":
    main()
