
### 미분이 불가능한 변수
```python
 Only Tensors of floating point and complex dtype can require gradients
 ```
해결법 : tensor -> Tensor 


### 변수가 존재하지 않을경우
```python
  @classmethod
 ```
해결법 : __init__, __getitem__ 에 변수 추가하기


#### 경로 문제
```python
num_samples should be a positive integer value, but got num_samples=0
```
* 경로가 잘못되었음 (특히 dataset 위치 확인)

#### 동일 loss 반복 backward
```
Trying to backward through the graph a second time, but the saved intermediate results have already been freed. Specify retain_graph=True when calling backward the first time.
```
* 동일 혹은 일부의 loss 값에 loss.backward를 반복했다.
* model 내에 y=nn.Lineard(concat(y1,y2)) 이런게 있을 때 y1과 y 동시에 학습


#### device 다 붙여라
``` python
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! 
```
* .to(device) 안 붙인게 있음

### 메모리 에러
* nvidia-smi 확인
* 다시 돌려라
* 그런데도 에러? ->....
* 
