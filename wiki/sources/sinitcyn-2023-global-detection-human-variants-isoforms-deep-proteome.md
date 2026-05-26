---
title: "Global detection of human variants and isoforms by deep proteome sequencing"
authors:
  - "Pavel Sinitcyn"
  - "Alicia L. Richards"
  - "Robert J. Weatheritt"
  - "Daniel R. Brademan"
  - "Evgenia Shishkova"
  - "Hunter Marx"
  - "Jesse G. Meyer"
  - "Anna Sophie Hebert"
  - "Michael S. Westphall"
  - "Benjamin J. Blencowe"
  - "Jürgen Cox"
  - "Joshua J. Coon"
year: 2023
journal: "Nature Biotechnology"
doi: "10.1038/s41587-023-01714-x"
url: "https://www.nature.com/articles/s41587-023-01714-x"
pdf: "raw/inbox/papers/sinitcyn-2023-global-detection-human-variants-isoforms-deep-proteome.pdf"
paper_kind: resource
cancer_types:
  - pan-cancer
modalities:
  - deep-proteome-sequencing
  - multi-protease-proteomics
  - etd-cad-hcd-fragmentation
  - proteogenomics
  - rna-seq
themes:
  - proteoform
  - alternative-splicing-detection
  - single-amino-acid-polymorphism
  - sap-variant-detection
  - multi-protease-strategy
  - sequence-coverage
  - encode-cell-lines
  - de-novo-protein-assembly
  - peptide-spectrum-match
  - methodology-reference
topic: cancer-multiomics-literature
discovery_method: user-shared
tags:
  - source
  - deep-proteome
  - proteoform
  - alternative-splicing
  - sap-variants
  - multi-protease
  - encode
  - methodology-resource
  - nature-biotechnology-2023
---

# Global detection of human variants and isoforms by deep proteome sequencing

