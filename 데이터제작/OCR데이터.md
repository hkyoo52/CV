## 생성 데이터
* 합성 이미지
* 실제 이미지
  * 크롤링된 데이터 -> 검증 필요
  * 외주 데이터

![image](https://user-images.githubusercontent.com/63588046/162865209-792a1c84-1de5-49c7-82d8-f4a281c85aba.png) 

![image](https://user-images.githubusercontent.com/63588046/162865253-a965e577-e51a-4da6-90b6-5a84fe0101e4.png)


## 데이터 모을 때 가져야 할 질문들
* 몇 장을 학습시키면 어느정도 성능이 나오는가
* 어떤 경우가 일반적이고 어떤경우가 희귀 케이스인가
* 현재 최신 모델의 한계는 무엇인가

## 데이터 모으는 방법
1. 대회(Kaggle, RRC)
2. OCR 데이터셋 논문 (arxiv, cvpr, iccv, aaai, icdar)
3. 구글 Datasearch
4. Zenodo.org
5. Datatang (유료)

## 데이터셋 특징
* 언어
* 용도
  - 검출기
  - 인식기
  - End to End
 * 데이터 수량
 * 라이센스
 * 데이터 저장 포맷
 * 특이사항

## OCR 용어
* Bounding Box
* text
* don't care
* File name
* Image width
* Image height



## UFO
* json, txt, xml, csv 하나로 통합
* 서로 다른 모듈에서 모두 쉽게 사용할 수 있음
* 모델 개선을 위해 필요한 case에 대한 정보를 데이터에 포함 시킬 수 있음
* 모든 데이터가 병렬로 되어있음 
  - 문장단위, 단어단위, 글자단위 다 따로 되어 있어서 바로 불러올 수 있음

* ids : paragraph, image, character 레벨 각각에서 모두 id 넘버를 매김 (순서 의미X)
* points : 각 레벨의 위치 좌표, 글자를 읽는 방향의 왼쪽 위에서부터 시계방향으로 x,y 좌표를 nested list 형태로 기록
  * 4points의 bbox가 기본적, 2n개의 points로 이루어진 polygon도 가능
  * [[x1,y1],[x2,y2],[x3,y3],[x4,y4]]
* language: 사용된 언어 Ex. "en", "ko", "others",,,
* tag : 성능에 영향을 주지만 별도로 기록하기 애매한 요소 (수직 방향이냐 수평방향이나 초점이 맞는가 등등)
* confidence : ocr 모델이 예측한 pseudo-label의 경우 confidence score를 함께 표시



# EDA 할때
* 이미지 당 단어 개수 분포
* image width, height 분포
* 전체 BBOX 크기 분포
  * 넓이 기준
* 태그 개수(histogram)
  * 언어
  * orientation
  * word tag
  * image tag
* Horizontal에 대한 aspect ratio(가로/세로) 




