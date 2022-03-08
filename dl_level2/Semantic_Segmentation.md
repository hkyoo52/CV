## Semantic Segmentaion
* 같은 클래스는 같은 색으로 분류

![image](https://user-images.githubusercontent.com/63588046/157149949-a85e98d6-dd7d-4108-bcd2-323b29c8bc26.png)


## FCN
* 입력부터 출력까지 미분 가능한 형태로 되어있어서 target을 구함
* input과 output의 사이즈 동일 -> 크기 문제 호환성 X
* fully connected layer를 fully convolution layer (1 * 1)로 바꿔서 만듬

![image](https://user-images.githubusercontent.com/63588046/157151053-1242b692-865f-43ce-8106-8c802633b755.png)

* fully connected layer는 한 filter를 쭉 핀다 -> filter 개수만큼 fully connected layer가 나온다
* fully convolution layer는 같은 위치에 있는 모든 pixel에 적용한다 -> 1 * 1 convolution 개수만큼 나온다

#### FCN - Upsampling
* 이미지로 복원하는 과정
* Transposed와 Upsample 2개 존재

#### Transposed convolution
![image](https://user-images.githubusercontent.com/63588046/157152730-8149f0fd-a0de-44b2-aa85-13abdfb265e4.png)

* 근데 중첩되는 부분을 그냥 더해도 되는건가???
* 섞이면 안되는 부분에 섞이는 부분이 발생한다!!

#### Upsample & convolution
* Upsample : 1개의 픽셀을 여러개로 만듬 -> 해상도가 안좋음
* convolution : 학습을 시킴



#### FCN layer별 특징
* 낮은 layer : 국지적, detail, 작은 차이에도 민감함
* 높은 layer : 해상도는 낮음, 전반적인 의미를 가짐

=> Semantic Segmentaion에서는 이게 어떤 물체인지도 알아야하고(전반적인 의미) 경계가 어디인지도 알아야함(국지적)

=> 각 layer마다 Upsampling을 진행함

![image](https://user-images.githubusercontent.com/63588046/157153756-e77587fe-352b-4733-a9e3-46e5bf3ec639.png)

![image](https://user-images.githubusercontent.com/63588046/157153797-f13bdd9f-656d-4d14-b2c1-bd406d495c9c.png)


## Hypercolumns for object segmentation
* 여러 층에서 upsampling을 해서 해상도를 맞춰서 합쳐서 사용
* bounding box를 출력 후 사용

![image](https://user-images.githubusercontent.com/63588046/157154180-d921990d-f304-48d2-8ba7-29dc32a4cf1b.png)


## U-Net
* fully convolutional network 
* FCN에 skip connection (concat 사용해서 과거 정보를 그대로 사용)

![image](https://user-images.githubusercontent.com/63588046/157155632-72da294f-2e03-45ce-87f1-d36e01aa6136.png)

#### Unet 주의할점
* downsampling : 7 * 7-> 3 * 3
* upsampling : 3 * 3-> 6 * 6
* 해상도 차이가 안맞음
* 그래서 홀수 크기가 안나오도록 주의해야함!!


```python
def double_conv(in_channels, out_channels):
  return nn.Sequential(
    nn.Conv2d(in_channels, out_channels, 3),
    nn.ReLU(inplace = True),
    nn.Conv2d(out_channels, out_channels, 3),
    nn.ReLU(inplace = True))
   
   
def double_conv(in_channels, out_channels):
  return nn.Sequential(
    nn.Conv2d(in_channels, out_channels, kernel_size=2,stride=2),     # kernel_size=2, stride=2이면 겹치는 부분 안생김
    nn.LeakyReLU(0.1,inplace = True),
    nn.Conv2d(out_channels, out_channels, kernel_size=2,stride=2),
    nn.LeakyReLU(0.1, inplace = True))
    
```

## DeepLab
#### Conditional Random Field 
* 정답과 비교할것이 없기 때문에 처음에는 성능 bad 학습을 하다보면 경계에 tight하게 만들어줌
![image](https://user-images.githubusercontent.com/63588046/157156858-acf8cd32-eb5a-4bba-85e1-f42749a024f8.png)

#### Dilated convolution 
* 한칸씩 띄어서 convolution 진행
* 동일한 파라미터 개수
* 넓은 지역을 볼 수 있음

![image](https://user-images.githubusercontent.com/63588046/157158143-9bbf554e-39bc-4b9f-aec8-4bee9f4eecd6.png)

#### Depthwise separable convolution
* 각 채널별로 1개의 크기로 만듬
* 모든 채널을 합침
* 계산량 감소 (파라미터 엄청 적어짐)

![image](https://user-images.githubusercontent.com/63588046/157158428-10eb9190-f109-4647-80b5-695a759d08dc.png)


![image](https://user-images.githubusercontent.com/63588046/157158526-690d1bc0-a0ae-49ad-98a8-8b2a9cdf1315.png)






