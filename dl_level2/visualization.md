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
