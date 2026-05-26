---
title: Antigen Loss, Lineage Switch, and Target Escape
tags:
  - concept
  - resistance
  - immunotherapy
themes:
  - antigen-loss
  - lineage-switch
  - target-escape
---

# Antigen Loss, Lineage Switch, and Target Escape

This concept page tracks how cancers evade target-directed immunotherapies by removing, reshaping, down-modulating, or phenotypically abandoning the molecule being targeted.

## Key Points

- Target escape can occur through irreversible gene disruption, alternative splicing, antigen-density reduction, or lineage reprogramming.
- In CD19-directed therapy, both molecular deletion/truncation and lineage switch are now well-supported relapse routes.
- These mechanisms matter because they push treatment design away from single-antigen dependence.
- Engineering responses include alternative epitope targeting, dual-target or multispecific systems, lower antigen-density thresholds, and logic-gated designs.

## Observation Unit Standard (genome → surface)

When comparing CAR-T, bispecific antibodies, and ADC papers, the “target” is often measured at different layers. Summaries should keep layers explicit.

| Layer | Typical assays | What it can prove | Common failure mode |
| --- | --- | --- | --- |
| DNA | WES/WGS, targeted sequencing, CNV calling | gene disruption, LOH, clonal selection | misses splicing, RNA regulation, protein trafficking |
| RNA | bulk RNA-seq, scRNA, isoform analysis | expression downregulation; alternative splicing | RNA does not guarantee surface protein |
| Protein (bulk) | proteomics, WB | abundance changes | does not guarantee surface density/epitope availability |
| Surface / epitope | flow cytometry, IHC, imaging; antigen density quant | what the therapy can physically bind | can miss tumor heterogeneity and sampling bias |
| Phenotype / lineage | immunophenotyping; single-cell states | lineage switch, dedifferentiation | phenotype may change without a single genetic driver |

## Extraction Table (for source pages)

For each target-escape paper, add a short table or bullet answers:

- Therapy type: `CAR-T` / `bsAb` / `ADC` / other
- Escape mode(s): `LOF mutation`, `splicing`, `CN loss`, `density down`, `lineage switch`, `antigen masking`, `trogocytosis`, `other`
- Evidence tier: DNA / RNA / protein / surface / longitudinal / functional
- Clinical context: indication, line of therapy, on-treatment timepoint(s)

## Connections

- [Convergence of Acquired Mutations and Alternative Splicing of CD19 Enables Resistance to CART-19 Immunotherapy](../sources/sotillo-2015-cd19-mutations-alternative-splicing-cart19.md)
- [Genetic mechanisms of target antigen loss in CAR19 therapy of acute lymphoblastic leukemia](../sources/orlando-2018-target-antigen-loss-car19-therapy.md)
- [The dynamic evolution of lineage switch under CD19 CAR-T treatment in non-KMT2A rearranged B-ALL patients](../sources/qiu-2025-lineage-switch-cd19-cart-treatment-ball.md)
- [CAR immune cells: design principles, resistance and the next generation](../sources/labanieh-2023-car-immune-cells-design-principles-resistance.md)

## Sources

- [Convergence of Acquired Mutations and Alternative Splicing of CD19 Enables Resistance to CART-19 Immunotherapy](../sources/sotillo-2015-cd19-mutations-alternative-splicing-cart19.md)
- [Genetic mechanisms of target antigen loss in CAR19 therapy of acute lymphoblastic leukemia](../sources/orlando-2018-target-antigen-loss-car19-therapy.md)
- [The dynamic evolution of lineage switch under CD19 CAR-T treatment in non-KMT2A rearranged B-ALL patients](../sources/qiu-2025-lineage-switch-cd19-cart-treatment-ball.md)
- [CAR immune cells: design principles, resistance and the next generation](../sources/labanieh-2023-car-immune-cells-design-principles-resistance.md)
