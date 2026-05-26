---
title: "msqrob2PTM: Differential Abundance and Differential Usage Analysis of MS-Based Proteomics Data at the Posttranslational Modification and Peptidoform Level"
authors:
  - "Demeulemeester"
  - "Gebelin"
  - "Caldi"
year: "2024"
journal: "Molecular & cellular proteomics : MCP"
paper_kind: proteogenomic
pdf: "raw/inbox/papers/demeulemeester-2024-msqrob2ptm-differential-abundance-differential-usage.pdf"
topic: ptmanchor
tags:
  - "ptmanchor"
  - "proteomics"
  - "ptm"
  - "phosphoproteomics"
  - "cancer-proteomics"
themes:
  - "ptm-correction"
  - "kinase-signaling"
  - "cancer-proteomics"
pmid: "38154689"
doi: "10.1016/j.mcpro.2023.100708"
pmcid: "PMC10875266"

batch_ingest_status: pdf-text-extracted
batch_ingested_on: 2026-05-13
---
# msqrob2PTM: Differential Abundance and Differential Usage Analysis of MS-Based Proteomics Data at the Posttranslational Modification and Peptidoform Level

_Mol Cell Proteomics, 2024._

## Summary

In the era of open-modification search engines, more posttranslational modifications than ever can be detected by LC-MS/MS-based proteomics. This development can switch proteomics research into a higher gear, as PTMs are key in many cellular pathways important in cell proliferation, migration, metastasis, and aging. However, despite these advances in modification identification, statistical methods for PTM-level quantification and differential analysis have yet to catch up. This absence can partly be explained by statistical challenges inherent to the data, such as the confounding of PTM intensities with its parent protein abundance. Therefore, we have developed msqrob2PTM, a new workflow in the msqrob2 universe capable of differential abundance analysis at the PTM and at the peptidoform level. The latter is important for validating PTMs found as significantly differential. Indeed, as our method can deal with multiple PTMs per peptidoform, there is a possibility that significant PTMs stem from one significant peptidoform carrying another PTM, hinting that it might be the other PTM driving the perceived differential abundance. Our workflows can flag both differential peptidoform abundance (DPA) and differential peptidoform usage (DPU). This enables a distinction between direct assessment of differential abundance of peptidoforms (DPA) and differences in the relative usage of peptidoforms corrected for corresponding protein abundances (DPU). For DPA, we directly model the log2-transformed peptidoform intensities, while for DPU, we correct for parent protein abundance by an intermediate normalization step which calculates the log2-ratio of the peptidoform intensities to their summarized parent protein intensities. We demonstrated the utility and performance of msqrob2PTM by applying it to datasets with known ground truth, as well as to biological PTM-rich datasets. Our results show that msqrob2PTM is on par with, or surpassing the performance of, the current state-of-the-art methods. Moreover, msqrob2PTM is currently unique in providing output at the peptidoform level.

## Batch PDF Ingest Status

- Status: `pdf-text-extracted` on 2026-05-13.
- Local PDF: `raw/inbox/papers/demeulemeester-2024-msqrob2ptm-differential-abundance-differential-usage.pdf`.
- Extracted text length: 25,240 characters.
- Scope note: automated local-PDF text ingest for the 100-paper drug-response/phospho-global batch; not yet a manual full-text deep-dive.
- Evidence boundary: downstream scientific claims should use this page only after source-specific Key Points are manually promoted or rechecked against the local PDF.
- High-signal PDF snippets:
  - RESEARCH msqrob2PTM: Differential Abundance and Differential Usage Analysis of MS-Based Proteomics Data at the Posttranslational Modiﬁcation and Peptidoform Level Authors Nina Demeulemeester, Marie Gébelin, Lucas Caldi Gomes, Paul Lingor, Christine Carapito, Lennart Martens, and Lieven Clement Correspondence Graphical Abstra...
  - However, statistical methods for PTM-level quantiﬁcation and differential analysis are lacking.
  - To address this, we introduce msqrob2PTM, offering differential usage analysis at the PTM and peptidoform level.
  - Demonstrating efﬁcacy on simulated datasets and PTM-rich biological data, msqrob2PTM outperforms existing methods and uniquely provides output at the peptidoform level.
  - 2024, Mol Cell Proteomics 23(2), 100708 © 2023 THE AUTHORS.

## Key Points

_Awaiting deep-dive — automated abstract is in the Summary section above. The paper-specific Key Points, Methods, Limitations, and Open Questions will appear here once the full PDF has been read._


## Connections

- [Ptmanchor Topic Hub](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- [Ptmanchor Anchor](../analyses/ptmanchor-manuscript-anchor.md)

## Sources

- Local PDF: `raw/inbox/papers/demeulemeester-2024-msqrob2ptm-differential-abundance-differential-usage.pdf`
