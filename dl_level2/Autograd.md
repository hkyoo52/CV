## Autograd
* Automatic gradient : 기울기를 알아서 구해줌
* 딥러닝을 굉장히 쉽게 해줌

```python
x=torch.randn(2,requires_grad=True)    # x가 grad 가능한 변수로 만듬
y=x*3
gradients=torch.tensor([100,0.1],dtype=torch.float)
y.backward(gradients)    # grad*(dy/d_)
print(x.grad)    # x에 미분값을 담을 수 있음
````

* backward 2번 하면 안되는 안되는 이유 : 한번 작동하면 중간 과정에 grad 저장하는 것을 다 없앰(메모리 아끼려고)
* 만약 backward를 지속적으로 하고 싶으면 y.backward(gradients, retain_graph=True)로 변경

![image](https://user-images.githubusercontent.com/63588046/157419707-6cc06d08-7533-4f83-ac91-816c580c3998.png)


#### 중간에서 grad 얻는 방법
* register_hook(hook) 사용한다!!

* register_forward_hook(hook_func) : 정전파했을때 값 출력
* register_backward_hook(hook_func) : 역전파했을때 값 출력

```python
# forward hook

class SimpleNet():
~
~
~
def hook_func(self, input, output):
 print('Inside ' + self.__class__.__name__+'forward')
 print('')
 print('input: ',type(input))
 print('input[0]: ',type(input[0])
 print('output: ',type(output))
 
net=SimpleNet()
net.conv1.register_forward_hook(hook_func)   # 원하는 것을 볼 수 있음
```

```python
# backward hook

class SimpleNet():
~
~
~
def hook_func(self, input, output):
 print('Inside ' + self.__class__.__name__+'backward')
 print('')
 print('input: ',type(input))
 print('input[0]: ',type(input[0])
 print('output: ',type(output))
 
 return ~    # 역전파할때 값을 변경할 수 있음
 
net=SimpleNet()
net.conv1.register_backward_hook(hook_func)   # 원하는 것을 볼 수 있음
```


#### feature  얻는법
```python
save_feat=[]
def hook_feat(module,input,output):
  save_feat.append(output)
  return output

for name,module in module.get_model_shortcuts():
  if(name == 'target_layer_name'):
    module.register_forward_hook(hook_feat)
  
img = img.unsqueeze(0)
s = model(img)[0]

```

