---
title: "Multiomics Proteomics PTM Identification — Topic Questions (Answered)"
tags:
  - question-bank
  - ptm
  - answered
date: 2026-06-08
status: answered-2026-06
---

# Multiomics Proteomics PTM Identification — Topic Questions (Answered)

위키 확장 질문에 로컬 `wiki/sources/` 논문 근거로 답을 단 sprint. 답·근거는 그래프(`interactives/llm-wiki-all.html`)에 질문 노드로 자동 반영된다.

## Section A — PTM identification methods (Q1-100)

### Q1. proteome identification count는 protein, protein group, gene product 중 어떤 단위로 보고되었는가?
**A.** 로컬 CPTAC 논문들은 같은 "proteome count"를 서로 다른 단위로 보고한다. Dou 2020은 전체 코호트에서 12,153개를 **identified protein groups**(단백질 그룹)로, Mertins 2016은 15,369개를 **identified proteins**로 보고하고, Zhang 2022 pan-cancer 컴펜디엄은 15,439를 단백질이 아니라 **unique genes(gene product)** 단위로 집계한다([Dou 2020](../sources/dou-2020-proteogenomic-characterization-endometrial-carcinoma.md); [Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md); [Zhang 2022](../sources/zhang-2022-proteogenomic-characterization-2002-human-cancers.md)). 따라서 proteome identification count를 인용할 때는 protein / protein group / gene product 중 어느 단위인지 원문 표기를 그대로 보존해야 하며, 단위를 명시하지 않으면 서로 다른 entity를 같은 수처럼 비교하게 된다.

**Cited**: [Dou 2020](../sources/dou-2020-proteogenomic-characterization-endometrial-carcinoma.md), [Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md), [Zhang 2022](../sources/zhang-2022-proteogenomic-characterization-2002-human-cancers.md)

### Q2. phosphoproteome identification count는 phosphosite, localized site, phosphopeptide, phosphospectrum 중 무엇을 의미하는가?
**A.** phosphoproteome count는 어느 처리 단계의 entity인지에 따라 phosphosite, localized(class I) site, phosphopeptide, phosphoprotein 등으로 의미가 달라진다. Clark 2020은 같은 데이터에서 42,889 **phosphopeptides** identified와 STAR Methods의 100,730 **phosphosites**를 서로 다른 처리 수준으로 따로 보고하며, 둘을 합치지 말고 count type을 보존하라고 명시한다([Clark 2020](../sources/clark-2020-integrated-proteogenomic-characterization-clear-cell.md)). Abelin 2023(MONTE)도 한 실험에서 28,523 phosphorylation **sites**와 6,745 **phosphoproteins**를 별도 단위로 보고해, phosphosite 수와 phosphopeptide/phosphoprotein 수가 전혀 다른 값임을 보여준다([Abelin 2023](../sources/abelin-2023-workflow-enabling-deepscale-immunopeptidome-proteome.md)). 즉 "phospho count"는 site인지 localized site인지 peptide인지 spectrum/feature인지를 반드시 확인해야 한다.

**Cited**: [Clark 2020](../sources/clark-2020-integrated-proteogenomic-characterization-clear-cell.md), [Abelin 2023](../sources/abelin-2023-workflow-enabling-deepscale-immunopeptidome-proteome.md)

### Q3. acetylome identification count는 acetylsite, acetylated peptide, lysine acetylation event 중 어떤 단위를 쓰는가?
**A.** acetylome count도 단위가 통일되어 있지 않다. Dou 2020은 10,862를 **lysine acetylation sites**로, Satpathy 2021은 15,186을 **acetylsites**로 보고하고, Zhao 2025는 185 **acetylated sites**가 135개 단백질 위에 있다고 site와 protein 단위를 함께 보고한다([Dou 2020](../sources/dou-2020-proteogenomic-characterization-endometrial-carcinoma.md); [Satpathy 2021](../sources/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.md); [Zhao 2025](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md)). 대부분 acetyl-lysine **site**(자리) 단위를 쓰지만 acetylated peptide나 acetylated protein 단위로 보고되는 경우도 있으므로, lysine acetylation event(site)인지 peptide인지 protein인지 원문 표기를 확인해야 한다.

**Cited**: [Dou 2020](../sources/dou-2020-proteogenomic-characterization-endometrial-carcinoma.md), [Satpathy 2021](../sources/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.md), [Zhao 2025](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md)

### Q4. 단백체, 인산화체, 아세틸체 count를 한 그래프에 놓을 때 어떤 단위 변환을 하면 안 되는가?
**A.** 세 layer는 측정 단위 자체가 달라서(단백질/단백질 그룹 vs phosphosite/phosphopeptide vs acetyl-lysine site) 하나의 공통 척도로 변환하면 안 된다. Chang 2025(TMT-Integrator)는 gene·protein·peptide·PTM-site 수준의 리포트를 따로 제공하면서 protein group, phosphosite, phosphopeptide, acetylsite, phosphoprotein을 거짓 공통 지표로 환산하지 말라고 명시한다([Chang 2025](../sources/chang-2025-analysis-isobaric-quantitative-proteomic-data.md)). Mertins 2016도 논문마다 proteins/protein groups/phosphosites/phosphopeptides/acetylsites 등 다른 entity를 보고해 count 단위가 harmonize되지 않는다고 경고하며, Zhang 2022가 phospho를 199,284 **phospho-protein features**로 보고하듯 단위가 다르면 단순 수치 비교가 불가능하다([Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md); [Zhang 2022](../sources/zhang-2022-proteogenomic-characterization-2002-human-cancers.md)). 한 그래프에 놓을 때는 단위를 명시해 layer별로 분리하고, site↔protein↔peptide 간 임의 환산은 하지 않아야 한다.

**Cited**: [chang-2025-analysis-isobaric-quantitative-proteomic-data](../sources/chang-2025-analysis-isobaric-quantitative-proteomic-data.md), [Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md), [Zhang 2022](../sources/zhang-2022-proteogenomic-characterization-2002-human-cancers.md)

### Q5. main text와 supplementary table의 identification count가 다를 때 어떤 값을 우선해야 하는가?
**A.** 로컬 근거상 main text와 supplementary(STAR Methods)의 수치 차이는 대개 "서로 다른 처리 단계/단위"에서 나오므로, 어느 값이 맞다기보다 각 값이 무엇을 센 것인지(단위·필터)를 함께 봐야 한다. Clark 2020은 본문 Results에서 42,889 phosphopeptides identified, 20,976 quantified를 보고하지만 STAR Methods에서는 100,730 phosphosites(이 중 2,443개 유전자의 5,584 site가 완전 관측)를 따로 보고한다([Clark 2020](../sources/clark-2020-integrated-proteogenomic-characterization-clear-cell.md)). 따라서 단순히 큰 값을 고르지 말고, 비교 목적과 일치하는 단위(예: 정량 가능한 site vs 전체 식별 phosphopeptide)를 supplementary 정의에 맞춰 우선 선택하고 출처 단계를 함께 기록해야 한다.

**Cited**: [Clark 2020](../sources/clark-2020-integrated-proteogenomic-characterization-clear-cell.md)

### Q6. localized site probability threshold는 phosphosite count를 얼마나 바꿀 수 있는가?
**A.** phosphosite count는 localization(자리 확정) probability threshold에 크게 좌우된다. Petralia 2020은 localization probability 0.75를 적용하고, 전체 식별·정량 18,235 phosphosites 중 다운스트림에 쓴 site는 4,548개로 줄었다고 보고한다([Petralia 2020](../sources/petralia-2020-integrated-proteogenomic-characterization-across-major.md)). Zhao 2025도 6,213개 phosphorylation site 중 localization score >0.75를 만족하는 **class I site**는 5,048개라고 보고해 threshold가 site 수를 직접 줄임을 보여주며, Krug 2020은 VM-polishing 후 phosphosite의 70%만 완전 localize되었다고 한다([Zhao 2025](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md); [Krug 2020](../sources/krug-2020-proteogenomic-landscape-breast-cancer-tumorigenesis.md)). 즉 threshold(예: 0.75/class I)를 명시하지 않으면 같은 데이터의 phosphosite count가 수천 단위로 달라진다.

**Cited**: [Petralia 2020](../sources/petralia-2020-integrated-proteogenomic-characterization-across-major.md), [Zhao 2025](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md), [Krug 2020](../sources/krug-2020-proteogenomic-landscape-breast-cancer-tumorigenesis.md)

### Q7. peptide-level FDR과 protein-level FDR은 reported count 해석에 어떤 차이를 만든다?
**A.** FDR가 적용된 수준에 따라 같은 "count"라도 통제된 오류율이 다르다. Krug 2020은 단백질 그룹 수준 FDR을 0.01% 미만으로 통제했지만, site 수준에서는 phosphosite aggregate FDR 0.44%, acetylsite aggregate FDR 0.57%로 보고해 protein-level과 site/peptide-level FDR이 별개임을 명시한다([Krug 2020](../sources/krug-2020-proteogenomic-landscape-breast-cancer-tumorigenesis.md)). Petralia 2020은 Philosopher 1% protein-level FDR을, Zhao 2025는 proteins·peptides·sites 각각에 1% FDR을 적용했다고 보고한다([Petralia 2020](../sources/petralia-2020-integrated-proteogenomic-characterization-across-major.md); [Zhao 2025](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md)). 따라서 reported count를 해석할 때 1% FDR이 protein 수준인지 peptide/site 수준인지 확인해야 하며, protein-level FDR만 통제된 경우 개별 site의 신뢰도는 따로 평가해야 한다.

**Cited**: [Krug 2020](../sources/krug-2020-proteogenomic-landscape-breast-cancer-tumorigenesis.md), [Petralia 2020](../sources/petralia-2020-integrated-proteogenomic-characterization-across-major.md), [Zhao 2025](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md)

### Q8. missing value 처리와 quantifiable feature 기준은 identification count와 어떻게 다르다?
**A.** identification count(식별된 feature 수)와 quantifiable feature(결측 처리 후 정량·분석에 실제 쓰인 feature 수)는 다른 숫자다. Mertins 2016은 15,369 proteins·62,679 phosphosites가 식별되었지만 필터 후 정량된 것은 12,553 proteins·33,239 phosphosites라고 보고한다([Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md)). Petralia 2020은 8,802 proteins·18,235 phosphosites가 식별·정량되었으나 최소 한 진단군에서 50% 초과 샘플에 관측된 다운스트림 feature는 6,429 proteins·4,548 phosphosites로 줄었고, Satpathy 2021은 70% 초과 결측 feature를 제거(특정 분석은 50% 기준)했다([Petralia 2020](../sources/petralia-2020-integrated-proteogenomic-characterization-across-major.md); [Satpathy 2021](../sources/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.md)). 즉 missing-value 처리·관측 비율 기준에 따라 정량 가능 feature는 식별 count보다 크게 작아지므로 둘을 구분해 보고해야 한다.

**Cited**: [Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md), [Petralia 2020](../sources/petralia-2020-integrated-proteogenomic-characterization-across-major.md), [Satpathy 2021](../sources/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.md)

### Q9. cohort-level total identification과 per-sample median identification은 어떤 질문에 각각 적합한가?
**A.** cohort 전체 합산 count는 코호트의 총 발견 규모를, per-sample(중앙값/평균) count는 개별 샘플에서 실제 얻는 depth를 답한다. Dou 2020은 전체 코호트에서 12,153 proteins·73,212 phosphosites·10,862 acetylation sites를 보고하면서, 종양 1개당 평균은 10,088 proteins·29,710 phosphosites·3,821 acetylation sites라고 별도로 명시한다([Dou 2020](../sources/dou-2020-proteogenomic-characterization-endometrial-carcinoma.md)). Petralia 2020처럼 전체 식별·정량 수와 샘플 커버리지로 필터된 수를 구분하는 것도 같은 맥락이다([Petralia 2020](../sources/petralia-2020-integrated-proteogenomic-characterization-across-major.md)). "이 플랫폼이 얼마나 깊게 보나"는 per-sample 값이, "코호트가 누적적으로 무엇을 덮나"는 cohort-total 값이 적합하다.

**Cited**: [Dou 2020](../sources/dou-2020-proteogenomic-characterization-endometrial-carcinoma.md), [Petralia 2020](../sources/petralia-2020-integrated-proteogenomic-characterization-across-major.md)

### Q10. pan-cancer compendium의 pooled count는 single cancer cohort count와 직접 비교 가능한가?
**A.** pan-cancer 컴펜디엄의 pooled count는 단일 코호트 count와 직접 비교하기 어렵다. Zhang 2022는 14개 암종·17개 연구의 2,002 종양을 통합한 cross-study 컴펜디엄으로, proteome를 15,439 **unique genes**, phospho를 199,284 **phospho-protein features**(11,671 유전자)로 보고하며 이는 새로 측정한 단일 MS 실험이 아니라 처리 파이프라인이 다른 공개 데이터의 합집합이라고 명시한다([Zhang 2022](../sources/zhang-2022-proteogenomic-characterization-2002-human-cancers.md)). 반면 Dou 2020·Mertins 2016 같은 단일 코호트는 한 워크플로우에서 protein group/phosphosite 단위로 보고한다([Dou 2020](../sources/dou-2020-proteogenomic-characterization-endometrial-carcinoma.md); [Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md)). pooled 값은 단위(gene/feature)·검색 파이프라인·중복 제거 방식이 단일 코호트와 다르므로, 직접 수치 비교 대신 단위와 통합 방식을 맞춘 뒤 해석해야 한다.

**Cited**: [Zhang 2022](../sources/zhang-2022-proteogenomic-characterization-2002-human-cancers.md), [Dou 2020](../sources/dou-2020-proteogenomic-characterization-endometrial-carcinoma.md), [Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md)

### Q11. 2016-2026 인간 암 proteogenomic 연구에서 가장 반복적으로 등장하는 cancer type은 무엇인가?
**A.** 로컬 proteogenomic 코퍼스에서 가장 반복적으로 등장하는 cancer type은 **폐암(lung)**이며, 그다음이 유방암이다. CPTAC 폐 계열만 해도 폐선암([Gillette 2020](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md), 110 tumor/101 NAT)과 편평세포폐암([Satpathy 2021](../sources/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.md), 108 tumor/99 NAT)이 각각 별도 atlas로 존재한다. 유방암 역시 CPTAC가 PAM50 전 아형을 포괄하는 전향적 코호트를 구축했고([Krug 2020](../sources/krug-2020-proteogenomic-landscape-breast-cancer-tumorigenesis.md), 134 tumor 중 122편 분석), 폐·유방이 단일암종 proteogenomic 연구의 중심 축임을 보여준다.

**Cited**: [Gillette 2020](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md), [Satpathy 2021](../sources/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.md), [Krug 2020](../sources/krug-2020-proteogenomic-landscape-breast-cancer-tumorigenesis.md)

### Q12. CPTAC-style cohort와 single-institution cohort는 sample processing과 count scale에서 어떻게 다른가?
**A.** CPTAC-style 코호트는 전향적·치료나이브 수술검체를 표준화된 PTM 보존 프로토콜(저온허혈 시간 통제, cryopulverization, urea 용해, TMT 라벨링·공통 reference, 분획화)로 처리해 100명 안팎의 tumor와 paired NAT를 동일 plex 설계로 측정한다([Gillette 2020](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md); [Satpathy 2021](../sources/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.md)). 예컨대 유방 CPTAC는 한 종양 절편에서 DNA·RNA·단백질을 함께 추출해 분획 간 불일치를 줄이고 15개 tumor TMT10 plex + 2개 NAT plex로 조직했는데, NAT plex는 정량 기준을 통과하지 못했다([Krug 2020](../sources/krug-2020-proteogenomic-landscape-breast-cancer-tumorigenesis.md)). 반면 단일기관 코호트는 검체 수가 적고(예: 45명 45 pre/12 post 검체) 자체 QC·아형 필터로 분석군을 좁히는 경향이 있어, count scale과 reference 설계 모두 CPTAC보다 작고 가변적이다([Holt 2025](../sources/holt-2025-proteogenomic-characterization-unveils-biomarkers-associated.md)).

**Cited**: [Gillette 2020](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md), [Krug 2020](../sources/krug-2020-proteogenomic-landscape-breast-cancer-tumorigenesis.md), [Satpathy 2021](../sources/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.md), [Holt 2025](../sources/holt-2025-proteogenomic-characterization-unveils-biomarkers-associated.md)

