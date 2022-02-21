#### EDA를 꼭 해야 한다!!!!!


## Preprocessing
* 80% 이상 비중을 차지함
* 잘 정제될수록 더 좋은 결과가 나옴
* bounding box
* resize

#### Data Feeding
* 먹이를 주다 : 대상의 상태를 고려해서 적정한 양을 준다. => 모델에 data를 주다.
* 모델이 처리할 수 있는 양을 알아야한다!!! -> 그에 맞게 데이터를 제공해야 한다. (효율성!!!)

![image](https://user-images.githubusercontent.com/63588046/154927485-828c4b6b-f2c2-4d2e-9e07-23e5b411155f.png)

**Dataset 생성 능력 비교**
```python
for i,data in enumerate(tqdm(dataset)):
         if i==300:
                  break
````
![image](https://user-images.githubusercontent.com/63588046/154928665-94395001-8591-4dd2-a246-89fbd94df61a.png)

* 동일한 transform을 어떤 순서로 했는지도 성능 차이가 크게 난다.

#### 예시
![image](https://user-images.githubusercontent.com/63588046/154896472-17839350-df0f-4528-8721-e471af2956f4.png)

* medical data는 전처리를 하면 더 좋은 결과가 나온다
* 밝게 이미지를 바꾸면 더 잘 되더라

## Generalization
* High Bias -> underfitting, High Variance -> Overfitting
* Train/Validation : 검증할 때 Test에 영향을 미치면 안됨!!
* Data Augmentation : 데이터가 가질 수 있는 Class, State의 다양성

         => 원본 데이터는 매우 잘 정제되있을 가능성이 있음, noise 등을 줘야 더 robust 하게 만들 수 있음

![image](https://user-images.githubusercontent.com/63588046/154897362-84dc87cc-0963-4962-abb8-350e53b3717c.png)


* 우리가 이미지를 뒤집어서 찍는 경우가 있을까?, 우리가 이미지가 짤릴 수 있는가? => 의미없는것은 안하기!!

* Albumentations : 좀 더 빠르고 좀더 다양하게 이미지를 변경해줌
* 여러가지 라이브러닌 도구일 뿐임!! (무조건 X) => 실험으로 증명해야 합니다!!


## Data를 Dataset으로 변경

![image](https://user-images.githubusercontent.com/63588046/154929054-60afe9ec-7bf1-49f8-8d5b-82f2b10e7d1d.png)

#### Dataset 구조
* 데이터를 원하는 형태로 출력해주는 클래스
```python
from torch.utils.data import Dataset        # Dataset 라이브러리 상속

class MyDataset(Dataset):                   # MyDataset 클래스 처음 선언
         def __init__(self):
                  pass
         
         def  __len__(self):                 # 아이템의 전체 길이     
                  return None         
                  
         def __getitem__(self,index):        # 데이터 중 index 위치의 아이템을 리턴
                  return index

```

#### DataLoader 구조
* Dataset을 더 효율적으로 사용하기 위함
```python
train_loader=torch.utils.data.DataLoader(train_set,
                           batch_size=batch_size,
                           num_workers=numworkers,
                           drop_last=True,
                           )                                   # 원하는 형식데로 데이터를 받아옴

```
**DataLoader 파라미터**
![image](https://user-images.githubusercontent.com/63588046/154930237-8ecbbe4a-c259-4ac4-96f0-9b713bd997f8.png)

**num_workers 최적 값 찾기**
![image](https://user-images.githubusercontent.com/63588046/154930432-452e6fbf-6096-4d28-8f91-997e537a0790.png)

**협업적인 일을 할 때는 Dataset과 DataLoader을 명확히 구분하는 것이 좋다**




