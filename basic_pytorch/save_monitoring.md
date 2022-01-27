### model.save() : 학습의 결과 저장

```python
torch.save(model.state_dict(),os.path.join(MODEL_PATH,'model.pt'))   
# state_dict : 모델의 파라미터를 표시, pt : path 줄인말
```


### summary : 파라미터 쉽게 볼 수 O
```python
from torchsummary import summary
 summary(model,(3,224,224)
```
 
### checkpoints : 학습 중간 결과 저장 -> 최선 결과 가질수 있음
* earlystopping : 이전 학습 결과 가짐, loss, metric 값을 지속적으로 저장

```python
torch.save({'epoch': e , 
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
        'loss': e_loss,},
        f"저장할장소/checkpoint_model_{e}_{e_loss/len(dataloader)}_{epoch_acc/len(dataloader)}.pt")
        
print(f'Epoch {e+0:03}: | Loss: {epoch_loss/len(dataloader):.5f} | Acc: {epoch_acc/len(dataloader):.3f}')
```

### transfer learning : 다른 데이터셋으로 만든 모델을 현재 데이터에 적용
* frozen : 이미지중에서 일부는 값을 변경 안하고 나머지만 학습시킴
```python
class ~~:
  def __init__(self):
    ~~~
    self.vgg16=models.vgg16(pretrained=True)
    ~~
    
  def forward(self,x):
    x=self.vgg16(x)
    ~~

# 마지막 레이어 제외하고 다 frozen
for param in my_model.parameters():
    param.requires_grad = False
for param in my_model.linear_layers.parameters():
    param.requires_grad = True
```

### tensorboard
```python
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter('app/fashion_mnist_experiment_1')
%load_ext tensorboard
%tensorboard --logdir "app"

# get some random training images
dataiter = iter(trainloader)
images, labels = dataiter.next()

# create grid of images
img_grid = torchvision.utils.make_grid(images)
print(img_grid.shape)

# show images
matplotlib_imshow(img_grid, one_channel=True)

# write to tensorboard    (내가 만든것을 writer에 넣어야 tensorboard에서 볼 수 있다.
writer.add_image('four_fashion_mnist_images', img_grid)

writer.add_graph(net, images)
writer.close()                 #close를 해야 tensorboard에서 사용 가능하다
```

유료 사이트중이서 weigth & bias라는 사이트 존재 (프로젝트형식으로 되어있고 시각화 good)
