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


