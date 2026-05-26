#!/usr/bin/env python3
"""Generate wiki/sources/<slug>.md stubs from a topic_sweep.py JSON output.

Creates a frontmatter-complete source page per candidate with placeholder
Summary and Key Points sections. A follow-up enrichment step (subagent or
manual) should fill those sections from the candidate's full_text.

Marks each page with batch_ingest_status: topic-sweep-stub-<DATE>.
"""
import argparse
import datetime as dt
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCES = ROOT / "wiki/sources"


def yaml_list(items, indent=2):
    if not items:
        return "[]"
    pre = " " * indent
    return "\n" + "\n".join(f"{pre}- \"{i}\"" for i in items)


def normalize_journal_short(j: str) -> str:
    j = re.sub(r"\s*\([^)]*\)\s*", " ", j or "").strip()
    j = re.sub(r"\s+", " ", j)
    abbrev = {
        "cell reports. medicine": "Cell Rep Med",
        "cell reports medicine": "Cell Rep Med",
        "cell reports.": "Cell Rep",
        "cell reports": "Cell Rep",
        "nature communications": "Nat Commun",
        "nature medicine": "Nat Med",
        "nature cancer": "Nat Cancer",
        "nature biotechnology": "Nat Biotechnol",
        "nature genetics": "Nat Genet",
        "nature reviews. clinical oncology": "Nat Rev Clin Oncol",
        "nature reviews clinical oncology": "Nat Rev Clin Oncol",
        "nature reviews. cancer": "Nat Rev Cancer",
        "nature immunology": "Nat Immunol",
        "science (new york, n.y.)": "Science",
        "science translational medicine": "Sci Transl Med",
        "science advances": "Sci Adv",
        "journal for immunotherapy of cancer": "J Immunother Cancer",
        "journal of clinical oncology": "J Clin Oncol",
        "annals of oncology": "Ann Oncol",
        "clinical cancer research : an official journal of the american association for cancer research": "Clin Cancer Res",
        "clinical cancer research": "Clin Cancer Res",
        "cancer cell": "Cancer Cell",
        "molecular cancer": "Mol Cancer",
        "molecular oncology": "Mol Oncol",
        "cancer letters": "Cancer Lett",
        "cancer research": "Cancer Res",
        "cancer immunology research": "Cancer Immunol Res",
        "signal transduction and targeted therapy": "Signal Transduct Target Ther",
        "the journal of clinical investigation": "J Clin Invest",
        "embo molecular medicine": "EMBO Mol Med",
        "embo reports": "EMBO Rep",
        "genome biology": "Genome Biol",
    }
    return abbrev.get(j.lower(), j.replace(".", "").strip())


def infer_paper_kind(title: str, abstract: str) -> str:
    t = (title + " " + abstract).lower()
    if re.search(r"\b(phase [I1-3]+|clinical trial|nct\d|randomized|randomised|first-in-human)\b", t):
        return "trial"
    if re.search(r"\b(review|perspective|opinion|consensus|guideline)\b", t[:200]):
        return "review"
    if re.search(r"\b(pipeline|benchmark|workflow|database|atlas resource|method|software|computational tool)\b", t[:200]):
        return "computational"
    return "research"


