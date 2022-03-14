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




## Pix2pix

* GAN Loss 값에서 x(조건부)가 추가됨
* LcGAN만 사용하면 학습이 불안정함
* L1을 사용해서 실제 값과 생성모델이 비슷하게 만듬

![image](https://user-images.githubusercontent.com/63588046/158104001-a9835925-f7a7-4ae3-9a3e-13e5d4fa3bd7.png)







