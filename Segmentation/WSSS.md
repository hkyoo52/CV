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


## CAM 영역을 확장하기 위한 접근



# WSSS History
