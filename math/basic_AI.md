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


L2 norm 표시 : ||y-XB||~2~

softmax(o) = (exp(o1)/시그마(exp(o_i),exp(o2)/시그마(exp(o_i),,,,)
softmax는 모델을 분류할 때 사용한다.
