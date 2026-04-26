#!/usr/bin/env python3
"""Generate wiki/sources/<slug>.md skeleton pages from parsed references.

Strategy per paper:
- Frontmatter: title, authors, year, journal, doi (best effort), pmid, pmcid, paper_kind, tags, themes, anchors
- Body sections (depth-b template):
  - Summary
  - Key Points (placeholder if abstract not available)
  - Open Questions
  - Connections
  - Sources

Inputs:
  --refs  : path to parsed JSON (with optional 'meta' from fetch_abstract)
  --topic : topic identifier for tags ('ptmanchor', 'resistance', 'bcell-neoantigen')
  --pdfs  : path to raw/inbox/papers
  --out   : path to wiki/sources

If a wiki page with the same slug already exists, skip (do not overwrite).
"""
import argparse
import json
import re
import sys
from pathlib import Path
from textwrap import dedent


TOPIC_TAGS = {
    "ptmanchor": ["proteomics", "ptm", "phosphoproteomics", "cancer-proteomics"],
    "resistance": ["resistance", "immune-evasion", "immunotherapy"],
    "bcell-neoantigen": ["neoantigen", "b-cells", "tls", "immunology"],
}
TOPIC_THEMES = {
    "ptmanchor": ["ptm-correction", "kinase-signaling", "cancer-proteomics"],
    "resistance": ["immune-evasion", "resistance-framework", "translational-oncology"],
    "bcell-neoantigen": ["neoantigen-discovery", "tls-biology", "clinical-translation"],
}
TOPIC_ANCHOR_PAGE = {
    "ptmanchor": "../analyses/ptmanchor-manuscript-anchor.md",
    "resistance": "../analyses/cancer-resistance-manuscript-anchor.md",
    "bcell-neoantigen": "../analyses/b-cell-neoantigen-proposal-anchor.md",
}
TOPIC_HUB_PAGE = {
    "ptmanchor": "../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md",
    "resistance": "../topics/immunotherapy-resistance-and-immune-evasion.md",
    "bcell-neoantigen": "../topics/b-cell-neoantigen-human-cancer.md",
}


def yaml_string(s):
    if s is None: return '""'
    s = str(s).replace('"', '\\"')
    return f'"{s}"'


def yaml_list(items):
    if not items:
        return "[]"
    out = []
    for it in items:
        out.append(f"  - {yaml_string(it)}")
    return "\n" + "\n".join(out)


def make_authors_short(authors_raw):
    if not authors_raw: return []
    parts = re.split(r",", authors_raw)
    out = []
    for p in parts[:3]:
        p = p.strip()
        if not p: continue
        # "Chen DS" -> "Chen"
        m = re.match(r"^([A-Za-zÀ-ÿ\-']+)", p)
        if m: out.append(m.group(1))
    return out


def detect_paper_kind(title, journal, mesh):
    t = (title or "").lower()
    j = (journal or "").lower()
    m_set = set(s.lower() for s in (mesh or []))
    if any(w in t for w in ["randomized", "phase 3", "phase iii", "phase 2", "phase ii", "trial"]):
        return "clinical-trial"
    if "clinical trial" in m_set or "randomized controlled trial" in m_set:
        return "clinical-trial"
    if any(w in t for w in ["review", "perspective", "consensus"]):
        return "review"
    if any(w in t for w in ["proteogenomic", "proteomic", "phosphoproteomic", "phospho"]):
        return "proteogenomic"
    if any(w in t for w in ["meta-analysis"]):
        return "meta-analysis"
    if "case report" in m_set:
        return "case-report"
    return "research"


def existing_pages(out_dir):
    return {p.stem for p in out_dir.glob("*.md") if p.stem != "index"}


