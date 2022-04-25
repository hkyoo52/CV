## FCN (Fully Convolutional Network for segmentation)
* VGG 네트워크 backbone 사용 -> pretrained weight 사용 가능!!
* VGG 네트워크의 FC layer(nn.Linear)를 Convolution으로 대체
* Transposed Convolution 이용해서 이용해서 Pixel Wise prediction 수행

#### Fully connected layer VS Convolution layer
* Fully connected layer는 마지막에 flatten을 해서 위치 정보를 없앰(위치 관심X, object가 뭔지만 궁금)
* Convolution layer는 위치정보를 해치지 않으면서 정보를 얻음

![image](https://user-images.githubusercontent.com/63588046/165026909-fc9f5e61-f961-42ef-bc1f-b6fff6863941.png)

* nn.Conv는 height, width와 상관이 없기 때문에 크기에 영향을 덜받는다.

#### Transposed Convolution = Upsampling = Deconvolution
![image](https://user-images.githubusercontent.com/63588046/165029759-13155d76-0cda-4f3c-8f6a-43cba9d095cd.png)

![image](https://user-images.githubusercontent.com/63588046/165029915-2f6b9c01-fb7b-4140-897c-5e6d55ab10df.png)

#### FCN 성능 향상 방법
* downsampling에서 32배 줄임 -> upsampling에서 32배 증가시켜야함
* 한번에 증가시키면 정보 손실이 너무 커서 천천히 증가시켜야함

=> skip connection 사용!!

![image](https://user-images.githubusercontent.com/63588046/165031656-2b70be36-18a4-435a-971e-baf2fb5d8e82.png)

#### Skip connection
* 이전에 pooling해서 나온 값들을 upsampling에서 더함

![image](https://user-images.githubusercontent.com/63588046/165032136-d9094407-7025-4d97-938c-a6a3523e4c62.png)


#### 평가지표
* Pixel accuracy

![image](https://user-images.githubusercontent.com/63588046/165032357-9f4e2189-ca54-4396-968f-fe290500303e.png)

* MIOU (Mean IOU)

![image](https://user-images.githubusercontent.com/63588046/165032547-87c3b1fb-3fee-417e-8451-06dc4ec752a5.png)


## 이미지마다 크기, 차원이 다른 것을 어떻게 사용
* pooling, crop -> 이미지 크기 통일
* 왜 1 * 1 conv -> 차원 크기 맞춤




