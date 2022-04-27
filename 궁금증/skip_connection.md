## 왜 skip connection이 더 학습을 잘 될까?
#### 가설 1 skip connection으로 층을 감소시킴
* skip connection을 통해 지나가면 몇개 layer를 지나지 않고 다음 layer로 이동
* layer 수의 감소 -> gradient vanishing/exploding 감소 가능성 높음

=> 문제점... 근데 gradient 문제는 initialization 문제일지도?


#### 가설 2 앙상블 역활을 한다.
* VGG같은 경우 layer들간에 종속적인 관계가 크다.
* 그래서 하나의 layer를 삭제하면 성능이 확 떨어진다.
* resnet은 skip connection을 하나 삭제하거나 다른 layer를 하나 삭제한다고 성능에 차이가 거의 없다.
* skip connection되는 부분과 아닌 layer간의 종속적인 관계가 적다.
* 서로 앙상블 되어있을 가능성이 크다.

#### 가설 3 이전 정보를 가지고 와서 잘못 가중치 업데이트되는 것을 완화시킨다.
