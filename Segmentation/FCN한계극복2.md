## 기존 FCN과 DialtedNet, DeepLab
* FCN은 32배만큼 줄이고 32배 늘림
* DialtedNet, DeepLab은 8배 줄이고 8배 늘림


## DeepLab v2
* AvgPool 없어짐
* ASTP : 4개로 나눠진 후 합침
* backbone을 resnet101로 바꿈
* conv4, conv5에서 down sampling을 수행하지 않고 dilated conv 사용
![image](https://user-images.githubusercontent.com/63588046/165229322-0b1962f8-025d-4cf0-85b9-6e0d9bd142a0.png)


#### resnet에서 차원이 다른거 어떻게 더할까?
* 1 * 1 conv 사용

![image](https://user-images.githubusercontent.com/63588046/165229827-47972e5a-a58c-4ce8-ba1a-57fe52841d78.png)



## PSPNet
#### 이전 방식에 문제점
* 외관이 비슷하면 잘못 맞춤 Ex. 자동차와 배를 햇갈림, 고층건물하고 그냥 건물 분별X
* 붙어있을때 분별 X 경향 있음 Ex. 침대, 베게 구별 X

#### FCN도 maxpool 사용해서 넓은 범위의 receptive field를 가지고 학습하는데 왜 성능이 안좋을까?
* 실제 receptive field VS 이론적 receptive field   -> 이게 차이가 남

#### Global Average Pooling
![image](https://user-images.githubusercontent.com/63588046/165239151-66563124-e245-4b5e-85fc-d7568e72fe7f.png)

#### Convolution VS Average Pooling
* Conv는 특징 추출
* Avg Pooling은 대표값 추출

![image](https://user-images.githubusercontent.com/63588046/165239562-3e6e2b03-b5d0-4404-8051-0cdb00879f01.png)


#### PSPNet
* 다양한 Conv 진행하여 channel이 1인 feature map 생성
* 크기가 다르기 때문에 Upsampling 진행
* 나온 feature map Concat 함

![image](https://user-images.githubusercontent.com/63588046/165239742-3cd4e89d-db30-440f-b06b-b3cc01247b99.png)



## DeepLab v3
* global average pooling 사용
* sum 하기 보다는 concat 사용

![image](https://user-images.githubusercontent.com/63588046/165429067-164cf06b-581e-4368-9df1-4d5f0952efff.png)


## DeepLab v3+
* Encoder Decoder 사용 -> spatial dimension의 축소로 인해 손실된 정보를 Decoder에서 점진적 복원
* skip connectoin을 이용

#### Encoder
* 수정된 Xception을 backbone으로 사용
* low level feature를 다양한 conv 사용한 후 concat함
* 그것을 1 * 1 conv 사용해서 1개 채널로 만들어서 decoder에 제공

![image](https://user-images.githubusercontent.com/63588046/165430617-b8cdc48a-e6bc-48c8-82e3-caae83eff78c.png)

#### Decoder
* low level feature와 Encoder output을 크기와 차원을 맞추서 concat
* conv, upsampling을 해서 예측
![image](https://user-images.githubusercontent.com/63588046/165430776-18288b64-2efa-4765-a58a-aaebc03a093b.png)

#### Depthwise Separable Convolution
* Depthwise Convolution : 각 채널마다 다른 filter를 사용하여 convolution 연산 후 결합
![image](https://user-images.githubusercontent.com/63588046/165431334-a198dea2-1776-47ca-8b64-601419eee2f5.png)

* Pointwise Convolution : 1 * 1 conv
* Depthwise Separable Convolution = Depthwise Convolution + Pointwise Convolution
![image](https://user-images.githubusercontent.com/63588046/165431582-d2940018-c5f7-436b-8df6-94835d72fb6a.png)

#### 다른 변경점
* MaxPoolint -> Depthwise Separble Convolution + BatchNorm + Relu
* 크기를 줄이면서 어느 부분이 중요한지, 어떻게 추출해야 정보 손실이 적은지 구함

![image](https://user-images.githubusercontent.com/63588046/165431894-6a7eb4a5-cd3a-480f-ab40-92dfe32278bb.png)

![image](https://user-images.githubusercontent.com/63588046/165431974-c2bb5be1-945f-4f18-8518-787c437d4a38.png)

* 동일한 층 반복 횟수를 8 -> 16
* 더 깊게 학습을 진행

![image](https://user-images.githubusercontent.com/63588046/165432116-ed2a2a2f-7b4f-4051-971a-59be0f58e911.png)

![image](https://user-images.githubusercontent.com/63588046/165432173-38941524-7ae0-493f-b0a8-7cd757848d4e.png)







