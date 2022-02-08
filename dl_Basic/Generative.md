Generation : x ~ p(x)

Density estimation : 분류

Unsupervised representation learning : 이 이미지가 정형적인 모습이 무엇인지

#### Distribution
* 베르누이 : D={head,tail}, P(X=head)=p, P(X=tail)=1-p
* Categorical : D={1,2,,,m}, P(Y=i)=pi

#### 어떤 식으로 생각을 해봐야할까?
* RGB fullly discritption 하기위해서는 256 * 256 * 256 * n 개의 파라미터 필요
* binary pixel 표현할려면 2^n 필요
* 모든 변수들이 independent => n개의 파라미터로 2^n개 표현 가능

## Conditional Independence
![image](https://user-images.githubusercontent.com/63588046/152950957-c028336f-567c-4ef8-8d67-567b4151e12f.png)

#### Chain rule 생각해보면
* p(x1)-> 1 parameter
* p(x2|x1) -> 2 parameter (p(x2|x1)=0 & p(x2|x1)=1)
* P(x3|x1,x2) -> 4 parameter
=> 총 1 + 2^1 + 2^2 +,,,,,2^n-1 = 2^n -1 개의 parameter 필요

#### Conditional independence -> Markov assumption : X_i+1은 X_i한테만 independent, 나머지는 그렇지 않음
* p(x1)-> 1 parameter
* p(x2|x1) -> 2 parameter 
* P(x3|x1,x2) -> 2 parameter
=> 총 2n-1 개의 parameter 필요

#### Auto regressive Model
* 이전 데이터의 dependence 한게 존재하면 Auto regressive Model
* Conditional independence를 주는 것이 chain rule이 joint distribution을 쪼개는 것에 어떤 관련이 있을까?


#### Nade : Neural Autoregressive Density Estimator
* 처음 pixel이 어떤 것에도 의존하지 않음
* i 번째 모델은 i-1번째 모델에 의존한다.
![image](https://user-images.githubusercontent.com/63588046/152954162-0678c4f9-3875-4057-9735-ecd7b9cb29f6.png)
![image](https://user-images.githubusercontent.com/63588046/152954245-79ace965-913c-4765-8429-8816b979ad5f.png)

* 입력에 대한 확률을 구할 수 있다.(1번째 확률 분포를 암, 1번째 확률 분포가 주어졌을때 2번째 확률 분포를 암 ,,,,)


#### Pixel RNN
n * n RGB 이미지인 경우
![image](https://user-images.githubusercontent.com/63588046/152954725-9dfe85b0-e6cd-4288-a369-54546898ae91.png)

* 어떤 순서로 ordering하느냐에 따라 나뉨
  - Row LSTM
  - Diagonal BiLSTM
  ![image](https://user-images.githubusercontent.com/63588046/152955028-bc4967b6-3db3-4320-9856-126156c793d4.png)



## VAE
* Variational inference(VI) : posterior distribution과 비슷한 variational distribution을 찾는것
* Posterior distribution : p(z|x) : x가 주어졌을 때 내가 관심 있어하는 것에 확률 분포(likehood 반대)
* variational distribution : q(z|x) : Posterior distribution과 근사하는 확률분포로 KL 사용함

![image](https://user-images.githubusercontent.com/63588046/152956429-0d9f21b3-7a9c-416a-ae9d-60746952417c.png)

#### ELBO
* reconstruction term : auto-encoder를 통해서 생성되는 loss 최소화
* Prior Fitting term : 사전 분포와 latent 분포(encoder를 통해 압축된 정보)가 닮았다.

![image](https://user-images.githubusercontent.com/63588046/152958463-c4540860-2806-4527-93f6-ea15c3831413.png)

#### VAE 특징
* AE와 다르게 latent vector z를 sampling 함
* intractable model : likelihood 평가하기 어려움
* prior fitting term이 미분이 가능해야 한다.(다양한 분포 사용 못함... 가우시안을 자주 사용)
* isotropic Gaussian : 모든 output이 independent 한다.

isotropic Gaussian
![image](https://user-images.githubusercontent.com/63588046/152959866-931c7da8-238b-4638-a669-62e670eb0e07.png)

#### VAE 단점
미분 가능해야함... 가우시안이 아니면 하기 힘듬


## Adversarial Auto-encoder
Gan을 사용해서 latent에 분포를 맞춰준다. => latent 분포가 미분 가능하다

## GAN
![image](https://user-images.githubusercontent.com/63588046/152960995-e4bf9201-5620-4b30-ba21-280639ba0b95.png)

장점 : 학습 결과가 점점 좋아진다.

![image](https://user-images.githubusercontent.com/63588046/152960526-32781804-ff9a-4cc1-9c8f-405cb5a2f58b.png)

* 내가 실제로 가지고 있는 데이터와 내가 만든 데이터의 거리가 가깝다\
* optimal discrimitor

![image](https://user-images.githubusercontent.com/63588046/152963397-c2d94d61-3f41-48da-ae59-2b9262d2e3c8.png)

* optimal discrimitor가 만족한다고 가정하면

![image](https://user-images.githubusercontent.com/63588046/152961059-f6f35dd8-d83a-4abe-bcc7-da607743cf89.png)



#### DCGAN
* leaky Relu를 사용해라
* MLP보다는 deconv가 성능이 더 좋다

#### Info-GAN (CGAN)
* c라는 벡터(라벨)로 결과를 잡아줌
![image](https://user-images.githubusercontent.com/63588046/152961639-79fc6624-cae6-4cdd-8689-9aeeed936b7e.png)


#### Text2Image
* 문장을 이미지로 바꿔줌


#### Puzzle GAN
* 일부분의 이미지로 원본처럼 복원

#### CycleGAN
* 비지도로 알아서 찾음

#### StarGAN
* control 할 수 있게 답을 찾아줌

#### Progressive GAN
* 고차원 생성 모델을 만들어줌





