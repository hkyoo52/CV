## Neck
과거 방식은 마지막 feature map을 사용했음
* 왜 마지막 feature map을 사용해야할까?

![image](https://user-images.githubusercontent.com/63588046/159216626-b5ec4058-55d9-478f-9e20-c46b8f3d959d.png)

* 현재는 중간중간의 feature map 사용 => neck

![image](https://user-images.githubusercontent.com/63588046/159216684-d912ff97-3b0a-46c6-960e-b0b31ef70734.png)


## 왜 neck을 사용할까?
* 마지막 feature map만 사용할경우 작은 객체는 탐지하기 매우 어려움
* neck을 사용해서 다양한 사이즈를 잘 탐지함


#### Feature Pyramid Network(FPN)
* Low level : 원래 이미지에 가까운 feature
* High level : 많이 학습한 이미지
* FPN : high level에서 low level로 semantic 정보 전달 -> **lateral connection** 사용

![image](https://user-images.githubusercontent.com/63588046/159422909-16d909c8-f877-418d-8566-d14f0dd1b7ad.png)

#### Lateral connections
* high level 정보와 low level 정보를 적절히 섞는 방법
* low level은 1 * 1 conv를 사용해서 차원수 늘림
* high level은 upsampling 사용해서 크기를 늘림
* 두개를 더함

```python
# build laterals
laterals=[lateral_conv(inputs[i]) for i, lateral_conv in enumerate(self.lateral_convs)]

for i in range(3,0,-1):
  prev_shape=laterals[i-1].shape[2:]
  laterals[i-1]+=F.interpolate(laterals[i],size=prev_shape)
  
outs=[self.fpn_convs[i](laterals[i]) for i in range(4)]



```


#### Pipeline
* FPN을 통해서 나온 것을 conv 진행
* 1 * 1 conv -> 분류
* 3 * 3 conv -> box regression
* 위의 것으로 1000개의 box선택
* 나온 ROI가 어느 stage(P5,P4,P3,P2 stage 존재)에서 왔는지 구하는 법 : k를 통해서 얻음

![image](https://user-images.githubusercontent.com/63588046/159424329-3e653968-68f5-49fd-8080-72917c1da1ca.png)




## Path Aggregation Network(PANet)

#### FPN 단점