### Q13. FFPE, fresh frozen, cell line, organoid, PDX sample은 MS depth에 어떤 영향을 준다?
**A.** 검체 유형은 MS depth와 해석 가능 layer를 크게 좌우한다. FFPE는 가교결합으로 까다롭지만 pan-cancer 1,220례에서 평균 4,000개 이상 단백질까지 프로파일링되어 대규모 회고적 코호트에 쓸 만한 깊이를 낸다([Tüshaus 2025](../sources/tshaus-2025-towards-routine-proteome-profiling-ffpe.md)). Fresh frozen 조직은 CPTAC 표준 프로토콜에서 12,000개 이상 단백질·25,000개 이상 phosphopeptide의 깊은 측정을 가능케 하며, 막단백질·DNA결합 단백질 회수는 sonication 추가로 더 향상된다([Li 2025](../sources/li-2025-sonication-assisted-protein-extraction-improves-proteomic.md)). Organoid·PDX·cell line은 tumor purity가 거의 100%에 가까워 종양세포 신호는 깊게 나오지만 면역·기질 등 미세환경 신호가 빠지고 cell line은 모종양 대표성이 가장 떨어진다([Ji 2023](../sources/ji-2023-pharmaco-proteogenomic-characterization-liver-cancer-organoids.md)).

**Cited**: [Tüshaus 2025](../sources/tshaus-2025-towards-routine-proteome-profiling-ffpe.md), [li-2025-sonication-assisted-protein-extraction-improves-proteomic](../sources/li-2025-sonication-assisted-protein-extraction-improves-proteomic.md), [Ji 2023](../sources/ji-2023-pharmaco-proteogenomic-characterization-liver-cancer-organoids.md)

### Q14. tumor purity와 stromal content는 proteome identification과 quantification 해석을 어떻게 바꾼다?
**A.** tumor purity와 stromal content는 identification 수보다 정량 해석의 신뢰도를 바꾼다. 단일검체 credentialing 분석에서 protein-mRNA 상관(PMC) 점수가 높은 검체일수록 total protein content와 tumor purity가 함께 높았고, CPTAC의 한 연구에서는 26%가 부적합 판정을 받아 정보 손실로 이어졌다 — 즉 purity가 낮으면 종양 신호가 기질에 희석된다([Zhao 2018](../sources/zhao-2018-credentialing-individual-samples-proteogenomic-analysis.md)). 그래서 atlas들은 평균 50% 종양핵·괴사 20% 미만 같은 병리 기준으로 검체를 선별하고([Gillette 2020](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md)), RTK phosphosite enrichment 점수 계산 시 purity 보정 항을 넣기도 한다([Satpathy 2021](../sources/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.md)). 근육·기질 오염이 우려되는 경우 고-purity 부분집합에서 신호를 재확인하는 절차도 보고된다([Holt 2025](../sources/holt-2025-proteogenomic-characterization-unveils-biomarkers-associated.md)).

**Cited**: [zhao-2018-credentialing-individual-samples-proteogenomic-analysis](../sources/zhao-2018-credentialing-individual-samples-proteogenomic-analysis.md), [Gillette 2020](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md), [Satpathy 2021](../sources/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.md), [Holt 2025](../sources/holt-2025-proteogenomic-characterization-unveils-biomarkers-associated.md)

### Q15. paired normal tissue가 있는 연구와 tumor-only 연구는 baseline 해석이 어떻게 다른가?
**A.** paired normal tissue가 있는 연구는 종양 변화를 정상 인접조직(NAT) 대비로 정의해 baseline을 명시적으로 잡는다. 예컨대 ccRCC CPTAC는 103 treatment-naive 종양과 paired NAT를 비교해 mRNA로는 안 보이는 종양특이 단백/인산화 변화를 분리해냈고([Clark 2020](../sources/clark-2020-integrated-proteogenomic-characterization-clear-cell.md)), 폐선암에서는 tumor-NAT PCA 분리와 함께 단백질 변화보다 큰 phosphosite/acetylsite 변화를 잡아 '단백질 보정 후 PTM 해석'의 근거를 제공했다([Gillette 2020](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md)). 반면 NAT plex가 QC를 통과하지 못하거나([Krug 2020](../sources/krug-2020-proteogenomic-landscape-breast-cancer-tumorigenesis.md)) tumor-only로 가는 연구는 절대 baseline 대신 코호트 내부 대조(아형 간·반응군 간 비교)에 의존하게 되어, 정상 대비 절대 증감 해석이 제약된다.

**Cited**: [Clark 2020](../sources/clark-2020-integrated-proteogenomic-characterization-clear-cell.md), [Gillette 2020](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md), [Krug 2020](../sources/krug-2020-proteogenomic-landscape-breast-cancer-tumorigenesis.md)

### Q16. sample amount가 적은 연구는 어떤 enrichment 또는 fractionation trade-off를 선택하는가?
**A.** 검체량이 적은 연구는 깊이·분획·enrichment 사이에서 trade-off를 택한다. CPTAC LSCC는 ubiquitylome(K-GG) 프로파일링을 재료가 충분한 일부 검체에만 수행해 전체 코호트와 동등하게 취급하지 말 것을 명시했다 — 즉 재료 제약 시 PTM enrichment layer를 부분집합으로 축소한다([Satpathy 2021](../sources/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.md)). FFPE 대규모 연구는 ion-mobility 기반 online fractionation으로 깊이를 확보하되 대용량 데이터를 처리할 소프트웨어 한계와 새 normalization 필요성을 trade-off로 보고했고([Tüshaus 2025](../sources/tshaus-2025-towards-routine-proteome-profiling-ffpe.md)), 추출 단계에서는 sonication을 추가해 동일 LC-MS/MS 조건에서 막·DNA결합 단백질 coverage를 끌어올리는 방식이 제시된다([Li 2025](../sources/li-2025-sonication-assisted-protein-extraction-improves-proteomic.md)).

**Cited**: [Satpathy 2021](../sources/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.md), [Tüshaus 2025](../sources/tshaus-2025-towards-routine-proteome-profiling-ffpe.md), [li-2025-sonication-assisted-protein-extraction-improves-proteomic](../sources/li-2025-sonication-assisted-protein-extraction-improves-proteomic.md)

### Q17. clinical cohort size와 MS depth 사이에는 어떤 실험 설계 trade-off가 보이는가?
**A.** 임상 코호트 크기와 MS depth 사이에는 뚜렷한 설계 trade-off가 보인다. 단일암종 CPTAC atlas는 100명 안팎으로 표본을 제한하는 대신 TMT 분획화로 단백질 1만여·phosphosite 4만~6만 수준의 깊은 PTM 측정을 확보한다([Gillette 2020](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md); [Satpathy 2021](../sources/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.md)). 반대로 999개 종양·22개 암종을 한 번에 다루는 pan-cancer atlas는 단일샷 DIA-MS로 약 9,670개 단백질의 비교적 얕지만 통일된 proteome scale을 택해 코호트 폭을 키운다([Knol 2025](../sources/knol-2025-pan-cancer-proteome-atlas-mass-spectrometry-based.md); [Du 2025](../sources/du-2025-unified-pan-cancer-proteome-atlas.md)). 즉 표본 수를 늘릴수록 검체당 깊이·분획·PTM enrichment를 줄이는 쪽으로 무게가 옮겨간다.

**Cited**: [Gillette 2020](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md), [Satpathy 2021](../sources/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.md), [Knol 2025](../sources/knol-2025-pan-cancer-proteome-atlas-mass-spectrometry-based.md), [Du 2025](../sources/du-2025-unified-pan-cancer-proteome-atlas.md)

### Q18. longitudinal 또는 treatment-response cohort는 baseline atlas cohort와 count reporting 방식이 다른가?
**A.** longitudinal·치료반응 코호트는 baseline atlas와 reporting 방식이 다르다. atlas는 treatment-naive 종양과 NAT의 절대 count·depth(단백질/phosphosite/acetylsite 수)를 강조하는 반면([Gillette 2020](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md)), 신보조화학요법 방광암 같은 반응 코호트는 pre/post-treatment matched 검체와 병리적 반응(downstaging vs 잔존병변) 라벨을 기준으로 검체를 나누고, pre-treatment 42개·post 12개처럼 분석 단계별로 가변적인 검체 수를 보고한다([Holt 2025](../sources/holt-2025-proteogenomic-characterization-unveils-biomarkers-associated.md)). 또 진행단계(pre-invasive→invasive) 진화 코호트는 단계별 검체군(98 pre-invasive/99 invasive)으로 묶어 정적 atlas보다 '시점·단계 간 변화'를 보고 단위의 중심에 둔다([Zhang 2024](../sources/zhang-2024-evolutionary-proteogenomic-landscape-pre-invasive-invasive.md)).

**Cited**: [Gillette 2020](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md), [Holt 2025](../sources/holt-2025-proteogenomic-characterization-unveils-biomarkers-associated.md), [zhang-2024-evolutionary-proteogenomic-landscape-pre-invasive-invasive](../sources/zhang-2024-evolutionary-proteogenomic-landscape-pre-invasive-invasive.md)

### Q19. tumor subtype discovery 논문과 therapeutic vulnerability 논문은 어떤 omics layer를 더 강조하는가?
**A.** 아형 발견(subtype discovery) 논문은 다층 통합 클러스터링과 단백질 기반 분류자를 강조한다. pan-cancer atlas는 단백질 co-expression 모듈과 단백질 마커로 RNA 기반 consensus molecular subtype을 재현하고 미상원발암 분류자를 만들었으며([Knol 2025](../sources/knol-2025-pan-cancer-proteome-atlas-mass-spectrometry-based.md)), 유방 CPTAC도 SCNA·mRNA·protein·phosphosite·acetylsite를 함께 NMF로 묶어 아형을 정의한다([Krug 2020](../sources/krug-2020-proteogenomic-landscape-breast-cancer-tumorigenesis.md)). 반면 therapeutic vulnerability 논문은 phosphoproteome/kinase signaling layer를 더 앞세워 — 예컨대 EGFR변이의 SHP2 Y62, KRAS의 SOS1 S1161 phosphosite처럼 — RNA·단백질에는 없고 인산화에서만 보이는 약물표적 신호를 강조한다([Gillette 2020](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md)).

**Cited**: [Knol 2025](../sources/knol-2025-pan-cancer-proteome-atlas-mass-spectrometry-based.md), [Krug 2020](../sources/krug-2020-proteogenomic-landscape-breast-cancer-tumorigenesis.md), [Gillette 2020](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md)

### Q20. multi-region sampling 연구는 identification count보다 heterogeneity map을 더 중요하게 다루는가?
**A.** 로컬 근거에서 multi-region sampling은 단일 identification count보다 region 간 이질성(heterogeneity) 파악에 무게를 둔다. 간암 organoid 연구는 동일 환자의 multi-region 검체(65개 중 13개)를 두어, 같은 환자 organoid가 다른 환자보다 분자·약물반응이 더 유사하면서도 환자 내 이질성이 남아 있음을 보였다 — 즉 region 간 차이 자체가 분석 대상이다([Ji 2023](../sources/ji-2023-pharmaco-proteogenomic-characterization-liver-cancer-organoids.md)). 다만 이 연구도 organoid당 깊은 omics depth(예: 23,754개 phosphosite)를 확보하므로, count와 heterogeneity map은 양자택일이라기보다 병행되며 해석의 초점이 후자로 이동한다고 보는 편이 정확하다.

**Cited**: [Ji 2023](../sources/ji-2023-pharmaco-proteogenomic-characterization-liver-cancer-organoids.md)

### Q21. TMT, iTRAQ, label-free, DIA는 multiplexing, missingness, quantification accuracy에서 어떻게 다른가?
**A.** 네 방식은 multiplexing·missingness·정량정확도에서 뚜렷이 갈린다. iTRAQ/TMT 같은 isobaric tag는 여러 시료를 한 번에 라벨링해 동시 정량하므로 missing value가 적고 batch 처리량이 크다 — TMT는 한 plex 안에서 reporter ion으로 상대정량을 한다([Chang 2025](../sources/chang-2025-analysis-isobaric-quantitative-proteomic-data.md)). 반면 DIA는 라벨 없이 모든 precursor를 체계적으로 단편화해 시료 수 제약이 없고 결측을 줄이며, 라벨프리/DDA 대비 정량 재현성과 깊이를 높인다([Lancaster 2024](../sources/lancaster-2024-fast-deep-phosphoproteome-analysis-orbitrap.md)). 직접 벤치마크에서는 TMT가 더 많은 peptide/protein을 더 낮은 CV로 정량했지만 DIA가 진짜 표적 식별의 정확도와 용량-반응 상관에서 우월해, 둘은 '재현성 vs 정확도' 트레이드오프 관계로 보는 것이 맞다([Koudelka 2025](../sources/koudelka-2025-benchmarking-quantitative-proteomics-workflows-limited.md)).

**Cited**: [chang-2025-analysis-isobaric-quantitative-proteomic-data](../sources/chang-2025-analysis-isobaric-quantitative-proteomic-data.md), [Lancaster 2024](../sources/lancaster-2024-fast-deep-phosphoproteome-analysis-orbitrap.md), [Koudelka 2025](../sources/koudelka-2025-benchmarking-quantitative-proteomics-workflows-limited.md)

### Q22. TMT 10/11/16/18-plex 발전은 cohort proteomics throughput을 어떻게 바꾸었는가?
**A.** plex 수 확대는 한 번의 측정에 담는 시료 수를 늘려 cohort proteomics의 처리량을 직접 끌어올렸다. CPTAC 코호트들은 TMT 10-plex([Clark 2020](../sources/clark-2020-integrated-proteogenomic-characterization-clear-cell.md))와 TMT 11-plex([Petralia 2020](../sources/petralia-2020-integrated-proteogenomic-characterization-across-major.md))로 수백 종양의 proteome·phosphoproteome를 reference 채널과 함께 묶어 정량했다. 최근에는 TMT 35-plex 시약과 Astral 장비까지 등장해 한 plex의 용량이 더 커졌고, 이를 처리하는 TMT-Integrator 같은 파이프라인이 gene/protein/peptide/PTM-site 수준 통합 리포트를 제공한다([Chang 2025](../sources/chang-2025-analysis-isobaric-quantitative-proteomic-data.md)).

**Cited**: [Clark 2020](../sources/clark-2020-integrated-proteogenomic-characterization-clear-cell.md), [Petralia 2020](../sources/petralia-2020-integrated-proteogenomic-characterization-across-major.md), [chang-2025-analysis-isobaric-quantitative-proteomic-data](../sources/chang-2025-analysis-isobaric-quantitative-proteomic-data.md)

### Q23. ratio compression 문제는 TMT 기반 cancer proteomics의 biological interpretation에 어떤 영향을 준다?
**A.** ratio compression은 동시 분리된 다른 peptide의 reporter ion이 섞여 들어가 진짜 fold-change가 0(=1:1) 쪽으로 압축되는 현상으로, TMT cancer proteomics에서 종양-정상·반응-비반응 간 차이를 실제보다 작게 보이게 해 생물학적 해석을 왜곡할 수 있다. 이를 줄이기 위해 CPTAC 코호트는 MS3 기반 TMT-centric 획득을 채택했고, 동시에 high-pH 역상 분획으로 동시분리(co-isolation)를 낮춰 reporter 간섭을 완화했다([Petralia 2020](../sources/petralia-2020-integrated-proteogenomic-characterization-across-major.md)). 처리 단계에서도 TMT-Integrator 같은 도구로 정량 결과를 정제하면 batch effect가 줄고 mRNA와의 gene-wise 상관이 올라가, 압축된 신호의 해석 신뢰도를 높일 수 있다([Chang 2025](../sources/chang-2025-analysis-isobaric-quantitative-proteomic-data.md)).

**Cited**: [Petralia 2020](../sources/petralia-2020-integrated-proteogenomic-characterization-across-major.md), [chang-2025-analysis-isobaric-quantitative-proteomic-data](../sources/chang-2025-analysis-isobaric-quantitative-proteomic-data.md)

### Q24. carrier/reference channel design은 cross-batch 비교를 어떻게 가능하게 하는가?
**A.** isobaric 실험에서 한 채널을 모든 plex에 공통으로 넣는 reference(common reference) 채널을 두면, 각 시료를 그 공통 기준에 대한 비(ratio)로 환산해 서로 다른 plex·batch의 값을 같은 척도로 맞출 수 있다. CPTAC LUAD는 TMT-10 라벨링에 'common reference sample'을 포함해 cross-batch 비교를 가능하게 했고([Gillette 2020](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md)), 다른 CPTAC 코호트도 동일하게 공통 reference 채널로 plex를 연결했다([Petralia 2020](../sources/petralia-2020-integrated-proteogenomic-characterization-across-major.md)). 다만 carrier/booster 성격의 채널 설계는 ratio compression 같은 간섭을 키울 수 있어, reference 채널은 정량 정규화 목적과 분리해 신중히 설계해야 한다([Chang 2025](../sources/chang-2025-analysis-isobaric-quantitative-proteomic-data.md)).

**Cited**: [Gillette 2020](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md), [Petralia 2020](../sources/petralia-2020-integrated-proteogenomic-characterization-across-major.md), [chang-2025-analysis-isobaric-quantitative-proteomic-data](../sources/chang-2025-analysis-isobaric-quantitative-proteomic-data.md)

