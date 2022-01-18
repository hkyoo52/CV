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

비선형 함수로서 딥러닝을 비선형으로 만들어서 학습하게 만든다.</details>

<details><summary> 경사하강법 </summary>
  


L2 norm 표시 : ||y-XB||~2~

softmax(o) = (exp(o1)/시그마(exp(o_i),exp(o2)/시그마(exp(o_i),,,,)
softmax는 모델을 분류할 때 사용한다.

