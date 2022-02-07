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
* Regression : MSE 
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

#### Gradient Descent
$$x+y=3\\-x+3y=2$$



