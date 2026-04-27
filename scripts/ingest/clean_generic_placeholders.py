#!/usr/bin/env python3
"""Replace the generic 3-question Open Questions placeholder block + the
generic 'Key claims' bullet on pages that still have them, so users don't see
the same template text on every page. Pages that already received a real deep
dive are untouched.
"""
import re
from pathlib import Path

GENERIC_KEY_POINTS = (
    "## Key Points\n\n"
    "- _Key claims to be filled in from full text. This page was created automatically as a placeholder._\n"
)
GENERIC_OPEN_Q = (
    "## Open Questions\n\n"
    "- _What does this paper actually claim about the topic anchor?_\n"
    "- _What evidence does it provide and is it clinical, mechanistic, or computational?_\n"
    "- _How does this fit alongside neighboring papers in the topic?_\n"
)
NEW_KEY_POINTS = (
    "## Key Points\n\n"
    "_Awaiting deep-dive — automated abstract is in the Summary section above. "
    "The paper-specific Key Points, Methods, Limitations, and Open Questions will appear here once the full PDF has been read._\n"
)
NEW_OPEN_Q = ""  # remove block entirely (consolidated into the marker above)


def main():
    sources = Path("wiki/sources")
    updated = 0
    for f in sources.glob("*.md"):
        if f.stem == "index": continue
        text = f.read_text()
        new = text
        if GENERIC_KEY_POINTS in new:
            new = new.replace(GENERIC_KEY_POINTS, NEW_KEY_POINTS)
        if GENERIC_OPEN_Q in new:
            new = new.replace(GENERIC_OPEN_Q, NEW_OPEN_Q)
        if new != text:
            f.write_text(new)
            updated += 1
    print(f"Cleaned {updated} placeholder pages")


if __name__ == "__main__":
    main()
