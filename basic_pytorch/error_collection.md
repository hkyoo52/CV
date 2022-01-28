
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

