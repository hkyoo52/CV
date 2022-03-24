## 2stage
* RCNN, SPPNet
  1) Localization(후보 영역 찾기)
  2) Classification(후보 영역에 대한 분류)
* 단점 : 매우 느리다

 ## 1stage
 * Localization과 Classification 동시 진행
 * 전체 이미지에 대해 특징 추출, 객체 검출 -> 간단하고 쉬운 디자인
 * 속도가 매우 빠름
 * 영역을 추출X, 전체 이미지 보기 -> 객체에 대한 맥략적 이해 높음 (Background error가 낮음)
 * YOLO, SSD, RetinaNet

## Yolo (You only look Once History)
#### Network
* GoogleNet 변형해서 사용
  * 24개의 convolution layer : 특징 추출
  * 2개의 fully connected layer : box의 좌표값 및 확률 계산

![image](https://user-images.githubusercontent.com/63588046/159830877-0457a4f9-b5a7-40b6-89e5-41eb969a179c.png)


#### Pipeline
* 입력 이미지를 S * S 그리드로 나누기(S=7)
* 각 그리드 영역마다 B개의 Bounding box와 Confidence score 계산 (B=2)
  * 신뢰도 = Pr(Object 확률) * IOU
* 각 그리드 영역마다 C개의 class에 대한 확률 계산(C=20)
  * conditional class probability = Pr(Class|Object)
* 각 그리드당 총 30차원
  * 5개는 x,y,w,h,c(confidence score) => 2개씩 있으므로 10개
  * 나머지 20개는 class 개수 (class일 확률)
  * confidence score * class 확률 -> 1 * 20 -> 한개의 그리드당 2개 * grid 수 = 98 * 20

![image](https://user-images.githubusercontent.com/63588046/159832435-7a2cd66c-7a2b-4932-8aba-2216a14d7933.png)


#### 장점
* Faster RCNN에 비해 6배 빠른 속도
* 다른 real-time detector에 비해 2배 높은 정확도
* 이미지 전체를 보기 때문에 클래스와 사진에 대한 맥락적 정보 가짐
* 물체의 일반화된 표현 학습
* 사용된 dataset외 새로운 이미지에도 성능이 좋음

#### 단점
* 7 * 7보다 작은 물체 검출 X
* 신경망을 통과하며 마지막 feature만 사용 -> 정확도 낮음


## SSD