### Q25. iTRAQ 기반 초기 연구와 TMT 기반 후속 연구는 depth와 reproducibility에서 어떻게 달라졌는가?
**A.** 초기 iTRAQ 기반 연구와 후속 TMT 기반 연구는 plex 폭·깊이·재현성에서 차이가 난다. iTRAQ 시대 CPTAC 유방암 파일럿은 iTRAQ 4-plex로 105개 중 77개 종양만 고품질 데이터를 얻었고([Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md)), 조기발병 위암도 iTRAQ + sequential IMAC로 약 9,625 protein group·28,944 phosphopeptide를 정량했다([Mun 2019](../sources/mun-2019-proteogenomic-characterization-human-early-onset-gastric.md)). 이후 TMT 10-plex 기반 ccRCC 코호트는 11,355 protein·42,889 phosphopeptide를 식별하는 등 한 batch에 더 많은 시료를 묶어 깊이와 cross-batch 정렬을 끌어올렸다([Clark 2020](../sources/clark-2020-integrated-proteogenomic-characterization-clear-cell.md)).

**Cited**: [Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md), [Mun 2019](../sources/mun-2019-proteogenomic-characterization-human-early-onset-gastric.md), [Clark 2020](../sources/clark-2020-integrated-proteogenomic-characterization-clear-cell.md)

### Q26. DIA는 DDA 대비 identification과 quantification completeness에서 어떤 장점을 갖는가?
**A.** DIA는 정해진 m/z 창의 모든 precursor를 체계적으로 단편화하므로, DDA의 stochastic한 상위-N 선택이 만드는 run 간 결측을 줄여 quantification completeness가 높다. Astral 기반 DIA는 30분에 약 3만 개 phosphosite를 매핑하고 합성 표준·DDA 플랫폼과의 벤치마크에서 빠르고 깊은 정량을 보였다([Lancaster 2024](../sources/lancaster-2024-fast-deep-phosphoproteome-analysis-orbitrap.md)). 직접 비교에서도 DIA는 진짜 표적의 식별 정확도와 용량-반응 상관이 더 강했고, 장비 발전으로 민감도·서열 커버리지가 더 개선될 여지가 있다([Koudelka 2025](../sources/koudelka-2025-benchmarking-quantitative-proteomics-workflows-limited.md)).

**Cited**: [Lancaster 2024](../sources/lancaster-2024-fast-deep-phosphoproteome-analysis-orbitrap.md), [Koudelka 2025](../sources/koudelka-2025-benchmarking-quantitative-proteomics-workflows-limited.md)

### Q27. library-based DIA와 library-free DIA는 cancer cohort 분석에서 어떤 trade-off가 있는가?
**A.** library 기반 DIA는 미리 만든 spectral library로 정확하고 깊은 정량을 얻지만 library 구축에 추가 측정·노동이 들고, library-free(DIA 데이터에서 직접 검색)는 그 부담을 없애 cohort 확장에 유리하지만 소프트웨어 선택에 따라 결과가 갈린다. DIA 분석 도구 비교에서 무료 FragPipe는 정밀도(precision), 상용 Spectronaut은 민감도(sensitivity)에 강해 어느 쪽을 택할지는 실험 맥락에 달렸다고 보고된다([Koudelka 2025](../sources/koudelka-2025-benchmarking-quantitative-proteomics-workflows-limited.md)). 실제로 single-shot DIA는 999개 종양·22개 암종을 균일하게 정량한 Pan-Cancer Proteome Atlas를 가능하게 해, library 부담을 줄인 DIA 워크플로우가 대규모 cohort에 적합함을 보여준다([Knol 2025](../sources/knol-2025-pan-cancer-proteome-atlas-mass-spectrometry-based.md); [Du 2025](../sources/du-2025-unified-pan-cancer-proteome-atlas.md)).

**Cited**: [Koudelka 2025](../sources/koudelka-2025-benchmarking-quantitative-proteomics-workflows-limited.md), [Knol 2025](../sources/knol-2025-pan-cancer-proteome-atlas-mass-spectrometry-based.md), [Du 2025](../sources/du-2025-unified-pan-cancer-proteome-atlas.md)

### Q28. BoxCar, gas-phase fractionation, high-pH fractionation 같은 전략은 depth를 어떻게 올리는가?
**A.** 이들 전략은 한 번에 분석기로 들어가는 분석물 복잡도를 낮춰 깊이를 올린다. high-pH(basic) 역상 분획은 시료를 여러 분획으로 나눠 동시분리를 줄이고 식별 깊이를 키우며, CPTAC 코호트는 이를 IMAC/Fe-NTA PTM 농축과 결합해 수천 protein·수만 phosphosite를 확보했다([Gillette 2020](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md); [Petralia 2020](../sources/petralia-2020-integrated-proteogenomic-characterization-across-major.md)). gas-phase/이온이동도 기반 분리도 같은 원리로 작동해, immunopeptidomics에서 IMS·m/z로 선택적으로 단편화한 Thunder-DDA-PASEF는 커버리지를 약 2배로 늘렸다([Gomez-Zepeda 2024](../sources/gomezzepeda-2024-thunder-dda-pasef-enables-high-coverage-immunopeptidomics-boosted.md)).

**Cited**: [Gillette 2020](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md), [Petralia 2020](../sources/petralia-2020-integrated-proteogenomic-characterization-across-major.md), [Gomez-Zepeda 2024](../sources/gomezzepeda-2024-thunder-dda-pasef-enables-high-coverage-immunopeptidomics-boosted.md)

### Q29. fractionation 수가 증가하면 identification count와 clinical scalability는 어떻게 교환되는가?
**A.** 분획 수를 늘리면 동시분리가 줄고 식별 깊이가 커지지만, 시료당 LC-MS 시간·장비 사용·노동이 분획 수에 비례해 늘어 임상 규모 확장성과 상충한다. CPTAC식 deep 워크플로우는 다중 분획 + PTM 농축으로 8,000~11,000 protein과 수만 phosphosite를 얻지만 시료당 측정 부담이 크다([Gillette 2020](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md); [Petralia 2020](../sources/petralia-2020-integrated-proteogenomic-characterization-across-major.md)). 반대로 분획을 없앤 single-shot DIA는 종양당 약 9,670 protein 수준이지만 999개 종양·22개 암종을 균일하게 정량해, 깊이를 다소 양보하는 대신 임상 scalability를 확보하는 교환을 보여준다([Knol 2025](../sources/knol-2025-pan-cancer-proteome-atlas-mass-spectrometry-based.md)).

**Cited**: [Gillette 2020](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md), [Petralia 2020](../sources/petralia-2020-integrated-proteogenomic-characterization-across-major.md), [Knol 2025](../sources/knol-2025-pan-cancer-proteome-atlas-mass-spectrometry-based.md)

### Q30. phosphoproteome과 acetylome을 동시에 측정할 때 sample split은 어떤 bias를 만들 수 있는가?
**A.** phospho와 acetyl을 따로 enrichment해야 해서, 한 시료를 분취(split)해 병렬 처리하면 분취 간 단백량·처리 변동이 두 PTM 층에 서로 다른 batch/loading bias로 들어와 PTM-PTM crosstalk 해석을 왜곡할 수 있다. MONTE 워크플로우는 동일 시료에서 proteome·phosphoproteome·acetylome(및 ubiquitylome·immunopeptidome)을 순차(serial)로 뽑아도 각 층의 깊이·정량 정밀도가 손상되지 않음을 보여, 병렬 분취 대신 직렬화로 이런 split bias를 줄일 수 있음을 시사한다([Abelin 2023](../sources/abelin-2023-workflow-enabling-deepscale-immunopeptidome-proteome.md)). 실제 kinase inhibitor 처리 대장암 세포에서 phospho와 acetyl을 함께 측정한 연구도 두 층을 같은 시료 기반으로 정렬해야 약물에 따른 PTM crosstalk를 신뢰성 있게 비교할 수 있음을 보여준다([Zhao 2025](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md)).

**Cited**: [Abelin 2023](../sources/abelin-2023-workflow-enabling-deepscale-immunopeptidome-proteome.md), [Zhao 2025](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md)

### Q31. phosphopeptide enrichment에는 IMAC, TiO2, Fe-NTA, PolyMAC 등이 어떻게 쓰이는가?
**A.** 로컬 근거에서 phosphopeptide 농축은 금속친화(IMAC/MOAC) 계열과 그 변형으로 쓰인다. [Liu 2025](../sources/liu-2025-dynamic-3d-network-coating-composite-enables.md)는 그래핀-메조다공실리카 위에 phosphonate와 Ti4+를 고정한 IMAC 흡착제를 만들어 0.1 fmol 검출한계와 1:15,000 선택성으로 phosphopeptide를 포집했다. 실제 cancer 워크플로우에서는 TiO2(MOAC)로 phosphopeptide를 농축한 [Zhao 2025](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md)와 Fe-IMAC를 쓴 [Hsu 2025](../sources/hsu-2025-phosphoproteomics-osimertinib-tolerant-persister-cells-reveals.md), AssayMAP IMAC를 쓴 [Abelin 2023](../sources/abelin-2023-workflow-enabling-deepscale-immunopeptidome-proteome.md)처럼 Ti4+/Fe3+ 금속 화학에 기반한 IMAC와 TiO2가 주로 보고된다. PolyMAC, Fe-NTA를 단독으로 다룬 로컬 논문은 확인되지 않아, 이 둘은 같은 금속친화 계열의 변형으로 이해하되 본 코퍼스에서 직접 근거를 제시하기는 어렵다.

**Cited**: [Liu 2025](../sources/liu-2025-dynamic-3d-network-coating-composite-enables.md), [Zhao 2025](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md), [Hsu 2025](../sources/hsu-2025-phosphoproteomics-osimertinib-tolerant-persister-cells-reveals.md), [Abelin 2023](../sources/abelin-2023-workflow-enabling-deepscale-immunopeptidome-proteome.md)

### Q32. mono-phosphopeptide와 multi-phosphopeptide 분리는 signaling 해석에 어떤 의미가 있는가?
**A.** mono-/multi-phosphopeptide 분리는 농축 단계에서 어떤 signaling 사건을 보게 되는지를 좌우한다. [Liu 2025](../sources/liu-2025-dynamic-3d-network-coating-composite-enables.md)는 IMAC 흡착제로 phosphopeptide를 전역 포집한 뒤 gradient elution으로 mono-와 multi-phosphopeptide를 단계적으로 분리할 수 있음을 보였고, 폐 정상(Beas-2B)과 선암(SPC-A1)에서 차등 phosphopeptide를 구분했다. multi-phosphopeptide는 한 펩타이드 안에 여러 site가 함께 있어 site 동시조절(coregulation) 해석에 중요하지만, 다중 인산화 펩타이드는 한 site의 변화가 같은 펩타이드의 다른 인산화에서 비롯될 수 있어 해석에 주의가 필요하다 — 이 confounding을 peptidoform 수준에서 다루는 통계가 [Demeulemeester 2024](../sources/demeulemeester-2024-msqrob2ptm-differential-abundance-differential-usage.md)의 msqrob2PTM이다.

**Cited**: [Liu 2025](../sources/liu-2025-dynamic-3d-network-coating-composite-enables.md), [Demeulemeester 2024](../sources/demeulemeester-2024-msqrob2ptm-differential-abundance-differential-usage.md)

### Q33. acetyl-peptide enrichment는 anti-acetyl-lysine antibody 의존성 때문에 어떤 bias를 갖는가?
**A.** acetyl-peptide 농축은 anti-acetyl-lysine 항체 면역침전에 의존하므로 항체가 인식하는 epitope 쪽으로 검출이 치우친다. [Zhao 2025](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md)는 phosphopeptide 농축 후 flowthrough에서 acetyl-lysine 항체로 acetyl-peptide를 농축했는데, 같은 시료에서 phosphosite 6,213개에 비해 acetylsite는 135개 단백질의 185개로 훨씬 적게 검출됐다. [Abelin 2023](../sources/abelin-2023-workflow-enabling-deepscale-immunopeptidome-proteome.md)도 PTMScan acetyl-lysine 항체 농축을 쓰며 phosphosite(약 28,523)에 비해 acetylsite(약 6,294)가 적게 보고돼, 항체 친화도와 면역침전 효율이 보고되는 acetylsite 범위를 제한함을 보여준다. 따라서 낮은 acetylsite 수는 생물학적 부재가 아니라 항체 의존 농축의 편향일 수 있다.

**Cited**: [Zhao 2025](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md), [Abelin 2023](../sources/abelin-2023-workflow-enabling-deepscale-immunopeptidome-proteome.md)

### Q34. PTM enrichment 효율은 reported site count와 biological absence를 구분하기 어렵게 만드는가?
**A.** 그렇다. 농축 효율이 site 검출 여부를 좌우하므로, 보고된 site 수가 적은 것이 실제 생물학적 부재인지 단지 농축·검출의 한계인지 구분하기 어렵다. [Zhao 2025](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md)에서 acetyl-lysine 항체로 농축한 acetylsite가 185개에 그친 것은 부위 부재가 아니라 항체 의존 농축의 효율 한계로 해석될 여지가 크고, [Abelin 2023](../sources/abelin-2023-workflow-enabling-deepscale-immunopeptidome-proteome.md)은 같은 시료에서도 HLA flow-through 유무에 따라 phosphosite/acetylsite 수가 달라져(예: acetylsite 3,702 대 5,380) 검출이 워크플로우에 민감함을 보인다. 이 때문에 미검출 site는 "없음"이 아니라 "이 농축·깊이에서는 안 잡힘"으로 보수적으로 표기해야 한다.

**Cited**: [Zhao 2025](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md), [Abelin 2023](../sources/abelin-2023-workflow-enabling-deepscale-immunopeptidome-proteome.md)

### Q35. enrichment 후 LC-MS/MS instrument time은 phosphosite depth를 얼마나 좌우하는가?
**A.** 농축 후 LC-MS/MS 측정 시간(장비 시간)은 phosphosite 깊이를 크게 좌우한다. [Lancaster 2024](../sources/lancaster-2024-fast-deep-phosphoproteome-analysis-orbitrap.md)는 Orbitrap Astral + DIA로 30분 수집에서 약 30,000개, 12시간 측정에서 81,120개의 고유 phosphosite를 매핑해 측정 시간이 길수록 검출 깊이가 늘어남을 직접 보였다. [Hsu 2025](../sources/hsu-2025-phosphoproteomics-osimertinib-tolerant-persister-cells-reveals.md)도 DIA 라이브러리와 다중 데이터셋을 합쳐 phosphoproteome 라이브러리를 53,182 site까지 키운 반면 조건당 평균 phosphopeptide는 약 21,500개로, 가용 장비 시간·라이브러리 깊이에 따라 실제 정량 site 수가 달라짐을 보여준다. 따라서 site 수 비교는 동일한 gradient·장비·획득방식 조건에서만 공정하다.

**Cited**: [Lancaster 2024](../sources/lancaster-2024-fast-deep-phosphoproteome-analysis-orbitrap.md), [Hsu 2025](../sources/hsu-2025-phosphoproteomics-osimertinib-tolerant-persister-cells-reveals.md)

### Q36. global proteome과 PTM layer를 같은 sample에서 측정하지 않았을 때 correction 해석에 어떤 문제가 생기는가?
**A.** global proteome와 PTM layer를 같은 시료에서 측정하지 않으면 PTM 변화에서 단백질 발현 변화를 빼주는 abundance correction을 신뢰성 있게 할 수 없다. 제목 그대로 [Wu 2011](../sources/wu-2011-correct-interpretation-comprehensive-phosphorylation-dynamics.md)은 phosphorylation dynamics의 올바른 해석에는 단백질 발현 변화에 의한 정규화가 필요하다고 못박는다. [Demeulemeester 2024](../sources/demeulemeester-2024-msqrob2ptm-differential-abundance-differential-usage.md)는 PTM 강도가 모단백질 abundance와 confounding된다는 점을 핵심 문제로 짚고, peptidoform 강도를 같은 시료의 모단백질 강도로 log2-ratio 정규화(DPU)해야 한다고 본다. 따라서 proteome가 다른 시료/배치에서 측정되면 이 모단백질 정규화가 깨져, 단순한 발현 증가를 signaling 활성으로 오독할 위험이 커진다.

**Cited**: [Wu 2011](../sources/wu-2011-correct-interpretation-comprehensive-phosphorylation-dynamics.md), [Demeulemeester 2024](../sources/demeulemeester-2024-msqrob2ptm-differential-abundance-differential-usage.md)

### Q37. acetylome이 phosphoproteome보다 적게 보고되는 이유는 biology 때문인가, method burden 때문인가?
**A.** 로컬 근거는 acetylome이 phosphoproteome보다 적게 보고되는 데에 method burden이 크게 작용함을 시사한다. [Abelin 2023](../sources/abelin-2023-workflow-enabling-deepscale-immunopeptidome-proteome.md)의 MONTE 워크플로우는 같은 조직에서 phosphosite(PDX 28,523)와 acetylsite(PDX 6,294)를 모두 측정했지만 acetylsite가 일관되게 적고, acetyl 농축은 PTMScan 항체 면역침전이라는 별도의 까다로운 단계를 거친다. [Zhao 2025](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md)도 동일 시료에서 phosphosite 6,213개 대 acetylsite 185개로, phospho는 TiO2 농축이 효율적인 반면 acetyl은 flowthrough에서 항체로 잡아 수율이 낮았다. 즉 생물학적 차이를 단정할 수 없고, 항체 의존 농축·검출 효율 차이라는 방법론적 부담이 주된 이유로 보인다.

