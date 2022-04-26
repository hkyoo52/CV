## FCN 한계점
* 객체 크기가 크거나 작은 경우 예측 잘 못함
* transfer conv가 너무 간단 -> 경계에 대해 학습이 어려움

## DeconvNet
* Encoder와 Decoder를 대칭으로 만듬
* Decoder는 Unpooling과 Deconvolution을 반복함
* Unpooling이 외곽의 모습을 찾아감
* Deconvolution이 안에 내용을 찾아감

![image](https://user-images.githubusercontent.com/63588046/165057596-8d41a6eb-f7ec-4f5a-a9cc-c310ce212019.png)

#### Unpooling VS Deconvolution
* 위치 정보를 정확히 알 수 X
* Unpooling은 위치정보를 기억했다가 복원하는 과정
* Unpooling은 노이즈를 제거하지만 정보 손실되는 문제점이 있음


```python
# Convolution Network
def CBR(in_channels,out_channels,kernel_size=3,stride=1,padding=1):
  return nn.Sequential(nn.Conv2d(in_channels=in_channels,out_channels=out_channels,kernel_size=kernel_size,stride=stride,padding=padding),
            nn.BatchNorm2d(out_channels),
            nn.ReLU())

# Deconvolution Network
def DCB(in_channels,out_channels,kernel_size=3,stride=1,padding=1):
  return nn.Sequential(nn.Conv2d(in_channels=in_channels,out_channels=out_channels,kernel_size=kernel_size,stride=stride,padding=padding),
            nn.BatchNorm2d(out_channels),
            nn.ReLU())

# pooling할때 위치정보 찾는 법
## conv1
self.conv1_1=CBR(3,64,3,1,1)
self.conv1_2=CBR(64,64,3,1,1)
self.pool1=nn.MaxPool2d(kernel_size=2,stride=2,ceil_mode=True,return_indices=True)   # retrun_indices=True 여서 위치 정보를 저장해놈

## unpool5
self.unpool5=nn.MaxUnpool2d(2,stride=2)
self.deconv5_1=DCB(512,512,3,1,1)
self.deconv5_2=DCB(512,512,3,1,1)
self.deconv5_3=DCB(512,512,3,1,1)

## output scores
self.score_fr = nn.Conv2d(64,num_classes,1,1,0,1)

# forwrd 부분
def forward(x):
  h=self.conv1_1(x)
  h=self.conv1_2(x)
  h.pool1_indices=self.pool1(h)   # 반드시 이것을 사용하고
  ~
  ~
  h=self.conv5_1(x)
  h=self.conv5_2(x)
  h.pool5_indices=self.pool5(h)   # 반드시 이것을 사용하고
  ~
  ~
  h=self.unpool5(h,pool5_indices)  # 여기에 넣는다
  h=self.deconv5_1(h)
  h=self.deconv5_2(h)
  h=self.deconv5_3(h)
  ~~~

  output = self.score_fr(h)
  return output
```


## SegNet
* 빠른 속도로 Semantic Segmentation을 수행하기 위해 모델이 필요한 능력 고민
* DeconvNet에 중앙 부분 제외 - 파라미터 수 감소
* UnPooling 학습X (DeconvNet과 공통점)
* Deconv 대신에 Conv 사용
* score 생성시 3 * 3 conv 사용


![image](https://user-images.githubusercontent.com/63588046/165115038-17d1d5b8-f341-4295-ba18-397ff1a777f1.png)

![image](https://user-images.githubusercontent.com/63588046/165115818-102462f7-eb30-4920-8c19-61b92ddc4d7c.png)


```python
# Convolution Network
def CBR(in_channels,out_channels,kernel_size=3,stride=1,padding=1):
  return nn.Sequential(nn.Conv2d(in_channels=in_channels,out_channels=out_channels,kernel_size=kernel_size,stride=stride,padding=padding),
            nn.BatchNorm2d(out_channels),
            nn.ReLU())

# Deconvolution Network
def DCB(in_channels,out_channels,kernel_size=3,stride=1,padding=1):
  return nn.Sequential(nn.Conv2d(in_channels=in_channels,out_channels=out_channels,kernel_size=kernel_size,stride=stride,padding=padding),
            nn.BatchNorm2d(out_channels),
            nn.ReLU())

# pooling할때 위치정보 찾는 법
## conv1
self.conv1_1=CBR(3,64,3,1,1)
self.conv1_2=CBR(64,64,3,1,1)
self.pool1=nn.MaxPool2d(kernel_size=2,stride=2,ceil_mode=True,return_indices=True)   # retrun_indices=True 여서 위치 정보를 저장해놈

## unpool5
self.unpool5=nn.MaxUnpool2d(2,stride=2)
self.dcbr5_1=CBR(512,512,3,1,1)
self.dcbr5_2=CBR(512,512,3,1,1)
self.dcbr5_3=CBR(512,512,3,1,1)

## output scores
self.score_fr = nn.Conv2d(64,num_classes,3,1,1,1)

# forwrd 부분
def forward(x):
  h=self.conv1_1(x)
  h=self.conv1_2(x)
  h.pool1_indices=self.pool1(h)   # 반드시 이것을 사용하고
  ~
  ~
  h=self.conv5_1(x)
  h=self.conv5_2(x)
  h.pool5_indices=self.pool5(h)   # 반드시 이것을 사용하고
  ~
  ~
  h=self.unpool5(h,pool5_indices)  # 여기에 넣는다
  h=self.dcbr5_1(h)
  h=self.dcbr5_2(h)
  h=self.dcbr5_3(h)
  ~~~

  output = self.score_fr(h)
  return output
```


## Skip Connection을 적용한 모델
## Skip Connection
* input과 output 더함
* 이전 layer의 정보를 줌 -> layer간에 gradient가 흐르는 것을 더 쉽게 만듬
* 깊은 layer에 대해서도 성능을 더 높게 만듬

![image](https://user-images.githubusercontent.com/63588046/165116037-fcea40cd-a2e7-4158-89bf-a7424f8204fe.png)


#### FC DenseNet
* 정보 전달 할때 일부 layer를 건너 뛴 후의 layer에게 입력으로 제공
![image](https://user-images.githubusercontent.com/63588046/165138449-c761dfb0-5638-44c2-832d-d8c528f38071.png)


#### UNET
![image](https://user-images.githubusercontent.com/63588046/165138627-a18df7f4-82cb-428d-bd42-2d5b549a83f3.png)


# Receptive Field 확장시킨 모델
## DeepLab v1
* receptive가 작다면 큰 객체에대해 탐지 X
* 아래 그림처럼 버스 유리창에 자전거가 비췄을때 자전거라고 예측할 확률 높음
![image](https://user-images.githubusercontent.com/63588046/165139031-ca0ea105-e1d2-4e5b-8041-7c7cef58c398.png)

* conv만 사용하기 보다는 중간에 max pooling을 사용하면 메모리도 아끼면서 효과적으로 receptive를 넓힐 수 있음 (파라미터 효과적으로 줄임)
* 근데 이미지의 크기가 많이 줄어든 상태에서 upsample을 하면 정보량이 너무 많이 손실된다.


![image](https://user-images.githubusercontent.com/63588046/165139405-b56325cf-de81-45c2-ba4e-99ff7f5f3965.png)

=> 의문점 이미지의 크기는 많이 줄이지 않고 파라미터 수도 적은 상태로 receptive field만 넓게 하는 방식은 없을까?

#### Dilated Convolution

![image](https://user-images.githubusercontent.com/63588046/165140049-b57a3381-e311-4a20-9e61-f0c3ab1fbe08.png)

![image](https://user-images.githubusercontent.com/63588046/165140210-60d81fde-28fc-4342-b21e-93d58d2927d3.png)

![image](https://user-images.githubusercontent.com/63588046/165140398-6f7e0286-4e10-4a7b-8239-45dbf24aefff.png)

![image](https://user-images.githubusercontent.com/63588046/165140576-8fb3d2e2-df6b-490a-b8fd-a3e8aa8c77b5.png)

![image](https://user-images.githubusercontent.com/63588046/165208690-97c3b566-28dd-41f5-b9f2-192901c07bf0.png)


* conv5에서는 maxpool이랑 avgpool 같이 사용

#### Dense CRF
* CRF를 통해서 이미지 경계를 더 정밀하게 만듬
* 유사한 색이 가까이 있으면 같은 범주로 보게 만듬
![image](https://user-images.githubusercontent.com/63588046/165210810-ac213797-85dd-4f2e-aa4e-38fa7b6e8d88.png)


```pytorch
def conv_relu(in_ch,out_ch,size=3,rate=1):
    conv_relu=nn.Sequential(nn.Conv2d(in_channels=in_ch,out_channels=out_ch,kernel_size=3,stride=1,padding=rate,dilation=rate),
                nn.Relu())
    return conv_relu
    
    
class VGG16(nn.Module):
    def __init__(self):
        super(VGG16,self).__init__()
        self.feature1 = nn.Sequetial((conv_relu(3,64,3,1),
                                      conv_relu(64,64,3,1),
                                      nn.Maxpool2d(3,stride=2,padding=1))     # 2 * 2 maxpool -> 3 * 3 maxpool
   

# FC6 ~ score
class DeepLabV1(nn.Module):
    def __init__(self, backbone, classifier, upsampling=8):
        super(DeepLabV1, self).__init__()
        self.backbone = backbone
        self.classifier = classifier
        self.upsampling = upsampling

    def forward(self, x):
        x = self.backbone(x)
        _, _, feature_map_h, feature_map_w = x.size()
        x = self.classifier(x)
        out = F.interpolate(x, size=(feature_map_h * self.upsampling, feature_map_w * self.upsampling), mode="bilinear")   # 이걸 사용해서 중간에 있는 값들을 채워줌!!!
        return out
# Upsampling
from 

```

#### DilatedNet
* DeepLab을 더 효율적으로 사용
* dilated와 padding을 같이 사용해서 이미지의 크기를 유지함
![image](https://user-images.githubusercontent.com/63588046/165211122-7b344206-1ef3-49b2-ab76-95aa1e7490ef.png)


