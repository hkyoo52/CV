<details><summary>행렬</summary>

![image](https://user-images.githubusercontent.com/63588046/149851781-065a0ca0-c514-4afb-b4e6-4f8d6412b95d.png)

![image](https://user-images.githubusercontent.com/63588046/149852171-8e835976-649c-4663-8ad1-71bab87114c7.png)

위 식을 사용하면 증명 가능 (기억하자!!)

</details> 


<details><summary>확률적 경사하강법</summary>

![image](https://user-images.githubusercontent.com/63588046/149854382-425bd18d-ed58-4aed-a523-e6523e73d483.png)

일부 데이터의 t+1번째 상태는 loss함수의 grad 값을 뺀다.  일부 데이터들의 grad의 평균은 전체 데이터의 grad와 거의 수렴한다.
데이터 중에서 한개 또는 일부 활용하여업데이트
여러개의 지점에서 경사하강법을 사용하므로 local minimum에 빠지지 않을 확률이 높음
^ : hat 으로 벡터라는 의미를 가짐
</details>

<details><summary> 활성함수 </summary>
  
![image](https://user-images.githubusercontent.com/63588046/149858244-1f353adb-8d10-450b-90d6-9b55aa988880.png)

비선형 함수로서 딥러닝을 비선형으로 만들어서 학습하게 만든다.
특히 relu가 가장 많이 사용된다.
</details>

<details><summary> 경사하강법 </summary>
  
  ![image](https://user-images.githubusercontent.com/63588046/149860872-f9017600-6151-4cd5-9de5-3ced3642df7e.png)
  
  chain rule을 사용해서 연속적으로 weight를 업데이트한다.
  
</details>


<details><summary> 확률론 </summary>
  
  * L2 노름 : 예측 오차의 **분산 최소화** 하는 방향으로 학습 유도
  * 교차 엔트로피 : 모델의 **불확실성 최소화**하는 방향으로 학습
  
  * 이산형 확률변수 : 확률변수가 가질 수 있는 **모든 경우의 수**  고려
  * 연속형 확률변수 : 데이터 공간에 정의된 확률변수의 밀도(density) 위에서 적분을 통해 모델링
  
  (**밀도**란 **누적확률분포의 변화율**을 모델링 하는 것)
  
  * 기댓값
  각각의 사건에 일어날 확률들을 곱한것을 다 합침
  
  ![image](https://user-images.githubusercontent.com/63588046/149862219-46ecaa22-01b0-4182-bc0e-e6d4e2b95f6a.png)
  
  => 분산, 첨도, 공분산에 이용 가능
  
  ![image](https://user-images.githubusercontent.com/63588046/149862329-257c1f5a-4f4b-471e-bef9-ea21f1b51f1a.png)
  
  (첨도 : 확률분포의 꼬리가 두꺼운 정도, 첨도=3이면 정규분포에 가깝다)

  * 몬테카를로 샘플링
  
  확률분포를 모를때 데이터를 이용하여 기댓값을 계산하는 방법 (샘플링 사용)
  
  이산형이든 연속적이든 상관 x
  
  반드시 **독립적**으로 샘플링 해야됨(대수의 법칙을 수렴성 보장)
  
  ![image](https://user-images.githubusercontent.com/63588046/149862846-534f8209-20c0-4ba0-a626-f99575da7274.png)
  
</details>


<details><summary> 통계학 </summary>
  
  * 통계적 모델링은 적절한 가정위에서 확률분포 추정
  * 유한한 개수의 데이터로 모집단 분포 정확히 파악 X -> 근사적 확률분포 추정
  * 모수적 방법론 : 데이터가 특정 확률분포 따른다고 가정한 후 그 분포를 결정하는 모수(parameter) 추정
  * 비모수적 방법론 : 특정 확률분포 가정 X, 모델의 구조 및 파라미터 개수 바꾸는 과정 
  
  * 확률 분포 예시
  
  베르누이분포 : 데이터가 2개의 값만 가짐(0 or 1)
  
  카테고리분포 : 데이터가 n개의 이산적 값 가짐
  
  베타분포 : 데이터가 [0,1]사이에서 값 가짐
  
  감마분포/로그정규분포 : 데이터가 양수 값만 가짐
  
  정규분포/라플라스분포 : 데이터가 R 전체 
  
  
  (파라미터 존재!!, 무한히 많거나 유연히 바뀜 )(일반적인 인공지능은 비모수)
  * 데이터 생성 원리 먼저 고려 -> 확률분포 가정
  * 표집 분포 : 표본 평균과 표본 분산과의 분포 != 표본 분포
  * 표집분포는 **샘플링에 평균** 으로 분포를 만듬
  
  ![image](https://user-images.githubusercontent.com/63588046/149907271-723bf15b-7e20-4e3f-9e6f-4dbc337bebbe.png)
  
  
  * 최대가능도 추정법 : 가장 가능성이 높은 모수 추정 방법 (데이터가 존재할 때 파라미터 찾는 것)
  
  ![image](https://user-images.githubusercontent.com/63588046/149910531-e161299a-1093-470b-bf47-40d8546df981.png)
  
  데이터가 독립적일때는 **로그 가능도**로 최적화
  
  (사용하는 이유 : 곱셈->덧셈으로 연산 가능(속도 굿, 최적화))
  
  로그가능도는 최대값을 찾으므로 음의 로그가능도를 가지고 최적화
  ![image](https://user-images.githubusercontent.com/63588046/149910697-a84fd93e-452b-459e-a538-413a17f70cfa.png)
  
 
  
  (표본분포는 정규분포가 될 수 없을수도 있지만 N이 커지면 표집분포는 정규분포가 된다.)

  * 정규분포에서 로그가능도 구하기
  
  ![image](https://user-images.githubusercontent.com/63588046/150072970-cdb2a477-686f-4661-945e-e43fc9eb83f5.png)
  
  => 최대 가능도로 바꾸려면 지수안에 넣어야함!!!!
  
  * 카테고리 분포에서 최대가능도 구하기
  카테고리 분포 Multinoulli(x; p1,p2,,,,pd) 단 모든 p들의 합은 1
  
  ![image](https://user-images.githubusercontent.com/63588046/150046876-391392f9-3b97-4550-bfb4-9c3e1f150f2f.png)
  
  * 라그랑주 승수법
  g(x, y)=k 인 조건에서 f(x, y)를 최대화할때 사용하는 방식
  g를 0으로 만들고 f와 g 의 grad 값이 동일하다고 가정하고 푼다.
  
  <pre><code> EX. 양수 x1,x2,,,xn의 합이 n일때 곱의 최대값은?</code></pre>
  
  ![image](https://user-images.githubusercontent.com/63588046/150055392-cba2c589-d39f-4fdd-9acb-c53b9b45248d.png)
 
  
  ![image](https://user-images.githubusercontent.com/63588046/150046972-235b1a3f-ce22-48bd-b21e-9fdc613397f2.png)
  
  ![image](https://user-images.githubusercontent.com/63588046/150047114-86934fbf-742e-4f32-a253-9d002b60e052.png)
  
  * 딥러닝 최대 가능도 추정
  분류문제에서는 softmax 벡터 (p1,,,pk) 모델링, 이때 y=(y1,,,yk)는 정답 레이블
  
  ![image](https://user-images.githubusercontent.com/63588046/150047658-03620076-4046-4c6b-94a6-8089a96da1cc.png)
  
  * 확률 분포의 거리 구하기 (확률 분포 P와 Q의 거리 구하기)
  1. 총변동 거리(TV)
  2. 쿨백-라이블러 발산 (KL)
  3. 바슈타인 거리 (Wasserstein Distance)
  4. IS, 
  * 총변동 거리(TV) : 두 확률 측도의 측정값이 벌어질 수 있는 값중 가장 큰 값(두 확률분포의 확률밀도함수가 겹치지 않으면 무조건 1)
  
  * KL
  분류 : **정답 레이블 P와 모델 예측 Q의 최대가능도 = KL 최소화**
  
  => 엔트로피 값은 상수임(p값은 고정되어 있으므로) 즉 KL 최소화는 크로스 엔트로피의 최소화를 의미함
  
  => 크로스 엔트로피 식은 로그가능도의 음수 붙이는 것과 동일
  
  => 크로스 엔트로피 최소화 = 로그 가능도 최대화
  
  ![image](https://user-images.githubusercontent.com/63588046/150049172-afecd54e-7ade-4bf5-b1ed-d78ff8781743.png)
  
  ![image](https://user-images.githubusercontent.com/63588046/150049207-9845a62b-8631-44db-a23c-c9ba64223dd6.png)
  
  </details> 
  
  
<details><summary> 베이즈 통계학 </summary>
  
  * 베이지안
  A 가 주어질때 B가 일어날 확률 -> B가 주어질때 A가 일어날 확률로 바꿈
  
  ![image](https://user-images.githubusercontent.com/63588046/150062503-6bf3d10b-d011-4a33-9dfa-10e4deaf0018.png)
  
  사전확률 : 데이터를 분석하기 전에 가설에 의해 생기는 확률
  
  Evidence : 데이터의 분포
  
  likelihood : 주어진 파라미터에서 D 분포가 관찰될 확률
  
  
   <pre><code> EX. Covid의 발병률이 10%로 알려져있다. 실제로 Covid에 걸렸을때 검진될 확률 99%, 실제로 걸리지 않았을 때 오검진 확률 1%
   어떤 사람이 질병에 걸렸다고 검진결과가 나왔을 때 정말로 Covid에 감염되었을 확률은?</code></pre>
  
  ![image](https://user-images.githubusercontent.com/63588046/150063434-fc1cdedb-d548-4579-888f-998a7b6dc14a.png)
  
  * 조건부 확률 시각화
  
  ![image](https://user-images.githubusercontent.com/63588046/150063748-9dfbdf91-9c83-4202-be34-7a33f77ee27b.png)
  
  * 조건부 확률로 인과관계 해석하면 안된다!!
  * **인과관계**를 가지고 예측 모형을 만들면 **강경한 모형**을 만들 수 있다.
  * 인과관계를 알아내기 위해서는 **중첩요인**을 제거하고 원인에 해당하는 변수만의 인간관계를 만들어야 한다. 
  
  (Ex. 키와 지능을 평가할때 나의!!의 요인 제거)
  
  
  </details>
  
  
  

<details><summary> CNN </summary>
  
  ![image](https://user-images.githubusercontent.com/63588046/150079904-c7bbd0a5-df84-4407-b6f0-dbac5c8f8be3.png)
  
  * convolution 연산 : 국수적으로 신호를 진폭, 감소
  * 정의역 내에서 계속 움직여도 커널은 변하지 않음
  * lacal하게 적용 (주어진 정보 증폭 or 감소)
  
  * Covn 장점
  1. parameter 축소 가능
  
  2. filter 수를 늘릴 수 있다(이미지는 주변 filter에 영향 많이 받아서 filter수 늘리는 것은 매우 좋음)=>공간감 생성
  
  
  Conv2d 연산 후 출력 크기
  
  ![image](https://user-images.githubusercontent.com/63588046/150099586-89b2da7d-a628-48e4-96d9-00336da973c6.png)
  
  * 연산할 때 채널의 개수만큼 커널의 개수 필요
  * convolution 연산은 역전파할때 convolution 연산이 나옴 (convolution 미분해도 convolution)
  
  ![image](https://user-images.githubusercontent.com/63588046/150099997-1b55ba48-1a0d-491b-b5ff-88c2fbaae56b.png)
  
  * convolution 연산 결과
  
  ![image](https://user-images.githubusercontent.com/63588046/150101528-64d93d64-2bdf-4f49-939d-a313198c7eb6.png)
  
  * 역전파 - 입력값 변화 (델타는 미분값)
  
  ![image](https://user-images.githubusercontent.com/63588046/150103238-501a9742-be2b-4890-8891-74a2c4af5188.png)
  
  * 역전파 - 커널값 변화
  
  ![image](https://user-images.githubusercontent.com/63588046/150102338-d06a8445-635b-470a-a13f-b7794dc0fc29.png)
  
  *최종
  
  ![image](https://user-images.githubusercontent.com/63588046/150102439-661deb03-8d35-499e-bfdc-a2d01704a0d8.png)

  </details>




<details><summary> RNN </summary>
  
  * 시퀀스 데이터
  소리, 문자열, 주가 등의 데이터 (과거 정보에 손실이나 순서가 바뀌면 X)
  
  * 시퀀스 데이터는 이전 정보를 가지고 앞으로 발생할 데이터의 확률분포를 다루기 때문에 조건부확률 사용
  * AR(Autoregressive Model) : 과거 모든 데이터 가지고 학습하는 것이 아니라 고정된 길이만큼의 시퀀스만 사용하는 경우
  
  ![image](https://user-images.githubusercontent.com/63588046/150106206-9f279b73-78ad-4f50-9aba-6a0c6b0f2c70.png)
  
  * 잠재 변수 : 바로 이전 정보를 제외한 나머지정보로 모델을 만든것
  
  ![image](https://user-images.githubusercontent.com/63588046/150106431-23f61dd8-f30a-4b84-8de8-7508b439425e.png)
  
  * RNN 모형
  
  ![image](https://user-images.githubusercontent.com/63588046/150106721-56383742-4838-43f6-ae6d-8c3e1c5e1745.png)
  
  * MLP와 유사한 모양, 이전 순서의 잡재변수와 현재 입력을 활용하여 모델링
  * RNN의 역전파는 잠재변수의 연결그래프에 따라 순차적으로 계산 
  * BPTT : RNN의 역전파 방법
  
  ![image](https://user-images.githubusercontent.com/63588046/150247378-b8defc53-1a9d-41e2-8c1c-697824ea9c22.png)
  
  * 미분값이 1 이상이거나 너무 작으면 학습이 불안정해짐
  
  ![image](https://user-images.githubusercontent.com/63588046/150297741-0b8b04fc-e876-48fc-89c0-3863d43cbea6.png)
  
  * 길이가 길어질수록 과거 정보에 대한 정보 소실이 커진다.
  
  => truncated BPTT : 모든 데이터 계산 X 길이를 끊고 계산
  
  </details>


L2 norm 표시 : ||y-XB||~2~

softmax(o) = (exp(o1)/시그마(exp(o_i),exp(o2)/시그마(exp(o_i),,,,)
softmax는 모델을 분류할 때 사용한다.


  
  
