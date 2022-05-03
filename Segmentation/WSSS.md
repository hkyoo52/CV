# WSSS 개요

## WSSS 소개
* 분류문제는 instance 당 1초 걸림
* object detection은 instance 당 10초 걸림
* Semantic Segmentation은 instance 당 78초 걸림...

=> classification의 정보를 가지고 segmentation 할 수는 없을까?

![image](https://user-images.githubusercontent.com/63588046/166401521-94992f96-2693-47c4-af92-9770690f6824.png)


## Native approach
* 가지고 있는 정보인 image level label을 활용하기 위한 classification 모델 학습
* 학습한 classification 모델을 통해 CAM, Grad-CAM 혹은 attention 추출 (pseudo mask 추출)
* 추출한 결과물은 pseudo mask로 segmetation 모델 학습


# CAM 기반의 접근

## CAM & Grad-CAM
* Classification 모델을 학습하면서 생성 가능
* 특정 class의 물체가 사진의 어떤 영역에 있는지 유추 가능

![image](https://user-images.githubusercontent.com/63588046/166406466-38d01611-a986-4de4-a56d-86e398f621e0.png)
 
#### 기본적인 classification 구조
![image](https://user-images.githubusercontent.com/63588046/166406681-db5b98c7-3811-449d-86da-2f9035b252c2.png)

#### CAM
* classification에서 GAP하기 전에 각각의 feature에서 중요하다고 말하는 위치를 찾음
![image](https://user-images.githubusercontent.com/63588046/166406837-90dd2cbc-94e2-4ee3-8fb6-3d7ecc8d7d7f.png)

#### CAM에 문제점
* 마지막 layer로만 만들수 있음 -> 이전 layer가 어떻게 활성화되고 있는지 확인 X

#### Grad-CAM
* feature에 변화를 주는데 score에 변화가 적다 -> 중요도가 낮다
* class score 변화량/feature 변화량 = 미분값 = 중요도 => 각 feature에 모든 픽셀을 적용해보고 그것을 평균낸 것을 feature 중요도로 판단

![image](https://user-images.githubusercontent.com/63588046/166407145-430cf432-633d-4891-b034-5ff9138a871a.png)

![image](https://user-images.githubusercontent.com/63588046/166407259-a3c21548-9255-49a6-858a-4fec73f33313.png)


## CAM을 sharp하게 만들기 위한 접근
* CAM은 sharp하지 않고 둥글둥글하게 나옴
* 마지막 layer의 크기가 실제 이미지와 다르기 때문

#### 해결법
1번 방식 boundary를 정밀하게 만들어서 loss에 추가

![image](https://user-images.githubusercontent.com/63588046/166407643-e65b2fb5-8f4c-4e01-98e6-46e33322da8f.png)

2번 방식 : Transfer Learning 이용
* Object-ness(saliency)를 학습한 모델 준비 (object를 바라볼때 어디를 처음 보는지) 
* 기존 방식과 Saliency를 합쳐서 더 sharp한 결과를 가짐

![image](https://user-images.githubusercontent.com/63588046/166435263-9a6d27ea-bf09-47f0-82fd-3e905b363026.png)

3번 방식 Self-supervised Learning
* 입력 이미지가 작아질수록 CAM이 동그란 이미지가 됨
* CAM 한 후 downsampling 한 결과와 downsampling한 후 CAM 한 결과 같도록 L1 loss 사용

![image](https://user-images.githubusercontent.com/63588046/166435447-2fb9c128-645f-41aa-a0e8-6703122b735a.png)

![image](https://user-images.githubusercontent.com/63588046/166435594-e5c24654-be08-4c49-9430-3585fc0f15e7.png)


## CAM 영역을 확장하기 위한 접근
* 동물 사진을 예시로 들면 CAM은 동물에 얼굴에만 집중하게 만듬

![image](https://user-images.githubusercontent.com/63588046/166435906-2987c914-0401-4345-9742-c82840fc67f3.png)

* 해결법 : CAM을 구한 후 CAM에서 가장 중요한 부분을 이미지에서 삭제하고 다시 CAM 추출
* 위 과정을 반복한다

![image](https://user-images.githubusercontent.com/63588046/166436048-d326a62b-1643-439d-a912-a1599bf4a238.png)

#### 위 과정 문제점
* Output 별로 다른 모델을 학습해야 하는 번거러움
* Class 별로 필요한 step이 다름...(Over Erasing : 과도한 step인 경우 물체가 아닌 영역까지 mask가 생기는 현상)


#### 해결법2
* random하게 이미지를 지우고 학습
 
![image](https://user-images.githubusercontent.com/63588046/166436420-95bbdd97-9756-4d18-aae1-54fb57454310.png)

![image](https://user-images.githubusercontent.com/63588046/166436465-af168af5-76f1-4a6e-af3b-4381b7a3e45c.png)

#### 해결법3
* Heatmap 얻음
* Thresholding을 통해 지울 영역 구함
* Erasing이 된 feature에서 다시 Heatmap얻음
* Heatmap을 더해서 통합

![image](https://user-images.githubusercontent.com/63588046/166436687-136a064e-5e0d-4f2d-a089-a63607f13ef4.png)

#### 해결법4
* 다양한 receptive field 사용

![image](https://user-images.githubusercontent.com/63588046/166436779-7b7179c5-4004-4025-9dec-19c42a478af4.png)

#### 해결법5
* MIXUP

# WSSS History

![image](https://user-images.githubusercontent.com/63588046/166436891-182d5e5f-ae26-4d6f-8121-5d4e0ab8aaf7.png)

