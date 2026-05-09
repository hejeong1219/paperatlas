#!/usr/bin/env python3
"""Ingest locally downloaded extra multiomics/PTM PDFs into source notes.

This is intentionally conservative: it creates or updates source pages from
local PDFs only, labels method/database/tool papers separately, and emits a
JSON summary that can be reviewed before adding rows to the visualization.
"""
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ROWS_PATH = Path("/tmp/wiki_work/extra_downloaded_32.json")
OUT_SUMMARY = Path("/tmp/wiki_work/extra_downloaded_32_ingest_summary.json")
SOURCE_DIR = ROOT / "wiki/sources"


COUNT_PATTERNS = [
    ("protein", r"([0-9][0-9,]{2,})\s+(?:unique\s+)?(?:protein groups|proteins|protein)\b"),
    ("phospho", r"([0-9][0-9,]{2,})\s+(?:unique\s+)?(?:phosphorylation sites|phosphosites|phospho-sites|phosphopeptides|phosphoproteins|phosphorylated proteins)\b"),
    ("acetyl", r"([0-9][0-9,]{2,})\s+(?:unique\s+)?(?:acetylation sites|acetylsites|acetyl-sites|acetylated sites|acetylated peptides|acetylated proteins|lysine acetylation sites)\b"),
]


def yaml_string(value):
    value = "" if value is None else str(value)
    return '"' + value.replace('"', '\\"') + '"'


def yaml_list(items):
    if not items:
        return "[]"
    return "\n" + "\n".join(f"  - {yaml_string(x)}" for x in items)


def extract_text(pdf_path: Path) -> str:
    res = subprocess.run(
        ["pdftotext", "-layout", str(pdf_path), "-"],
        capture_output=True,
        text=True,
        timeout=120,
    )
    text = res.stdout
    for marker in ["\nReferences\n", "\nREFERENCES\n", "\nBibliography\n"]:
        idx = text.find(marker)
        if idx > 5000:
            text = text[:idx]
            break
    return text


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def sentence_hits(text: str, terms, limit=6):
    sentences = re.split(r"(?<=[.!?])\s+", clean(text))
    out = []
    for sentence in sentences:
        lower = sentence.lower()
        if any(term in lower for term in terms):
            if len(sentence) > 360:
                sentence = sentence[:357] + "..."
            out.append(sentence)
        if len(out) >= limit:
            break
    return out


def first_count(text: str, kind: str):
    for key, pat in COUNT_PATTERNS:
        if key != kind:
            continue
        m = re.search(pat, text, flags=re.I)
        if m:
            return int(m.group(1).replace(",", ""))
    return None


def classify(title: str, text: str):
    t = title.lower()
    l = text[:30000].lower()
    is_tool = any(x in t for x in ["web-based", "application", "platform", "tmt-integrator", "fragpipe", "sonication-assisted"])
    is_method = any(x in t for x in ["workflow", "assay", "extraction", "analysis of isobaric", "platform"])
    has_ms = any(x in l for x in ["mass spectrometry", "lc-ms", "lc-ms/ms", "orbitrap", "q exactive", "tmt", "itraq", "phosphoproteom", "acetylom"])
    has_ptm = any(x in l for x in ["phosphoproteom", "phosphorylation", "acetylom", "acetylation"])
    has_human_cancer = any(x in l for x in ["patient", "patients", "tumor", "tumour", "cancer", "carcinoma", "glioblastoma", "leukemia"])
    if is_tool:
        return "methods/tool", False
    if is_method:
        return "methods/workflow", has_ms and has_ptm and has_human_cancer
    if has_ms and has_ptm and has_human_cancer:
        if any(x in l for x in ["cell line", "cells treated", "xenograft"]):
            return "cell-line/xenograft perturbation", True
        return "tumor or pan-cancer study", True
    if has_ms and has_human_cancer:
        return "broader cancer proteomics", False
    return "out-of-scope or insufficient PDF evidence", False


def cancer_guess(title: str, text: str):
    hay = (title + " " + text[:5000]).lower()
    mapping = [
        ("breast", "Breast cancer"),
        ("colorectal", "Colorectal cancer"),
        ("colon", "Colorectal cancer"),
        ("glioblastoma", "Glioblastoma"),
        ("head and neck", "Head and neck squamous cell carcinoma"),
        ("hypopharyngeal", "Hypopharyngeal squamous cell carcinoma"),
        ("esophageal", "Esophageal squamous cell carcinoma"),
        ("cholangiocarcinoma", "Cholangiocarcinoma"),
        ("pancreatic", "Pancreatic cancer"),
        ("nasopharyngeal", "Nasopharyngeal carcinoma"),
        ("lung", "Lung cancer"),
        ("hepatocellular", "Hepatocellular carcinoma"),
        ("cervical", "Cervical cancer"),
    ]
    for key, label in mapping:
        if key in hay:
            return label
    if "pan-cancer" in hay:
        return "Pan-cancer"
    return "Human cancer / model"


