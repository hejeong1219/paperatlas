#!/usr/bin/env python3
"""Fetch Notion '참고 논문 및 아이디어' child pages → candidates JSON.

Stdout: JSON with {date, parent_page_id, synced_count, fetched_total,
                   after_dedup, skipped, candidates: [...]}
Stderr: progress log.

Env vars:
  NOTION_API_KEY    required
  LIMIT             optional, cap on candidates emitted
  ONLY_PAGE_ID      optional, restrict to one page (debug)
"""
import argparse
import datetime
import json
import os
import re
import sys
from pathlib import Path

try:
    from notion_client import Client
except ImportError:
    print("ERROR: notion-client not installed. Run: pip install notion-client",
          file=sys.stderr)
    sys.exit(1)

REPO = Path(__file__).resolve().parents[2]
PARENT_PAGE_ID = "344302d9-c598-8188-8a05-d5041134fb3d"
STATE_PATH = REPO / "wiki/_meta/notion-synced.json"
WIKI_SOURCES = REPO / "wiki/sources"

DOI_RE = re.compile(r"10\.\d{4,9}/[^\s\"<>)]+")


# ---------------------------------------------------------------------------
# State + dedup helpers
# ---------------------------------------------------------------------------

def load_state():
    if not STATE_PATH.exists():
        return {"last_run": None, "synced": [], "history": []}
    return json.loads(STATE_PATH.read_text())


def synced_page_ids(state):
    return {e["page_id"] for e in state.get("synced", []) if e.get("page_id")}


def slug_exists(slug):
    return (WIKI_SOURCES / f"{slug}.md").exists()


def doi_already_in_wiki(doi):
    """grep wiki/sources/*.md for matching `doi:` frontmatter line."""
    if not doi:
        return False
    pat = re.compile(r'^doi:\s*"?' + re.escape(doi.lower()) + r'"?\s*$',
                     re.IGNORECASE | re.MULTILINE)
    for md in WIKI_SOURCES.glob("*.md"):
        try:
            text = md.read_text(errors="ignore")
        except Exception:
            continue
        if pat.search(text):
            return True
    return False


# ---------------------------------------------------------------------------
# Notion page parser
# ---------------------------------------------------------------------------

def block_to_text(block):
    """Render a Notion block to plain markdown (best-effort)."""
    btype = block.get("type")
    if not btype:
        return ""
    payload = block.get(btype, {})
    rich = payload.get("rich_text", [])
    text = "".join(rt.get("plain_text", "") for rt in rich)
    if btype == "heading_1":
        return f"# {text}"
    if btype == "heading_2":
        return f"## {text}"
    if btype == "heading_3":
        return f"### {text}"
    if btype == "bulleted_list_item":
        return f"- {text}"
    if btype == "numbered_list_item":
        return f"1. {text}"
    if btype == "quote":
        return f"> {text}"
    if btype == "code":
        lang = payload.get("language", "")
        return f"```{lang}\n{text}\n```"
    if btype == "paragraph":
        return text
    return text  # divider, image, etc. — best-effort fall-through


def fetch_page_body(notion, page_id):
    """Concatenate all child blocks of a page into markdown-ish text."""
    parts = []
    cursor = None
    while True:
        resp = notion.blocks.children.list(block_id=page_id, start_cursor=cursor)
        for blk in resp.get("results", []):
            line = block_to_text(blk)
            if line:
                parts.append(line)
        if not resp.get("has_more"):
            break
        cursor = resp.get("next_cursor")
    return "\n\n".join(parts)


def extract_property_value(prop):
    """Notion property → plain str (handles title, rich_text, url, select, ...)."""
    if not prop:
        return ""
    ptype = prop.get("type")
    if ptype == "title":
        return "".join(t.get("plain_text", "") for t in prop.get("title", []))
    if ptype == "rich_text":
        return "".join(t.get("plain_text", "") for t in prop.get("rich_text", []))
    if ptype == "url":
        return prop.get("url") or ""
    if ptype == "select":
        sel = prop.get("select") or {}
        return sel.get("name", "")
    if ptype == "number":
        return prop.get("number")
    if ptype == "multi_select":
        return [s.get("name", "") for s in prop.get("multi_select", [])]
    return ""


def find_doi(properties, body_text):
    """Look for DOI in properties first, then body text."""
    for key, prop in properties.items():
        if "doi" in key.lower():
            val = extract_property_value(prop)
            if isinstance(val, str) and val:
                m = DOI_RE.search(val)
                if m:
                    return m.group(0).rstrip(".,;)")
    m = DOI_RE.search(body_text or "")
    return m.group(0).rstrip(".,;)") if m else None


def find_url(properties):
    for key, prop in properties.items():
        if "url" in key.lower() or "link" in key.lower():
            val = extract_property_value(prop)
            if isinstance(val, str) and val.startswith("http"):
                return val
    return ""