**Cited**: [Abelin 2023](../sources/abelin-2023-workflow-enabling-deepscale-immunopeptidome-proteome.md), [Zhao 2025](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md)

### Q38. ubiquitinomics, glycoproteomics 등 다른 PTM layer가 포함된 논문은 이 topic에서 어떻게 분류해야 하는가?
**A.** ubiquitinome·glycoproteome 등 다른 PTM layer를 담은 논문은 PTM abundance correction과 kinase signaling이라는 본 topic에서 별개 layer가 아니라 같은 "serial multi-PTM" 방법론 축으로 분류하는 것이 근거에 맞다. [Abelin 2023](../sources/abelin-2023-workflow-enabling-deepscale-immunopeptidome-proteome.md)의 MONTE는 한 시료에서 immunopeptidome·ubiquitylome·proteome·phosphoproteome·acetylome을 순차 측정하며 각 layer가 깊이·정량 정밀도를 잃지 않음을 보였고, [Lin 2025](../sources/lin-2025-comprehensive-ptm-profiling-scasp-ptm-uncovers.md)의 SCASP-PTM은 phospho·ubiquitin·acetyl·glyco·biotin 펩타이드를 단일 시료에서 순차 농축해 DIA-MS로 정량한다. 따라서 이런 논문은 "phospho 중심 글"과 구분하되, 다중 PTM 동시 측정·serial enrichment 플랫폼 사례로 묶어 phospho/acetyl과 같은 PTM-correction 프레임 안에서 다루면 된다.

**Cited**: [Abelin 2023](../sources/abelin-2023-workflow-enabling-deepscale-immunopeptidome-proteome.md), [Lin 2025](../sources/lin-2025-comprehensive-ptm-profiling-scasp-ptm-uncovers.md)

### Q39. PTM count가 높아도 site localization이 낮으면 어떤 caveat를 달아야 하는가?
**A.** PTM count가 높아도 site localization이 낮으면 "정확히 어느 잔기가 수식됐는지 불확실"이라는 caveat를 달아야 한다. [Hsu 2025](../sources/hsu-2025-phosphoproteomics-osimertinib-tolerant-persister-cells-reveals.md)와 [Zhao 2025](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md)는 모두 localization probability >= 0.75를 만족하는 class I site만 신뢰 부위로 보고하고, Zhao는 6,213개 phosphosite 중 5,048개만 class I로 구분했다. localization 점수가 낮은 부위는 펩타이드 안 인접 S/T/Y 사이에서 위치가 모호해 특정 잔기에 묶은 kinase-substrate 해석이 흔들리므로, 그런 site는 별도 표시하거나 class I 집합과 분리하고, [Hsu 2025](../sources/hsu-2025-phosphoproteomics-osimertinib-tolerant-persister-cells-reveals.md)처럼 단일 site 호출 대신 substrate-set 수준(KSEA) 해석으로 보완하는 것이 안전하다.

**Cited**: [Hsu 2025](../sources/hsu-2025-phosphoproteomics-osimertinib-tolerant-persister-cells-reveals.md), [Zhao 2025](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md)

### Q40. PTM identification과 PTM quantification의 차이를 페이지에서 어떻게 시각적으로 구분할 것인가?
**A.** PTM identification(부위가 검출·국재화됐는가)과 PTM quantification(그 부위가 조건 간에 모단백질 보정 후 유의하게 변했는가)은 별개이며, 페이지에서도 두 단계를 분리해 보여야 한다. [Kohler 2023](../sources/kohler-2023-msstatsptm-statistical-relative-quantification-posttranslational.md)의 MSstatsPTM과 [Demeulemeester 2024](../sources/demeulemeester-2024-msqrob2ptm-differential-abundance-differential-usage.md)의 msqrob2PTM은 모두 식별과 별개로 차등 정량 단계를 두며, 특히 msqrob2PTM은 모단백질 abundance로 보정한 differential usage(DPU)와 보정 없는 differential abundance(DPA)를 구분해 출력한다. 시각적으로는 식별 지표(검출 site 수, class I localization 통과 여부)와 정량 지표(모단백질 보정 fold-change, kinase activity 추정)를 서로 다른 축·색으로 분리하고, 정량 막대에는 "protein-abundance corrected" 여부를 명시하는 것이 근거에 맞는 구분이다.

**Cited**: [Kohler 2023](../sources/kohler-2023-msstatsptm-statistical-relative-quantification-posttranslational.md), [Demeulemeester 2024](../sources/demeulemeester-2024-msqrob2ptm-differential-abundance-differential-usage.md)

### Q41. Orbitrap Fusion, Fusion Lumos, Q Exactive, Exploris, Eclipse, Astral은 어떤 시기와 연구 유형에서 등장하는가?
**A.** 로컬 근거상 instrument는 연구 시기·유형과 뚜렷이 맞물린다. 2020~2021년 CPTAC형 deep TMT proteogenomics(폐선암·폐편평세포암)에서는 whole proteome에 Q Exactive HF-X, phosphoproteome·acetylproteome에 Orbitrap Fusion Lumos를 쓰는 조합이 표준이었다([Gillette 2020](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md); [Satpathy 2021](../sources/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.md)). 2024년 이후의 방법론 연구에서는 Orbitrap Astral이 DIA와 결합해 빠른 deep phosphoproteome를 겨냥하며 등장하고([Lancaster 2024](../sources/lancaster-2024-fast-deep-phosphoproteome-analysis-orbitrap.md)), 2025년 pan-cancer atlas류는 single-shot DIA 기반의 대규모 코호트 스캔에 쓰인다([Knol 2025](../sources/knol-2025-pan-cancer-proteome-atlas-mass-spectrometry-based.md)). 즉 Fusion/Lumos·Q Exactive는 심층 분획 TMT 시대, Exploris·Astral은 고속 DIA·atlas 시대에 주로 나타난다.

**Cited**: [Gillette 2020](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md), [Satpathy 2021](../sources/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.md), [Lancaster 2024](../sources/lancaster-2024-fast-deep-phosphoproteome-analysis-orbitrap.md), [Knol 2025](../sources/knol-2025-pan-cancer-proteome-atlas-mass-spectrometry-based.md)

### Q42. instrument generation 변화는 count 증가와 얼마나 직접적으로 연결되는가?
**A.** instrument 세대 교체는 count 증가와 연결되지만 단독 인과는 아니다. Orbitrap Astral은 30분 측정에서 약 30,000개 phosphosite, 12시간에 81,120개를 매핑해 차세대 기기가 동일 시간 대비 깊이를 크게 끌어올림을 보여준다([Lancaster 2024](../sources/lancaster-2024-fast-deep-phosphoproteome-analysis-orbitrap.md)). 다만 1,220-case FFPE 연구는 ion mobility 기반 데이터의 잠재 depth를 기존 소프트웨어가 처리하지 못해 실제 식별 수가 데이터 처리·정규화 단계에서 제약됨을 보고하므로([Tüshaus 2025](../sources/tshaus-2025-towards-routine-proteome-profiling-ffpe.md)), count는 기기 세대뿐 아니라 분석 파이프라인과 입력량에도 함께 좌우된다.

**Cited**: [Lancaster 2024](../sources/lancaster-2024-fast-deep-phosphoproteome-analysis-orbitrap.md), [Tüshaus 2025](../sources/tshaus-2025-towards-routine-proteome-profiling-ffpe.md)

### Q43. high-field Orbitrap과 ion mobility, FAIMS, Astral-like speed improvement는 PTM depth에 어떤 의미가 있는가?
**A.** high-field Orbitrap·ion mobility·Astral류의 속도/분해능 향상은 PTM depth에 직접적 의미를 가진다. Orbitrap Astral은 DIA와 결합해 반시간 만에 약 3만 개 phosphosite를 잡을 만큼 phosphoproteome 측정의 깊이와 처리량을 동시에 끌어올렸다([Lancaster 2024](../sources/lancaster-2024-fast-deep-phosphoproteome-analysis-orbitrap.md)). timsTOF의 ion mobility(TIMS/PASEF) 최적화는 IMS·m/z 기반 semi-selective fragmentation으로 immunopeptidome coverage를 약 2배로 늘렸고([Gomez-Zepeda 2024](../sources/gomezzepeda-2024-thunder-dda-pasef-enables-high-coverage-immunopeptidomics-boosted.md)), FFPE 연구도 ion-mobility 기반 online fractionation으로 평균 4,000개 이상 단백질 깊이에 도달했다([Tüshaus 2025](../sources/tshaus-2025-towards-routine-proteome-profiling-ffpe.md)). 단 그만큼 데이터 부하가 커져 소프트웨어 처리 한계가 새 병목으로 떠오른다.

**Cited**: [Lancaster 2024](../sources/lancaster-2024-fast-deep-phosphoproteome-analysis-orbitrap.md), [Gomez-Zepeda 2024](../sources/gomezzepeda-2024-thunder-dda-pasef-enables-high-coverage-immunopeptidomics-boosted.md), [Tüshaus 2025](../sources/tshaus-2025-towards-routine-proteome-profiling-ffpe.md)

### Q44. instrument name이 main text에 없고 methods supplement에만 있는 경우 extraction을 어떻게 표준화할 것인가?
**A.** 이 표준화 자체를 정면으로 다룬 로컬 논문은 없고, 위키의 PDF 추출 작업에서 instrument 정보가 본문이 아닌 methods/snippet 수준에 흩어져 있을 때의 처리 사례만 확인된다. 예컨대 Keshishian 2021 페이지는 IMAC·TiO2 같은 method/instrument 근거를 본문 PDF 텍스트에서 별도로 발췌해 'method/instrument evidence' 항목으로 보존하고, 단위를 임의 변환하지 말라는 추출 규칙을 명시한다([Keshishian 2021](../sources/keshishian-2021-highly-multiplexed-quantitative-phosphosite-assay.md)). PTM 분야 리뷰도 사이트 수·정량·stoichiometry 보고가 방법별로 제각각이라 완전한 inventory가 없다고 지적하므로([Olsen 2013](../sources/olsen-2013-status-large-scale-analysis-post-translational-modifications.md)), 실무적으로는 본문·supplement·원문 PDF를 함께 파싱해 instrument 필드를 별도 근거 슬롯에 표준 보존하는 방식이 합리적이다.

**Cited**: [keshishian-2021-highly-multiplexed-quantitative-phosphosite-assay](../sources/keshishian-2021-highly-multiplexed-quantitative-phosphosite-assay.md), [Olsen 2013](../sources/olsen-2013-status-large-scale-analysis-post-translational-modifications.md)

### Q45. LC gradient length와 column setup은 identification depth를 어떻게 바꾼다?
**A.** LC gradient·column setup은 분획·분리 깊이를 통해 identification depth를 직접 바꾼다. CPTAC형 deep workflow는 basic reverse-phase fractionation 후 LC-MS/MS로 단백체·phosphoproteome·acetylproteome를 측정해 6만 개 이상 phosphosite 규모의 깊이를 확보한다([Gillette 2020](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md)). FFPE pan-cancer 연구는 ion-mobility 기반 online fractionation으로 평균 4,000개 이상 단백질에 도달했지만 그 깊은 데이터를 처리할 소프트웨어 한계를 새 병목으로 보고했다([Tüshaus 2025](../sources/tshaus-2025-towards-routine-proteome-profiling-ffpe.md)). 즉 더 길고 분리력 높은 LC 설정은 coverage를 늘리지만, 시간·처리 비용과의 균형이 함께 결정된다.

**Cited**: [Gillette 2020](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md), [Tüshaus 2025](../sources/tshaus-2025-towards-routine-proteome-profiling-ffpe.md)

### Q46. FAIMS 또는 ion mobility를 쓴 연구는 peptide coverage와 missingness에서 어떤 이득을 보고하는가?
**A.** ion mobility/FAIMS를 쓴 로컬 연구는 주로 coverage 이득을 보고한다. timsTOF의 ion mobility(TIMS)를 최적화한 Thunder-DDA-PASEF는 IMS 해상도를 넓히고 MS/MS frame을 줄여 immunopeptidome coverage를 proteomics-tailored DDA-PASEF 대비 약 2배로 늘렸고, 100만 세포 등가물에서 5,738개 HLA 펩타이드를 식별했다([Gomez-Zepeda 2024](../sources/gomezzepeda-2024-thunder-dda-pasef-enables-high-coverage-immunopeptidomics-boosted.md)). FFPE pan-cancer 연구도 ion-mobility 기반 online fractionation으로 평균 4,000개 이상 단백질 깊이에 도달했다([Tüshaus 2025](../sources/tshaus-2025-towards-routine-proteome-profiling-ffpe.md)). 다만 이들 논문은 coverage 향상을 명시적으로 보고하는 반면, cohort-wide missingness 감소를 정량 지표로 직접 보고하지는 않는다.

**Cited**: [Gomez-Zepeda 2024](../sources/gomezzepeda-2024-thunder-dda-pasef-enables-high-coverage-immunopeptidomics-boosted.md), [Tüshaus 2025](../sources/tshaus-2025-towards-routine-proteome-profiling-ffpe.md)

### Q47. DDA의 stochastic sampling은 cohort-wide missingness를 어떻게 만드는가?
**A.** DDA의 stochastic(준확률적) precursor 선택은 코호트마다 검출되는 펩타이드 집합이 달라져 sample 간 missing value를 키운다는 것이 DIA 기반 atlas들이 전제하는 배경이다. Knol 등은 대부분의 암 단백체 연구가 단일 암종에 머무른 한계를 넘기 위해 999개 종양·22개 암종을 single-shot DIA로 '통일된 방식(in a unified manner)'으로 정량했다고 강조하는데([Knol 2025](../sources/knol-2025-pan-cancer-proteome-atlas-mass-spectrometry-based.md); [Du 2025](../sources/du-2025-unified-pan-cancer-proteome-atlas.md)), 이는 코호트 전반의 일관된 정량을 위해 DIA를 택했음을 보여준다. LiP-MS 벤치마크도 DIA가 dose-response 상관과 진짜 표적 식별에서 강점을 보인다고 보고해 일관 정량 측면의 이점을 뒷받침한다([Koudelka 2025](../sources/koudelka-2025-benchmarking-quantitative-proteomics-workflows-limited.md)).

**Cited**: [Knol 2025](../sources/knol-2025-pan-cancer-proteome-atlas-mass-spectrometry-based.md), [Du 2025](../sources/du-2025-unified-pan-cancer-proteome-atlas.md), [Koudelka 2025](../sources/koudelka-2025-benchmarking-quantitative-proteomics-workflows-limited.md)

### Q48. DIA는 phosphoproteome에서도 동일하게 유리한가?
**A.** 로컬 근거상 DIA는 phosphoproteome에서도 유리하게 작동한다. Orbitrap Astral과 DIA를 결합하면 30분에 약 3만 개, 12시간에 81,120개 phosphosite를 매핑할 만큼 phospho 분석에서도 깊이·처리량 이점이 확인된다([Lancaster 2024](../sources/lancaster-2024-fast-deep-phosphoproteome-analysis-orbitrap.md)). EGFR 변이 NSCLC drug-tolerant persister 모델 연구도 DIA-MS global·phosphoproteomics로 CDK1·YAP1·mTOR·BAD 인산화 같은 내성 신호를 매핑해 phospho 적용성을 보여준다([Hsu 2025](../sources/hsu-2025-phosphoproteomics-osimertinib-tolerant-persister-cells-reveals.md)). 다만 LiP-MS 벤치마크는 DIA가 정확도·상관에서 강하나 정량 펩타이드 수와 CV에서는 TMT가 앞설 수 있다고 보고하므로([Koudelka 2025](../sources/koudelka-2025-benchmarking-quantitative-proteomics-workflows-limited.md)), 이점의 크기는 목적·기기에 따라 달라진다.

**Cited**: [Lancaster 2024](../sources/lancaster-2024-fast-deep-phosphoproteome-analysis-orbitrap.md), [Hsu 2025](../sources/hsu-2025-phosphoproteomics-osimertinib-tolerant-persister-cells-reveals.md), [Koudelka 2025](../sources/koudelka-2025-benchmarking-quantitative-proteomics-workflows-limited.md)

