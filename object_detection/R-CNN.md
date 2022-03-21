# R-CNN

#### Selective Search
* 이미지 색, 특징 등으로 후보 객체를 고르는 방법

## Pipeline
1. 입력 이미지 받기
2. Selective Search를 통해 2000개 ROI 추출
3. 이미지 크기 조절
4. ROI를 CNN에 넣어 feature를 추출
  * 각 region마다 4096-dim feature vector 추출 (2000 * 4096)
  * Pretrained AlexNet 사용(마지막에 FC layer 추가, finetuning 진행)
5-1. feature를 SVM에 넣어 분류 진행
  * Input : 2000 * 4096
  * Output : Class(C+1(배경))+Confidence score
5-2. feature를 regression을 통해 bounding box를 예측

![image](https://user-images.githubusercontent.com/63588046/159199647-91c80f14-0731-4c12-ae63-992397203cac.png)

## Training
#### AlexNet
* IOU > 0.5 : positive sample
* IOU < 0.5 : negative sample

#### Linear SVM
* Ground truth : positive sample
* IOU < 0.3 : negative sample

#### Hard negative mining
* 배경인데 대상으로 잘못 예측한 것을 다음 배치에 negative sample로 넣어서 학습하는 방법


# SPPNet

#### R-CNN 단점
* 이미지를 고정시킴
* ROI마다 CNN 통과 (2000번 통과해야됨)

#### R-CNN vs SPPNet

![image](https://user-images.githubusercontent.com/63588046/159200101-76c513ef-6db6-4a80-9566-06adfe830796.png)

![image](https://user-images.githubusercontent.com/63588046/159200221-4ce8740b-dc67-49cc-82c9-c5b3c698c603.png)


#### Spatial Pyramid Pooling
* Spatial Pyramid Pooling Layer를 통해서 이미지를 고정시킴
* 크기에 따라 다른 filter를 가지고 만듬 => 고정된 feature vector 만듬

![image](https://user-images.githubusercontent.com/63588046/159204930-0ae7c551-5f80-4700-9814-39867febf2e2.png)


# Fast R-CNN
* Fast R-CNN + Spatial Pyramid Pooling

![image](https://user-images.githubusercontent.com/63588046/159205002-1286c39f-945a-44a1-9e2b-82b39c8f8d9a.png)

#### ROI projection
* feature map에서 바로 ROI 뽑을 수 X -> 원본 이미지에서 ROI를 구하고 그 위치에 맞게 feature map에 적용

![image](https://user-images.githubusercontent.com/63588046/159205469-abd96973-f28f-4ef8-9d44-ffea9ea70ca1.png)

# Faster R-CNN

* selective search -> RPN(REgion Proposal Network)

![image](https://user-images.githubusercontent.com/63588046/159205625-3e9dd8af-aa1f-4c10-b9f2-71c7ba411b70.png)

#### Pipeliine
* Anchor box : 다양한 크기에 box
* anchor box generator : 크기 * anchor box 개수* 4(x,y,x,h)
* Classification prediction : 크기 * anchor box 개수 * 2(객체/객체X)
* Box prediction :크기 * anchor box 개수 * 4(이동해야 할 x,y 키워야 하는 w,h)


#### RPN
* 각 pixel마다 객체가 있는지, 무슨 class인지 파악
* 객체가 있을 경우 어떤 anchor box를 사용할 지 선택

![image](https://user-images.githubusercontent.com/63588046/159205943-1ea535b3-bb66-42ff-99b3-c47d2830c49a.png)





## 정리

![image](https://user-images.githubusercontent.com/63588046/159207769-bcc209ee-ed32-44e9-92e4-889b73701b8d.png)





