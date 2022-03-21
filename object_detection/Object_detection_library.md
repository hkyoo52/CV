## 대표적인 라이브러리
* MMDetection
* Detectron2

![image](https://user-images.githubusercontent.com/63588046/159211071-1a678da2-be15-4364-99cc-b602e7afb1b5.png)


# MMDetection

* 완벽하게 이해하면 매우 편리하다. 기능이 매우 많다.
* library를 완벽하게 이해하기 어렵다
* config 파일 하나로 모든 것을 다 조절한다.
* Backbone : 입력 이미지를 특징 맵으로 변형
* Neck-backbone과 head를 연결, feature map을 재구성
* DenseHead : 특징 맵의 dense location을 수행하는 부분
* ROIHead : ROI 특징을 입력으로 받아 box 분류, 좌표 regression 등을 예측하는 부분


![image](https://user-images.githubusercontent.com/63588046/159211261-4bf33f83-4c87-4db8-aedc-025a8d1e22f6.png)


## 파이프 라인
#### 라이브러리 및 모듈 import


![image](https://user-images.githubusercontent.com/63588046/159211665-9d56ffdc-89d3-43bb-ab36-c0d15fae0c2f.png)


#### config 파일 불러오기

![image](https://user-images.githubusercontent.com/63588046/159211697-95f4c4a4-7b6d-47a3-936f-770eaf26f767.png)


#### config 파일 수정하기
* 데이터셋, 모델, scheduler, optimizer 정의
* object detection 모델들의 config 파일 정의
* dataset, model, schedule, default_runtime 4가지 기본 구성요서 존재
* Dataset-COCO, VOC, Cityscape 등등
* Model-faset_rcnn, retinanet, rpn 등등

![image](https://user-images.githubusercontent.com/63588046/159211733-6d0795bb-8284-4243-a6a9-583ac7751665.png)

![image](https://user-images.githubusercontent.com/63588046/159211757-587b05d2-801e-43a1-b350-fea295d2f444.png)


#### 모델, 데이터셋 build, 학습
```python
model = build_detector(cfg.model)
datasets = [build_dataset(cfg.data.train)]
train_detector(model, datasets[0], cfg, distributed=False, validate=True)
```




# Detectron2
* Config
* Trainer
  * build model
  * build detection train/test loader
  * build optimizer
  * build lr_scheduler
* Training



