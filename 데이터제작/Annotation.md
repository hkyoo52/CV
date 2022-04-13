## 가이드라인
* 좋은 데이터를 확보하기 위한 과정을 정리해 놓은 문서
* 데이터가 골고루 모임 (Raw Data)
* 일정하게 라벨링된 데이터 (Ground Truth)

#### 가이드 라인 3가지 요소
* 특이 케이스
* 단순함 - 너무 내용이 많으면 작업자가 다 숙지 못함
* 명확함 

#### 데이터셋 제작 파이프라인
* 서비스 요구사항 -> 제작 목적 설정 -> 가이드라인 제작 -> Raw image 수집 -> annotation(라벨링)

![image](https://user-images.githubusercontent.com/63588046/163085765-66a5cf13-5a31-43e9-a6ef-328f4e9ee029.png)



## 가이드 라인 제작 과정
* 받은 데이터 검수
  * 라벨링 검수
  * 데이터 검수

![image](https://user-images.githubusercontent.com/63588046/163085891-caab4ea9-0f3a-4a81-a087-a1e4bfee3f16.png)

#### 기본적인 용어 정의

![image](https://user-images.githubusercontent.com/63588046/163086068-2b5a9ba3-1f20-4d42-a82f-665782f14c00.png)

#### Annotation 규칙
* 이미지 내에 글자 영역 존재X 이미지
* 이미지의 모든 글자 영역 속 글자 알아보기 어려운 경우
* 같은 글자, 패턴이 5회 이상 반복되는 이미지
* 영어, 한국어가 아닌 외국어가 1/3 이상인 이미지


