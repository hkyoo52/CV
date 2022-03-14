![image](https://user-images.githubusercontent.com/63588046/158090275-e2c32756-7230-402b-a454-376c00f8f8bb.png)


## Insatance segmentation
* 각 물체를 개별 분리 가능

![image](https://user-images.githubusercontent.com/63588046/158090356-6edda08b-f0a0-45de-a8c0-b29fa6721011.png)

#### Mask R-CNN
* RoIAlign 사용 : 소수점 단위로 pixel 뽑음
* Mask Branch 추가 : 80개에 마스크 뽑음, 각 마스크를 class와 비교
* Mask R-CNN = Faster-R-CNN + Mask Branch

![image](https://user-images.githubusercontent.com/63588046/158090469-c93fc82d-1e48-41ab-9488-9638e5acd9fb.png)


#### YOLACT (You Only Look At CoefficienTs)
* Protonet : 마스크를 생성할 수 있는 coefficience 관한 Prototypes 생성
* 각각 coefficience 더해서 NMS 출력값과 합성함


![image](https://user-images.githubusercontent.com/63588046/158090869-ee653fcd-ae58-452c-8b2a-22cebba9a08c.png)


## Panoptic segmentation
* 모든 물체를 다 분리함 (같은 class도 분리)

![image](https://user-images.githubusercontent.com/63588046/158091151-6c877040-42f8-4a19-a35c-3da3fb67f036.png)

#### UPSNet
* segmantic Head로 물체 semantic
* instance Head로 class, box, mask logit 생성
* Panoptic Head로 합침

![image](https://user-images.githubusercontent.com/63588046/158091271-63afb61e-4af4-4b53-91ea-5dada32cc3ec.png)

* mask 부분을 semantic head에 물체(thing)에 더해서 채널 만듬
* unknown(물체 부분에서 class 있는 부분 빼)를 채널에 추가
* 배경(stuff) 채널 추가

![image](https://user-images.githubusercontent.com/63588046/158091464-7f0a1e08-4b84-499a-9311-8dc6d52db912.png)


#### VPSNet
* 이전 feature에서 나온 값들과 현재 feature에서 나온 값을 합쳐서 사용
* track head를 통해 이전에 나온 ROI와 이번에 나온 ROI 매핑


![image](https://user-images.githubusercontent.com/63588046/158092604-37b3f2e1-048c-4068-8dca-2e2b0da183e7.png)



## Landmark Localization

#### Heatmap

* N개의 채널 생성
* 각 채널은 landmark가 될 확률이 높은 한 점을 구함

![image](https://user-images.githubusercontent.com/63588046/158093156-cb48a41b-52d9-430c-8ffe-cf547ec525f7.png)

* Landmark의 위치는 가우시안 분포에 있다고 가정한다.

![image](https://user-images.githubusercontent.com/63588046/158093218-4ea0df50-ad54-4f74-9c82-74a8e4a978c2.png)


```python
size=6*sigma+1
x=np.arrange(0,size,1,float)    # (size,1)
y=x[:,np.newaxis]               # (1, size)
x0=y0=size//2
if type == 'Gaussian':
  g = np.exp(-((x-x0)**2 + (y-y0)**2)/(2*sigma**2))       # 브로드캐스팅 : (size,1) + (1,size) = (size,size)
elif type == 'Caucy':
  g = sigma/(((x-x0)**2 + (y-y0) **2 + sigma**2) **1.5)
```

* 고민점 : 모델의 출력은 heatmap으로 나오는데 이것을 어떻게 좌표로 바꿀까?


#### Hourglass network

* 여러개 Unet으로 되어 있음
* skip할때 concat하는 것이 아니라 conv를 하고 더하는 구조
* 더하기 때문에 차원이 늘지 않음

![image](https://user-images.githubusercontent.com/63588046/158094149-db89c009-620c-4843-a3a2-44b5a419e877.png)



#### DensePose
* 신체 모든 부분 landmark -> 3D surface 얻음
* UV map은 고정된 점으로 각각 id 존재, 움직여도 그 부분에 id가 있으므로 tracking하기 편함
* id는 text로 표현하지 않고 색으로 표현함(메모리 절약)