### Q49. single-shot proteomics와 deep fractionated proteomics는 atlas 구축 목적이 어떻게 다른가?
**A.** 두 전략은 atlas 구축 목적이 다르다. single-shot DIA atlas는 999개 종양·22개 암종을 통일된 방식으로 빠르게 정량해 pan-cancer·암종 특이 단백질, 약물 표적, 바이오마커를 넓게 발굴하는 '폭과 일관성' 중심 자원을 지향한다([Knol 2025](../sources/knol-2025-pan-cancer-proteome-atlas-mass-spectrometry-based.md); [Du 2025](../sources/du-2025-unified-pan-cancer-proteome-atlas.md)). 반면 CPTAC형 deep fractionated proteomics는 basic RP 분획과 IMAC·acetyl 농축을 거쳐 6만 개 이상 phosphosite와 acetylsite까지 측정함으로써, driver 변이를 단백질·PTM 층에서 해석 가능한 치료 취약점으로 연결하는 '깊이와 다층 PTM' 중심 자원을 만든다([Gillette 2020](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md); [Satpathy 2021](../sources/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.md)).

**Cited**: [Knol 2025](../sources/knol-2025-pan-cancer-proteome-atlas-mass-spectrometry-based.md), [Du 2025](../sources/du-2025-unified-pan-cancer-proteome-atlas.md), [Gillette 2020](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md), [Satpathy 2021](../sources/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.md)

### Q50. limited sample workflow는 deep atlas workflow와 어떤 다른 질문에 최적화되는가?
**A.** limited sample workflow는 적은 입력으로 신뢰성 있는 정량·표적 식별을 얻는 질문에 최적화된다. LiP-MS 벤치마크는 입력이 제한된 상황에서 DIA-MS가 진짜 약물 표적 식별과 dose-response 상관에서 강점을 보이고, Astral 같은 기기 발전이 민감도·서열 coverage를 높여 TMT 라벨링 필요성을 줄일 수 있다고 본다([Koudelka 2025](../sources/koudelka-2025-benchmarking-quantitative-proteomics-workflows-limited.md)). 표적형 SigPath assay도 0.05~1 mg 수준의 낮은 입력에서 수백 개 phosphosite를 정량해 소량 시료의 약력학 모니터링에 맞춰져 있다([Keshishian 2021](../sources/keshishian-2021-highly-multiplexed-quantitative-phosphosite-assay.md)). 반대로 deep atlas workflow는 다층 PTM을 깊게 측정해 driver→signaling 해석과 치료 취약점 발굴이라는 다른 질문에 최적화된다([Gillette 2020](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md)).

**Cited**: [Koudelka 2025](../sources/koudelka-2025-benchmarking-quantitative-proteomics-workflows-limited.md), [keshishian-2021-highly-multiplexed-quantitative-phosphosite-assay](../sources/keshishian-2021-highly-multiplexed-quantitative-phosphosite-assay.md), [Gillette 2020](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md)

### Q51. database search engine 선택은 identification count에 얼마나 영향을 준다?
**A.** 검색 엔진 선택은 동정 수에 직접 영향을 준다. 동일한 ccRCC 데이터에서 FragPipe/TMT-Integrator는 MaxQuant나 Proteome Discoverer보다 더 많은 단백질을 동정했다([Chang 2025](../sources/chang-2025-analysis-isobaric-quantitative-proteomic-data.md)). LiP-MS DIA 데이터 벤치마크에서도 무료 도구 FragPipe와 상용 Spectronaut는 정밀도(precision)와 민감도(sensitivity)의 트레이드오프를 보여, 동정 수와 정확도가 도구마다 갈렸다([Koudelka 2025](../sources/koudelka-2025-benchmarking-quantitative-proteomics-workflows-limited.md)). 인산화 분석에서도 동정·정량 결과가 도구에 따라 크게 달라지므로 엔진 선택은 1차 의사결정 변수다([Savage 2020](../sources/savage-2020-phosphoproteomics-bioinformatics-comprehensive-guide.md)).

**Cited**: [chang-2025-analysis-isobaric-quantitative-proteomic-data](../sources/chang-2025-analysis-isobaric-quantitative-proteomic-data.md), [Koudelka 2025](../sources/koudelka-2025-benchmarking-quantitative-proteomics-workflows-limited.md), [Savage 2020](../sources/savage-2020-phosphoproteomics-bioinformatics-comprehensive-guide.md)

### Q52. MaxQuant, Proteome Discoverer, MSFragger, SpectroMine, DIA-NN, FragPipe는 어떤 데이터 유형에 자주 쓰이는가?
**A.** TMT/iTRAQ 같은 isobaric 표지 데이터에는 FragPipe/TMT-Integrator, Proteome Discoverer, MaxQuant가 자주 쓰이며, 이들은 유전자·단백질·펩타이드·PTM 사이트 수준의 정량 리포트를 만든다([Chang 2025](../sources/chang-2025-analysis-isobaric-quantitative-proteomic-data.md)). DIA(데이터 비의존 획득) 데이터에는 DIA-NN과 FragPipe, 상용 Spectronaut(SpectroMine 계열)가 쓰이며, 도구에 따라 정밀도와 민감도가 다르다([Koudelka 2025](../sources/koudelka-2025-benchmarking-quantitative-proteomics-workflows-limited.md)). 단일샷 DIA-MS로 22개 암종 999개 종양을 통일 정량한 범암 atlas도 DIA 워크플로우 기반이다([Du 2025](../sources/du-2025-unified-pan-cancer-proteome-atlas.md)).

**Cited**: [chang-2025-analysis-isobaric-quantitative-proteomic-data](../sources/chang-2025-analysis-isobaric-quantitative-proteomic-data.md), [Koudelka 2025](../sources/koudelka-2025-benchmarking-quantitative-proteomics-workflows-limited.md), [Du 2025](../sources/du-2025-unified-pan-cancer-proteome-atlas.md)

### Q53. search space에 variant peptide, fusion peptide, noncanonical ORF가 포함되면 FDR control은 어떻게 어려워지는가?
**A.** search space에 variant·fusion peptide와 noncanonical ORF를 넣으면 후보 펩타이드 공간이 폭증해 동일한 동정 점수에서도 위양성이 늘어 FDR control이 어려워진다. moPepGen은 변이·noncoding ORF·fusion·circRNA를 그래프로 열거해 표준 워크플로우가 놓치는 비정규 공간을 크게 넓히는데, 그만큼 엄격한 사후 필터가 필요하다([Zhu 2025](../sources/zhu-2025-identification-of-non-canonical-peptides.md)). Deutsch 등은 7,264개 ncORF를 별도 증거(immunopeptidomics·Ribo-seq·보존성·CRISPR)로 재분류해야 신뢰할 수 있음을 보였다([Deutsch 2026](../sources/deutsch-2026-expanding-human-proteome-peptideins-noncanonical-orfs.md)). 다중효소 deep proteome에서도 PSM·펩타이드·단백질에 순차적 1% FDR을 적용했고, 검출 안 된 SAP에서 deleterious 변이가 enriched되는 등 변이 펩타이드의 동정 편향이 관찰됐다([Sinitcyn 2023](../sources/sinitcyn-2023-global-detection-human-variants-isoforms-deep-proteome.md)).

**Cited**: [Zhu 2025](../sources/zhu-2025-identification-of-non-canonical-peptides.md), [Deutsch 2026](../sources/deutsch-2026-expanding-human-proteome-peptideins-noncanonical-orfs.md), [Pavel Sinitcyn 2023](../sources/sinitcyn-2023-global-detection-human-variants-isoforms-deep-proteome.md)

### Q54. open search 또는 spectral library search는 PTM discovery에 어떤 기회를 준다?
**A.** open-modification search는 사전에 지정하지 않은 수식까지 잡아내, 과거보다 훨씬 많은 PTM을 LC-MS/MS로 발견할 기회를 준다([Demeulemeester 2024](../sources/demeulemeester-2024-msqrob2ptm-differential-abundance-differential-usage.md)). 다만 발견된 PTM이 같은 펩타이드에 실린 다른 수식 때문일 수 있어, peptidoform 수준 검증과 모(母)단백 abundance 보정이 함께 필요하다([Demeulemeester 2024](../sources/demeulemeester-2024-msqrob2ptm-differential-abundance-differential-usage.md)). spectral library 기반 DIA 수식 분석도 인산화·유비퀴틴화·아세틸화·당화를 한 시료에서 순차 농축·정량해 PTM 발견 폭을 넓힌다([Lin 2025](../sources/lin-2025-comprehensive-ptm-profiling-scasp-ptm-uncovers.md)).

**Cited**: [Demeulemeester 2024](../sources/demeulemeester-2024-msqrob2ptm-differential-abundance-differential-usage.md), [Lin 2025](../sources/lin-2025-comprehensive-ptm-profiling-scasp-ptm-uncovers.md)

### Q55. phosphosite annotation은 UniProt, PhosphoSitePlus, kinase-substrate DB와 어떻게 연결되는가?
**A.** phosphosite annotation은 실험 큐레이션 DB와 키나아제 참조 DB로 연결한다. Savage·Zhang은 27개 인산화 사이트 DB 중 PhosphoSitePlus(239,664 사이트)를 가장 자주 갱신되는 실험 근거 자원으로, KinBase(538개 인간 키나아제)를 1차 키나아제 참조로 권한다([Savage 2020](../sources/savage-2020-phosphoproteomics-bioinformatics-comprehensive-guide.md)). kinase-substrate 연결은 NetworKIN 같은 예측과 KSEA App·KEA2 같은 활성 추론 도구로 이어지지만, PEG/MELK·PDPK1/PDK1·PTPN11(인산가수분해효소를 키나아제로 오기재) 같은 ID-매핑 오류가 UniProt·HPRD에서 하류 도구로 전파되므로 sanity-check가 필요하다([Savage 2020](../sources/savage-2020-phosphoproteomics-bioinformatics-comprehensive-guide.md)).

**Cited**: [Savage 2020](../sources/savage-2020-phosphoproteomics-bioinformatics-comprehensive-guide.md)

### Q56. acetylsite annotation은 histone vs non-histone을 어떻게 나눠야 하는가?
**A.** acetylsite annotation은 히스톤 아세틸화와 비(非)히스톤 아세틸화를 구분해 해석해야 한다. Zhao 등은 대장암 세포에서 185개 아세틸화 사이트(135개 단백질)를 정량했는데, 이는 HNRNPA1 K350·HSPD1 K72처럼 대부분 비히스톤 단백질 사이트로, 키나아제 저해제가 인산화뿐 아니라 라이신 아세틸화도 바꾼다는 비히스톤 신호 맥락을 보여준다([Zhao 2025](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md)). 임상 조직에서도 ALDOA K330 같은 비히스톤 대사효소 아세틸화/유비퀴틴화가 종양 진행과 연결되어, 사이트별로 히스톤(크로마틴 조절) 대 비히스톤(효소·신호) 기능을 나눠 주석해야 함을 시사한다([Lin 2025](../sources/lin-2025-comprehensive-ptm-profiling-scasp-ptm-uncovers.md)).

**Cited**: [Zhao 2025](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md), [Lin 2025](../sources/lin-2025-comprehensive-ptm-profiling-scasp-ptm-uncovers.md)

### Q57. batch correction과 normalization은 count보다 biological clustering에 더 큰 영향을 주는가?
**A.** 단순 동정 수보다 batch correction·normalization이 생물학적 클러스터링에 더 결정적일 수 있다. 1,220케이스 FFPE 범암 연구는 코호트 간 균등·재현 가능한 로딩을 위해 새로운 normalization 방법이 필요했음을 핵심 결과로 보고했다([Tüshaus 2025](../sources/tshaus-2025-towards-routine-proteome-profiling-ffpe.md)). FragPipe/TMT-Integrator 파이프라인도 ccRCC 데이터에서 batch effect를 줄이고 mRNA와의 유전자별 상관을 높였는데, 이는 동정 수 자체보다 보정·정규화가 다운스트림 통합·군집 신호의 질을 좌우함을 보여준다([Chang 2025](../sources/chang-2025-analysis-isobaric-quantitative-proteomic-data.md)).

**Cited**: [Tüshaus 2025](../sources/tshaus-2025-towards-routine-proteome-profiling-ffpe.md), [chang-2025-analysis-isobaric-quantitative-proteomic-data](../sources/chang-2025-analysis-isobaric-quantitative-proteomic-data.md)

### Q58. bridge/reference pool이 없는 연구는 cross-cohort 비교에서 어떤 한계를 갖는가?
**A.** bridge/reference pool이 없으면 cross-cohort 비교가 어렵다. TMT/iTRAQ 정량은 본질적으로 플렉스 내부 상대값이라, TMT-Integrator도 채널 간 비교를 위해 reference 기반 비율 산출을 전제로 한다([Chang 2025](../sources/chang-2025-analysis-isobaric-quantitative-proteomic-data.md)). 공통 bridge가 없으면 배치·플렉스 효과가 생물학적 차이와 교란되어 코호트 간 절대 비교가 왜곡되므로, 3년·여러 코호트에 걸친 FFPE 범암 연구는 코호트 간 균등 로딩을 보장하는 별도 normalization 방법을 따로 개발해야 했다([Tüshaus 2025](../sources/tshaus-2025-towards-routine-proteome-profiling-ffpe.md)).

**Cited**: [chang-2025-analysis-isobaric-quantitative-proteomic-data](../sources/chang-2025-analysis-isobaric-quantitative-proteomic-data.md), [Tüshaus 2025](../sources/tshaus-2025-towards-routine-proteome-profiling-ffpe.md)

### Q59. multi-omics integration 전에 layer별 missingness/depth 차이를 어떻게 표시해야 하는가?
**A.** multi-omics 통합 전에는 레이어별 missingness와 depth 차이를 명시해야 한다. CPTAC 범암 워킹그룹은 NGS(서열)와 MS(단백체) 데이터를 함께 다룰 때의 고유한 통합·해석 난제를 명시적으로 강조했는데, MS 단백체는 결측·깊이 편차가 NGS와 다르기 때문이다([Li 2023](../sources/li-2023-proteogenomic-data-resources-pan-cancer-analysis.md)). 실제 유방암 proteogenomic 연구에서도 동정된 인산화 사이트 62,679개 중 필터 후 정량된 것은 33,239개로 줄어, '동정 대비 정량(결측 보정 후)' 차이를 사이트 단위로 표시해야 통합이 왜곡되지 않음을 보여준다([Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md)).

**Cited**: [Li 2023](../sources/li-2023-proteogenomic-data-resources-pan-cancer-analysis.md), [Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md)

### Q60. supplement table extraction을 자동화할 때 units, sheet names, abbreviations를 어떻게 기록해야 하는가?
**A.** supplement table를 자동 추출할 때는 단위·시트명·약어를 명시적으로 기록해 단위 혼동을 막아야 한다. 인산화 연구는 protein groups·phosphosites·phosphopeptides·acetylsites 등 서로 다른 entity를 보고하므로 이들을 거짓 공통 지표로 합치면 안 되며, 추출 시 보고된 단위를 보존해야 한다([Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md)). TMT-Integrator도 gene·protein·peptide·PTM site의 서로 다른 수준 리포트를 내므로, 단백질군·인산사이트·인산펩타이드·아세틸사이트 같은 카운트를 하나의 metric으로 변환하지 말고 리포트 단위·시트 구분을 그대로 기록할 것을 권한다([Chang 2025](../sources/chang-2025-analysis-isobaric-quantitative-proteomic-data.md)).

**Cited**: [Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md), [chang-2025-analysis-isobaric-quantitative-proteomic-data](../sources/chang-2025-analysis-isobaric-quantitative-proteomic-data.md)

### Q61. genome, transcriptome, proteome, phosphoproteome, acetylome이 함께 있을 때 가능한 질문은 무엇인가?
**A.** genome·transcriptome·proteome·phosphoproteome·acetylome가 한 환자에서 모두 측정되면, 한 층의 변화가 다음 층으로 어느 정도 전달되는지(예: 변이/CNA → 단백질 → phosphosite → kinase 활성)와 층마다 다른 hallmark 신호를 함께 물을 수 있다. 실제로 [Geffen 2023](../sources/geffen-2023-pan-cancer-analysis-post-translational-modifications-reveals.md)는 11개 암종 PTM 프로파일에서 phosphorylation이 주도하는 DNA repair 이상, acetylation이 주도하는 대사·면역 조절, 그리고 acetylation–phosphorylation crosstalk가 kinase 특이성에 미치는 영향을 함께 분석했다. [Li 2023](../sources/li-2023-pan-cancer-proteogenomics-connects-oncogenic-drivers.md)는 동일한 다층 데이터에서 driver의 cis-효과와 distal trans-효과를 RNA·protein·phosphoprotein 수준으로 동시에 정량하여, 단일 층만으로는 답할 수 없는 '어떤 유전 이벤트가 어떤 기능 상태로 이어지는가'를 질문 형태로 만들 수 있음을 보여준다.

**Cited**: [Geffen 2023](../sources/geffen-2023-pan-cancer-analysis-post-translational-modifications-reveals.md), [Li 2023](../sources/li-2023-pan-cancer-proteogenomics-connects-oncogenic-drivers.md)