def infer_themes(topic: str, title: str, abstract: str) -> list[str]:
    t = (title + " " + abstract).lower()
    themes = set()
    if topic == "bcell-neoantigen":
        themes.add("neoantigen-discovery") if re.search(r"neoantigen|neoepitope|immunopeptidom", t) else None
        themes.add("tls-biology") if re.search(r"tertiary lymphoid|tls|tumor.infiltrating b|intratumoral b", t) else None
        themes.add("b-cells") if re.search(r"\bb cell|\bb-cell|humoral", t) else None
        themes.add("vaccine") if re.search(r"vaccine|mrna therapy", t) else None
        themes.add("tcr-t") if re.search(r"\btcr-t|tcr therapy|t cell receptor", t) else None
        themes.add("immunotherapy") if re.search(r"immunotherapy|checkpoint|anti-pd|pd-1|pd-l1|ctla", t) else None
        themes.add("clinical-translation") if re.search(r"clinical|trial|patient", t) else None
        themes.add("cryptic-antigen") if re.search(r"cryptic|non-canonical|noncanonical|noncoding orf", t) else None
        themes.add("proteogenomics") if "proteogenom" in t else None
    elif topic == "cancer-multiomics":
        themes.add("proteogenomics") if "proteogenom" in t else None
        themes.add("phosphoproteomics") if "phosphoproteom" in t else None
        themes.add("spatial-omics") if re.search(r"spatial", t) else None
        themes.add("single-cell") if re.search(r"single.cell|scrna|sc.rna", t) else None
        themes.add("kinase-signaling") if re.search(r"kinase|kinome|ksea", t) else None
        themes.add("drug-resistance") if re.search(r"resistan|tolerant|relapse|recurrence", t) else None
        themes.add("treatment-response") if re.search(r"response|pcr|recist|respond", t) else None
        themes.add("immunotherapy") if re.search(r"immunotherapy|checkpoint|anti-pd|pd-1|pd-l1|ctla", t) else None
        themes.add("subtype-stratification") if re.search(r"subtyp|stratification|classifier", t) else None
        themes.add("clinical-translation") if re.search(r"clinical|trial|patient", t) else None
    return sorted(themes) or [topic]


def infer_cancer_types(title: str, abstract: str) -> list[str]:
    t = (title + " " + abstract).lower()
    mapping = {
        r"\bbreast\b|\btnbc\b|\bher2\b": "breast-cancer",
        r"\bnsclc\b|non.small.cell lung|lung adeno|lscc|lusc": "non-small-cell-lung-cancer",
        r"\bsclc\b|small.cell lung": "small-cell-lung-cancer",
        r"\bcolorect|\bcrc\b|colon": "colorectal-cancer",
        r"\bgastric\b|stomach": "gastric-cancer",
        r"\bovari": "ovarian-cancer",
        r"\bmelanom": "melanoma",
        r"\bpancrea|pdac\b": "pancreatic-cancer",
        r"\bhepatocell|\bhcc\b|liver cancer": "hepatocellular-carcinoma",
        r"\bcholangio|\bcca\b|biliary|gallbladder": "biliary-tract-cancer",
        r"\bglioblastom|\bgbm\b|glioma": "glioblastoma",
        r"\bendometri": "endometrial-cancer",
        r"\bcervical": "cervical-cancer",
        r"\bprostat": "prostate-cancer",
        r"\bhead.and.neck|\bhnscc\b|nasopharyng": "head-and-neck-cancer",
        r"\brenal|\bccrcc\b|kidney cancer": "renal-cell-carcinoma",
        r"\burothel|bladder": "urothelial-cancer",
        r"\besophag|oesophag": "esophageal-cancer",
        r"\bsarcoma": "soft-tissue-sarcoma",
        r"\blymphoma|\bdlbcl\b|mantle cell|hodgkin": "lymphoma",
        r"\bleuk|\baml\b|\ball\b\s|myeloid": "leukemia",
        r"\bmyeloma|\bmm\b": "multiple-myeloma",
        r"\bpan.cancer|across cancer|across tumor": "pan-cancer",
        r"\bsolid tumor": "solid-tumors",
    }
    cts = []
    for pat, ct in mapping.items():
        if re.search(pat, t):
            cts.append(ct)
    return cts or ["pan-cancer"]


TOPIC_HUB = {
    "bcell-neoantigen": "b-cell-neoantigen-human-cancer",
    "cancer-multiomics": "cancer-multiomics-literature",
}


