## 글자 영역 검출
#### 특징
* 객체의 위치만 탐지 (class 고르지 X)
* 매우 높은 밀도
* 극단적인 종횡비
* 특이 모양 (구겨진 영역)
* 휘여진 영역
* 가로/세로 쓰기
* 모호한 객체 영역
* 글자 크기 편차

#### 글자 영역 표현
* 직사각형 + 각도
* 다각형 (좌표, 시계방향)


#### 글자 영역 탐지 기술
* Regression : 이미지를 입력 받아 글자 영역 표현값들을 바로 출력
  * anchor box를 통해서 x,y,w,h 값을 얻음
  * 직사각형으로 못받을 경우 성능 bad
  * anchor box보다 클 경우 성능 bad
* Segmentation : 이미지를 입력 받아 글자 영역 표현값들에 사용되는 화소 단위 정보 뽑고 후처리 통해서 글자영역 표현값 확보
  * 각 화소별로 글자 영역에 속할 확률 구함
  * 만약 속한다면 인접한 모든 화소가 글자영역일지 구함
  * 너무 오래걸림
  * 서로 간섭이 있을경우 bad
  * 인접한 객체간의 구분 bad
![image](https://user-images.githubusercontent.com/63588046/162712987-36f3b8eb-47fc-4677-85e9-40f416fc2a1e.png)


## 기본적인 모델
#### Character Based Methods
* CRAFT 
  * 글자 별로 어디 있는지
  * 글자 간에 연결되어 있는지
  * 단순히 두가지 정보를 겹쳐서 영역 확보

* EAST
  * 빠르고 성능도 좋음
  * ai로 화소단위 정보를 뽑음
  * 글자영역 중심에 해당하는지(score map) (글자->1, 배경 ->0)
  * 글자영역이라면 bounding box의 위치는 어디인지(geometry map) (rotated box, 직사각형 + 각도)

  * 모델 구조
   1. Feature Extractor stem (backbone) : feature 추출, VGG,ResNet 사용
   2. Feature merging branch : Unpool로 크기 맞추고 concat (1 * 1, 3 * 3 conv로 channel수 조정)
   3. Output : (H/4, W/4, C) map

   ![image](https://user-images.githubusercontent.com/63588046/162862700-5483eb6a-b8e5-4b5c-b4f4-c87e0a7993c6.png) 

  * NMS -> Locality-Aware NMS
   * 인접한 픽셀에서 예측되는 bounding box들은 같은 text instance -> 행 우선으로 탐색하면서 하나로 통합
   * 통합시 score map값으로 weight merge  

  * Loss 값
   * score map : cross entropy
   * RBOX loss : IOU loss + cosing loss
![image](https://user-images.githubusercontent.com/63588046/162863671-51eff2c7-04e9-42e1-ab1f-87eba796b753.png)

![image](https://user-images.githubusercontent.com/63588046/162863764-0c77da2c-41cc-45df-96a8-df43e00b563b.png)


#### Word Based Method

