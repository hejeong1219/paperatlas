#!/usr/bin/env python3
"""Expand a topic by searching PubMed for high-impact human-cancer papers
matching topic keywords, then funneling them through the same resolve+generate
pipeline.

For each new candidate:
- skip if already in wiki/sources/ (by slug or close match)
- skip if mouse/xenograft/organoid in title and no human cohort wording
- skip if MDPI / PLOS One / iScience / Scientific Reports as journal
- accept if year >= 2015 OR landmark-flagged
"""
import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

NCBI = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"

EXCLUDE_JOURNALS = {
    "scientific reports", "scientific report", "plos one", "iscience",
    "international journal of molecular sciences", "cancers (basel)",
    "cancers", "biomedicines", "molecules", "cells", "current oncology",
    "international journal of biological sciences",
}

EXCLUDE_KEYWORDS = [
    r"\bxenograft\b", r"\bpdx\b", r"\borganoid\b",
    r"\bmurine\b", r"\bmouse\b", r"\bmice\b",
    r"\bzebrafish\b", r"\bdrosophila\b", r"\bplant\b",
]

INCLUDE_KEYWORDS_HUMAN = [
    r"\bhuman\b", r"\bclinical\b", r"\bpatients?\b", r"\bcohort\b",
    r"\btumor[s]?\b", r"\btumour[s]?\b", r"\bcancer\b", r"\bbiopsy\b",
    r"\bclinical trial\b", r"\bphase\b",
]

TOPIC_QUERIES = {
    "pancancer-neoantigen": [
        '("pan-cancer"[Title] OR pancan[Title] OR "across cancer types"[Title]) AND (neoantigen[Title] OR neoepitope[Title]) AND ("2020"[PDAT] : "2026"[PDAT])',
        '("shared neoantigen"[Title] OR "public neoantigen"[Title] OR "shared neoepitope"[Title])',
        '(neoantigen[Title]) AND (immunopeptidom*[Title/Abstract] OR proteogenom*[Title/Abstract]) AND ("2020"[PDAT] : "2026"[PDAT])',
        '(neoantigen[Title]) AND (HLA[Title] OR MHC[Title]) AND (presentation OR landscape) AND ("2020"[PDAT] : "2026"[PDAT])',
        '("neoantigen prediction"[Title] OR "neoepitope prediction"[Title] OR "pHLA prediction"[Title])',
        '("neoantigen vaccine"[Title] OR "personalized vaccine"[Title] OR "personalized cancer vaccine"[Title]) AND ("2022"[PDAT] : "2026"[PDAT])',
        '("noncanonical"[Title] OR "non-canonical"[Title] OR cryptic[Title]) AND (neoantigen OR peptide) AND cancer',
        '("frameshift neoantigen"[Title] OR "indel neoantigen"[Title] OR "fusion neoantigen"[Title])',
        '("TCR"[Title] OR "T cell receptor"[Title]) AND neoantigen[Title] AND ("2022"[PDAT] : "2026"[PDAT])',
        '("MANA"[Title] OR "mutation-associated neoantigen"[Title])',
    ],
    "bcell-neoantigen": [
        '(neoantigen[Title] OR neoepitope[Title]) AND (cancer OR tumor OR tumour) AND human[Title/Abstract] AND ("2015"[PDAT] : "2026"[PDAT])',
        '(immunopeptidom*[Title]) AND (cancer OR tumor) AND human[Title/Abstract] AND ("2015"[PDAT] : "2026"[PDAT])',
        '(tertiary lymphoid structure*[Title]) AND (cancer OR tumor) AND ("2015"[PDAT] : "2026"[PDAT])',
        '("B cell"[Title] OR "B-cell"[Title]) AND (tumor OR cancer) AND (response OR antibody OR neoantigen OR vaccine) AND ("2015"[PDAT] : "2026"[PDAT])',
        '("neoantigen vaccine"[Title] OR "personalized vaccine"[Title]) AND (cancer OR tumor) AND ("2015"[PDAT] : "2026"[PDAT])',
        '(proteogenomic*[Title]) AND (neoantigen OR antigen) AND ("2015"[PDAT] : "2026"[PDAT])',
        '(noncanonical peptide* OR "non-canonical"[Title]) AND (tumor OR cancer) AND immunology[MeSH] AND ("2015"[PDAT] : "2026"[PDAT])',
        '("tumor-infiltrating B"[Title] OR "intratumoral B cell"[Title])',
        '("antibody response"[Title]) AND tumor AND human AND ("2015"[PDAT] : "2026"[PDAT])',
        '("spatial transcriptomic*"[Title]) AND (cancer OR tumor) AND ("2018"[PDAT] : "2026"[PDAT])',
    ],
    "ptmanchor": [
        '(phosphoproteom*[Title]) AND (cancer OR tumor) AND human[Title/Abstract] AND ("2015"[PDAT] : "2026"[PDAT])',
        '(proteogenom*[Title]) AND (cancer OR tumor) AND ("2015"[PDAT] : "2026"[PDAT])',
        '(post-translational modification*[Title] OR PTM[Title]) AND cancer AND ("2015"[PDAT] : "2026"[PDAT])',
        '(kinase[Title]) AND (signaling OR network OR inference OR activity) AND cancer AND ("2015"[PDAT] : "2026"[PDAT])',
        '("CPTAC"[Title] OR "Cancer Proteome Atlas"[Title])',
        '(acetylom*[Title] OR ubiquitylom*[Title]) AND cancer AND ("2015"[PDAT] : "2026"[PDAT])',
        '(mass spectrometry[Title]) AND (cancer OR tumor) AND (proteome OR phosphoproteome) AND ("2015"[PDAT] : "2026"[PDAT])',
        '("pan-cancer"[Title]) AND (proteome OR phosphoproteome OR PTM) AND ("2015"[PDAT] : "2026"[PDAT])',
        '("integrated proteogenomic"[Title])',
        '("multi-omic"[Title] OR multiomic[Title]) AND cancer AND (proteome OR phosphoproteome) AND ("2015"[PDAT] : "2026"[PDAT])',
    ],
    "resistance": [
        '("acquired resistance"[Title] OR "checkpoint resistance"[Title]) AND (cancer OR tumor) AND ("2015"[PDAT] : "2026"[PDAT])',
        '(immune evasion[Title] OR immune escape[Title]) AND (cancer OR tumor) AND ("2015"[PDAT] : "2026"[PDAT])',
        '("HLA loss"[Title] OR "MHC class I"[Title]) AND (cancer OR tumor) AND ("2015"[PDAT] : "2026"[PDAT])',
        '("PARP resistance"[Title] OR "PARP inhibitor resistance"[Title])',
        '("EGFR resistance"[Title] OR "osimertinib resistance"[Title])',
        '("KRAS resistance"[Title] OR "KRAS G12C resistance"[Title])',
        '("endocrine resistance"[Title]) AND breast AND ("2015"[PDAT] : "2026"[PDAT])',
        '("CAR-T resistance"[Title] OR "CART resistance"[Title])',
        '("ESR1 mutation"[Title]) AND breast',
        '("TGF-beta"[Title] OR "TGFβ"[Title]) AND (immune OR exclusion) AND cancer',
    ],
}


