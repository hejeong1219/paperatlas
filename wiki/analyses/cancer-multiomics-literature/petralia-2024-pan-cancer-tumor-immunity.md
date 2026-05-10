# Petralia 2024 - Pan-Cancer Proteogenomics of Tumor Immunity

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Petralia, Ma, Yaron et al.
- 저널/연도: Cell, 2024
- DOI: 10.1016/j.cell.2024.01.027
- Wiki 경로: [Pan-cancer proteogenomics characterization of tumor immunity](../../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)

## 한 줄 요약

CPTAC pan-cancer proteogenomics를 이용해 tumor immune subtype, pathway activity, kinase activity를 함께 정의한 면역-단백유전체 지도.

## 표준 메타데이터

- 치료 맥락: pan-cancer immune atlas 성격; 치료/반응 라벨 포함 여부는 PDF 확인 필요
- 데이터 레이어: multi-omics + proteome + phosphoproteome 기반 immune subtype/kinase activity (세부 레이어는 PDF 확인 필요)
- 데이터 공개: CPTAC 기반(공개 경로는 PDF 확인 필요)

## 과제 관련성 (Cancer Multiomics)

- Cancer Multiomics 과제의 신생항원/면역회피/표적-면역치료제 반응성 예측 축과 가장 직접적으로 연결되는 pan-cancer immune proteogenomics reference다.
- 단순 immune cell abundance가 아니라 pathway activity와 phosphoproteomic kinase activity를 같이 보았다는 점이 Cancer Multiomics의 인산화단백체 기반 면역반응 해석에 중요하다.
- immune subtype별 genomic, epigenomic, transcriptomic, proteomic change를 함께 정리해 response model feature set 설계에 도움을 준다.
- CPTAC data harmonization, PDC/GDC 기반 분석 흐름, kinase enrichment는 과제의 데이터 기탁/공유 계획과도 연결된다.

## 주요 결과

- 1,000개 이상 tumor, 10개 cancer type의 CPTAC pan-cancer data로 immune landscape를 통합 분석했다.
- cell type composition과 pathway activity 기반으로 7개 immune subtype을 정의했다.
- immune subtype별 genomic, epigenetic, transcriptomic, proteomic feature를 함께 정리했다.
- phosphoproteomics를 이용해 subtype-specific kinase activity와 잠재적 therapeutic target을 제시했다.

## Slack 메시지 초안

Petralia et al. Cell 2024는 CPTAC pan-cancer proteogenomics로 tumor immunity를 7개 subtype으로 정리하고, phosphoproteomics 기반 kinase activity까지 연결한 논문입니다. Cancer Multiomics 과제에서 WGS/인산화단백체/neoantigen/immune feature를 통합해 표적-면역치료제 반응성을 예측하려는 방향과 매우 잘 맞고, 면역회피 feature를 어떻게 proteogenomic layer로 구성할지 참고할 만합니다.
