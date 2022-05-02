## mmSegmentation

```python
pip install git+https://github.com/qubvel/segmentation_models.pytorch

import segmentation_models_pytorch as smp
model = smp.Unet(
          encoder_name='efficientnet-b0',
          encoder_weights='imagenet',
          in_channels=3,
          classes=11,

model = model.to(device)
```

## baseline 이후에 실험해봐야할 사항들
#### 주의해야할 사항들
1. 디버깅 모드 : 실험 환경이 잘 설정되었는지 체크
  * 샘플링을 통해서 데이터셋의 일부만 추출
  * 1~2 epoch만 설정해서 loss 감소하는지 확인
  * step에 따라 loss가 제대로 감소했다면 CFG.debug를 False로 바꿔서 전체 실험 진행

2. seed 고정
  * 실험마다 성능이 달라지는 것을 방지하고 재생산하기 위해서
  * Validation 검증셋의 시드 고정

3. 실험기록
  * network 종류, augmentation 방법, hyperparamet 등 조건 바꿔가면서 실험 진행

4. 실험은 한번에 한번씩
5. 팀원마다 역활 분재
  * 하나의 베이스라인 코드를 기반으로 가장 좋은 솔류션 만들기
    * 같은 코드 중복X 진행
  * 독립적인 베이스라인 코드 만들어서 마지막 앙상블
  * EDA/코드 만들기/솔류션 조사/디스커션 조사 등 역활을 분배


#### Validation 설정
* Hold Out
* K-Fold
  * 각각을 가지고 독립적인 모델을 생성
  * 독립적인 모델을 가지고 앙상블 진행
* Stratified K-Fold
  * 각 클래스를 균등하게 분배
* Group K-Fold
  * Validation에는 train에 없는 label만 넣어놈

![image](https://user-images.githubusercontent.com/63588046/166181794-921482f6-3736-4b47-ac37-ba1c7b0f2476.png)

![image](https://user-images.githubusercontent.com/63588046/166181881-17379375-e038-4648-b47e-38813194b8f5.png)

![image](https://user-images.githubusercontent.com/63588046/166181982-993f16fc-b0d0-4557-b2d8-e899ad9571c9.png)


#### Augmentation
* Robust하게 만들어줌
* Rotation/Flip/Transpose
* Albumentation 사용!! (속도가 빠름)
* 실제로 있을 법하게 Augentation 적용
  * Segmentation에 좋은 Augmentation
    * Cutout -> 가려진 것을 잘 찾음
    * Gridmask -> cutout을 grid 형식으로 만듬 (cutout보다 성능이 좋음)
    * Mixup -> 섞어서 합침
    * Cutmix -> 잘라서 붙임 (mixup보다 성능이 좀 더 좋음)
    * SnapMix
    * CropNonEmptyMaskIfExists

![image](https://user-images.githubusercontent.com/63588046/166182242-4a42af83-81cb-4280-a9a0-1b7b163b4300.png)

![image](https://user-images.githubusercontent.com/63588046/166183325-5bf080c2-5d3f-4117-a4fd-f387a9a83fab.png)

![image](https://user-images.githubusercontent.com/63588046/166183413-eae080cc-db1c-4772-9bd4-552ddec9bccc.png)
  
![image](https://user-images.githubusercontent.com/63588046/166183451-208fb168-8358-497f-afe6-ff5c65c316c2.png


#### SOTA Model 사용

#### 하이퍼파라미터 조정
* Learning rate -> Scheduler (대표적으로 Cosine AnnealingLR, ReduceLROnPlateau, Gradual Warmup(checkpoint 가져올때 좋음))
* Gradient Accumulation 
  * 일정 step동안 gradient 누적한 다음 weight 업데이트하는 방법
  * 배치사이즈 키울수 있음
* Optimizer 조절
  * Adam,AdamW,AdamP,Radam
  * Lookahead optimizer
    * k번 업데이트 한 후 처음 시작했던 point 방향으로 1 step back 후 그 지점을 다시 k번 업데이트
    * local minmum 빠져나올 수 있음
* 다양한 Loss 사용 (Cross Entropy, IOU, Focal Loss, DiceFocal Loss 등등)



#### 앙상블
* Kfole
* Epoch 앙상블
* SWA : 일정 주기마다 weight 평균내는 방법 -> loss 대비 성능이 높아짐(일반화가 잘됨)
  * 75% 일반적인 모델 학습 25% SWA 진행
![image](https://user-images.githubusercontent.com/63588046/166184790-f75e78ca-bf6f-44cf-b672-95113c7fe938.png)

* Seed Ensemble
* Resize Ensemble : object의 크기를 다양하게 만듬 -> 앙상블할때는 크기를 맞춰줘야함
* TTA


#### Pseudo Labeling 
* 외부 데이터 사용해서 학습 올릴때 외부 데이터에 labeling이 잘 안되어 있을때
![image](https://user-images.githubusercontent.com/63588046/166192682-470edde5-cb04-4dbb-8c52-a5115fe9ffbc.png)

#### Classification 사용해보고
* Encoder Head 마지막 부분에 claasification head를 달아서 같이 활용 -> 모델 수렴을 도와줌

![image](https://user-images.githubusercontent.com/63588046/166192790-2732de99-2aca-4a93-b78b-6906753c9af7.png)



## 너무 데이터가 많을 경우
#### Mixed Precision Traing of Deep Neural Network
* FP16과 FP32를 섞어서 학습
![image](https://user-images.githubusercontent.com/63588046/166193002-ac3d7b3c-2163-4162-a937-6f206b4b8cea.png)

#### 가벼운 상황에서 실험
* 일부 데이터 사용
* 이미지 크기를 줄임 (그냥 resize하기 보다는 maxpooling이랑 conv 사용하고 결합)
* 단일 Fold로 검정하고 마지막에 KFold로 전체데이터 사용해서 학습
* 가벼운 모델들로 augmentation등 기법들이 의미가 있는지 찾음
* Sliding Window 사용하는 것도 생각해봐라 -> 데이터 수가 많아짐, 중복되는 부분을 앙상블해서 성능향상, 단 학습량 늘어남...
  * Segmentation 부분만 sliding window 하는것도 good  
![image](https://user-images.githubusercontent.com/63588046/166193113-eb9ed23f-67b1-46ff-8ff4-209803d61e39.png)

![image](https://user-images.githubusercontent.com/63588046/166193476-fcbf0216-4646-46f8-8cc2-dcc9d828bc03.png)


## Label Noise가 있는 경우

#### Label Smoothing
* Hard Target -> Soft Target
![image](https://user-images.githubusercontent.com/63588046/166194312-386d0c2c-5a6d-4da1-8ed8-52d7902532bb.png)

#### Pseudo-labeling
* KFold로 데이터셋 나눔
* 나눈 데이터 셋으로 학습을 하고 validation부분 예측
* validation Ground Truth와 prediction 값의 IOU가 많이 작을 경우 잘못된거라고 생각

