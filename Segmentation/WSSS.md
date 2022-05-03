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

## CAM을 sharp하게 만들기 위한 접근

## CAM 영역을 확장하기 위한 접근



# WSSS History
