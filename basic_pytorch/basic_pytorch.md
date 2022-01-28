### 데이터 불러오기

```python
transform=torchvision.transforms.Compose([torchvision.transforms.ToTensor(),
                                          ~~~~])

train_transformed=torchvision.데이터셋(root=~, train=True,download=True,transform=transform)
test_transformed=torchvision.데이터셋(root=~, train=False,download=True,transform=transform)
```

### 데이터 학습하기
```python
batch_size=64
train_dataloader = torch.utils.data.DataLoader(train_transformed, batch_size=BATCH_SIZE, shuffle=True, num_workers=2)
test_dataloader = torch.utils.data.DataLoader(test_transformed, batch_size=BATCH_SIZE, shuffle=False, num_workers=2)

# 데이터 분류
class_num=100
# 마지막 fully-connecting-layer 만들기
resnet18.fc= torch.nn.Linear(in_features=512, out_features=MNIST_CLASS_NUM, bias=True)
# 초기화하기
stdv=0.01
torch.nn.init.xavier_uniform_(resnet18.fc.weight)
resnet18.fc.bias.data.uniform_(-stdv, stdv)



```
