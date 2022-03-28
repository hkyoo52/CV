## Efficientdet
* 어떻게 성능을 좋게 하면서 속도를 빠르게 할까?

#### 모델 쌓는 방법
(a) : 기본

(b) : 채널을 크게 만들기

(c) : 깊게 쌓기

(d) : 이미지 크기 늘리기

(e) : 모두 다 하기

![image](https://user-images.githubusercontent.com/63588046/160315817-13b315e4-f7f1-44d0-8a27-9b9151dc097a.png)


## EfficientNet
#### 등장 배경
* 파라미터 수가 점점 많아짐
* ConvNet이 커짐에 따라 점점 정확해지고 있지만 속도가 매우 느려짐

#### 수식
* 모델이 가장 정확할 수 있는 d,w,r을 찾아라
* d: 모델의 깊이
* w: 모델 채널 수
* r: 모델 해상도
* F_i: i번째 레이어

* 각 레이어를 합성곱을 한다.

![image](https://user-images.githubusercontent.com/63588046/160316465-a05ed7fe-df65-4dfd-82f5-c84a16119cdb.png)


![image](https://user-images.githubusercontent.com/63588046/160316520-3081d210-fa72-414f-9ea4-9828530df394.png)

* 아래 제약조건을 만듬
* B,r이 제곱인 이유는 채널수 늘릴때 파라미터가 더 많이 생김, 해상도는 양옆으로 제곱만큼 늘어남 

![image](https://user-images.githubusercontent.com/63588046/160317010-e9b1cfc3-f27a-4156-843c-3cc22544fcab.png)


![image](https://user-images.githubusercontent.com/63588046/160317515-ca566374-8482-4336-b27c-2878346e572c.png)


![image](https://user-images.githubusercontent.com/63588046/160317651-79e0bcd4-19eb-495f-adb8-bc4ff3d69c21.png)


## EfficientDet
* Neck에서 서로 다른 것을 단순합하는 것이 성능이 정말 좋을까? => 단순합 대신 가중합을 하자
* BiFPN의 경우 가중치의 합으로 가중치를 나눠줌
* 가중치들은 ReLU를 통과한 값으로 항상 0 이상
* 분모가 0이 되지 않도록 아주 작은 E를 더해줌

![image](https://user-images.githubusercontent.com/63588046/160318747-693962fc-bf63-48e6-997a-4974d4f5dac0.png)

#### Model Scaling
* 더 좋은 성능을 위해서 더 큰 backbone 모델 사용해 detector의 크기를 키움
* accuracy & efficient 모두 잡기 위해 EfficientNet과 같은 compound scaling 방식 제안

* EfficinetNet backbone 사용
* BiFPN network : 네트워크 width와 depth를 compound 개수에 따라 증가시킴
* Box/class prediction network : width는 고정, depth를 아래 식처럼 증가시킴

![image](https://user-images.githubusercontent.com/63588046/160319086-bbc94803-12ae-4806-82b6-abfce4efe066.png)


* image resolution

![image](https://user-images.githubusercontent.com/63588046/160319140-f3ebfa31-9d6f-43be-bf47-21436a2ce50b.png)





 
