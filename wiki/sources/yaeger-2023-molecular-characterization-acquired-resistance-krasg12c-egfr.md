---
title: "Molecular Characterization of Acquired Resistance to KRASG12C-EGFR Inhibition in Colorectal Cancer."
authors:
  - "Yaeger"
  - "Mezzadra"
  - "Sinopoli"
year: "2023"
journal: "Cancer Discovery"
doi: "10.1158/2159-8290.CD-22-0405"
pmid: "36355783"
pmcid: "PMC9827113"
paper_kind: research
pdf: "raw/inbox/papers/yaeger-2023-molecular-characterization-acquired-resistance-krasg12c-egfr.pdf"
pdf_status: full-text-read
claim_audit_status: acquired-resistance-patient-serial-ctdna
topic: resistance
tags:
  - resistance
  - acquired-resistance
  - kras-g12c
  - colorectal-cancer
  - ctdna
  - pmid-36355783
themes:
  - acquired-resistance
  - serial-ctdna
  - kras-amplification
  - erk-signaling
  - mtor-signaling
  - senescence
---
# Molecular Characterization of Acquired Resistance to KRASG12C-EGFR Inhibition in Colorectal Cancer.

Yaeger et al. use cell lines, PDX, patient samples, and serial ctDNA to show that acquired resistance to combined KRASG12C and EGFR inhibition in colorectal cancer is genetically heterogeneous but often converges on failure to suppress ERK signaling, with KRASG12C amplification acting as a recurrent resistance mechanism that changes dynamically with drug pressure.

## Key Points

- **Claim-audit classification:** acquired-resistance evidence with direct patient serial ctDNA support. This is stronger than a static resistant-sample paper for timing, but it is mainly genomic/ctDNA plus targeted pathway assays rather than broad proteogenomics/phosphoproteomics.
- **Clinical design:** cfDNA was collected from 12 colorectal cancer patients treated with adagrasib + cetuximab or sotorasib + panitumumab who initially had tumor regression and then developed radiographic or clinical progression.
- **Serial timing:** in 4 patients, ctDNA was collected during treatment approximately every 6 weeks, allowing resistance alterations to be tracked before and at clinical progression.
- **Genomic resistance landscape:** emergent resistance alterations included KRASG12C amplification, multiple KRAS secondary mutations, NRAS Q61 mutations, BRAF mutations/fusions, MEK1 mutations, RTK activation events such as MET amplification/fusion, RET fusion, EGFR mutations, and MYC amplification.
- **Dynamic finding:** many resistance alterations were low-frequency/subclonal and appeared or disappeared over treatment, whereas KRASG12C amplification rose with tumor markers and clinical progression in a recurrent pattern.
- **State-transition finding:** drug withdrawal in KRASG12C-amplified resistant cells induced oncogene-induced senescence with elevated mTOR pathway signaling; patient tissue collected after drug stop showed acquired high-level KRAS amplification, increased pERK, elevated pS6, and increased p16.
- **Use for this wiki project:** Yaeger 2023 is a key patient-time-axis paper. It supports the need for serial sampling to call acquired resistance, but it also shows why genomic timing alone leaves a functional-state question: ERK/mTOR/senescence states need pathway/protein/phospho readouts.

## Claim Audit

| Question | Audit result |
| --- | --- |
| Is this primary or acquired resistance? | Acquired resistance after initial response to KRASG12C-EGFR combination therapy. |
| Does it have patient time-axis data? | Yes. Serial ctDNA during treatment in a subset, plus pre/progression tissue evidence in at least one KRASG12C-amplified case. |
| Does it have broad proteogenomics/phosphoproteomics? | No. It uses genomic/ctDNA tracking plus targeted signaling assays/IHC/western blot rather than global proteome/phosphoproteome. |
| What claim is safe? | Serial genomic monitoring can reveal acquired resistance dynamics and distinguish low-frequency subclonal alterations from recurrent KRASG12C amplification under drug pressure. |
| What claim would overreach? | That phosphoproteomics has been shown here to classify acquired resistance states. The paper motivates that need but does not provide broad phosphoproteomic data. |

## Evidence Details

### Patient Serial ctDNA and Resistance Dynamics

