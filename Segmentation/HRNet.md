# HRNet 필요성
* 성능이 매우 높다
* 고해상도 정보 유지

 
#### 왜 classification에서 이미지의 크기를 점차 줄일까?
* 분류할때 이미지의 모든 정보 필요 X
* 파라미터 수가 줄어들어서 연산량 good
* maxpool로 중요 정보만 얻어서 과접합 방지
* receptive field 커짐

#### Segmentation
* 위치 정보가 중요함 -> pooling등을 사용하면 위치정보가 사라짐
* Skip connection으로 위치정보 살릴려고 함
* Deeplab : dilated conv 사용해서 이미지 해상도 적게 줄이면서 넓은 receptive field 가짐



# HRNet 구조 살펴보기
## HRNet 구성 요소
## 고해상도 유지
* 크기를 1/4까지만 줄임
![image](https://user-images.githubusercontent.com/63588046/166219170-b90f586d-cde0-4bd1-98ae-d4178255d303.png)

## 고해상도부터 저해상도까지 다양한 크기의 해상도 병렬적 연결
* 넓은 receptive field 갖는 특징을 고해상도와 함께 학습 가능
![image](https://user-images.githubusercontent.com/63588046/166219538-b1422a7c-698b-4351-8cd0-215018431d7b.png)

## 다중 해상도 정보 반복적 융합
* 고해상도 특징 : 공간상의 높은 위치 정보 민감도 가짐
* 저해상도 특징 : 넓은 receptive field로 인해 상대적으로 풍부한 의미정보
* 저->고 : strided convolution 연산
* 고->저 : Bilinear upsampling 및 1 * 1 conv 연산
![image](https://user-images.githubusercontent.com/63588046/166219707-e309bbaa-36af-4328-b5ca-3aa4c2d9965e.png)

## Representation Head
* 고해상도만 사용 -> Pose Estimation
* 저해상도를 고해상도로 upsampling한 후 모두 합쳐서 사용 -> Semantic Segmentation
* 저해상도를 고해상도로 upsampling한 후 모두 합치고 나서 Downsampling -> Object Detection

## 정리
* 이미지 해상도를 1/4로 축소
* 해상도를 유지하면서 저해상도와 정보 융합

# HRNet 세부 구조 및 구현
![image](https://user-images.githubusercontent.com/63588046/166220462-69a12511-5807-46ce-be13-c80ecc9bcdab.png)



# HRNet 실험 결과
