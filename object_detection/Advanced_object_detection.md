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





