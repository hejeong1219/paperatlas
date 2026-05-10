# Li 2023 - Pan-Cancer Driver-to-Functional-State Proteogenomics

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Li, Porta-Pardo, Tokheim et al.
- 저널/연도: Cell, 2023
- DOI: 10.1016/j.cell.2023.07.014
- Wiki 경로: [Pan-cancer proteogenomics connects oncogenic drivers to functional states](../../sources/li-2023-pan-cancer-proteogenomics-connects-oncogenic-drivers.md)

## 한 줄 요약

1,000명 이상의 CPTAC pan-cancer cohort에서 oncogenic driver가 RNA, protein, phosphoprotein functional state로 어떻게 연결되는지 분석한 대규모 단백유전체 연구.

## 표준 메타데이터

- 치료 맥락: pan-cancer compendium(관찰/아틀라스 성격); 치료/반응 라벨은 PDF 확인 필요
- 데이터 레이어: genomics + transcriptomics + proteome + phosphoproteome (WGS/WES 등 상세는 PDF 확인 필요)
- 데이터 공개: CPTAC 통합 데이터 기반(공개 경로는 PDF 확인 필요)

## 과제 관련성 (Cancer Multiomics)

- Cancer Multiomics 과제의 “변이 목록”을 넘어서 “변이가 실제 단백질/인산화 기능 상태로 이어지는지”를 묻는 핵심 논리와 직접 연결된다.
- WGS에서 얻는 somatic mutation, CNV, structural alteration을 protein/phosphoprotein layer와 통합해 feature화하는 방법론적 기준점이 된다.
- pan-cancer/basket trial 관점에서 cancer type을 넘는 shared functional state를 찾는다는 점이 과제의 바구니형 표적-면역치료제 방향과 맞는다.
- predicted neoantigen burden과 measured T cell infiltration의 연결은 WGS 기반 neoantigen과 immune feature 통합에 참고할 수 있다.

## 주요 결과

- 1,064명, 7개 CPTAC tumor type의 proteomic/phosphoproteomic data를 통합했다.
- 15,699 quantified proteins와 110,274 quantified phosphosites를 활용해 driver event의 cis/trans effect를 분석했다.
- sequence-based kinase activity profile에서 여러 cancer gene이 유사한 molecular state로 수렴할 수 있음을 보였다.
- driver 중심 genomic 해석을 functional proteogenomic state 해석으로 확장했다.

## Slack 메시지 초안

Li et al. Cell 2023은 CPTAC pan-cancer 데이터를 이용해 암 driver 변이가 RNA/protein/phosphoprotein functional state로 어떻게 이어지는지 정리한 논문입니다. Cancer Multiomics 과제에서 WGS 변이, CNV, 구조변이를 단순 annotation에 그치지 않고 인산화단백체와 연결해 치료반응 feature로 만들 때 핵심 reference가 될 수 있습니다.