_Nature Biotechnology 41:1776–1786, December 2023 (Coon lab, University of Wisconsin–Madison + Cox lab, Max Planck Institute of Biochemistry + Blencowe lab, University of Toronto. Co-first authors: Pavel Sinitcyn + Alicia L. Richards; co-corresponding: Jürgen Cox + Joshua J. Coon)._ DOI: [10.1038/s41587-023-01714-x](https://doi.org/10.1038/s41587-023-01714-x) · Open access cc-by · ProteomeXchange/MassIVE: PXD024364 · Online resource: [deep-sequencing.app](https://deep-sequencing.app)

## Summary

Sinitcyn, Richards 등은 ENCODE 6개 세포주(H1-hESC, HeLa S3, HepG2, GM12878, K562, HUVEC)에 6종 단백분해효소(trypsin, LysC, LysN, AspN, GluC, chymotrypsin)와 3종 fragmentation(HCD/CAD/ETD)을 조합하여 24–80 fraction 고-pH RP 분획 + Orbitrap Tribrid 측정으로 단일 매트릭스 deep proteome reference를 구축했다. 총 2,491 raw files, ~164M MS/MS spectra, 1% FDR에서 17,717 proteins / 1,119,510 unique peptides / 12,151,708 PSMs를 동정했고, 평균 단백 sequence coverage가 79.2%(median; 790 proteins에서 100%)로, 트립신 단독 56.5% 대비 큰 폭의 증가가 보고됐다. 이 깊이를 활용하여 (i) SAP(single amino acid polymorphism) 검출 수가 트립신 대비 두 배로 증가했고(총 5,060 SAPs across cell lines, 평균 transcriptome SNP의 73%가 단백질 수준에서 확인), (ii) 검출되지 않은 SAP에서 SIFT/PolyPhen-2 deleterious 변이가 통계적으로 enriched(P=2e-8, 1.1e-12)되어 protein instability 가설을 지지했으며, (iii) GENCODE annotation 기준 13,450개 AS event 중 4,608(34.3%)을 적어도 한 isoform에서 검출, 6,145개 양방향 event 중 1,141(18.6%)에서 양 isoform 모두 검출, frame-preserving 비율이 안정 발현 transcript에서 64%로 보고됐다. (iv) XGBoost classifier로 transcript abundance, PSI(percent spliced-in), frame status를 핵심 feature로 AS 검출 가능성을 ROC AUC 0.83으로 예측, PSI ~33% 부근이 단백체 검출 최적이라는 비-단조 패턴을 도출했다. (v) De novo SOAPdenovo-Trans assembly에서 35,480 scaffold 중 16,496(~47%)이 9,695 protein group에 정확 매칭됨을 보고했다. 저자 직접 표현으로 "가장 깊은 단백체 지도"이자 "이 정도 깊이의 SAP variant proteogenomic study"는 처음이며, multi-enzyme 전략을 "global-scale proteoform 검출에 적용한 사례는 보고된 바 없다"고 명시했다. 데이터·코드 모두 PXD024364 / GitHub coongroup/DeepProteomeSequencing-Software / deep-sequencing.app 으로 공개된다.

## Key Points

- **목적 / novelty 주장 (저자 표현 그대로)**: "deepest proteomics map collected to date"로 모든 단백질군의 multi-isoform·SAP·AS event를 동일 매트릭스에서 표면화. SAP-aware proteogenomic study가 이 정도 깊이로 수행된 적 없으며, multi-enzyme 전략을 global-scale proteoform 검출에 적용한 사례는 본 논문 시점까지 보고되지 않았다고 명시.
- **샘플 매트릭스 (ENCODE 6세포주)**: H1-hESC(embryonic stem; Thomson lab 기증), HeLa S3(자궁경부암; ATCC CCL-22), HepG2(간암; ATCC HB-8065), GM12878(B-lymphoblastoid; Coriell GM12878-K), K562(CML; ATCC CCL-243), HUVEC(제대정맥내피세포; Lonza CC-2517). ENCODE 표준 세포주여서 동일 RNA-seq(SRP014320)과 직접 비교 가능.
- **단백분해효소 (6종)**: trypsin(참조), LysC, LysN, AspN, GluC, chymotrypsin. 각 효소별 digestion 조건 명시(예: chymotrypsin 1 M urea, GluC 0.5 M urea, LysN 4 M urea 4 h at 37 °C 등) — non-tryptic cleavage 분포로 트립신이 놓치는 C-term/N-term 영역 보강.
- **분획 + LC**: 고-pH RP fractionation(60-min gradient at 0.45–0.8 ml/min). 24–80 fractions/run. H1-hESC trypsin 만 SCX(polysulfoethyl-aspartamide column 9.4 × 200 mm²) 4분획 후 HpH-RP 2D 분획. nanoLC RP column 35 cm × 75 μm BEH C18 1.7 μm(Waters), 60 °C, 100-min gradient.
- **MS 측정 + fragmentation**: Thermo Orbitrap Fusion + Lumos Tribrid. HCD(주로 트립신), CAD(chymotrypsin + 일부 저질량 precursor), ETD(LysC/LysN/AspN/GluC/chymotrypsin non-tryptic; +2는 EThcD 25% supplemental). 정밀 charge-state-specific ETD reaction times: +3 40 ms, +4 22 ms, +5 14 ms, +6 10 ms, +2 70 ms. Precursor scan 60,000 또는 120,000 resolution; isolation 0.7 Th; top-speed 3 또는 5 s cycles.
- **데이터 스케일**: 2,491 raw files. ~20M MS spectra, ~164M MS/MS spectra. 1% FDR (실 PSM 0.06% / peptide 0.4% / protein 0.99%)에서 PSMs 12,151,708 / unique peptides 1,119,510 / proteins 17,717. Median protein sequence coverage 79.2% (790 proteins 100% coverage).
- **트립신 단독 vs 결합 비교**: trypsin 단독 17,631 proteins / median coverage 56.5%. 6-protease 결합은 +86 proteins(modest)에 그치지만 median coverage가 56.5% → 79.2%로 약 +22.7%p 상승. MassIVE all-tryptic 대비 multi-enzyme 추가 매핑 잔기는 +34.4% (2.12M residues).
- **SAP 검출 — 전체 결과**: 6 세포주 합계 5,060 SAPs. 세포주별 median으로 transcriptome SNP의 73%가 단백질 수준에서도 직접 검출. Multi-enzyme 사용 시 SAP 검출 수가 트립신 단독 대비 약 2배 증가. HeLa S3 referenece에서 ~4.5M total SNPs / ~30K coding / 4,740 nonsynonymous(reference 라인).
- **SAP 검출 — instability 가설 (저자 명시)**: 미검출 SAP가 검출된 SAP에 비해 SIFT "deleterious" 비율 enriched (P=2e-8), PolyPhen-2 "probably damaging"도 enriched (P=1.1e-12). 저자 해석: deleterious 변이가 단백질 instability/turnover 가속화로 인해 MS-검출 가능 단백 풀에서 underrepresented되는 가설을 지지.
- **AS 검출 — 전체 결과 (GENCODE 기준)**: 단일-isoform 검출 가능한 AS event 13,450개 중 4,608(34.3%)을 적어도 한 isoform에서 식별. 양방향 검출 가능한 6,145 event 중 1,141(18.6%)에서 alternative 양쪽 모두 검출. 이는 본문에서 "AS가 단백질 수준에서 광범위함"의 근거로 사용되며, ribosome-profiling 기반 선행 연구(Weatheritt 2016)와 일치한다고 저자가 명시.
- **AS 검출 — frame-preserving 비율**: 안정 발현 transcript의 frame-preserving AS event 64%. Low PSI 또는 frame-shift event는 단백 수준 검출 비율이 낮음. NMD-coupled frame-shift AS의 검출 빈도가 낮은 것이 단순 트립신 cleavage 한계가 아닌 transcript turnover 의 영향임을 뒷받침.
- **AS 검출 — XGBoost 예측 모델**: ROC AUC 0.83. Top features: transcript abundance, PSI(percent spliced-in), frame status. PSI ~33%에서 단백체 검출 확률이 최대인 비-단조 패턴을 발견 (very-low PSI는 단백 stoichiometry 부족, very-high PSI는 isoform-distinguishing peptide 부재로 검출 어려움).
- **AS 검출 — 트립신만 사용한 선행 연구 반박**: 본문은 "AS가 proteome complexity의 주요 source가 아니다"라고 결론낸 두 선행 리뷰(Tress 2017; Blencowe 2017)와 트립신-only 검출 한계 분석(Wang 2018)을 직접 인용하여 반박. multi-protease + deep fractionation을 적용하면 AS 검출이 대폭 확장된다고 주장.
- **De novo proteome assembly**: 모든 PSM의 nucleotide 역번역 → SOAPdenovo-Trans-31mer (k-mer 23, min contig 100 = 34 aa) → 35,480 scaffold. 이 중 16,496(~47%)이 9,695 protein group sequence와 brute-force string match 성공. 단백체 단독으로 reference DB에 없이도 부분적 proteome reconstruction이 가능함을 시연 (de novo protein assembly proof-of-concept).
- **사용 도구 stack**: MaxQuant v1.5.7.5 + Andromeda search engine. Database = UniProt canonical(UP000005640_9606, release 2017_02) + UniProt isoform(UP000005640_9606_additional) + Ensembl canonical(GRCh38.pep.all release 86) + Ensembl isoform(GRCh38.pep.abinitio). Precursor tolerance 20 p.p.m. first / 4.5 p.p.m. main, product tolerance 0.35 Da. Cysteine carbamidomethylation 고정, Met oxidation + N-term acetylation 변이. PSMs + protein groups 모두 sequential 1% FDR.
- **PSM nucleotide 역번역 변이 검출**: MaxQuant Variation extraction(Tools/Variation extraction) 기준 — total read depth ≥10, mutated read ≥5, mutation frequency ≥15%, base/map quality ≥13(multi-mapped 자동 필터). protein.fa 파일에 nonsynonymous 변이를 inline header로 기록 → 같은 MaxQuant 검색에서 "Mutated" 컬럼이 peptides.txt에 추가됨.
- **RNA-seq 정합**: ENCODE SRP014320(6 cell lines paired-end). trimmomatic 0.36 default → STAR 2.5.3a → GRCh38 (Ensembl release 91) → SAMtools 1.6 sorting. proteomics와 비교는 Perseus 1.6.14.0에서 row-wise log + pseudocount 1 + z-score 정규화 후 imputation(normal distribution width 0.3, shift 1.8). Component 1(분산 27.8%)은 proteomics/transcriptomics 차이를 설명하므로 제외하고 PCA 비교.
- **저자 명시 한계 + 윤리·임상 적용 제언**: 본 데이터셋은 6 세포주에 한정되므로 normal tissue/disease tissue로의 확장에는 추가 검증 필요(저자 명시). 임상 단백체 측면에서는 Mann 2021(ref 71)의 ethical principles, Fierro-Monti 2022(ref 72)의 "identifying individuals using proteomics"를 인용하며 임상 적용 시 개인 식별성·동의 등 추가 고려가 필요함을 시사.
- **공개 자산**: ProteomeXchange / MassIVE PXD024364(raw + MaxQuant output). 변이·아이소폼 인터랙티브 검색: [deep-sequencing.app](https://deep-sequencing.app) (D.R. Brademan 구축). Code: [github.com/coongroup/DeepProteomeSequencing-Software](https://github.com/coongroup/DeepProteomeSequencing-Software) + MaxQuantAnalyzer (github.com/cwenger/cwenger.github.io). Two highlighted spectra USIs: `mzspec:PXD024364:20160115_alr_CompleteHumanProteome_HUVEC_chymo_CAD_fr14:scan:50088:CMAVCGSAIPTTAASTPDAVDKY/2` + `mzspec:PXD024364:HeLaS3_trypsin_19_140824180249:scan:34854:DPVKLPTTAASTPDAVDK/2`.
- **이해 관계 / Funding**: J.J.C.는 Thermo Fisher Scientific, 908 Devices, Seer의 컨설턴트(MS 장비/시약 회사). 본 연구는 NIH P41108538(NCQBCS) + R35GM118110(Coon) + T32HG002760(A.L.R., Genomic Sciences Training Program) + Morgridge Interdisciplinary Postdoctoral Fellowships(P.S., D.R.B.) + Canadian Institutes for Health Research(Blencowe) 지원. Open access funding은 Max Planck Society.

## Methods

- **샘플 조제**: 6세포주 별도 ATCC/Coriell/Lonza 표준 배지에서 >70% confluency까지 배양 → 300g 5 min 4 °C 원심 → PBS 세척 → −80 °C 보관. Lysis = 8 M urea + 50 mM Tris pH 8 + 5 mM CaCl2 + 30 mM NaCl + protease/phosphatase inhibitor (Roche). 4 cycles sonication 4 °C (20 s on/off). BCA assay 정량.
- **환원/알킬화 → digestion**: 5 mM DTT 45 min 55 °C → 15 mM iodoacetamide 30 min 암실 → 5 mM DTT quench. 효소별 조건:
  - Trypsin: 20 µg, 1 M urea, RT overnight
  - LysC: 20 µg, 4 M urea, RT overnight
  - LysN: 20 µg, 4 M urea, 37 °C 4 h
  - GluC: 25 µg, 0.5 M urea, RT overnight
  - Chymotrypsin: 12.5 µg, 0.2% formic acid in 1 M urea, RT overnight
  - AspN: 6 µg, RT overnight
  - 공통: TFA quench → C18 Sep-Pak 100 mg desalt
- **High-pH RP fractionation**: 5-µm C18 250 × 4.6 mm² (Phenomenex) Surveyor LC quaternary pump(@1 ml/min) 또는 1.7-µm BEH 50 × 1 mm² Dionex UltiMate 3000(@0.45 ml/min). Buffer A 20 mM ammonium formate pH 10 / Buffer B 20 mM ammonium formate pH 10 in 80% ACN, 또는 ammonium bicarbonate 변형. **H1-hESC trypsin 추가 SCX**: polysulfoethyl-aspartamide 9.4 × 200 mm² + Surveyor LC @3 ml/min, 8–25 min에서 4 fraction 채취 후 HpH-RP 재분획.
- **LC-MS/MS**: 35 cm × 75 μm 인-house bare-fused silica capillary RP column + laser-pulled electrospray tip + 1.7-µm BEH C18 130-Å Particles (Waters), 60 °C column heater. Mobile phase A = water + 0.2% FA, B = 70% ACN + 0.2% FA + 5% DMSO. 100-min gradient, 300–350 µl/min. Thermo Orbitrap Fusion 또는 Lumos.
- **MS 설정 — 모드별**:
  - **HCD (트립신 전체)**: precursor 300–1,500 m/z, 60k–120k resolution. Fusion 5e5 / Lumos 1e6 ion-target. Quadrupole 0.7 Th isolation, NCE 30, turbo scan(ion trap detection). MS/MS max IT 25–35 ms (일부 더 김), 1e4 ion target. Charge state 2–8, dynamic exclusion 15 s ± 10 ppm. Monoisotopic precursor selection ON, top-speed 3/5 s cycles.
  - **HCD + CAD 분기 (일부 분석)**: 500 m/z 이상 HCD, 미만 CAD NCE 30.
  - **ETD (LysC/LysN/AspN/GluC/chymotrypsin)**: precursor 200–800 m/z, 60k–120k resolution. Charge-state-specific reaction times +3 40 ms / +4 22 ms / +5 14 ms / +6 10 ms / +2 70 ms. +2 precursors는 EThcD 25% supplemental activation. Selection 순서 +3>+4>+5>+6>+2. Ion trap fragment 검출.
  - **CAD (chymotrypsin 별도)**: 300–1,500 m/z, NCE 30, turbo scan, IT 25–35 ms+, 1e4 target.
- **Database search (MaxQuant v1.5.7.5)**: Andromeda 검색. 2,491 raw files 동시 분석. DB UniProt canonical/isoform(UP000005640_9606, 2017_02) + Ensembl canonical/isoform(GRCh38, release 86). Specific cleavage, missed cleavage 2(chymotrypsin 4). Fixed Cys carbamidomethyl, variable Met ox + protein N-term acetyl. PSM + protein 1% FDR sequential (실제 0.06% / 0.99%). protein group 'Only identified by site' / 'Reverse' / 'Contaminant' 필터. Gene locus는 UniProt + Ensembl BioMart로 매핑.
- **Sequence coverage 측정**: 커스텀 C# (MaxQuantAnalyzer; github.com/cwenger/cwenger.github.io) — 각 protein group의 첫 major protein sequence에서 peptide 발견 위치를 효소 specificity 무시한 brute-force string match로 누적, 고유 아미노산 residue 수 / 총 residue 수로 계산. MaxQuant 내장 coverage와 cross-validate.
- **Spectra 시각화**: 웹기반 Interactive Peptide Spectra Annotator (Brademan 2019).
- **De novo proteome assembly**: evidence.txt에서 PSM 추출 → 'Potential contaminant'/'Reverse' 필터 → nondegenerate codon table로 nucleotide 역번역 → FASTA → SOAPdenovo-Trans-31mer(k-mer 23 = min 8 aa, min contig 100 = 34 aa). Scaffold ↔ reference proteome brute-force string match.
- **RNA-seq 정합 + 변이 추출**: ENCODE SRP014320 paired-end → trimmomatic 0.36(default) → STAR 2.5.3a → GRCh38 Ensembl 91 → SAMtools 1.6. Variation extraction (MaxQuant 내장 Tools): read depth ≥10, mutated reads ≥5, mutation freq ≥15%, base/map quality ≥13. protein.fa 출력 → 다시 MaxQuant에 입력해서 peptides.txt에 'Mutated' / 'Mutation names' 컬럼 생성.
- **AS 검출 — 그래프 알고리즘**: gene graph(노드=엑손 시작/끝, 엣지=엑손-엑손 junction + intra-exon) 기반 local subgraph 형식의 splicing event 정의(Sammeth 2009 알고리즘 변형). protein coordinate를 genome coordinate로 역변환(intron-exon 구조 고려), Perseus plugin으로 구현(Supplementary Fig. 6).
- **AS 검출 — XGBoost binary classifier**: XGBoost 1.5.0. 7-fold CV + RandomizedSearchCV(sklearn 0.24). 선택 파라미터: learning rate 0.05, L1 1.15, L2 4.0, min child weight 2.0, max depth 3, gamma 2.0, colsample 0.3, subsample 0.65, scale_pos_weight 4.44.
- **단백체-전사체 정합**: Perseus 1.6.14.0에서 raw read count log+pseudocount 1 + z-score, iBAQ proteomics는 cell line별 (fraction/fragmentation/protease 합산)→log→z-score→missing imputation(normal distribution width 0.3, downshift 1.8). PCA 비교 시 component 1(27.8% 분산)은 proteomics vs transcriptomics 차이로 해석 가능해 제외하고 component 2 이후 사용.

## Cancer Multiomics Project Relevance

논문이 직접 보고한 사실과 한미암 프로젝트 축과의 직접 매칭만 기록. 응용·추론은 별도 분석으로 분리.

- **데이터 레이어 직접 매칭 (논문 보고)**: 본 논문은 cancer 코호트가 아닌 ENCODE 표준 6세포주의 reference deep proteome. 환자 cohort 매칭은 불가. 그러나 한미암 프로젝트에서 "단백체 깊이"가 phosphoproteome·neoantigen·proteoform 해석에 필요한 단계에서 (a) DB augmentation 자료(deep-sequencing.app 변이/아이소폼 카탈로그), (b) multi-protease 사용 의사결정 reference, (c) ENCODE 세포주 단백체 baseline 으로 활용 가능. 임상 코호트 자체는 본 논문이 다루지 않음.
- **SAP/proteoform 검출 framework (논문 보고)**: WGS/WES nonsynonymous 변이가 단백 수준에서 어느 정도 검출되는지를 ENCODE 세포주에서 처음으로 정량(median 73% transcriptome SNP↔proteome 매칭). 한미암 환자 코호트의 somatic SAP 검출률 기대치를 산정할 때 reference로 인용 가능 — 단, 본 결과는 normal 세포주 SNP(germline) 기준이므로 somatic mutation으로 직접 외삽은 저자도 시사하지 않음.
- **AS 검출 framework (논문 보고)**: 13,450 AS event 중 34.3% / 6,145 양방향 event 중 18.6%만 단백 수준에서 검출됨을 보고. 이는 한미암 코호트에서 RNA-seq AS 후보를 단백체로 validation할 때 기대 검출률의 lower-bound reference로 사용 가능. XGBoost 모델 feature(transcript abundance, PSI, frame status)는 한미암 splice-derived neoantigen 후보 ranking 시 transcript-level pre-filter 기준으로 인용 가능.
- **Multi-enzyme 전략의 비용-효익 (논문 보고)**: trypsin 단독 17,631 proteins / median coverage 56.5% → 6 protease 결합 17,717 proteins(+86) / 79.2%. 즉 protein 식별 수 증가는 modest이나 sequence coverage는 +22.7%p로 SAP/AS 검출에 결정적. 한미암 단백체 코호트에서 multi-protease 도입 여부를 평가할 때 trade-off 수치 reference.
- **사용 도구의 직접 참조 가능성**: MaxQuant Variation extraction(WGS 변이 → custom DB → MS search) 방법론은 한미암 WGS-단백체 통합 시 직접 적용 가능한 워크플로 — 단, MaxQuant 1.5.7.5는 2017년대 빌드이며 후속 MaxQuant 2.x 또는 DIA 워크플로로 대체 시 별도 검토 필요. SOAPdenovo-Trans-31mer + brute-force PSM 매칭은 reference-DB-free proteoform discovery에 한정된 proof-of-concept.
- **저자 명시 한계 (논문 보고)**: 6 ENCODE 세포주 한정 — normal tissue, disease tissue, FFPE biopsy로의 외삽은 별도 검증 필요. multi-protease + deep fractionation은 200–500 mass-spec hour 수준의 자원이 필요한 reference-quality 측정이므로 임상 routine pipeline으로 직접 transfer 불가. SAP underdetection이 protein instability를 시사하지만 functional validation은 본 논문 범위 외.
- **한미암 적용 한계 (본 페이지 명시)**: 본 논문은 cancer 임상 코호트가 아니며 폐암-특이 적용 사례를 보고하지 않음. 한미암 lung cancer 단백체 결과를 본 논문 수치에 직접 비교하려면 (a) sample-type 차이(세포주 vs 환자 tumor), (b) total mass-spec hour 차이, (c) MaxQuant 버전·DB 빌드 차이를 명시해야 함.

## Connections

- [Lehe 2026 — MS Instrumentation for Alternative Protein Isoforms (Review)](./lehe-2026-mass-spectrometry-alternative-protein-isoforms-review.md) — Sheynkman lab 리뷰가 본 논문(Sinitcyn 2023)을 "ultra-deep DDA / 4,608 AS events" 대표 사례로 인용. AS 검출 acquisition 매트릭스에서 본 논문이 DDA-deep 축의 reference benchmark로 기록되어 있음.
- [Awasthi 2026 — PEXMap (k-mer Exon/Isoform Peptide Mapping)](./awasthi-2026-pexmap-proteogenomic-exon-isoform-mapping.md) — PSM ↔ exon/transcript 매핑 도구. 본 deep proteome reference에 PEXMap 적용 시 exon-level / EXj-level 해상도 확장 가능(별도 검증 필요).
- [Jiang 2026 — 3DisoGalaxy Breast Cancer Isoform Foldome Atlas](./jiang-2026-3disogalaxy-breast-cancer-isoform-foldome.md) — translation-supported isoform atlas. 본 논문이 ENCODE에서 보고한 AS 양방향 검출률 18.6%는 유방암 코호트의 translation-supported ORF set과 직접 비교 가능한 baseline 수치.
- [Cancer Multiomics Proteogenomic Atlas](../topics/cancer-multiomics-literature.md) — topic hub (Section 7, Methodology / Resource Atlases).

## Sources

- Raw PDF: `raw/inbox/papers/sinitcyn-2023-global-detection-human-variants-isoforms-deep-proteome.pdf` (3.6 MB, 13 pages; Nature direct download cc-by)
- Publisher (open access cc-by): https://www.nature.com/articles/s41587-023-01714-x
- DOI: https://doi.org/10.1038/s41587-023-01714-x
- ProteomeXchange / MassIVE: PXD024364 (raw + MaxQuant output)
- Online resource: https://deep-sequencing.app (variant/isoform browser, D.R. Brademan)
- Code: https://github.com/coongroup/DeepProteomeSequencing-Software + MaxQuantAnalyzer (https://github.com/cwenger/cwenger.github.io)
