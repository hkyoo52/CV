## Dataset 구조
```python
class MyDataset(Dataset):
   def __init__(self):
        mydata = 데이터 로딩하기
        super(MyDataset,self).__init__()

        self.X=~~
        self.y=~~
        
        # 만약 데이터를 불러올때 라벨링 하고 싶으면
        self.data['A']=self.data['불러올 column'].map({'S':0,'C':1,'Q':2}) # 이런식으로 라벨링
        
        ~~~
    def __len__(self):
        return len(self.X)
   
    def __getitem__(self, idx):
        X=self.X[idx]       #데이터 프레임이면 X=self.X[idx]
        y=self.y[idx]       #데이터 프레임이면 y=self.y[idx]
        X=torch.tensor(X,dtype=torch.float32)
        return X, y

```

### collate_fn
* 하나의 데이터의 라벨이 여러개일 수도 있음 (detection 분야같은 경우)
* 데이터 사이즈를 맞춰서 batch 단위로 바꿀 수 있게 만들기 위해서 사용한다.

**이 코드는 외우자!!**
```python
def my_collate_fn(samples):
    collate_X = []
    collate_y = []
    
    for sample in samples:
        diff = max(sample['X'],key=len)-len(sample['X'])
        if diff > 0:
            zero_pad = torch.zeros(size=(diff,))
            collate_X.append(torch.cat([sample['X'], zero_pad], dim=0)) ### 이부분 기억!!
        else:
            ~~~
            
    collate_y = ~~~
    
    return {'X': torch.stack(collate_X),
             'y': torch.stack(collate_y)}
```

### drop_last
* 마지막에 batch size가 안맞아서 학습이 실패한 경우가 존재
```python
~~~DataLoader(dataset,~~~,drop_last=True)
```

### data transform & compose
```python
dataset=~dataset~('다운로드 경로 지정', train=True,
                    transform=transforms.Compose([transforms.Resize((224,224)),
                              transforms.RandomHorizontalFlip(0.5),
                              transforms.CenterCrop(150)])),
                     download=True)
'''
