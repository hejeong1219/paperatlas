# Research Questions Queue (50)

50 scientific research questions across the three active research themes. Each question, once processed, expands a concept/analysis/synthesis page in `wiki/` (and the touched paper sources where relevant). Status: `[ ]` pending, `[x]` done, `[~]` in progress.

## ptmanchor — PTM correction & kinase signaling (17)

- [x] **Q1.** Why does protein abundance confound phosphosite quantification, and how often is a "raw-up" phosphosite actually a protein-driven artifact in CPTAC cohorts? → created [concepts/ptm-correction-confounding-foundations.md](../concepts/ptm-correction-confounding-foundations.md)
- [ ] **Q2.** When does a single global protein-to-PTM correction (subtraction) outperform a site-specific coupling model, and when does it fail? → analyses page
- [ ] **Q3.** How much does PTM correction change kinase activity inference (KSEA, NetworKIN, CoPheeKSA), and which kinases gain or lose hits most? → analyses page
- [ ] **Q4.** Are acetylation and ubiquitylation as protein-confounded as phosphorylation, or do they show different coupling distributions? → concept page
- [ ] **Q5.** What is the cross-cohort reproducibility of the same phosphosite call (corrected vs uncorrected) across CPTAC tumor types? → analyses page
- [ ] **Q6.** Does corrected phosphoproteome data improve patient stratification (subtype clustering, survival) over raw data? → analyses page
- [ ] **Q7.** Which dark phosphosites become "rescued" by correction + network propagation (CoPheeMap)? → analyses page
- [ ] **Q8.** How do RNA-protein-PTM cross-layer correlations differ between cancer types, and what does that imply for layer-aware target discovery? → concept page
- [ ] **Q9.** Should kinase activity inference be done per-cohort or pan-cancer combined, and what's the trade-off? → analyses page
- [ ] **Q10.** What is the false discovery rate of "PTM-specific" calls in real CPTAC data once linear-model assumptions are tested? → analyses page
- [ ] **Q11.** When tumor-normal pair sample size is small (<20), does ptmanchor break down and how should it be handled? → concept page
- [ ] **Q12.** Are kinase-substrate associations from CoPheeKSA biased by the same protein-abundance confound that ptmanchor fixes? → analyses page
- [ ] **Q13.** How do TKI-treatment response phosphosites (e.g., osimertinib, palbociclib) change after correction, and does correction reveal new mechanisms of resistance? → analyses page
- [ ] **Q14.** Can ptmanchor-corrected phosphoproteome data identify novel druggable kinases that are missed by uncorrected data? → analyses page
- [ ] **Q15.** What's the right way to handle missing values in PTM data when fitting per-site coupling models? → concept page
- [ ] **Q16.** How do PTM-correction approaches differ in their handling of stoichiometry (occupancy %)? → concept page
- [ ] **Q17.** Do post-translational modifications other than phospho/acetyl/ubiquitin (e.g., O-GlcNAc, methylation, glycosylation) show similar confounding? → concept page

## B-cell neoantigen (17)

- [ ] **Q18.** Are tumor B cells neoantigen-specific or self-reactive, and what is the evidence in human studies? → concept page
- [ ] **Q19.** Does TLS maturity (germinal center presence, CD23⁺ B cells) predict ICB response better than TLS density alone? → concept page (b-cells-and-tertiary-lymphoid-structures)
- [ ] **Q20.** Can mature TLS convert immune-cold tumors to hot, and what are the documented interventions to induce TLS? → concept page
- [ ] **Q21.** Do BCR repertoire features (clonality, isotype switching, mutation load) predict ICB response, and how do they map to T-cell repertoire? → analyses page
- [ ] **Q22.** What is the role of plasma cells vs memory B cells in tumor microenvironment — distinct functional axes or a continuum? → concept page
- [ ] **Q23.** Does anti-CD20 (rituximab) abrogate ICB benefit in melanoma or other TLS-rich cancers? → analyses page
- [ ] **Q24.** Is CXCL13 a master regulator of TLS formation, and is targeting it a viable intervention? → concept page
- [ ] **Q25.** How do public neoantigens (KRAS G12D, TP53 R175H, MSI frameshifts) compare to personalized neoantigens for B-cell engagement? → analyses page
- [ ] **Q26.** Are noncanonical / cryptic peptides (TE-derived, lncRNA, intronic) functionally targetable by B cells? → concept page
- [ ] **Q27.** Personalized neoantigen vaccines (mRNA-4157, GNOS-PV02): is the response T-cell-only or do humoral arms also engage? → analyses page
- [ ] **Q28.** In immune-cold tumors (HCC, PDAC), does B-cell signature retain prognostic value, or only in hot tumors? → analyses page
- [ ] **Q29.** Does TLS spatial location (peritumoral, intratumoral, invasive margin) change its functional role? → concept page
- [ ] **Q30.** What's the link between TLS biology and clonal hematopoiesis / age-related immune drift? → concept page
- [ ] **Q31.** How do BCR repertoires in tumor compare across cancer types — convergent or tissue-specific? → analyses page
- [ ] **Q32.** Is HLA-II expression on tumor cells required for productive B-cell help, and how does HLA-II loss affect TLS? → concept page
- [ ] **Q33.** Can spatial transcriptomics quantify TLS function (active vs inactive) beyond density measurement? → analyses page
- [ ] **Q34.** Do regulatory B cells (Bregs) explain a subset of TLS-rich, ICB-failing tumors? → concept page

