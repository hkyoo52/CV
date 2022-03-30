## Faster RCNN 학습
* backbone 학습(conv)
* region proposal 학습
* head 학습

#### 아키텍처
* 처음 H0에서 ROI 구함 -> C0은 배경인지 아닌지, B0은 객체에 위치
* H1에서 어떤 객체인지랑 box의 위치 고름 -> C1은 어떤 객체인지, B1은 box 위치


## Cascade 

* iou에 임계값에 따라 성능이 많이 달라짐
![image](https://user-images.githubusercontent.com/63588046/160325905-434b94a9-6013-4b5f-9284-38527f4d6eb1.png)

* 아래 그래프는 head network를 통과했을때 IOU가 어떻게 변하는지에 관한 것이다.
* ![image](https://user-images.githubusercontent.com/63588046/160326131-cfdb1e6a-6c37-4a09-8eca-2452794977c1.png)


* IOU를 높이는 것은 성능이 좋아지지 않음
* quality가 높이려면 IOU를 높여야함
![image](https://user-images.githubusercontent.com/63588046/160328751-18b62f4e-51bf-4457-abc1-dccadeb8a472.png)

#### Cascade
* IOU를 높이면서 성능도 높임
* Iteractiv BBox : head에서 구한 box를 가지고 지속적으로 계산하는 방식(성능 bad)

![image](https://user-images.githubusercontent.com/63588046/160329298-3d98bf1b-5b10-4f64-8e27-4e96a6dd5e40.png)

* 여러개의 head를 구해서 학습을 해볼까? => integral 방식
* IOU threshold를 여러개를 두고 학습을 했음(앙상블처럼) => 성능 변화 거의 없음
![image](https://user-images.githubusercontent.com/63588046/160329857-9fd5f706-52f7-4e13-a0ab-ba6afe6c1ee9.png)

* interactive + integral = **Cascade**
* 성능이 꽤 좋았다. 특히 IOU가 높을때 매우 좋은 성능 향상을 보였다.



## Deformable Convolutional Network
* 이전 방식들은 고정된 filter로 학습 -> 동일한 물체도 geometric transform 하면 다른 물체라고 인식함
* 이전에는 물체 회전 등등 transform을 함으로써 해결했음

#### Deformable convolution
* offset을 진행해서 convolutin 연산을 진행(계산하는 위치를 다양하게 바꿈)

![image](https://user-images.githubusercontent.com/63588046/160339071-b38b5ab6-7467-47d3-a357-aa6f8bbfb0c5.png)

* 아래는 convolution 게산, deformable convolution은 R이 다양한 위치에 존재
![image](https://user-images.githubusercontent.com/63588046/160339502-76540e06-fab0-4659-806e-a468c3269d50.png)



## Transformer -> Swin 
#### VIT
* patch로 나눠서 각 patch당 flatten 시킴

![image](https://user-images.githubusercontent.com/63588046/160342381-a5d1afe2-a47d-40d2-b739-7db8f69b5cbb.png)

* 나온 값을 embedding 시켜줌

![image](https://user-images.githubusercontent.com/63588046/160342447-d5189882-6a1c-42f6-ba05-a25006614e47.png)

* 임의의 class embedding 추가, position enbedding 추가

![image](https://user-images.githubusercontent.com/63588046/160342585-abec0dda-7054-4c9f-ad2b-5af86d3051a6.png)

* transformer encoder 진행해서 예측

![image](https://user-images.githubusercontent.com/63588046/160342776-c8c21765-baa8-4545-9190-d5914ebd0bfb.png)

#### VIT 문제점
* 굉장히 많은 data를 가지고 학습해야함
* transformer 특성상 계산량이 많음
* 일반적은 backbone 사용 X

## DETR
* 연산량이 너무 많아서 가장 높은 feature만 사용
* FFN에서는 N개의 output이 나오는데 이때 N은 이미지가 가지고 있는 object보다 많아야함
*
#### train
* 무조건 N개가 나올 것임
* no object는 padding 처리해야함
* 가장 높은 level feature만 사용해서 작은 물체는 탐지를 잘 못한다.


## Swin Transformer

#### VIT 문제점
* VIT에 너무 많은 양의 Data를 학습해야 성능나옴
* transformer 특성상 계산량이 많음
* 일반적인 backbone 사용 못함

#### 해결법
* CNN과 유사한 구조로 설계 (지속적으로 크기 줄임)
![image](https://user-images.githubusercontent.com/63588046/160366682-8dd8dd7f-6b51-4c89-97fe-5062be72f19b.png)

* Window라는 계념을 활용하여 cost 줄임(Multi-Head Attention 대신에 사용)
* attention을 2번 진행

![image](https://user-images.githubusercontent.com/63588046/160367033-2bee4a65-1b67-4efd-a3ff-3bb0734efa25.png)


#### Multi-Head Attention (W-MSA)
* window 단위로embedding 나눔
* 기존 VIT는 embedding을 transformer에 넣지만 Swin은 Window 안에서 transformer 연산 진행
* 그러나 window안에서만 수행해서 receptive field를 제한하는 단점이 존재한다.

![image](https://user-images.githubusercontent.com/63588046/160367354-4cd4a3a3-0ecd-4a4e-ad6a-7f3a11cfc7b2.png)

#### Shifted Window Multi-Head Attention
* 다르게 나눠서 transformer 진행
* 남는 부분들은 옆 혹은 아래로 이동
* 크기가 다른 경우 masking 처리해서 self-attention 연산이 되지 않도록 함

![image](https://user-images.githubusercontent.com/63588046/160367685-ff51e025-eed4-4b8a-8887-648fbafa0a26.png)

#### 장점
* 적은 데이터로도 학습 잘됨
* Window 사용해서 계산량 적음
* 다양한 backbone 사용 가능 (CNN과 비슷한 구조)





#### Bag of Freebies (BOF)
* 입력 이미지의 변화시켜 과접합을 막고, 다양한 환경에서도 강력해지는 방법 
  * Data augmentation
  * Semantic Distribution Bias : 데이터셋에 특정 라벨이 많은 경우 사용
  * Label smoothing : 0과 1로 라벨링하는 것이 아니라 0.1, 0.9 로 바꿈, overfitting, regularization 효과가 있음
![image](https://user-images.githubusercontent.com/63588046/160376688-085dfbcf-6ee6-4c53-8810-9eab17617e49.png)


## IOU 기반 loss
* Bounding box 좌표값들을 예측하는 방법은 거리가 일정하더라도 iou가 다를 수 있음
* iou 기반 loss 사용

#### GIOU
* 기본적인 iou는 box 사이가 떨어지면 무조건 0임(거리 반영 못함)

## Bag of Specials
* cost는 발생하지만 성능을 높일 수 있는 도구
#### Enhancement of Receptive field
#### Attention Module
* attention을 사용해서 원하는 것에 집중

![image](https://user-images.githubusercontent.com/63588046/160795819-35b759a5-2a2c-444a-8e1b-6f94ee076b02.png)


#### Feature Integration

#### Activation Function
* Relu를 사용하면 음수값이 될 경우 훈련 X
* Swis/Mish : 약간의 음수를 허용 -> 모든 구간 미분 가능

#### Post-processing method

## Yolo v4
* BOF : inference 비용을 늘리지 않고 정확도 향상시키는 방법
* BOS : inference 비용을 늘리지만 정확도를 크게 향상시키는 방법

![image](https://user-images.githubusercontent.com/63588046/160376585-5d1eb385-2f14-4f7f-8b5a-a1e3c7c5c5c6.png)

* CSPNet 사용 

## M2Det



## CornerNet




