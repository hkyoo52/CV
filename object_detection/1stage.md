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
* Extra convolution layer에서 나온 모든 feature map 사용(6개)
* fully connected layer 사용 X (convolution layer 사용) => 속도 향상
* default box (anchor box) 사용

![image](https://user-images.githubusercontent.com/63588046/159856359-c5da7994-0778-4547-8f06-c1ee330692b3.png)


#### Pipeline
* (x, y, w, h) 4개 + class 개수 20개 + background 1개
* box 개수, 위치 구할때 -> scale 0.2 ~ 0.9 6개
* anchor box : 1/3 ~ 3 5개

![image](https://user-images.githubusercontent.com/63588046/159857558-693e87e0-bacf-4752-b89e-f507bbc7603b.png)

* 6개의 feature map에서 나온 총 bounding box 개수는 8732개

![image](https://user-images.githubusercontent.com/63588046/159858439-ca313dc4-f492-45ab-b9d1-7dad2987ab57.png)


#### Training 방법
* Hard negative mining
* Non maximum suppression

![image](https://user-images.githubusercontent.com/63588046/159858617-10d32c75-2a31-451b-be6d-046f8c25ef2d.png)



## YOLO v2
* Batch normalization 사용 -> mAP 2% 증가
* 이미지 해상도 증가 -> mAP 4% 증가
* fully connected layer 제거
* anchor box 적용 -> 5개
* Fine-grained feature 사용
* multi scale training : 다양한 입력 이미지 사용
* Googlenet -> Darknet (속도 증가)
* Imagenet 데이터는 classification loss만 학습, detection 데이터는 classification & bbox loss 학습

#### Fine-grained feature
* 크기가 작은 feature map은 low level 정보 부족
* Early feature map은 low level 정보 함축
* Early feature map을 late feature map에 합쳐주는 passthrough layer 도입
* 26 * 26 feature map 분할 후 결합

![image](https://user-images.githubusercontent.com/63588046/159859336-0e16040b-b565-4ca2-b068-dbcf70d5284c.png)



## YOLO v3
* skip connection 사용
* Max pooling, conv2d 사용 => resnet과 비슷
* Multi-scale feature maps 사용


#### Multi-scale feature map
* 서로 다른 3개 scale 사용
* feature pyramid network 사용

## RetinaNet

#### 1stage 단점
* 1 stage detector는 ROI가 없음 -> grid를 기준으로 만듬...
* class imbalance -> positive > negative(객체가 없는 배경 영역)


#### Focal Loss
* 쉬운 예제는 낮은 가중치, 어려운 예제는 큰 가중치
* 결과적으로 어려운 예제 집중
* class imbalance가 심한 dataset에도 매우 효과적임