def make_page(row, text, classification, include_in_quant):
    slug = row["slug"]
    title = row.get("title") or slug
    year = row.get("year") or ""
    journal = row.get("journal") or ""
    doi = row.get("doi") or ""
    pmid = row.get("pmid") or ""
    pmcid = row.get("pmcid") or ""
    pdf_path = row.get("pdf_path")
    protein = first_count(text, "protein")
    phospho = first_count(text, "phospho")
    acetyl = first_count(text, "acetyl")
    method_hits = sentence_hits(text, ["tmt", "itraq", "orbitrap", "q exactive", "lc-ms", "lc-ms/ms", "imac", "tio2", "fe-nta", "acetyl", "maxquant"], 8)
    count_hits = sentence_hits(text, ["identified", "quantified", "proteins", "phosphosites", "phosphopeptides", "acetylation sites", "acetylated"], 8)
    summary_hits = sentence_hits(text, ["proteogenomic", "proteomics", "phosphoproteomics", "acetylome", "multi-omics", "multiomics"], 4)
    tags = [
        "multiomics-proteomics-ptm-identification",
        "local-pdf-ingest",
        "cancer-proteomics",
    ]
    if "phospho" in text[:30000].lower():
        tags.append("phosphoproteomics")
    if "acetyl" in text[:30000].lower():
        tags.append("acetylomics")
    fm = [
        "---",
        f"title: {yaml_string(title)}",
        f"year: {yaml_string(year)}" if year else None,
        f"journal: {yaml_string(journal)}" if journal else None,
        f"doi: {yaml_string(doi)}" if doi else None,
        f"pmid: {yaml_string(pmid)}" if pmid else None,
        f"pmcid: {yaml_string(pmcid)}" if pmcid else None,
        f"paper_kind: {yaml_string(classification)}",
        f"pdf: {yaml_string(pdf_path)}",
        'topic: "multiomics-proteomics-ptm-identification"',
        "tags:" + yaml_list(tags),
        "themes:" + yaml_list(["multiomics-identification", "ptm-methodology"]),
        "---",
    ]
    fm = "\n".join(x for x in fm if x is not None)
    body = [
        f"# {title}",
        "",
        "## Summary",
        "",
        "Local-PDF ingest note for the cancer multiomics/PTM atlas. " + (summary_hits[0] if summary_hits else "The paper was ingested from a locally downloaded PDF and requires any final numerical claims to be checked against the source PDF or supplements."),
        "",
        "## Key Points",
        "",
        f"- Atlas classification: {classification}.",
        f"- Quantitative atlas row: {'candidate' if include_in_quant else 'not used as a direct quantitative study row unless manually promoted'}.",
        "- Claims in this page were extracted from the local PDF text; web pages were not used as evidence.",
        "",
        "## Multi-Omics Identification Extraction",
        "",
        f"- Cohort/scope: {cancer_guess(title, text)}; classification `{classification}`.",
        f"- Proteome count candidate: {protein if protein is not None else 'not confidently extracted from main PDF text'}.",
        f"- Phosphoproteome count candidate: {phospho if phospho is not None else 'not confidently extracted from main PDF text'}.",
        f"- Acetylome count candidate: {acetyl if acetyl is not None else 'not confidently extracted from main PDF text'}.",
        "- Method/instrument evidence from local PDF:",
    ]
    if method_hits:
        body.extend(f"  - {h}" for h in method_hits[:5])
    else:
        body.append("  - Method/instrument phrases were not confidently exposed in the extractable main PDF text.")
    body.extend([
        "- Count evidence snippets from local PDF:",
    ])
    if count_hits:
        body.extend(f"  - {h}" for h in count_hits[:5])
    else:
        body.append("  - Count phrases were not confidently exposed in the extractable main PDF text.")
    body.extend([
        "- Interpretation note: preserve the reported unit; do not convert protein groups, phosphosites, phosphopeptides, acetylsites, and phosphoproteins into a false common metric.",
        "",
        "## Connections",
        "",
        "- [Multiomics Proteomics PTM Identification](../topics/multiomics-proteomics-ptm-identification.md)",
        "- [Multiomics PTM Corpus Queue](../analyses/multiomics-ptm-corpus-queue.md)",
        "",
        "## Sources",
        "",
        f"- Local PDF: `{pdf_path}`",
    ])
    if pmid:
        body.append(f"- PubMed: <https://pubmed.ncbi.nlm.nih.gov/{pmid}/>")
    if doi:
        body.append(f"- DOI: <https://doi.org/{doi}>")
    if pmcid:
        body.append(f"- PMC: <https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}/>")
    return fm + "\n" + "\n".join(body) + "\n"


def main():
    rows = json.loads(ROWS_PATH.read_text())
    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    summary = []
    for row in rows:
        pdf = ROOT / row["pdf_path"]
        if not pdf.exists():
            continue
        text = extract_text(pdf)
        classification, include_in_quant = classify(row.get("title", ""), text)
        page = SOURCE_DIR / f"{row['slug']}.md"
        content = make_page(row, text, classification, include_in_quant)
        old = page.read_text() if page.exists() else ""
        if "## Multi-Omics Identification Extraction" in old and "Local-PDF ingest note" not in old:
            action = "kept_existing_curated"
        else:
            page.write_text(content)
            action = "updated" if old else "created"
        summary.append({
            "slug": row["slug"],
            "title": row.get("title"),
            "year": row.get("year"),
            "pdf_path": row.get("pdf_path"),
            "source_page": f"wiki/sources/{row['slug']}.md",
            "classification": classification,
            "quant_candidate": include_in_quant,
            "protein_count_candidate": first_count(text, "protein"),
            "phospho_count_candidate": first_count(text, "phospho"),
            "acetyl_count_candidate": first_count(text, "acetyl"),
            "cancer_guess": cancer_guess(row.get("title", ""), text),
            "action": action,
        })
    OUT_SUMMARY.write_text(json.dumps(summary, indent=2, ensure_ascii=False))
    print(json.dumps({
        "processed": len(summary),
        "quant_candidates": sum(1 for x in summary if x["quant_candidate"]),
        "created_or_updated": sum(1 for x in summary if x["action"] != "kept_existing_curated"),
        "kept_existing_curated": sum(1 for x in summary if x["action"] == "kept_existing_curated"),
        "summary": str(OUT_SUMMARY),
    }, indent=2))


if __name__ == "__main__":
    main()
