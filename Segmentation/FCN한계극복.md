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




