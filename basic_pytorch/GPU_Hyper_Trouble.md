## GPU 분배 방식
1. DataParallel
* 단순히 데이터를 분배한 후 평균 취함
* GPU사용 불균형, Batch size 감소(한 GPU 병목)
  EX. AlexNet
  
```python
parallel_model=torch.nn.DataParallel(model)
predictions=parallel_model(inputs)
loss=loss_function(predictions,labels)
loss.mean().backward()      # 평균으로 구하고 나서 역전파
optimizer.step()
```
  
2. DistributedDataParallel
* 각 CPU마다 process 생성하여 개별 GPU에 할당
* 기본적으로 DataParallel로 하나 개별적으로 연산의 평균을 냄
* minibatch를 병렬적으로 한다고 생각하면 됨
```python
def main():
  n_gpus=torch.cuda.device_count()
  torch.multiprocessing.spawn(main_worker,nprocs=n_gpus,args=(n_agpus, ))
  ~~
  
def main_worker(gpu,n_gpus):
   image_size=~
   batch_size
   num_worker
   
   batch_size=int(batch_size/n_gpus)
   num_worker=int(num_worker/n_gpus)
   
   gorch.distributed.init_process_group(backend='nccl',init_method='~~',world_size=n_gpus,rank=gpu) #멀티프로세싱 통신규약 정의

   model=MODEL
   
   torch.cuda.set_devic(gpu)
   model=model.cuda(gpu)
   model=torch.nn.parallel.DistributedDataParallel(model,device_ids=[gpu])
   
   
train_sampler=torch.utils.data.distributed.DistributedSampler(train_data)
shuffle=False
pin_memory=True     # 메모리에 바로바로 데이터를 올리는 방식
trainloader=torch.utils.data.DataLoader(trin_data,batch_size=20,shuffle=False,pin_memory=pinmemory,num_workers=3,sampler=train_sampler)
```

## 하이퍼파라미터 튜닝

방식
* grid search
* random search
* 베이지안

### Ray 
* 효율적으로 학습 가능
* 필요 없는 방향으로 가는 것은 학습 안함

```python
! pip install ray 
!pip install tensorboardX
!pip install wandb

from ray.tune.suggest.bayesopt import BayesOptSearch
from ray.tune.suggest.hyperopt import HyperOptSearch

def main(num_samples=10, max_num_epochs=10, gpus_per_trial=2):    
    data_dir = os.path.abspath("./data")
    load_data(data_dir)
    
    config = {
        "l1": tune.sample_from(lambda _: 2 ** np.random.randint(2, 9)),
        "l2": tune.sample_from(lambda _: 2 ** np.random.randint(2, 9)),
        "lr": tune.loguniform(1e-4, 1e-1),
        "batch_size": tune.choice([2, 4, 8, 16])
    }
    scheduler = ASHAScheduler(
        metric="loss",
        mode="min",
        max_t=max_num_epochs,
        grace_period=1,
        reduction_factor=2)
    reporter = CLIReporter(
        # parameter_columns=["l1", "l2", "lr", "batch_size"],
        metric_columns=["loss", "accuracy", "training_iteration"])
    
    result = tune.run(
        partial(train_cifar, data_dir=data_dir),
        resources_per_trial={"cpu": 2, "gpu": gpus_per_trial},
        config=config,
        num_samples=num_samples,
        scheduler=scheduler,
        progress_reporter=reporter)
```


## Trouble shooting

### OOM (device-side-assert도 OOM의 일종)
메모리 부족현상으로 동작이 비정상 종료하는 현상

### 해결 방법
#### Batch Size 갑소
* Batch Size 줄이기 
* GPU clean

#### GPUUtil 사용
* nvidia-smi처럼 GPU의 상태를 보여주는 모듈
* iter마다 메모리가 늘어나는지 확인(메모리가 새고있다는 것을 의미)
```python
!pip install GPUtil
import GPUtil
GPUtil.showUtilization
```

#### 사용되지 않는 GPU상 cache 정리
```python
from GPUtil import showUtilization as gpu_usage

gpu_usage()   #초기 GPU Usage 보여줌

tensorList=[]
for x in range(10):
  tensorList.append(torch.randn(1000000,10).cuda())
gpu_usage()   #텐서 할당 후 GPU Usage 상태 보여줌

del tensorList
gpu_usage()   #텐서 지운 후 GPU Usage 상태 보여줌

torch.cuda.empty_cache()
gpu_usage()   #cache 비운 후 GPU Usage 상태 보여줌 <= 효과적으로 GPU 메모리 지워줌(학습 직전에 사용!!)
```
#### CPU cache 삭제
```python
import gc
gc.collect()
torch.cuda.empty_cache()
````


#### tensor로 축적되는 변수 확인

```python
Ex. loss 값 축적
loss=criterion(output)
loss.backward()
optimizer.step()
#total_loss+=loss    # 쓸데없이 loss값이 축적되고 있다.
total_loss+=loss.item()     #이렇게 사용
```

#### 학습 끝나면 no_grad() 사용
```python
with torch.no_grad():
  for data,target in test_loader:
    output=network(data)
    test_loss+=F.nll_loss(output,target,size_average=False).item()
    pred=output.data.max(1,keepdim=True)[1]
    correct+=pred.eq(target.data.view_as(pred)).sum()
```