### Q62. copy number alteration이 protein abundance로 전달되는 정도는 cancer type마다 어떻게 다른가?
**A.** copy number alteration이 protein abundance로 전달되는 정도는 모든 유전자·암종에서 일정하지 않고, 상당 부분이 단백질 수준에서 약화(attenuation)된다. [Chen 2023](../sources/chen-2023-global-impact-somatic-structural-variation-cancer-proteome.md)은 1,307개 종양의 WGS+proteomics 통합에서, mRNA 수준에서 보이는 SV/copy 연관 cis-조절 효과 중 약 25%만이 단백질 수준에서도 유지된다고 보고해 전달 효율이 부분적임을 정량했다. [Mertins 2016](../sources/mertins-2016-proteogenomics-somatic-mutations-signalling-breast-cancer.md)은 유방암에서 5q 결손의 trans-효과(CETN3·SKP1 손실 → EGFR/SRC 상승)처럼 copy 손실이 단백질 신호로 이어지는 정도가 유전자별로 다름을 보여주며, [Zhang 2022](../sources/zhang-2022-proteogenomic-characterization-2002-human-cancers.md)도 단백질 abundance가 mRNA·copy number와 대체로 상관하지만 생물학적으로 의미 있는 불일치 신호를 동시에 가진다고 정리한다.

**Cited**: [Chen 2023](../sources/chen-2023-global-impact-somatic-structural-variation-cancer-proteome.md), [Mertins 2016](../sources/mertins-2016-proteogenomics-somatic-mutations-signalling-breast-cancer.md), [Zhang 2022](../sources/zhang-2022-proteogenomic-characterization-2002-human-cancers.md)

### Q63. RNA-protein discordance는 proteogenomic study에서 어떤 insight로 해석되는가?
**A.** RNA-protein discordance는 proteogenomic study에서 'transcriptome만으로는 놓치는 단백질 수준 조절·치료 타깃'의 신호로 해석된다. [Goncalves 2022](../sources/gonalves-2022-pan-cancer-proteomic-map-949-human.md)는 949개 세포주 proteome에서 전사체 수준에서는 유의하지 않은 수천 개의 단백질 취약성 바이오마커를 발견했고, [Elmas 2021](../sources/elmas-2021-pan-cancer-proteogenomic-investigations-identify-post-transcriptional.md)은 CDK4/6·PDK1·MET 같은 kinase가 DNA·RNA 변화 없이 단백질 수준에서 과발현되는 post-transcriptional 타깃임을 보였다. [Zhang 2022](../sources/zhang-2022-proteogenomic-characterization-2002-human-cancers.md)는 단백질이 mRNA와 대체로 상관하면서도 의미 있는 불일치를 담는다고 정리하며, [Chen 2023](../sources/chen-2023-global-impact-somatic-structural-variation-cancer-proteome.md)도 mRNA cis-효과의 일부만 단백질로 전달된다는 점에서 불일치 자체가 환자 분류 확장의 근거가 된다고 본다.

**Cited**: [Gonçalves 2022](../sources/gonalves-2022-pan-cancer-proteomic-map-949-human.md), [elmas-2021-pan-cancer-proteogenomic-investigations-identify-post-transcriptional](../sources/elmas-2021-pan-cancer-proteogenomic-investigations-identify-post-transcriptional.md), [Zhang 2022](../sources/zhang-2022-proteogenomic-characterization-2002-human-cancers.md), [Chen 2023](../sources/chen-2023-global-impact-somatic-structural-variation-cancer-proteome.md)

### Q64. driver mutation이 phosphoproteome 또는 kinase activity로 이어지는 사례는 무엇인가?
**A.** driver mutation이 phosphoproteome·kinase activity로 이어지는 사례는 proteogenomic 연구에서 반복적으로 관찰된다. [Mertins 2016](../sources/mertins-2016-proteogenomics-somatic-mutations-signalling-breast-cancer.md)은 유방암에서 체세포 변이·copy 변화를 실제 신호 출력으로 연결해 ERBB2 외에도 CDK12·PAK1·PTK2·RIPK2·TLK2 같은 고인산화 kinase를 타깃 후보로 제시했고, [Li 2023](../sources/li-2023-pan-cancer-proteogenomics-connects-oncogenic-drivers.md)은 점돌연변이·CNA가 단백질 상호작용 네트워크를 재배선하며 대부분의 cancer gene이 서열 기반 kinase activity 프로파일로 수렴함을 보였다. [Zhang 2017](../sources/zhang-2017-pan-cancer-proteogenomic-atlas-pi3kaktmtor-pathway.md)은 PI3K/AKT/mTOR 경로 변이가 하류 활성으로 이어지는 한편, canonical 유전 변이 없이도(예: IDH1·VHL 변이 종양) 높은 mTOR 활성을 보이는 경우가 있어 변이→kinase 활성 연결이 부분적임을 함께 보여준다.

**Cited**: [Mertins 2016](../sources/mertins-2016-proteogenomics-somatic-mutations-signalling-breast-cancer.md), [Li 2023](../sources/li-2023-pan-cancer-proteogenomics-connects-oncogenic-drivers.md), [Zhang 2017](../sources/zhang-2017-pan-cancer-proteogenomic-atlas-pi3kaktmtor-pathway.md)

### Q65. acetylome은 chromatin/metabolism/mitochondria 중 어떤 축을 더 잘 보여주는가?
**A.** 로컬 근거에 따르면 acetylome은 chromatin/metabolism/mitochondria 어느 한 축만이 아니라 여러 축을 동시에 보여주되, 대규모 단백질 복합체와 대사·염색질 기능에 특히 풍부하게 나타난다. [Choudhary 2009](../sources/choudhary-2009-lysine-acetylation-targets-protein-complexes.md)는 lysine acetylation이 chromatin remodeling·cell cycle·splicing·nuclear transport 등 거대 복합체를 우선적으로 표적함을 보였다. [Geffen 2023](../sources/geffen-2023-pan-cancer-analysis-post-translational-modifications-reveals.md)는 pan-cancer PTM 분석에서 acetylation이 면역 반응과 연관된 대사 조절 및 histone 조절 변화를 주도한다고 보고해, 단일 축으로 환원하기보다 대사–염색질 축을 함께 드러내는 층으로 해석하는 것이 근거에 부합한다.

**Cited**: [Choudhary 2009](../sources/choudhary-2009-lysine-acetylation-targets-protein-complexes.md), [Geffen 2023](../sources/geffen-2023-pan-cancer-analysis-post-translational-modifications-reveals.md)

### Q66. proteome-only subtype과 phosphoproteome-informed subtype은 환자 분류를 어떻게 다르게 만든다?
**A.** proteome-only subtype과 phosphoproteome-informed subtype은 분류 해상도가 다르다. [Chen 2019](../sources/chen-2019-pan-cancer-molecular-subtypes-proteomic-characterization.md)는 532개 종양의 질량분석 proteome로 조직 계통을 가로지르는 10개 pan-cancer subtype을 정의하고 여기에 phosphoproteome 특징을 추가로 반영했으며, [Zhang 2022](../sources/zhang-2022-proteogenomic-characterization-2002-human-cancers.md)도 단백질 기반 11개 subtype이 transcriptomics만으로는 보이지 않는 경로 구조를 드러낸다고 보고한다. 특히 [Mertins 2016](../sources/mertins-2016-proteogenomics-somatic-mutations-signalling-breast-cancer.md)은 phosphoproteome 경로 분석에서 mRNA로는 쉽게 잡히지 않는 G-protein-coupled receptor 신호 클러스터를 추가로 식별해, phospho 정보를 더하면 같은 환자도 신호 활성 기준으로 다르게 묶일 수 있음을 보여준다.

**Cited**: [Chen 2019](../sources/chen-2019-pan-cancer-molecular-subtypes-proteomic-characterization.md), [Zhang 2022](../sources/zhang-2022-proteogenomic-characterization-2002-human-cancers.md), [Mertins 2016](../sources/mertins-2016-proteogenomics-somatic-mutations-signalling-breast-cancer.md)

### Q67. phosphoproteome은 druggable kinase pathway를 어떻게 드러내는가?
**A.** phosphoproteome는 기질 인산화 패턴으로부터 kinase 활성을 추론해 druggable kinase pathway를 드러낸다. [Casado 2013](../sources/casado-2013-kinase-substrate-enrichment-analysis-provides-insights.md)은 KSEA(kinase-substrate enrichment analysis)로 AML에서 PI3K·CK·CDK·PAK 경로 활성을 체계적으로 추론하고 기질 abundance 기반 모델로 PI3K/mTOR 억제제 감수성을 예측했으며, [Wiredja 2017](../sources/wiredja-2017-ksea-app-web-based-tool-kinase.md)은 이를 누구나 쓸 수 있는 KSEA App으로 구현했다. [Zhao 2025](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md)는 대장암 세포에 kinase inhibitor를 처리한 뒤 PTM-SEA·KSEA로 lapatinib→ERBB2 억제, AT7519→CDK1/2/6 억제 같은 표적 효과는 물론 lapatinib→CDK4 활성화 같은 보상성 우회 경로까지 phosphoproteome로 포착해, 어떤 kinase 경로가 실제로 약물에 반응하는지를 보여준다.

**Cited**: [Casado 2013](../sources/casado-2013-kinase-substrate-enrichment-analysis-provides-insights.md), [Wiredja 2017](../sources/wiredja-2017-ksea-app-web-based-tool-kinase.md), [Zhao 2025](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md)

### Q68. acetylome은 epigenetic regulator와 metabolic enzyme을 어떻게 연결하는가?
**A.** acetylome는 epigenetic regulator(histone·chromatin)와 metabolic enzyme을 같은 lysine acetylation 층 위에서 연결한다. [Geffen 2023](../sources/geffen-2023-pan-cancer-analysis-post-translational-modifications-reveals.md)는 pan-cancer에서 acetylation이 histone 조절 변화와 면역 연관 대사 조절을 동시에 주도한다고 보고했고, [Choudhary 2009](../sources/choudhary-2009-lysine-acetylation-targets-protein-complexes.md)는 acetylation이 chromatin remodeling 복합체뿐 아니라 광범위한 대사·세포주기 단백질을 표적함을 보였다. HDAC 억제제 SAHA를 처리한 [Huang 2022](../sources/huang-2022-suberoylanilide-hydroxamic-acid-saha-treatment.md)는 acetylome 변화가 proteome·phosphoproteome 변화와 crosstalk함을 보였고, [Zhao 2025](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md)는 abundance 보정 후 HSPD1(샤페론) K72–S70 같은 동일 단백질 acetyl-phospho 짝을 찾아 대사·신호 효소 수준에서 두 PTM이 연결됨을 구체적으로 보여준다.

**Cited**: [Geffen 2023](../sources/geffen-2023-pan-cancer-analysis-post-translational-modifications-reveals.md), [Choudhary 2009](../sources/choudhary-2009-lysine-acetylation-targets-protein-complexes.md), [huang-2022-suberoylanilide-hydroxamic-acid-saha-treatment](../sources/huang-2022-suberoylanilide-hydroxamic-acid-saha-treatment.md), [Zhao 2025](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md)

### Q69. supervised clinical outcome model과 unsupervised subtype model은 목적이 어떻게 다른가?
**A.** supervised clinical outcome model과 unsupervised subtype model은 목적이 다르다. unsupervised 모델은 결과 라벨 없이 데이터 구조만으로 환자 군(endotype/subtype)을 발견하는 것이 목적으로, [Tyler 2021](../sources/tyler-2021-merged-affinity-network-association-clustering.md)의 MANAclust는 임상·다중오믹스 데이터를 통합해 라벨 없이 군집을 찾고 임상적으로 유사한 환자도 분자적으로는 이질적일 수 있음을 드러낸다. 반면 supervised 모델은 미리 정해진 표적(예: 약물 감수성, 기능 라벨)을 예측하도록 학습하는데, [Casado 2013](../sources/casado-2013-kinase-substrate-enrichment-analysis-provides-insights.md)은 기질 abundance로 PI3K/mTOR 억제제 감수성을 예측하는 supervised 모델을 만들었고 [Shi 2025](../sources/shi-2025-mapping-functional-network-human-cancer.md)의 FunMap은 supervised machine learning으로 기능적 유전자 네트워크를 구축한다. 즉 unsupervised는 '어떤 군이 존재하는가'를, supervised는 '특정 결과를 어떻게 예측·설명하는가'를 묻는다.

**Cited**: [Tyler 2021](../sources/tyler-2021-merged-affinity-network-association-clustering.md), [Casado 2013](../sources/casado-2013-kinase-substrate-enrichment-analysis-provides-insights.md), [shi-2025-mapping-functional-network-human-cancer](../sources/shi-2025-mapping-functional-network-human-cancer.md)

### Q70. pan-cancer clustering에서 tissue of origin과 molecular state를 어떻게 분리할 수 있는가?
**A.** pan-cancer clustering에서 tissue of origin과 molecular state를 분리하려면, 조직 계통을 가로지르는 단백질·경로 기반 군집을 따로 정의하면 된다. [Chen 2019](../sources/chen-2019-pan-cancer-molecular-subtypes-proteomic-characterization.md)와 [Zhang 2022](../sources/zhang-2022-proteogenomic-characterization-2002-human-cancers.md)는 proteome 기반 pan-cancer subtype이 원발 조직 계통을 넘어 공통의 경로 구조(예: 면역·기질·대사 상태)로 묶임을 보여, tissue of origin과 분자 상태가 서로 다른 축임을 드러낸다. [Li 2023](../sources/li-2023-pan-cancer-proteogenomics-connects-oncogenic-drivers.md)도 서로 다른 cancer gene·암종이 유사한 kinase activity로 정의되는 분자 상태로 수렴한다고 보고해, 조직 기원으로 설명되지 않는 molecular state 축을 분리해 분석할 근거를 제공한다.

**Cited**: [Chen 2019](../sources/chen-2019-pan-cancer-molecular-subtypes-proteomic-characterization.md), [Zhang 2022](../sources/zhang-2022-proteogenomic-characterization-2002-human-cancers.md), [Li 2023](../sources/li-2023-pan-cancer-proteogenomics-connects-oncogenic-drivers.md)

### Q71. identification count가 높은 논문이 반드시 더 좋은 biological insight를 주는가?
**A.** identification count가 높다고 더 좋은 biological insight를 보장하지는 않는다. [Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md)은 105개 유방암에서 62,679개 phosphosite를 잡았지만, 핵심 통찰(5q 결손의 trans-effect로 EGFR·SRC 상승, mRNA에서 안 보이던 GPCR cluster)은 수 자체가 아니라 phosphoproteome를 유전체 이벤트와 통합한 분석에서 나왔다. [Clark 2020](../sources/clark-2020-integrated-proteogenomic-characterization-clear-cell.md)도 동일 유전체 alteration이 RNA보다 protein/phospho 수준에서 기능 모듈(대사·번역·kinase signaling)을 더 직접 드러낸다는 점을 강조해, count보다 abundance 맥락·통합 설계가 insight를 만든다는 것을 보여준다. 따라서 atlas 시각화에서 count는 자원 규모 지표일 뿐, 생물학적 가치의 대리지표로 쓰면 안 된다.

**Cited**: [Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md), [Clark 2020](../sources/clark-2020-integrated-proteogenomic-characterization-clear-cell.md)

### Q72. count가 낮지만 perturbation design인 논문은 어떤 가치가 있는가?
**A.** count가 낮아도 perturbation 설계 논문은 정적 atlas가 줄 수 없는 인과·동역학 정보를 준다. [Hsu 2025](../sources/hsu-2025-phosphoproteomics-osimertinib-tolerant-persister-cells-reveals.md)는 한 세포주에서 평균 약 5,200 단백질·21,500 phosphopeptide 정도만 정량했지만, osimertinib 급성→persister→회복의 시간 분해 설계로 CDK1 기질·mTOR·YAP1·BAD 인산화 같은 약물내성 상태 신호를 분리해냈다. [Huang 2022](../sources/huang-2022-suberoylanilide-hydroxamic-acid-saha-treatment.md)도 SAHA 처리 한 세포주에서 acetylation site는 수백 개 수준이지만, HDAC 억제 후 인산화-아세틸화 crosstalk를 직접 관찰하는 데 가치가 있었다. 즉 perturbation 논문의 가치는 규모가 아니라 '특정 자극에 어떤 site가 어떻게 반응하는가'라는 가설 검증력에 있다.

**Cited**: [Hsu 2025](../sources/hsu-2025-phosphoproteomics-osimertinib-tolerant-persister-cells-reveals.md), [huang-2022-suberoylanilide-hydroxamic-acid-saha-treatment](../sources/huang-2022-suberoylanilide-hydroxamic-acid-saha-treatment.md)

### Q73. cohort atlas 논문과 cell-line perturbation 논문은 같은 visualization에 넣을 때 어떻게 구분해야 하는가?
**A.** cohort atlas와 cell-line perturbation 논문은 같은 plot에 넣더라도 '관찰 대상'과 '비교 축'이 달라 명시적으로 구분해야 한다. [Huang 2022](../sources/huang-2022-suberoylanilide-hydroxamic-acid-saha-treatment.md)는 자신이 단일 세포주 perturbation 연구이므로 환자 종양 코호트와 시각적으로 분리되어야 한다고 직접 언급하며, count 단위도 코호트 atlas와 다르게 reporting된다고 적는다. 반대로 [Knol 2025](../sources/knol-2025-pan-cancer-proteome-atlas-mass-spectrometry-based.md)의 TPCPA는 22개 암종 999개 일차 종양을 가로지르는 cross-tumor 비교가 목적이다. 따라서 색·패널·축으로 sample type(환자 종양 vs 세포주)과 비교 의도(횡단 atlas vs 처리 전후 동역학)를 분리 표기하는 것이 안전하다.

