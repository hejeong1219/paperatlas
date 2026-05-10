# Chen 2026 - Enrichment of Phosphorylated/Glycosylated MHC Peptides (Methods)

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Chen, Li
- 저널/연도: Methods in Molecular Biology, 2026 (Methods chapter)
- DOI: 10.1007/978-1-0716-4832-2_8
- Wiki 경로: [Enrichment of Phosphorylated and Glycosylated MHC Peptides for Mass Spectrometry-Based Neoantigen Analysis](../../sources/chen-2026-enrichment-phosphorylated-glycosylated-mhc-peptides.md)

## 한 줄 요약

phospho-neoantigen/glyco-neoantigen처럼 **PTM이 붙은 MHC peptide**는 예측만으로 한계가 있어, immunopeptidome에서 PTM peptide를 순차적으로 농축해 LC–MS/MS로 동정하는 워크플로를 제시한다.

## 과제 관련성 (Cancer Multiomics)

- WGS 기반 neoantigen 후보는 주로 “서열 변화(SNV/indel/SV)” 중심이지만, 실제 면역반응 유발 항원은 **PTM 기반 특이성**(phospho/glyco 등)까지 포함할 수 있어, 후보 확장 방향(예측→측정)의 레퍼런스가 된다.
- 인산화단백체와 면역펩티돔을 연결할 때 “phosphosite 변화가 곧바로 phospho-MHC peptide로 제시되는가?” 같은 질문을 던질 수 있고, 이를 실험적으로 접근하는 방법을 제공한다.
- 방법론 중심 논문이므로, 과제의 핵심 코퍼스에서는 “방법/확장 옵션”으로 분류해 두고 필요 시 적용 검토하는 형태가 적절하다.

## 주요 결과

- workflow 개요: MHC immunoprecipitation으로 immunopeptidome을 분리한 뒤, HILIC SPE로 glycopeptide를, TiO2 nanoparticle로 phosphopeptide를 순차 농축하고 LC–MS/MS + DB search로 동정한다.
- 예시 데이터(Calu-3 세포)에서 glycosylated MHC peptide는 주로 MHC class II, phosphorylated MHC peptide는 주로 MHC class I에서 관찰된다는 패턴을 보고한다.

## Slack 메시지 초안

Chen & Li Methods Mol Biol 2026는 immunopeptidome에서 glycosylated/phosphorylated MHC peptide를 순차적으로 농축(HILIC SPE → TiO2)해 LC–MS/MS로 동정하는 방법을 정리한 챕터입니다. Cancer Multiomics 과제에서 WGS 기반 neoantigen을 넘어 phospho-neoantigen 같은 PTM 기반 항원까지 확장하려면 “예측”이 아니라 “측정+농축” 워크플로가 필요할 수 있다는 점을 보여주는 방법 레퍼런스입니다.

