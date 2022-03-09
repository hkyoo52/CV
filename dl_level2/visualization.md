## CNN 문제점
* hidden layer를 볼 수가 없다.
* 언제 실패를 하는지 알기 어렵다
* 왜 perfromance가 좋은지 알 수 없다.

#### visualize network
* 모델의 특성 분석
* 어째서 그런 결론을 내었는지 분석

![image](https://user-images.githubusercontent.com/63588046/157356308-ec4a33f2-7e1e-4d91-ab28-f1407abae32b.png)


## Embedding feature analysis (High level feature 분석)
* fc layer 이전에 feture들을 가지고 분석

![image](https://user-images.githubusercontent.com/63588046/157357073-c98e9231-8ff2-4308-80ba-744f0fbeb40f.png)


#### Nearest neighbors
* 질의 데이터와 NN으로 유사한 이미지 모음
* 비슷하게 생긴것 모을 수 있음
* 위치변화에 강인함 (픽셀별 비교를 하지 않음)

![image](https://user-images.githubusercontent.com/63588046/157357267-7b165bbc-d715-44c8-aded-5b3e41c2ec06.png)




#### Dimensionality reduction
* 고차원 -> 3차원
* 대표적을 t-SNE 

![image](https://user-images.githubusercontent.com/63588046/157357597-592d2a60-3581-42f0-abc1-b6e1419c1939.png)



## Activation investigation
* hidden node 분석

#### Layer activation
* 해석하기 용이하게 해줌

![image](https://user-images.githubusercontent.com/63588046/157358634-59918ec2-d383-48b6-af46-b1a7dc42b6c4.png)

#### Maximually activating patch
* channel 중에 가장 큰 값을 가진 patch와 그 주변에 감ㅅ을 찾음
* 선을 찾는다, 원을 찾는다, 등등 찾을 수 있음
* 국부적인 것을 
방식!!!

* 특정 레이어 선택
* 예제 데이터를 넣어서 backbone activation 값을 뽑아서 저장
* 가장 큰 값을 가진 patch 고름 & 이전 layer의 receptive field 얻음

![image](https://user-images.githubusercontent.com/63588046/157358853-b019c5ef-6811-4c0c-92e3-f3b09d8f4161.png)


#### Class visualization
* 네트워크가 어떤 클래스를 상상


![image](https://user-images.githubusercontent.com/63588046/157380479-5ed66170-3791-4e83-9f33-816bc662fb20.png)

위 사진에서 분석할 점
  * 해당 물체만 찾는 것이 아니라 주변에 있는 것도 찾음

![image](https://user-images.githubusercontent.com/63588046/157381642-89f73fce-53e7-465a-acac-5cba361d9cb5.png)

* 2개의 loss를 합쳐서 사용
* I : 영상 이미지 (0~255 or 0~1)
* f : CNN을 통해서 나오는 값
* argmax(f(I)) : pred 값
* reg term : 값이 너무 커지는 것을 막게 해줌

* 과정
  * pred score 얻음
  * backward를 진행해서 maximizing target class score에 해당하는 w.r.t만 input image에 이미지에 넣음
  * 위 과정 반복함
* pred값을 높이는 방향
* 초기값을 어떻게 설정하는가에 따라 값이 달라짐

![image](https://user-images.githubusercontent.com/63588046/157381864-a65c76e8-8f5b-4a29-ab42-6542e3206641.png)

## Saliency test
#### Occlusion map
* 각 patch를 가리고 예측정도를 측정해서 어떤 부분이 중요한지 파악

![image](https://user-images.githubusercontent.com/63588046/157382380-08ec07e3-4e2f-40b6-a44d-b7c079524340.png)

#### via Backpropagation
* 관심 영역을 빛나게 만듬
* 과정
  * class score 얻음
  * backpropogete -> visualiz gradient magnitude map


![image](https://user-images.githubusercontent.com/63588046/157382743-fb03ba9a-b43b-419e-a633-0229eda67069.png)


* relu로 학습할 때 일반적으로는 backward 할때는 forward에서 바뀐 값의 위치를 기억해서 그 위치를 0으로 바꾸는데 여기서는 그때그때마다 음수인 곳을 0으로 바꿔준다

![image](https://user-images.githubusercontent.com/63588046/157393316-e09160d8-e698-43cc-894a-ac757dedbcc7.png)



#### Class Activatoin Mapping (CAM)
* 가장 많이 사용되는 방식
* 어떤 부분을 참고했는지 heatmap으로 표현
* 마지막을 Global average poolling(GAP) 추가한 후 fc layer 1개 지나게 함

![image](https://user-images.githubusercontent.com/63588046/157396160-2ded730c-09cb-4def-b13a-7cc6c931284c.png)

* c : class
* S : class 점수
* F : fc layer 나온 값
* w : fc layer 나올 때 곱해지는 가중치
* Gap feature : 마지막 layer 값들
* k : channel 번호
* f : GAP 하기 전 각각의 채널의 픽셀 값

![image](https://user-images.githubusercontent.com/63588046/157396194-6a09fc2c-2a6f-4081-9dcb-4051ffa57dd1.png)


![image](https://user-images.githubusercontent.com/63588046/157396257-2c8f349d-3fcc-4e6a-a73d-54c5640be20a.png)



#### Grad-CAM
* 아키텍처 구조가 다른 것에도 다 사용 가능
* backbone이 CNN이기만 하면 다 사용 가능

![image](https://user-images.githubusercontent.com/63588046/157399042-e9db99f0-c83e-44c6-a7ff-36d71ba1e915.png)



## 질문
* CAM에서 나온 결과랑 원래 이미지랑 이미지 크기 차이가 날 것 같은데
* 