**Cited**: [huang-2022-suberoylanilide-hydroxamic-acid-saha-treatment](../sources/huang-2022-suberoylanilide-hydroxamic-acid-saha-treatment.md), [Knol 2025](../sources/knol-2025-pan-cancer-proteome-atlas-mass-spectrometry-based.md)

### Q74. sample 수와 feature 수를 동시에 보여주는 plot은 어떤 해석을 가능하게 하는가?
**A.** sample 수(코호트 크기)와 feature 수(단백질·phosphosite 수)를 한 plot에서 같이 보여주면 '통계 검정력'과 '분자 해상도'를 동시에 읽을 수 있다. 다만 feature 축은 단위가 섞이지 않게 주의해야 하는데, [Clark 2020](../sources/clark-2020-integrated-proteogenomic-characterization-clear-cell.md)은 phosphopeptide(42,889 식별)와 phosphosite(100,730)를 서로 다른 처리 수준으로 보고하므로 count type을 합치지 말라고 명시하고, [Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md)도 proteins/phosphosites의 식별 vs 정량(15,369→12,553, 62,679→33,239) 수가 다르다는 점을 보여준다. 즉 이런 plot은 '큰 코호트지만 얕은 coverage' vs '작지만 깊은' 연구를 한눈에 대비시키되, feature 축에는 반드시 단위(identified/quantified, peptide/site)를 라벨해야 오독을 막는다.

**Cited**: [Clark 2020](../sources/clark-2020-integrated-proteogenomic-characterization-clear-cell.md), [Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md)

### Q75. method/instrument/enrichment/count를 함께 보여줄 때 가장 이해하기 쉬운 시각화 구조는 무엇인가?
**A.** method/instrument/enrichment/count를 함께 보여줄 때는 각 논문을 한 행(row)으로 두고 단위가 보존된 다속성 테이블/패널 구조가 가장 읽기 쉽다. 로컬 sources의 'Multi-Omics Identification Extraction' 항목이 이미 이 구조를 따르는데, 예컨대 [Clark 2020](../sources/clark-2020-integrated-proteogenomic-characterization-clear-cell.md)은 proteome/phospho count, TMT 10-plex, IMAC enrichment, Fusion Lumos를 한 묶음으로 보고하고, [Huang 2022](../sources/huang-2022-suberoylanilide-hydroxamic-acid-saha-treatment.md)는 TMT 6-plex·TiO2·anti-acetyl-lysine·Q Exactive와 함께 'count 단위가 코호트 논문과 다르다'고 주석한다. 핵심은 method·enrichment·instrument를 count 옆 메타 컬럼으로 두어, 큰 count가 깊은 분석 때문인지 다른 enrichment/플랫폼 때문인지 독자가 분리해 볼 수 있게 하는 것이다.

**Cited**: [Clark 2020](../sources/clark-2020-integrated-proteogenomic-characterization-clear-cell.md), [huang-2022-suberoylanilide-hydroxamic-acid-saha-treatment](../sources/huang-2022-suberoylanilide-hydroxamic-acid-saha-treatment.md)

### Q76. 연도별 기술 발전을 보여주는 plot은 count 증가와 method adoption을 어떻게 분리해야 하는가?
**A.** 연도별 plot은 'count 증가'와 'method adoption'을 같은 축에 섞지 말고, 한 트랙은 식별 수, 다른 트랙은 도입된 기술(예: DIA, Astral)로 분리해야 한다. count 증가의 상당 부분이 방법 전환에서 오기 때문인데, [Lancaster 2024](../sources/lancaster-2024-fast-deep-phosphoproteome-analysis-orbitrap.md)는 Orbitrap Astral과 DIA로 30분 만에 약 30,000개 인간 phosphosite를 매핑해, 깊이 자체가 기기·획득방식의 함수임을 보여준다. [Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md)의 iTRAQ 시대 코호트와 비교하면 절대 수 차이는 생물학이 아니라 enrichment·labeling·instrument 세대 차이를 반영하므로, 연도 plot은 method를 명시적 범주(색/주석)로 표기해 count 곡선과 분리해야 한다.

**Cited**: [Lancaster 2024](../sources/lancaster-2024-fast-deep-phosphoproteome-analysis-orbitrap.md), [Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md)

### Q77. cancer type별 proteome/phospho/acetyl coverage gap은 어떤 ingest 우선순위를 만든다?
**A.** cancer type별 proteome/phospho/acetyl coverage를 비교하면 layer가 빠진 암종이 곧 ingest 우선순위가 된다. 로컬 코호트에서 phospho는 흔하지만 acetylome은 드문데, [Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md)과 [Clark 2020](../sources/clark-2020-integrated-proteogenomic-characterization-clear-cell.md) 모두 추출 텍스트상 별도 acetylome layer를 보고하지 않아 acetyl coverage 공백이 크다. 반면 [Knol 2025](../sources/knol-2025-pan-cancer-proteome-atlas-mass-spectrometry-based.md)의 TPCPA는 22개 암종 proteome를 넓게 덮어 proteome 공백은 작은 편이다. 따라서 우선순위는 acetylome이 있는 암종/연구(예: HCC의 다중 PTM 프로파일)를 먼저 채우고, proteome만 풍부하고 phospho/acetyl이 비는 암종을 다음으로 ingest하는 식으로 layer-결손 기준으로 정하는 것이 합리적이다.

**Cited**: [Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md), [Clark 2020](../sources/clark-2020-integrated-proteogenomic-characterization-clear-cell.md), [Knol 2025](../sources/knol-2025-pan-cancer-proteome-atlas-mass-spectrometry-based.md)

### Q78. acetylome 포함 연구가 적다면 methods-level explanation을 별도 section으로 써야 하는가?
**A.** acetylome 포함 연구가 적다면 별도 methods-level section을 두는 것이 타당하다. 로컬 acetylome 연구들은 count 단위·enrichment가 phospho와 뚜렷이 다르기 때문인데, [Huang 2022](../sources/huang-2022-suberoylanilide-hydroxamic-acid-saha-treatment.md)는 anti-lysine-acetylation 항체 enrichment로 441개 acetyl site(298 단백질)만 식별하고 이 단위가 코호트 atlas와 다르다고 주석하며, [Choudhary 2009](../sources/choudhary-2009-lysine-acetylation-targets-protein-complexes.md)는 고해상도 MS로 3,600개 acetyl site를 처음 전역 측정해 acetylation 측정 자체가 기술적으로 phospho와 별개 워크플로우임을 보여준다. 즉 적은 수와 다른 enrichment·정량 단위를 설명하는 methods 노트를 분리해 두면, 독자가 'acetylome 데이터 희소 = 생물학적 부재'로 오해하지 않는다.

**Cited**: [huang-2022-suberoylanilide-hydroxamic-acid-saha-treatment](../sources/huang-2022-suberoylanilide-hydroxamic-acid-saha-treatment.md), [Choudhary 2009](../sources/choudhary-2009-lysine-acetylation-targets-protein-complexes.md)

### Q79. 2024-2026 흐름(DIA, Astral, single-cell/spatial)은 어떻게 등장하는가?
**A.** 2024-2026 흐름은 DIA와 Orbitrap Astral 같은 신형 기기, 그리고 pan-cancer atlas 규모 확대로 등장한다. [Lancaster 2024](../sources/lancaster-2024-fast-deep-phosphoproteome-analysis-orbitrap.md)는 Astral+DIA로 30분에 약 30,000개 phosphosite, 12시간에 81,120개를 매핑하며 single-shot 고심도 phospho 시대를 연다. [Knol 2025](../sources/knol-2025-pan-cancer-proteome-atlas-mass-spectrometry-based.md)/[Du 2025](../sources/du-2025-unified-pan-cancer-proteome-atlas.md)의 TPCPA는 single-shot DIA-MS로 22개 암종 999 종양을 통합해 atlas 규모를 키웠고, [Koudelka 2025](../sources/koudelka-2025-benchmarking-quantitative-proteomics-workflows-limited.md)는 Astral 같은 기기 발전이 sequence coverage를 높여 TMT labeling 필요를 줄일 수 있다고 전망한다. 다만 로컬 sources에서 single-cell/spatial proteomics를 직접 다룬 핵심 PTM 논문은 드물어, 이 축은 현재 위키 근거가 얇다.

**Cited**: [Lancaster 2024](../sources/lancaster-2024-fast-deep-phosphoproteome-analysis-orbitrap.md), [Knol 2025](../sources/knol-2025-pan-cancer-proteome-atlas-mass-spectrometry-based.md), [Du 2025](../sources/du-2025-unified-pan-cancer-proteome-atlas.md), [Koudelka 2025](../sources/koudelka-2025-benchmarking-quantitative-proteomics-workflows-limited.md)

### Q80. foundation model/ML integration은 atlas에서 어떤 downstream task에 쓰이는가?
**A.** foundation model/ML integration은 atlas에서 주로 (1) 미주석 site/유전자에 기능을 부여하는 network 추론과 (2) kinase 활성·기질 관계 예측 같은 downstream task에 쓰인다. [Shi 2025](../sources/shi-2025-functional-network-human-cancer-proteogenomics.md)는 CPTAC 11개 암종 1,194명 데이터에 supervised ML을 적용해 FunMap(10,525개 유전자 functional network)을 만들고, protein coexpression이 RNA보다 기능 추론에 유리함을 보이며 understudied 단백질에 기능을 배정한다. [Jiang 2025](../sources/jiang-2025-deciphering-dark-cancer-phosphoproteome-using.md)는 XGBoost 기반 CoPheeMap/CoPheeKSA로 dark phosphosite의 co-regulation을 학습해 9,399개 site와 104개 S/T kinase 사이 24,015개 kinase-substrate 관계를 예측하고, 이를 kinase-activity 추론의 pan-cancer prior 및 understudied kinase 가설 생성기로 제시한다.

**Cited**: [Shi 2025](../sources/shi-2025-functional-network-human-cancer-proteogenomics.md), [Jiang 2025](../sources/jiang-2025-deciphering-dark-cancer-phosphoproteome-using.md)

### Q81. human cancer 대상이 아닌 method paper는 support source로 남길 것인가 제외할 것인가?
**A.** 로컬 코퍼스에는 human cancer 대상이 아닌 method/atlas 논문이 실제로 섞여 있다 — 예컨대 [Lancaster 2024](../sources/lancaster-2024-fast-deep-phosphoproteome-analysis-orbitrap.md)는 EGF 자극 HeLa 벤치마크와 mouse multi-tissue phosphoproteome atlas이고, [Gonçalves 2022](../sources/gonalves-2022-pan-cancer-proteomic-map-949-human.md)는 949개 cancer cell line map, [Gong 2020](../sources/gong-2020-time-resolved-multi-omic-atlas-developing-mouse.md)은 mouse liver atlas다. 이들은 환자 코호트 count 비교(proteome/phospho/acetyl bar)에는 넣지 말고, MS 기법·instrument·localization·KSA prior 같은 method context를 뒷받침하는 support source로만 남기는 것이 일관된 처리다. 즉 제외가 아니라 '환자 count 축에서 분리, method 근거로 보존'이며, 이는 위키 atlas가 pan-cancer compendia를 단일 실험 bar가 아닌 aggregate로 따로 다루는 원칙과 같은 결이다.

**Cited**: [Lancaster 2024](../sources/lancaster-2024-fast-deep-phosphoproteome-analysis-orbitrap.md), [Gonçalves 2022](../sources/gonalves-2022-pan-cancer-proteomic-map-949-human.md), [Gong 2020](../sources/gong-2020-time-resolved-multi-omic-atlas-developing-mouse.md)

### Q82. review 논문은 count source가 아니라 method context로만 써야 하는가?
**A.** 그렇다 — review는 identification count source가 아니라 method/decision context로 쓰는 것이 맞다. [Savage 2020](../sources/savage-2020-phosphoproteomics-bioinformatics-comprehensive-guide.md)은 16개 kinase 지식베이스·27개 phospho-site DB와 4개 kinase activity inference 도구(KSEA App·PHOXTRACK 등)를 벤치마크한 review로, 자체 코호트 단백질/phosphosite count를 생산하지 않고 '어떤 도구·DB를 ground truth로 쓸지'의 의사결정 매트릭스를 제공한다. 실제로 위키의 100-PDF bulk-ingest 작업도 promotion 우선순위를 'primary human cancer response 논문 > methods·reviews·databases'로 두어 review를 count가 아닌 맥락 근거로 분리한다. 따라서 review의 PhosphoSitePlus(실험)·NetworKIN(예측) 권고나 ID-mapping 오류 경고는 파이프라인 가이드로만 인용하고, atlas count bar에는 반영하지 않는다.

**Cited**: [Savage 2020](../sources/savage-2020-phosphoproteomics-bioinformatics-comprehensive-guide.md)

### Q83. raw PDF만 있고 source page가 약한 논문은 어떤 extraction checklist로 보강해야 하는가?
**A.** raw PDF만 있고 source page가 약한 논문은 위키의 'Multi-Omics Identification Extraction' 체크리스트로 보강하는 것이 일관된 방식이다 — 즉 (1) cohort/scope, (2) proteome count(+단위), (3) phospho count(+단위), (4) acetyl/기타 PTM, (5) MS method(labeling·enrichment), (6) instrument/platform, (7) extraction evidence(어느 본문/STAR Methods 문장에서 왔는지) 7필드를 본문 그대로의 reporting unit으로 채운다. [Dou 2020](../sources/dou-2020-proteogenomic-characterization-endometrial-carcinoma.md)이 이 체크리스트의 모범으로, 12,153 protein groups·73,212 phosphosites·10,862 acetyl sites를 STAR Methods 문장과 함께 적고 instrument(nanoACQUITY UPLC–Orbitrap Fusion Lumos)까지 명시한다. PDF 본문에 instrument가 안 나오면 [Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md)처럼 해당 필드를 `needs_supplement`로 표시해 보강 대상으로 남긴다.

**Cited**: [Dou 2020](../sources/dou-2020-proteogenomic-characterization-endometrial-carcinoma.md), [Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md)

### Q84. supplement(Excel/PRIDE)가 필요한 논문은 ingest status를 어떻게 표시해야 하는가?
**A.** supplement(Excel/PRIDE)가 있어야 정확한 값이 나오는 논문은 ingest status를 단계적으로 표시한다 — 로컬 PDF만 자동 추출한 상태는 `pdf-text-extracted`(본문 high-signal snippet만 확보, 과학적 단정 보류)로, 수동 정독을 마치면 `full-text-read`로 promotion한다. [Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md)은 본문에 instrument 모델이 안 나와 그 필드를 `needs_supplement`로 두고, 나머지 count는 본문 추출치(15,369 identified vs 12,553 quantified proteins)로 채운 좋은 예다. 핵심은 필드별로 'extraction evidence'를 적고, supplement가 raw/로 다운로드되어 재정독되기 전에는 그 값을 확정 인용하지 않는다는 점이다.

**Cited**: [Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md), [Dou 2020](../sources/dou-2020-proteogenomic-characterization-endometrial-carcinoma.md)

### Q85. inaccessible supplement는 visualization에서 어떤 caveat로 처리해야 하는가?
**A.** 접근 불가한 supplement는 visualization에서 '추정 금지·보류' caveat로 처리한다 — 해당 count/필드를 임의 보간하지 말고 NR(not reported) 또는 `needs_supplement`로 비워 두고, bar 옆에 'PDF 본문 추출치이며 supplement 미확보' 단서를 붙인다. 실제로 [Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md)은 instrument를 supplement 확보 전까지 `needs_supplement`로 보류했고, [Satpathy 2021](../sources/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.md)은 proteome 총수가 본문에 안 잡혀 atlas에서 'NR'로 둔 채 phospho 68,674·acetyl 15,186만 표기한다. 이렇게 하면 inaccessible supplement가 만든 결측이 0으로 오독되거나 다른 코호트와 부당 비교되는 것을 막는다.

**Cited**: [Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md), [Satpathy 2021](../sources/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.md)

### Q86. 같은 논문 내에서 proteome vs phospho vs acetyl count의 정의가 뒤섞일 때 어떻게 정리할까?
**A.** 같은 논문 안에서 proteome·phospho·acetyl의 count 정의가 섞이면, 변환하지 말고 각 PTM layer를 별도 단위로 분리 기록하는 것이 원칙이다. [Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md) Key Points는 'proteins, protein groups, phosphosites, phosphopeptides, acetylsites'를 하나의 공통 metric으로 합치면 count unit이 깨진다고 명시한다. [Dou 2020](../sources/dou-2020-proteogenomic-characterization-endometrial-carcinoma.md)은 이를 모범적으로 처리해 protein groups(12,153)·phosphosites(73,212)·acetyl sites(10,862)를 각각 다른 단위로 적고, 게다가 전체 합계와 per-tumor 평균(10,088 proteins·29,710 phosphosites·3,821 acetyl)을 구분해 둔다. 따라서 layer별·집계수준별로 칸을 나누고 'reported unit 그대로' 보존하는 것이 정답이다.

