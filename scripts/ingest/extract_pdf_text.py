#!/usr/bin/env python3
"""Extract text content from a single PDF (for LLM analysis input)."""
import subprocess
import sys
from pathlib import Path


def extract(pdf_path: Path, out_path: Path = None) -> str:
    res = subprocess.run(
        ["pdftotext", "-layout", str(pdf_path), "-"],
        capture_output=True, text=True, timeout=120
    )
    text = res.stdout
    # Trim references section to keep tokens reasonable for LLM input
    for marker in ["\nReferences\n", "\nReference\n", "\nBibliography\n"]:
        idx = text.find(marker)
        if idx > 5000:
            text = text[:idx]
            break
    # Cap at 30K chars (~7K tokens)
    if len(text) > 30000:
        text = text[:30000] + "\n\n[truncated]"
    if out_path:
        out_path.write_text(text)
    return text


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: extract_pdf_text.py <pdf>"); sys.exit(1)
    out = extract(Path(sys.argv[1]))
    print(out)