def render_source_page(c: dict, topic: str, today: str) -> str:
    slug = c["slug"]
    title = c["title"].rstrip(".")
    title_escaped = title.replace('"', '\\"')
    authors = c.get("authors", [])
    year = c.get("year", "")
    journal_raw = c.get("journal", "")
    journal_short = normalize_journal_short(journal_raw)
    doi = c.get("doi", "")
    pmid = c.get("pmid", "")
    pmcid = c.get("pmcid", "")
    pdf_path = c.get("pdf_path", "")
    abstract = (c.get("abstract") or "").strip()
    full_text_head = (c.get("full_text") or "")[:3500].strip()

    paper_kind = infer_paper_kind(title, abstract)
    themes = infer_themes(topic, title, abstract)
    cancer_types = infer_cancer_types(title, abstract)
    topic_hub = TOPIC_HUB[topic]

    tags = sorted(set(themes + [topic_hub, f"{journal_short.lower().replace(' ', '-')}-{year}", "topic-sweep"]))
    tags = [t for t in tags if t and not t.startswith("-")]

    pmcid_line = f"pmcid: \"{pmcid}\"\n" if pmcid else ""
    pmid_line = f"pmid: \"{pmid}\"\n" if pmid else ""

    # Build links section
    links = []
    if doi:
        links.append(f"[{doi}](https://doi.org/{doi})")
    if pmid:
        links.append(f"[PubMed {pmid}](https://pubmed.ncbi.nlm.nih.gov/{pmid}/)")
    if pmcid:
        links.append(f"[PMC {pmcid}](https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/)")
    links_line = " · ".join(links) if links else ""

    fm_themes = "\n".join(f"  - \"{t}\"" for t in themes)
    fm_cancers = "\n".join(f"  - \"{c}\"" for c in cancer_types)
    fm_authors = "\n".join(f"  - \"{a}\"" for a in authors[:8])
    fm_tags = "\n".join(f"  - \"{t}\"" for t in tags)

    body = f"""---
title: "{title_escaped}"
authors:
{fm_authors}
year: {year}
journal: "{journal_raw}"
doi: "{doi}"
{pmid_line}{pmcid_line}pdf: "{pdf_path}"
paper_kind: {paper_kind}
cancer_types:
{fm_cancers}
themes:
{fm_themes}
topic: {topic_hub}
discovery_method: topic-sweep-{today}
tags:
{fm_tags}
batch_ingest_status: topic-sweep-stub
batch_ingested_on: {today}
---

# {title}

_{journal_short}, {year}._{(' ' + links_line) if links_line else ''}

## Summary

_PLACEHOLDER — Korean 2-4 문장 요약을 full_text 기반으로 채울 것. 현재는 stub._

## Key Points

- _PLACEHOLDER — 3-5 bullets, full_text 근거._

## 한미암 활용 가능성

_PLACEHOLDER — 한미암 과제 연결 1-2 문장 (해당되는 topic만)._

## Topic Sweep Ingest Status

- Status: `topic-sweep-stub` ({today})
- Topic: `{topic_hub}`
- Local PDF: `{pdf_path}`
- Download path: `{c.get('download_via', '')}`
- Extracted text length: {len(c.get('full_text', ''))} characters
- Scope note: automated topic-sweep batch ingest; not yet a manual full-text deep-dive.

## Abstract (PubMed)

{abstract if abstract else '_No abstract available._'}

## High-signal PDF head

```
{full_text_head[:1500]}
```

## Sources

- Local PDF: `{pdf_path}`
{('- DOI: <https://doi.org/' + doi + '>' ) if doi else ''}
{('- PubMed: <https://pubmed.ncbi.nlm.nih.gov/' + pmid + '/>') if pmid else ''}
{('- PMC: <https://pmc.ncbi.nlm.nih.gov/articles/' + pmcid + '/>') if pmcid else ''}
"""
    return body


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", required=True, help="topic_sweep.py output JSON")
    ap.add_argument("--topic", required=True, choices=list(TOPIC_HUB.keys()))
    ap.add_argument("--force", action="store_true",
                    help="Overwrite existing source pages")
    args = ap.parse_args()

    data = json.loads(Path(args.json).read_text())
    candidates = data["candidates"]
    today = dt.date.today().isoformat()

    SOURCES.mkdir(parents=True, exist_ok=True)
    created = []
    skipped = []
    for c in candidates:
        slug = c["slug"]
        out = SOURCES / f"{slug}.md"
        if out.exists() and not args.force:
            skipped.append(slug)
            continue
        out.write_text(render_source_page(c, args.topic, today), encoding="utf-8")
        created.append(slug)
        print(f"  + {slug}")

    print(f"\n[done] created {len(created)}, skipped {len(skipped)}")


if __name__ == "__main__":
    main()
