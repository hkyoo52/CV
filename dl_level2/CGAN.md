##  Conditional generative model
* 조건이 주어졌을 때 특정 확률이 나옴 
* 기존에 생성 모델은 단지 random으로 생성만함
* Conditional 생성 모델은 내가 원하는데로 생성함

![image](https://user-images.githubusercontent.com/63588046/158096894-77e4e447-888d-4815-a90e-bdc97a13609c.png)


#### Super resolution
* 저해상도 -> 고해상도
* cgan을 사용 안할경우 mae, mse는 모든것을 다 섞인 이미지가 발생(모든 이미지 중간을 생성하고자 함)

![image](https://user-images.githubusercontent.com/63588046/158097029-f24df6e0-fb78-46e2-b34b-b9d47b1edb00.png)


* CGAN은 discriminator가 있어서 그러한 중간값의 이미지 생성 X 




#### Pix2pix (CGAN)

* GAN Loss 값에서 x(조건부)가 추가됨
* LcGAN만 사용하면 학습이 불안정함
* L1을 사용해서 실제 값과 생성모델이 비슷하게 만듬

![image](https://user-images.githubusercontent.com/63588046/158104001-a9835925-f7a7-4ae3-9a3e-13e5d4fa3bd7.png)



#### CycleGan

* GAN loss : L(DX)+L(DY)+L(G)+L(F)
* 문제점 : 모든 생성값이 동일한 것 생성할 수 있음
* content 유지하기 위해 Cycle consistency loss 추가
* 비지도학습


#### CGAN 특징
* 성능이 좋음
* 학습이 잘 안되는 경우가 많음


## Gan loss and Perceptual loss
* GAN loss : Generator & Discriminator 균형 중요 -> 학습이 매우 어려움
* pre-trained 필요 X -> 매우 다양하게 사용 가능
* Perceptual loss : 매우 간단하게 학습 가능
* pre-trained network 필요


#### Perceptual Loss
* Image Transform Net에서 한개의 style 결정
* Loss Network에 넣어서 각각의 layer에 feature을 얻음
* Loss Network에서 얻은 각각의 loss로 backward해서 Image Transform Net 학습(Loss Network는 학습X)

![image](https://user-images.githubusercontent.com/63588046/158105987-28030bd8-f017-4cdb-a75f-f6a88e28bc8e.png)

* 원하는 style을 넣음 (변환하고 싶은 style) (horse2zebra이면 zebra 사진)
* Style target, Transformed Target을 Loss Network에 넣어서 나온 feature map을 gram metric으로 loss 구함
* gram matric : 위치 정보를 사용하지 않고 feature map의 확률값을 구함
* gram matric은 동일한 스타일을 같이 발생할 확률을 구해서 matric을 만드는 방법이다.


* Content Target에는 일반적으로 input값 X를 넣음 그래서 동시에 Loss Network에 넣어서 나온 feature map이 일치하도록 loss 값을 구함
* 이때 loss는 L2 loss 사용한다.

![image](https://user-images.githubusercontent.com/63588046/158106226-9fb485b3-1e98-4032-b490-8025a3d3a22d.png)







## 심화 과제
#### Gram matric
* (C,H,W) -> (C, H * W) 로 변경
* 각 채널마다 내적 => (C, H * W) * (C, H * W)T = (C, C) 
* 각 채널마다 어떤 무늬를 띄는지 가지고 있음
* 내적해서 큰 값을 가진다 => 동시에 두 무늬를 가진다

=> correlation 정보를 담음

![image](https://user-images.githubusercontent.com/63588046/158533238-d89abd9b-0069-4789-be19-c693e9302670.png)

* F : filter
* i,j : i,j번째 filter
* k : channel
* l : layer


![image](https://user-images.githubusercontent.com/63588046/158537341-90a5fdca-8560-4ce0-aec9-57d03413abbe.png)








