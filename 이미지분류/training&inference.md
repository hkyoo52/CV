## Loss
* 역전파
* nn.Module Family 중 하나
* Fecal Loss : Class Imbalance 문제가 있을 경우 확률이 높은 Class는 조금의 loss를, 확률이 높은 Class는 Loss를 높게 부여
* Label Smoothing Loss : Class target label을 Onehot 표현으로 사용하기 보다는 조금 soft하게 표현
          Ex. [0,1,0,0,0] -> [0.025,0.9,0.025,0.025,0.025]

## Optimizer
* 수렴을 빠르게 만듬(어느 방향으로 얼마나 움직일 것인가)

#### LR scheduler
* 학습 시에 learning rate를 동적으로 조절(Ex. 학습할수록 lr 감소)
* StepLR : 고정된 step만큼 learning rate 두고 그 이후에는 learning rate 감소
```python
scheduler=torch.optim.lr_scheduler.StepLR(optimizer,step_size=2,gamma=0.1)
```
* CosineAnnealingLR : cosine 함수 형태로 lr 변경함 => 변화를 다양하게 줄 수 있음, local minimum에 잘 탈출
```python
scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer,T_max=10,eta_min=0)
```
* ReduceLROnPlateau : 더이상 학습을 안하면 lr 감소
```python
scheduler=torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer,'min')
```

## Metric
* 모델의 평가
* 정확한 Metric을 사용했는지 파악해야한다!!!

#### Classification
* Accuracy, F1-score, precision, recall, AUC-ROC
* Accuracy : Class 별로 밸런스가 적절히 분포
* F1-Score : Class 별로 밸런스가 좋지 않아 각 클래스별로 성능을 잘 낼 수 있는지 확인 필요


#### Regression
* MAE, MSE

#### Ranking 
* MRR, NDCG, MAP

#### 학습 프로세스
```python
for epoch in range(2):
  running_loss=0.0
  for i, data in enumerate(trinaloader,0):
    inputs,labels=data
    optimizer.zero_grad()         # 파라미터가 가지고 있는 grad를 초기화 
                                  # loss를 현재 배치에서 나오는 것만 활용하겠다.
    outputs=net(inputs)
    loss=criterion(outputs,labels)  # criterion도 하나의 module family -> chain이 만들어짐
    loss.backward()
    optimizer.step()
    
    running_loss+=loss.item()
    if i%2000 == 1999:
      print('[%d,%5d] loss : %.3f'%(epoch+1,i+1,running_loss/2000))
      running_loss=0.0
```

#### 학습 프로세스 - Gradient Accumulation
* GPU가 한정적임 -> 배치를 늘릴 수 없는 경우가 존재
* n번째마다 파라미터를 업데이트 하는 방식(배치를 늘리는 것과 비슷한 방식이 됨)
```python
NUM_ACCUM=2
optimizer.zero_grad()
for epoch in range(2):
  running_loss=0.0
  for i,data in enumerate(train_loader,0):
    inputs,labels=data
    outputs=net(inputs)
    
    loss=crieterion(outputs,labels)/NUM_ACCUM
    loss.backward()
    
    if i%NUM_ACCUM == 0:
      optimizer.step()
      optimizer.zero_grad()           # optimizer가 중첩되고 NUM_ACCUM때에 초기화 시킴
```


#### inference(추론) 프로세스
```python
correct=0
total=0
with torch.no_grad():                 # 모든 tensor는 grad=0
  for data in testloader:
    images, labels = data
    outputs=net(images)
    _, predicted=torch.max(output.data,1)
    total +=labels.size(0)
    correct += (predicted == labels).sum().item()

print("Accracy : %d %%'%(100*correct/total))
```

#### Checkpoint
```python
if val_loss<best_val_loss:
  torch.save(model.state_dict(), f:result/{name}/{epoch:03}_loss_{val_loss:4.2}.ckpt")
  best_val_loss=val_loss
  
if val_acc>best_val_acc:
  torch.save(model.state_dict(), f:result/{name}/{epoch:03}_loss_{val_acc:4.2}.ckpt")
  best_val_acc=val_acc
```


## Pythorch Lightning
![image](https://user-images.githubusercontent.com/63588046/155098018-dc912b90-4a14-4d2e-9e31-1c3bdbbe4e5e.png)


