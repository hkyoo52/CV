## 이전 모델과 bottleneck

* CNN에서는 3 * 3 conv를 사용해서 지역적인 것을 전체적으로 보게 만들려고 함
* 근데 계산량이 너무 많아서 bottleneck을 사용

![image](https://user-images.githubusercontent.com/63588046/164141119-ea986300-e936-4bf9-93bc-a3b3169b00c1.png)

* 차원을 줄이고 계산을 하면 계산량은 줄지만 정보 손실이 발생함
* 속도와 계산량은 trade-off이므로 적절한 합의점 찾아야함

![image](https://user-images.githubusercontent.com/63588046/164141286-07f5ce3a-b2e9-43b3-97f1-4f412e453c85.png)


![image](https://user-images.githubusercontent.com/63588046/164141428-db0af6fd-14ef-4fdd-a5b9-47f0f953f150.png)
