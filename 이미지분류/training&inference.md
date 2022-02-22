## Loss
* 역전파
* nn.Module Family 중 하나
```python
for epoch in range(2):
  running_loss=0.0
  for i, data in enumerate(trinaloader,0):
    inputs,labels=data
    optimizer.zero_grad()
    outputs=net(inputs)
    loss=criterion(outputs,labels)
    loss.backward()
    optimizer.step()
    
    running_loss+=loss.item()
    if i%2000 == 1999:
      print('[%d,%5d] loss : %.3f'%(epoch+1,i+1,running_loss/2000))
      running_loss=0.0
```
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