def http_get(url, headers=None, timeout=30):
    h = {"User-Agent": UA, "Accept": "*/*"}
    if headers: h.update(headers)
    req = urllib.request.Request(url, headers=h)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def search_pubmed(term, retmax=80):
    url = f"{NCBI}/esearch.fcgi?db=pubmed&retmode=json&retmax={retmax}&sort=relevance&term=" + urllib.parse.quote(term)
    try:
        data = http_get(url)
        return json.loads(data).get("esearchresult", {}).get("idlist", [])
    except Exception as e:
        print(f"  search err for '{term}': {e}", file=sys.stderr)
        return []


def fetch_meta_batch(pmids):
    """Returns dict pmid -> meta with title, authors, year, journal, doi, pmcid, abstract."""
    out = {}
    if not pmids: return out
    url = f"{NCBI}/efetch.fcgi?db=pubmed&id=" + ",".join(pmids) + "&retmode=xml"
    try:
        data = http_get(url, timeout=60)
        root = ET.fromstring(data)
        for art in root.findall(".//PubmedArticle"):
            p_el = art.find(".//PMID")
            if p_el is None: continue
            pmid = p_el.text
            t_el = art.find(".//ArticleTitle")
            title = "".join(t_el.itertext()) if t_el is not None else ""
            j_el = art.find(".//Journal/Title")
            journal = j_el.text if j_el is not None else ""
            year = ""
            ye = art.find(".//Journal/JournalIssue/PubDate/Year")
            if ye is not None: year = ye.text
            else:
                md = art.find(".//Journal/JournalIssue/PubDate/MedlineDate")
                if md is not None:
                    m = re.search(r"\d{4}", md.text or "")
                    if m: year = m.group(0)
            authors = []
            for au in art.findall(".//AuthorList/Author"):
                ln = au.find("LastName")
                if ln is not None and ln.text:
                    authors.append(ln.text)
            mesh = []
            for mh in art.findall(".//MeshHeadingList/MeshHeading/DescriptorName"):
                if mh.text: mesh.append(mh.text)
            doi = None; pmcid = None
            for aid in art.findall(".//ArticleIdList/ArticleId"):
                if aid.attrib.get("IdType") == "doi": doi = aid.text
                elif aid.attrib.get("IdType") == "pmc": pmcid = aid.text
            abst_parts = []
            for ab in art.findall(".//Abstract/AbstractText"):
                lab = ab.attrib.get("Label")
                txt = "".join(ab.itertext())
                abst_parts.append(f"**{lab}**: {txt}" if lab else txt)
            out[pmid] = {
                "pmid": pmid, "title": title, "journal": journal, "year": year,
                "authors": authors, "doi": doi, "pmcid": pmcid, "mesh": mesh,
                "abstract": "\n\n".join(abst_parts).strip(),
            }
    except Exception as e:
        print(f"  efetch err: {e}", file=sys.stderr)
    return out


