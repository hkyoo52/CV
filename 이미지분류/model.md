모델 : 시스템을 표현 -> 어떻게 모델(파라미터)을 업데이트 할지를 고민

#### 파이토치의 장점
* 자유로움 (매우 low level로 되어있음)
* 연구하기 편리함

#### nn.Module
* 파이썬의 모든 모듈은 nn.Module을 상속받는다.
* Module은 파라미터를 저장해놓는다.
* 상속하므로써 파라미터를 업데이트하고 저장 가능
* init에서 모델을 불러오고 저장 가능
* forward는 input과 ouput 사이의 chain
* 

```python
import torch.nn as nn
import torch.nn.functional as F

class MyModel(nn.Module):
  def __init__(self):
    super(MyModel,self).__init__()
    self.conv1=nn.Conv2d(1,20,5)
    self.conv2.nn.Conv2d(20,20,5)
  def forward(self,x):
    x=F.relu(self.conv1(x))
    return F.relu(self.conv2(x))
```

![image](https://user-images.githubusercontent.com/63588046/154984468-4eb312b6-e46e-426a-bc8e-2a54f52f3916.png)
![image](https://user-images.githubusercontent.com/63588046/154984626-318afdb1-dced-4111-aba4-b4a80ee7aca4.png)

=> module에 어떤 함수가 있고 어떤 파라미터가 잇는지 알 수 있음

=> 어떤 grad를 가지고 있는지 알 수 있음 (required_grad가 false로 되어있으며 학습X)

#### pythonic 하다는 것에 장점
* 형식과 구조를 알고 있다면 응용가능
* class를 특별히 만들지 않아도 구조를 알 수 있다.
* 모델의 weight만 안다면 바로 모델을 적용하고 업데이트 가능하다.
* 에러들도 핸들링 할 수 있다.
![image](https://user-images.githubusercontent.com/63588046/154985913-712c3021-a4e6-4817-b6ce-5620970872e7.png)


## Pretrained Model
* transfer learning = 좋은 품질, 대용량 데이터로 미리 학습한 모델 -> 내 목적에 맞게 변형하여 사용
* Pretrained 모델은 많고 Pretrained weight를 다운받을 수 있다.

#### 주의점
* ImageNet은 실생활에 존재하는 이미지를 1000개로 분류
* 내 목적과 비슷한지 파악해야 한다!!!!

#### Case 1. 학습 데이터가 충분하다
![image](https://user-images.githubusercontent.com/63588046/155051570-ece79a8b-306f-4bf7-a2ed-2e3064b54bf3.png)
* **주제가 비슷** => **feature extraction** :Backbone은 학습안해도 된다!!(마지막 분류만 학습하면 됨)
* **주제가 다름** => **finetuning** : Backbone부터 학습한다.(완전히 무에서 시작하는것보다 ImageNet Pretrained weight를 가지고 학습하는 것이 훨씬 빠르다)

#### Case 2. 학습 데이터가 부족하다

* **주제가 비슷** => classifier만 하는거 추천
* **주제가 다름** => 다른 모델을 만들어서 다르게 해보자