**Cited**: [Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md), [Dou 2020](../sources/dou-2020-proteogenomic-characterization-endometrial-carcinoma.md)

### Q87. “quantified”와 “identified”를 혼용하는 논문은 어떻게 구분해 기록할까?
**A.** 'identified'와 'quantified'를 혼용하는 논문은 두 수를 같은 칸에 합치지 말고 별도 필드로 분리해 적어야 한다. [Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md)이 대표 사례로, 본문 추출 근거가 '15,369 proteins·62,679 phosphosites identified'인 반면 필터링 후 '12,553 proteins·33,239 phosphosites quantified'여서 두 정의의 격차가 약 2배에 이른다. [Jiang 2025](../sources/jiang-2025-deciphering-dark-cancer-phosphoproteome-using.md)도 pan-cancer에서 158,796 phosphosites '검출' 중 77,442개만 '≥20% 샘플에서 quantified'로 따로 보고하므로, 기록 시 'identified(검출 총수)'와 'quantified(결측 기준 통과)'를 양 칸으로 나누고 quantifiable 기준(예: missing-value threshold)을 함께 명시하는 것이 일관된 처리다.

**Cited**: [Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md), [Jiang 2025](../sources/jiang-2025-deciphering-dark-cancer-phosphoproteome-using.md)

### Q88. protein group vs gene-level abundance를 동일 축에 놓을 수 있는가?
**A.** protein group과 gene-level abundance는 정의가 달라 같은 축에 무비판적으로 놓을 수 없고, 단위를 명시한 뒤에만 비교해야 한다. [Dou 2020](../sources/dou-2020-proteogenomic-characterization-endometrial-carcinoma.md)은 reporting unit을 명시적으로 'protein groups'(12,153)로 적어 단백질 그룹이 곧 gene 수가 아님을 드러내고, 위키 atlas는 phosphopeptide/phosphosite/protein group을 'false common metric'으로 환산하지 않는다는 원칙을 둔다. 한편 [Jiang 2025](../sources/jiang-2025-deciphering-dark-cancer-phosphoproteome-using.md)의 CPTAC pan-cancer matrix처럼 14,103 proteins와 21,592 genes(RNA)를 별 축으로 둔 사례는, protein group을 gene 축에 합치려면 명시적 group→gene 매핑이 선행돼야 함을 보여준다. 따라서 동일 축 표기는 '단위가 protein group인지 gene-level인지'를 라벨로 고정하고 매핑 규칙을 밝힌 경우에 한해 허용한다.

**Cited**: [Dou 2020](../sources/dou-2020-proteogenomic-characterization-endometrial-carcinoma.md), [Jiang 2025](../sources/jiang-2025-deciphering-dark-cancer-phosphoproteome-using.md)

### Q89. phosphosite count가 “localized”인지 여부를 어떻게 표준화할까?
**A.** phosphosite count의 'localized' 여부 표준화에 대해 localization probability 임계(예: class I, 0.75)를 명시적으로 정의한 전용 로컬 논문은 확인되지 않았다 — 다만 로컬 근거가 시사하는 일관된 처리는, count를 본문이 보고한 단위(phosphosite vs phosphopeptide)와 통과 기준 그대로 보존하는 것이다. [Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md)은 phosphopeptide와 phosphosite를 별개 단위로 구분하라고 지적하고, [Jiang 2025](../sources/jiang-2025-deciphering-dark-cancer-phosphoproteome-using.md)은 158,796개 검출 site 중 '≥20% 샘플 quantified' 77,442개만 분석에 쓰는 식으로 site-level 필터 기준을 명시한다. 따라서 표준화 시 각 논문이 site를 어떤 단위·어떤 필터(검출/quantified, 그리고 보고됐다면 localization 기준)로 셌는지를 메타필드로 기록하고, 그 기준이 본문에 없으면 `needs_supplement`로 보류하는 것이 권고된다.

**Cited**: [Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md), [Jiang 2025](../sources/jiang-2025-deciphering-dark-cancer-phosphoproteome-using.md)

### Q90. LC/MS 기기 업그레이드가 sample 처리량과 어떻게 연결되는가?
**A.** LC/MS 기기 업그레이드는 단위 시간당 깊이를 키워 sample 처리량과 직결된다. [Lancaster 2024](../sources/lancaster-2024-fast-deep-phosphoproteome-analysis-orbitrap.md)는 Orbitrap Astral+DIA로 30분 측정에 약 30,000개 human phosphosite를, 12시간에 81,120개를 매핑해 짧은 gradient에서도 deep phosphoproteome가 가능함을 보였다 — 즉 같은 시간 예산에서 더 많은 샘플을 돌릴 수 있다. [Koudelka 2025](../sources/koudelka-2025-benchmarking-quantitative-proteomics-workflows-limited.md)도 Astral 같은 기기 발전이 sensitivity·sequence coverage를 높여 TMT multiplexing 의존을 줄일 수 있다고 본다. atlas 기록 관점에서는 instrument/platform을 cohort count와 함께 적어야 하는 이유가 여기에 있으며([Dou 2020](../sources/dou-2020-proteogenomic-characterization-endometrial-carcinoma.md)의 Orbitrap Fusion Lumos 명시처럼), 동일 count도 어떤 기기·throughput에서 나왔는지에 따라 해석이 달라지기 때문이다.

**Cited**: [Lancaster 2024](../sources/lancaster-2024-fast-deep-phosphoproteome-analysis-orbitrap.md), [Koudelka 2025](../sources/koudelka-2025-benchmarking-quantitative-proteomics-workflows-limited.md), [Dou 2020](../sources/dou-2020-proteogenomic-characterization-endometrial-carcinoma.md)

### Q91. “많이 식별했다”보다 중요한 method quality indicator는 무엇인가?
**A.** 단순 식별 수(phosphosite/peptide count)보다 정량의 정확도와 site-localization 신뢰도가 더 중요한 품질 지표다. [Koudelka 2025](../sources/koudelka-2025-benchmarking-quantitative-proteomics-workflows-limited.md)는 TMT가 더 많은 펩타이드를 낮은 CV로 정량하지만 실제 표적을 정확히 잡고 용량-반응 상관이 강한 쪽은 오히려 DIA였음을 보여, '많이'와 '정확히'가 다른 축임을 입증한다. [Hornbeck 2015](../sources/hornbeck-2015-phosphositeplus-2014-mutations-ptms-recalibrations.md)는 100만 개 이상의 스펙트럼을 공통 기준으로 재분석해 site assignment P>0.05인 부위를 제거했는데, 이런 localization FDR 통제가 raw count보다 신뢰성을 좌우한다. 따라서 위키에서는 식별 수와 함께 정량 CV·재현성, FDR·localization 기준, 검증된 표적 회수율을 method quality로 명시해야 한다.

### Q92. reproducibility, missingness, batch correction, clinical scalability를 한 페이지에 어떻게 같이 설명할 것인가?
**A.** reproducibility, missingness, batch correction, clinical scalability는 '정량 신뢰도'라는 한 축으로 묶어 단계별로 배치하면 한 페이지에 정리된다. [Kohler 2023](../sources/kohler-2023-msstatsptm-statistical-relative-quantification-posttranslational.md)의 MSstats(PTM) 프레임워크는 다양한 실험설계와 데이터 획득 방식에서 차등 풍부도를 검정하는 통계 모델·컨버터를 제공해, missingness 처리와 모델 견고성이 reproducibility로 이어짐을 보여준다. [Abelin 2023](../sources/abelin-2023-workflow-enabling-deepscale-immunopeptidome-proteome.md)의 MONTE 워크플로우는 한 시료에서 여러 ome를 직렬 분석해도 각 ome의 coverage와 정량 정밀도가 손상되지 않음을 보여 batch/시료 절약과 재현성을 동시에 다루는 사례다. 따라서 한 페이지에는 (1) 재현성·CV, (2) 결측 처리, (3) 배치 보정, (4) 적은 시료로의 임상 확장성을 동일 정량-신뢰도 흐름으로 도식화하면 된다.

### Q93. 현재 위키에서 identification count와 biological interpretation 사이의 연결이 약한 지점은 어디인가?
**A.** 식별 수와 생물학적 해석이 끊기는 지점은 '검출된 phosphosite가 어떤 상위 kinase·기능에 연결되는가'를 잇지 못하는 곳이다. [Savage 2020](../sources/savage-2020-phosphoproteomics-bioinformatics-comprehensive-guide.md)은 집계된 485개 kinase substrate set 중 절반 이상이 기질 10개 미만이라, 부위를 많이 식별해도 대부분이 상위 kinase로 귀속되지 못함을 보고한다. [Muller-Dott 2025](../sources/muller-dott-2025-phosphoproteomic-kinase-activity-inference.md) 역시 라이브러리에서 상위 kinase로 귀속 가능한 부위가 적어 kinase activity inference 범위가 제한된다고 지적한다. 위키에서는 count 옆에 '몇 %가 kinase/기능 주석에 연결되는가'를 함께 적어야 식별-해석 간 연결 약점이 드러난다.

### Q94. 각 source page의 `Multi-Omics Identification Extraction` 섹션을 표준화하려면 어떤 fields가 필수인가?
**A.** 각 source page의 `Multi-Omics Identification Extraction` 섹션은 코호트/범위·분류, ome별 count 후보(proteome/phospho/acetylome), 그리고 정량/기기 근거 같은 필수 field로 표준화하는 것이 좋다. 실제 [Zou 2024](../sources/zou-2024-iprophos-web-based-interactive-platform-integrated.md)의 source page는 'Cohort/scope', 'Proteome count candidate: 1426', 'Phosphoproteome count candidate: not confidently extracted', 'Method/instrument evidence' 형식을 이미 쓰고 있어 이 골격을 공통 템플릿으로 삼을 수 있다. 핵심은 추출이 불확실하면 'not confidently extracted'처럼 결측을 명시하고, 모든 수치에 로컬 PDF 근거를 붙여 환각을 막는 것이다. 따라서 필수 field는 분류(paper_kind), ome별 count(+추출 신뢰도), 기기/방법 근거, 그리고 근거 출처 표기다.

### Q95. `interactives/.../data/studies.json`과 source page 사이 provenance를 어떻게 검증할 것인가?
**A.** `studies.json`과 source page 사이 provenance는 각 수치가 동일한 로컬 PDF 근거로 역추적되는지 대조해 검증한다. [Zou 2024](../sources/zou-2024-iprophos-web-based-interactive-platform-integrated.md) source page는 count 후보(예: proteome 1426)와 'Method/instrument evidence from local PDF' 스니펫을 함께 기록하고 '웹 페이지는 근거로 쓰지 않았다'고 명시하므로, studies.json의 각 study row를 이 PDF-근거 스니펫·count 후보와 1:1로 맞추면 된다. 추출 신뢰도가 낮은 항목('not confidently extracted')은 studies.json에서도 결측 또는 미검증으로 표기해 일치시켜야 한다. 즉 검증 절차는 (1) slug 매칭, (2) count·방법 수치의 PDF 스니펫 대조, (3) 불확실 항목의 결측 표기 일치 확인이다.

### Q96. 같은 논문의 duplicate source page가 있을 때 어떤 canonical page를 유지할 것인가?
**A.** 같은 논문의 중복 source page가 있으면, 로컬 PDF가 실제로 ingest되어 Summary/Key Points·근거 스니펫이 채워진 페이지를 canonical로 유지해야 한다. 예컨대 [Muller-Dott 2025](../sources/muller-dott-2025-phosphoproteomic-kinase-activity-inference.md)는 'pdf-text-extracted'로 high-signal 스니펫과 Key Points·Relevance가 정리된 반면, 같은 연구의 다른 슬러그 'mullerdott-2025-comprehensive-evaluation-phosphoproteomic-based-kinase-activity'는 Publisher Correction에 가까운 얇은 페이지다. 이때 DOI/PMID가 동일하고 본문 근거가 풍부한 쪽을 canonical로 두고 다른 쪽은 redirect/merge 대상으로 표시한다. 판단 기준은 ingest 상태('pdf-text-extracted')와 Summary·근거의 충실도다.

### Q97. 다음 ingest batch는 cancer cohort diversity와 method diversity 중 무엇을 우선해야 하는가?
**A.** 다음 ingest 배치는 method diversity보다 cancer cohort diversity를 우선하는 편이 합리적이다. [Muller-Dott 2025](../sources/muller-dott-2025-phosphoproteomic-kinase-activity-inference.md)는 kinase activity inference 성능이 알고리즘 선택보다 substrate library 선택에 더 좌우되고, 세포주가 아닌 실제 종양 코호트 기반 평가에서 예측 표적을 더하면 성능이 개선됨을 보여, 다양한 종양 코호트의 가치가 큼을 시사한다. 다만 [Abelin 2023](../sources/abelin-2023-workflow-enabling-deepscale-immunopeptidome-proteome.md)의 MONTE처럼 한 시료에서 여러 ome를 정밀도 손실 없이 얻는 방법은 이미 확보돼 있으므로, 방법 축은 보강 수준으로 두고 코호트(암종) 다양성을 1차 우선순위로 삼는 것이 해석력 향상에 효율적이다.

### Q98. 최종 synthesis는 기술 발전사, cancer biology map, visualization atlas 중 무엇을 중심으로 구성해야 하는가?
**A.** 최종 synthesis는 기술 발전사나 visualization atlas보다 cancer biology map을 중심으로 구성하는 것이 적절하다. [Casado 2013](../sources/casado-2013-kinase-substrate-enrichment-analysis-provides-insights.md)은 KSEA로 일차 AML 환자에서 PI3K·CK·CDK·PAK 등 활성 kinase를 체계적으로 프로파일링하고 약물 감수성까지 예측해, phosphoproteomics가 암 신호전달 지도로 수렴할 때 임상적 의미가 생김을 보여준다. [Muller-Dott 2025](../sources/muller-dott-2025-phosphoproteomic-kinase-activity-inference.md)도 종양 코호트에서 신뢰할 만한 kinase 상태 추론을 downstream 생물학 해석에 쓰도록 프레임을 제시한다. 따라서 기술사·시각화는 이 cancer biology map(암종별 kinase/신호 축)을 뒷받침하는 보조 레이어로 두는 것이 좋다.

### Q99. 교수님께 공유할 때 가장 먼저 보여줘야 하는 plot과 가장 먼저 읽혀야 하는 explanation은 무엇인가?
**A.** 교수님께는 먼저 암종별 kinase activity(또는 신호 축) 비교 plot을 보여주고, 그 옆에 'count가 아니라 정량·해석 신뢰도가 핵심'이라는 설명을 가장 먼저 읽히는 것이 좋다. [Casado 2013](../sources/casado-2013-kinase-substrate-enrichment-analysis-provides-insights.md)의 KSEA 활성 프로파일처럼 추론된 kinase 활성·약물 감수성 연결이 한눈에 들어오는 그림이 메시지를 가장 빠르게 전달한다. 동시에 [Koudelka 2025](../sources/koudelka-2025-benchmarking-quantitative-proteomics-workflows-limited.md)가 보인 '많이 정량 vs 정확히 정량'의 구분을 설명 첫 문장에 두어, 그림의 수치를 어떻게 읽어야 하는지 caveat를 먼저 제시해야 한다. 즉 plot=생물학적 결론, 첫 설명=정량 신뢰도/해석 한계다.

### Q100. 독자가 methods를 읽고 스스로 count/method caveat를 판단하려면 무엇을 알아야 하는가?
**A.** 독자가 methods만 읽고 스스로 count·method caveat를 판단하려면, 정량 방식(예: TMT vs DIA)과 그 정확도-민감도 trade-off, FDR·site-localization 기준, 그리고 풍부도 보정 여부를 알아야 한다. [Koudelka 2025](../sources/koudelka-2025-benchmarking-quantitative-proteomics-workflows-limited.md)는 TMT가 더 많이·낮은 CV로 정량하지만 DIA가 표적 정확도·용량반응에서 낫고 FragPipe(정밀)와 Spectronaut(민감) 선택이 맥락 의존적임을 보여, 같은 데이터도 워크플로우에 따라 count·해석이 달라짐을 알려준다. [Wu 2011](../sources/wu-2011-correct-interpretation-comprehensive-phosphorylation-dynamics.md)은 phosphorylation 동역학의 올바른 해석에 단백질 발현 변화에 의한 정규화(abundance correction)가 필요함을 제목에서부터 못박는다. 따라서 methods에는 정량 플랫폼·FDR/localization 임계·단백질 수준 보정 여부를 명시해 독자가 caveat를 스스로 판단하게 해야 한다.