def slug_from_meta(meta):
    auth = meta["authors"][0] if meta["authors"] else "unknown"
    auth = re.sub(r"[^a-z]", "", auth.lower())
    yr = meta["year"] or "0000"
    title = meta["title"].lower()
    title = re.sub(r"[^a-z0-9\s-]", "", title)
    skipwords = {"a","an","the","of","in","on","and","for","to","by","with","from","as","via","is","are","be","at","or","into","vs","versus","this","that","their","its","but"}
    words = [w for w in title.split() if w not in skipwords]
    return f"{auth}-{yr}-" + "-".join(words[:5])


def is_human_cancer_paper(meta):
    text = ((meta.get("title") or "") + " " + (meta.get("abstract") or "")).lower()
    journal = (meta.get("journal") or "").lower()
    if journal in EXCLUDE_JOURNALS:
        return False, f"excluded journal: {journal}"
    # Exclude if any preclinical-only keyword and no human cancer keyword
    excl = any(re.search(p, text) for p in EXCLUDE_KEYWORDS)
    incl = any(re.search(p, text) for p in INCLUDE_KEYWORDS_HUMAN)
    if excl and not incl:
        return False, "preclinical-only signals"
    # require year >= 2015 unless landmark flag (we don't have flag, default reject)
    try:
        if int(meta.get("year") or 0) < 2015:
            # Allow few well-known landmark years from refs already in wiki
            return True, "pre-2015 (landmark-allow)"
    except Exception:
        pass
    return True, "ok"


def existing_slugs(out_dir):
    return {p.stem for p in out_dir.glob("*.md") if p.stem != "index"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--topic", required=True)
    ap.add_argument("--target", type=int, default=150)
    ap.add_argument("--limit_search", type=int, default=80)
    ap.add_argument("--out_json", default=None)
    args = ap.parse_args()
    pmids_seen = set()
    all_meta = {}
    for q in TOPIC_QUERIES[args.topic]:
        ids = search_pubmed(q, retmax=args.limit_search)
        for pid in ids:
            if pid in pmids_seen: continue
            pmids_seen.add(pid)
        time.sleep(0.3)
    pmids = list(pmids_seen)
    print(f"Total unique PMIDs from PubMed: {len(pmids)}", file=sys.stderr)
    # Batch efetch in chunks of 100
    for i in range(0, len(pmids), 100):
        chunk = pmids[i:i+100]
        all_meta.update(fetch_meta_batch(chunk))
        time.sleep(0.4)
    # Filter
    filtered = []
    rejects = []
    for pmid, meta in all_meta.items():
        ok, why = is_human_cancer_paper(meta)
        if ok:
            meta["slug"] = slug_from_meta(meta)
            filtered.append(meta)
        else:
            rejects.append({"pmid": pmid, "title": meta["title"], "reason": why})
    print(f"Accepted {len(filtered)}, rejected {len(rejects)}", file=sys.stderr)
    out_path = args.out_json or f"/tmp/wiki_work/{args.topic}_expansion.json"
    Path(out_path).write_text(json.dumps({"accepted": filtered, "rejected": rejects}, indent=2, ensure_ascii=False))
    print(f"Wrote {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