def build_page(ref, topic, pdf_dir, has_pdf, abstract=None):
    meta = ref.get("meta") or {}
    title = meta.get("title") or ref.get("title") or ref["slug"]
    title = re.sub(r"\s+\.$", "", title.strip())
    authors_short = make_authors_short(ref.get("authors_raw") or "")
    if meta.get("authors"):
        authors_short = []
        for au in meta["authors"][:3]:
            authors_short.append(au.split()[0])
    year = meta.get("year") or ref.get("year") or ""
    journal = meta.get("journal") or ref.get("journal") or ""
    doi = meta.get("doi") or ref.get("doi")
    pmid = ref.get("pmid")
    pmcid = ref.get("pmcid")
    mesh = meta.get("mesh") or []
    kws = meta.get("keywords") or []
    paper_kind = detect_paper_kind(title, journal, mesh)
    abstract_text = abstract or meta.get("abstract") or ""
    tags = [topic] + TOPIC_TAGS.get(topic, [])
    if pmid: tags.append(f"pmid-{pmid}")
    themes = TOPIC_THEMES.get(topic, [])

    fm_lines = ["---"]
    fm_lines.append(f"title: {yaml_string(title)}")
    if authors_short:
        fm_lines.append("authors:" + yaml_list(authors_short))
    if year: fm_lines.append(f"year: {year}")
    if journal: fm_lines.append(f"journal: {yaml_string(journal)}")
    if doi: fm_lines.append(f"doi: {yaml_string(doi)}")
    if pmid: fm_lines.append(f"pmid: {yaml_string(pmid)}")
    if pmcid: fm_lines.append(f"pmcid: {yaml_string(pmcid)}")
    fm_lines.append(f"paper_kind: {paper_kind}")
    if has_pdf:
        fm_lines.append(f"pdf: \"raw/inbox/papers/{ref['slug']}.pdf\"")
    else:
        fm_lines.append("pdf_status: pending")
    fm_lines.append(f"topic: {topic}")
    fm_lines.append("tags:" + yaml_list(tags))
    fm_lines.append("themes:" + yaml_list(themes))
    fm_lines.append("---")
    fm = "\n".join(fm_lines)

    # Body
    body = []
    body.append("")
    body.append(f"# {title}")
    body.append("")
    if year and journal:
        body.append(f"_{journal}, {year}._" + (f" PMID: [{pmid}](https://pubmed.ncbi.nlm.nih.gov/{pmid}/)." if pmid else ""))
        body.append("")
    if doi:
        body.append(f"DOI: [{doi}](https://doi.org/{doi})")
        body.append("")
    if abstract_text:
        body.append("## Summary")
        body.append("")
        body.append(abstract_text)
        body.append("")
    else:
        body.append("## Summary")
        body.append("")
        body.append(f"_Abstract pending — see source PDF or external link for full content._")
        body.append("")
    body.append("## Key Points")
    body.append("")
    body.append("- _Key claims to be filled in from full text. This page was created automatically as a placeholder._")
    body.append("")
    body.append("## Open Questions")
    body.append("")
    body.append("- _What does this paper actually claim about the topic anchor?_")
    body.append("- _What evidence does it provide and is it clinical, mechanistic, or computational?_")
    body.append("- _How does this fit alongside neighboring papers in the topic?_")
    body.append("")
    body.append("## Connections")
    body.append("")
    body.append(f"- [{topic.replace('-', ' ').title()} Topic Hub]({TOPIC_HUB_PAGE.get(topic, '../topics/index.md')})")
    body.append(f"- [{topic.replace('-', ' ').title()} Anchor]({TOPIC_ANCHOR_PAGE.get(topic, '')})")
    body.append("")
    body.append("## Sources")
    body.append("")
    if has_pdf:
        body.append(f"- Local PDF: `raw/inbox/papers/{ref['slug']}.pdf`")
    else:
        body.append("- Local PDF: pending acquisition")
    if pmid:
        body.append(f"- PubMed: <https://pubmed.ncbi.nlm.nih.gov/{pmid}/>")
    if doi:
        body.append(f"- DOI: <https://doi.org/{doi}>")
    if pmcid:
        body.append(f"- PMC: <https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}/>")
    body.append("")
    return fm + "\n".join(body)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--refs", required=True)
    ap.add_argument("--topic", required=True, choices=list(TOPIC_TAGS.keys()))
    ap.add_argument("--pdfs", default="raw/inbox/papers")
    ap.add_argument("--out", default="wiki/sources")
    ap.add_argument("--force", action="store_true", help="overwrite existing pages")
    args = ap.parse_args()

    refs = json.loads(Path(args.refs).read_text())
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    pdf_dir = Path(args.pdfs)
    existing = existing_pages(out_dir)

    created = 0; skipped = 0; written_paths = []
    for ref in refs:
        slug = ref["slug"]
        page = out_dir / f"{slug}.md"
        if page.exists() and not args.force:
            skipped += 1
            continue
        has_pdf = (pdf_dir / f"{slug}.pdf").exists() and (pdf_dir / f"{slug}.pdf").stat().st_size > 5000
        content = build_page(ref, args.topic, pdf_dir, has_pdf)
        page.write_text(content)
        created += 1
        written_paths.append(str(page))
    print(f"Created {created}, skipped (existing) {skipped}", file=sys.stderr)
    Path("/tmp/wiki_work/last_generated.json").write_text(json.dumps(written_paths, indent=2))


if __name__ == "__main__":
    main()