# ---------------------------------------------------------------------------
# Slug builder + page parsing orchestration
# ---------------------------------------------------------------------------

def make_slug(first_author_last, year, title):
    """authoryear-firstwords-of-title kebab. Mirror existing wiki slug convention."""
    base = re.sub(r"[^a-z0-9\s-]", "", (title or "").lower())
    words = base.split()[:6]
    slug = f"{first_author_last}-{year}-" + "-".join(words)
    return re.sub(r"-+", "-", slug).strip("-")


def parse_title_for_author_year(notion_title):
    """Best-effort: Notion title is freeform user text like
    'Xu et al. 2026 — Chinese HER2-low BC proteogenomics + lactylome'.
    Extract first author surname + year. Falls back to defaults on no match."""
    title = notion_title or ""
    yr_m = re.search(r"\b(19|20)\d{2}\b", title)
    year = int(yr_m.group(0)) if yr_m else 0
    name_m = re.match(r"^\s*([A-Za-zÀ-ſ][A-Za-zÀ-ſ\-']*)", title)
    first_author_last = (name_m.group(1) if name_m else "unknown").lower()
    first_author_last = re.sub(r"[^a-z]", "", first_author_last) or "unknown"
    return first_author_last, year


def parse_notion_page(notion, page):
    """Page payload → candidate dict (or None if no DOI)."""
    page_id = page["id"]
    properties = page.get("properties", {})

    # Notion stores child page name as a 'title' property — find it.
    title_text = ""
    for prop in properties.values():
        if prop.get("type") == "title":
            title_text = "".join(t.get("plain_text", "") for t in prop.get("title", []))
            break

    body = fetch_page_body(notion, page_id)
    doi = find_doi(properties, body)
    if not doi:
        return None  # caller logs warning

    first_author_last, year = parse_title_for_author_year(title_text)
    if not year:
        # Final fallback: this year
        year = datetime.date.today().year

    slug = make_slug(first_author_last, year, title_text)

    return {
        "page_id": page_id,
        "title": title_text,
        "doi": doi,
        "first_author_last": first_author_last,
        "year": year,
        "journal": "",   # left blank; deep-dive will fill
        "slug_candidate": slug,
        "notion_url": page.get("url", ""),
        "notion_body": body,
    }


# ---------------------------------------------------------------------------
# main() with dedup loop
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--parent", default=PARENT_PAGE_ID,
                    help="Notion parent page ID (default: 참고 논문 및 아이디어 root)")
    args = ap.parse_args()

    token = os.environ.get("NOTION_API_KEY")
    if not token:
        print("ERROR: NOTION_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    only = os.environ.get("ONLY_PAGE_ID")
    limit = int(os.environ.get("LIMIT", "0"))

    notion = Client(auth=token)
    state = load_state()
    synced_ids = synced_page_ids(state)

    # Enumerate child pages of parent.
    children = []
    cursor = None
    while True:
        resp = notion.blocks.children.list(block_id=args.parent, start_cursor=cursor)
        for blk in resp.get("results", []):
            if blk.get("type") == "child_page":
                children.append(blk["id"])
        if not resp.get("has_more"):
            break
        cursor = resp.get("next_cursor")

    print(f"[fetch] parent has {len(children)} child pages", file=sys.stderr)

    skipped = {"already_synced": 0, "slug_collision": 0, "doi_collision": 0,
               "no_doi": 0, "filter": 0}
    candidates = []

    for page_id in children:
        if only and page_id != only:
            skipped["filter"] += 1
            continue
        if page_id in synced_ids:
            skipped["already_synced"] += 1
            continue
        try:
            page = notion.pages.retrieve(page_id=page_id)
        except Exception as e:
            print(f"  {page_id}: retrieve failed: {e}", file=sys.stderr)
            continue
        cand = parse_notion_page(notion, page)
        if cand is None:
            print(f"  {page_id}: DOI missing — skip", file=sys.stderr)
            skipped["no_doi"] += 1
            continue
        if slug_exists(cand["slug_candidate"]):
            print(f"  {page_id}: slug {cand['slug_candidate']} exists — skip",
                  file=sys.stderr)
            skipped["slug_collision"] += 1
            continue
        if doi_already_in_wiki(cand["doi"]):
            print(f"  {page_id}: DOI {cand['doi']} already in wiki — skip",
                  file=sys.stderr)
            skipped["doi_collision"] += 1
            continue
        candidates.append(cand)
        if limit and len(candidates) >= limit:
            print(f"[fetch] LIMIT={limit} reached", file=sys.stderr)
            break

    out = {
        "date": datetime.date.today().isoformat(),
        "parent_page_id": args.parent,
        "synced_count": len(synced_ids),
        "fetched_total": len(children),
        "after_dedup": len(candidates),
        "skipped": skipped,
        "candidates": candidates,
    }
    json.dump(out, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