The study evaluated cfDNA from 12 colorectal cancer patients treated with KRASG12C inhibitor plus EGFR antibody combinations. All had initial tumor regression followed by radiographic or clinical progression.

Emergent alterations at resistance included KRASG12C amplification, secondary KRAS mutations, NRAS mutations, BRAF/MEK pathway alterations, RTK events, and MYC amplification. Individual patients often had multiple alterations, consistent with polyclonal resistance.

In serial ctDNA from 4 patients, many alterations remained at low VAF and appeared before clinical resistance. The exception was KRASG12C amplification, which increased with clinical progression and tumor marker changes, making it a recurrent and higher-burden acquired resistance mechanism.

### Drug Withdrawal and State Transition

RW7213 resistant cells with high-level KRASG12C amplification were used to model drug withdrawal. Removing cetuximab-sotorasib increased MAPK and PI3K-mTOR pathway activation and induced a senescence-like state with beta-galactosidase positivity, low Ki-67, p16/p21/uPAR expression, and SASP cytokine accumulation.

Patient 12 had pretreatment and progression liver metastasis biopsies. The progression biopsy was collected 8 days after stopping KRASG12C and EGFR inhibitors and before new therapy. Sequencing/FISH showed acquired high-level KRAS amplification; pERK increased, pS6 became elevated, and p16 staining increased, supporting a similar state transition in patient tissue.

### Therapeutic Implication

After drug withdrawal, rechallenge suppressed MAPK signaling incompletely as a therapeutic strategy because mTOR signaling stayed elevated and apoptotic potential was not restored. AZD8055, an mTOR inhibitor proposed as a senolytic agent in this context, selectively inhibited pS6K/pS6 and reduced proliferation in drug-withdrawn KRASG12C-amplified resistant cells, whereas navitoclax did not show the same effect.

## Cancer Multiomics Project Relevance

- **For sampling design:** Yaeger 2023 is a strong example of why acquired resistance requires serial or paired sampling. Static resistant samples would miss the rise/fall of KRASG12C amplification under drug pressure.
- **For WGS/ctDNA layer:** the paper shows that acquired resistance can be polyclonal and low-frequency, so a single biopsy may underrepresent resistance diversity.
- **For functional-layer gap:** the main pathway conclusion is ERK suppression failure and mTOR/senescence transition, but the paper does not perform broad phosphoproteomics. It therefore motivates adding phosphoproteome/kinase assays to patient serial resistance designs.
- **For the current working hypothesis:** Yaeger supplies patient timing evidence; Solanki supplies broad functional-omics model evidence. Together they support a two-level review structure: patient time-axis proof plus mechanistic functional-state decomposition.

## Open Questions

- Which low-frequency ctDNA alterations actually drive resistant lesions versus mark transient subclones?
- Would paired pre/progression phosphoproteomics separate ERK-reactivated, RTK-reactivated, and mTOR/senescence states more cleanly than ctDNA alone?
- Can KRASG12C amplification dynamics be paired with tissue proteome/phosphoproteome to distinguish drug-pressure fitness from drug-withdrawal senescence?
- How general is the one-two punch idea of drug withdrawal plus senolytic/mTOR targeting across other acquired resistance contexts?

## Connections

- [Primary and Acquired Resistance Proteogenomics Ingest Map](../analyses/primary-acquired-resistance-proteogenomics-ingest-map.md)
- [Cancer Multiomics brief: Yaeger 2023](../analyses/cancer-multiomics-literature/yaeger-2023-molecular-characterization-acquired-resistance-krasg12c-egfr.md)
- [KRAS G12C Resistance and Ecosystem Remodeling](../concepts/kras-g12c-resistance-and-ecosystem-remodeling.md)
- [Cancer Resistance Convergence Framework](../syntheses/resistance-convergence-framework.md)

## Sources

- Local PDF: `raw/inbox/papers/yaeger-2023-molecular-characterization-acquired-resistance-krasg12c-egfr.pdf`
- PubMed: <https://pubmed.ncbi.nlm.nih.gov/36355783/>
- DOI: <https://doi.org/10.1158/2159-8290.CD-22-0405>
- PMC: <https://pmc.ncbi.nlm.nih.gov/articles/PMC9827113/>
