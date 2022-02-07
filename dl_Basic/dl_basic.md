<details><summary> 딥러닝 기본 구조 </summary>
  
#### Data
문제를 어떻게 해결할건지에 따라 데이터가 달라짐

#### Model
내가 알고 싶어하는 것으로 바꿔주는 것
AlexNet, GoogleNet 등등 존재

#### Loss
원하는 것을 성취하기 위한 proxy
Ex. MSE, CE, MLE

#### Optimizzation Algorithm
실제 환경에서 잘 작동하도록 사용하는 테크닉
</details>

<details><summary> 딥러닝 기본  </summary>

### Linear Regression
$$
y=x+b
$$

### Deep NN
![image](https://user-images.githubusercontent.com/63588046/152712592-4444895b-3ce6-405c-80a4-1e6c92224fc6.png)

왜 딥러닝이 잘되?
* 인간의 뇌를 본따서
* layer의 개수가 1개여도 충분히 설명 가능 하지만 여러 층이여야 더 빠르게 설명할 수 있다.

#### loss function
* Regression : MSE (Loss를 제곱해서 많이 틀리는 곳을 더 많이 집중하게 만들어줌) 
* Classification : CE => y값이 원핫 인코딩으로 되어있음, 그래서 원하는 값만 더 커지게 하고 싶음
* Probability : MLE => 출력값이 단지 숫자가 아니라 확률적인 것을 알고 싶을때


#### Gradient Descent
편미분 사용해서 minimum 값을 찾으러 감

#### Generalization
* 일반화 성질을 높임
![image](https://user-images.githubusercontent.com/63588046/152716728-da631c0b-eb5f-4d5f-94cc-5ec6e6702e76.png)

#### Cross-validation (=K-Fold)
* 학습데이터와 테스트 데이터를 나눠서 학습
* k개로 나눠서 그중 1개를 validation으로 사용
* Test 데이터는 절대 학습때 사용하지 않는다.

#### Bias & Variance
![image](https://user-images.githubusercontent.com/63588046/152716983-010bbd1e-80db-4d2d-ba65-04d1ac583a58.png)

* 일반적으로 loss에는 bias^2, variance, noise 모두 존재
* Bias와 Variance 둘 다 줄이는 것은 어렵다.

![image](https://user-images.githubusercontent.com/63588046/152717519-3ec7af5f-08e3-430d-a33d-e99aaabe3eea.png)

#### Bootstrapping
학습데이터를 여러개로 만들어서 각 데이터당 다른 모델을 사용해서 학습을 한다.
* Bagging(=앙상블) : 나온 output 값을 평균내서 결과를 구한다.
* Boosting : 모델을 sequence하게 만듬. 처음 모델을 만들고 그 다음 모델을 첫 모델에서 학습을 잘 못하는 것을 학습 잘하도록 만듬

#### Gradient Descent Method
* Stochastic gradient Descent : 1개의 sample로 gradient update
* Mini-batch gradient Descent : 여러개의 sample로 gradient update
* Batch gradient Descent : 데이터 전체로로 gradient update

#### Batch-size의 중요성
* Large batch-size=>sharp minimizer
* small batch-size=>flat minimizer
![image](https://user-images.githubusercontent.com/63588046/152718136-dfe1d73e-0064-40db-bfd4-4f4c3cc0402c.png)
sharp할 경우 약간의 차이로 인하여 결과값이 많이 차이남 => small batch가 일반적으로 더 좋은 성능을 보인다.

</details>
  
#### Gradient Descent
![image](https://user-images.githubusercontent.com/63588046/152719316-5785eea4-407a-40da-ae6d-546940cd5bab.png)
* 적절한 learning rate 구하는게 너무 어려움

#### Momentum
![image](https://user-images.githubusercontent.com/63588046/152719460-24c13f7d-6be2-4466-ba84-46ca570137f1.png)
* 이전에 갔던 gradient를 가지고 다음번에 사용
* 이전의 정보를 사용하므로 훨씬더 많은 데이터를 볼 수 있음

#### Nesterov Accelerated Gradient
![image](https://user-images.githubusercontent.com/63588046/152719746-0729c46e-ed6d-48fd-b903-8b7e29daf2e2.png)
* 현재 정보를 가지고 이동을 한 다음에 그 정보를 가지고 gradient를 계산해서 accumerate를 함
* momentum이 local minimum을 잘 못들어가는 것에 비해 NAG는 잘 들어간다.
    
#### Adagrad
![image](https://user-images.githubusercontent.com/63588046/152719874-786d31b1-beba-4efa-919a-741008646a5a.png)

* 각각의 파라미터가 얼마나 변했는지 파악하고 많이 변할수록 조금 학습시킴
* G 값이 계속 커지기때문에 학습 할수록 학습이 안됨

#### Adadelta
![image](https://user-images.githubusercontent.com/63588046/152726941-2418ecce-abc5-454a-9835-f1c29955fbd8.png)

* G가 계속 커지는 것을 방지

#### RMSprop
![image](https://user-images.githubusercontent.com/63588046/152727007-b26623e8-2517-48d1-8757-4ac318eb3687.png)

#### Adam
![image](https://user-images.githubusercontent.com/63588046/152727110-d09c06eb-70d3-4007-8284-3d00692a552b.png)

* moment + Adapt learning(적게 학습한 파라미터는 많이 학습)
* EMA 정보를 계속 가지고 있음
* 성능이 보통 제일 좋음
* Adam이 매우 빠르게 학습한다.

## Regularization
#### Early stopping
* validation error가 올라갈려고 할때 학습을 멈춤

#### Parameter Norm Penalty
![image](https://user-images.githubusercontent.com/63588046/152727388-4aa2e877-b0ac-4ccf-8f2b-3ff8d835559c.png)

* 파라미터 값을 최대한 작게 만듬 -> 함수가 부드러워짐
* 일반 가정 : 함수가 부드러울수록 일반화가 잘 된다.

#### Data Augmentation
* 데이터가 한정적이기 때문에 가지고 있는 데이터를 가지고 변화를 줌(돌리고 크기를 키우는 것 등)

#### Noise Robustness
* 입력 데이터 혹은 weight에 noise를 줌
* test에서 더 좋은 결과를 보여줌

#### Label Smoothing - 노력대비 성능이 많이 높아짐
* 입력값과 label을 섞어줌 => 함수가 부드러워짐

#### Dropout
* 노드를 몇개 없앰

#### Batch Normalization
* 적용하려고한 레이어를 정규화시킴
* 레이어가 깊어질수록 성능이 좋아진다.