## Cancer resistance (16)

- [ ] **Q35.** Does the convergence framework (visibility / access / effector dysfunction) hold across all therapy classes — checkpoint, CAR-T, BsAb, ADC, targeted, endocrine, PARP? → synthesis page
- [ ] **Q36.** Do EGFR, KRAS, ESR1, and PARP resistance share an immune-evasion endpoint, and is the mechanism convergent or independent? → analyses page
- [ ] **Q37.** Antigen loss (CD19, CD20, BCMA, HER2): is it a clonal selection event, a transient adaptation, or both? → concept page (antigen-loss-lineage-switch-and-target-escape)
- [ ] **Q38.** What is the precise mechanism by which STK11/KEAP1 co-mutation creates an immune-cold phenotype in lung adenocarcinoma? → concept page
- [ ] **Q39.** Are JAK1/2 mutations more often a primary or acquired resistance mechanism to checkpoint blockade, and how do the mutation patterns differ? → analyses page
- [ ] **Q40.** Does ESR1 mutation in endocrine-resistant breast cancer drive immune surveillance disruption beyond ER signaling? → analyses page
- [ ] **Q41.** Does PARP inhibitor resistance silence the cGAS-STING pathway, and is this reversible? → analyses page
- [ ] **Q42.** Do CDK4/6 inhibitors trigger senescence and improved immunogenicity together, or are these decoupled? → concept page (cdk46-inhibition-senescence-and-tumor-immunogenicity)
- [ ] **Q43.** What antiandrogen-driven changes in the prostate immune microenvironment shape ICB resistance? → concept page (ar-pathway-resistance-and-immune-context-in-prostate-cancer)
- [ ] **Q44.** How do CAR-T resistance and bispecific-antibody resistance differ mechanistically when the target is the same (CD20 vs CD19)? → analyses page
- [ ] **Q45.** TGF-β blockade in clinic (bintrafusp alfa) — why did it fail despite strong preclinical rationale? → analyses page
- [ ] **Q46.** Are cancer-associated fibroblasts (CAFs) primary drivers of ICB resistance or downstream amplifiers? → concept page (stromal-and-myeloid-barriers-to-immunotherapy)
- [ ] **Q47.** Gut microbiota and ICB response: which species are most replicated as response-promoting, and what's the mechanism? → concept page (gut-microbiota-and-immunoresistance)
- [ ] **Q48.** Among TMB, PD-L1, MSI-H, HLA evolutionary divergence, GEP — which biomarker has the strongest stand-alone predictive value, and which combinations beat single biomarkers? → analyses page (biomarkers-and-response-models)
- [ ] **Q49.** Does ESR1 + CDK4/6 combined resistance generate a distinct immune phenotype (e.g., NE differentiation), and is this targetable? → analyses page
- [ ] **Q50.** What does "immune editing" look like at single-cell resolution in human ICB-treated tumors over time, and which clones are eliminated vs. selected? → analyses page

## Status

- Total: 50
- Done: 0
- In progress: 1 (Q1, demonstrative example below)
- Pending: 49

## Next-step automation

A wakeup loop processes the next pending question every ~30 minutes:
1. Read related paper sources + existing concept/analysis pages
2. Synthesize an answer
3. Update the target page (or create a new one)
4. Append a log entry in `wiki/_meta/log.md`
5. `git push` so GitHub Pages reflects the change
