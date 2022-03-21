## Object detection 예시

![image](https://user-images.githubusercontent.com/63588046/159194748-eedf0ae1-6598-4bcf-b9e5-c4c0c652049c.png)

![image](https://user-images.githubusercontent.com/63588046/159194759-546b6571-1bac-43a1-b2e2-20b6ef6de10a.png)

## 알고리즘 별 object detection

![image](https://user-images.githubusercontent.com/63588046/159194788-51752e91-6f33-4ddf-9c1b-1faae6015145.png)

## 논문 발전 정도

![image](https://user-images.githubusercontent.com/63588046/159194808-3b961fea-c546-400d-9e78-15dc2fe30240.png)


## 평가 지표
* 성능 : mAP
* 속도 : FPS, Flops

#### mAP
* Precision : 예측한 것중에서 정답
* Recall : 정답중에서 내가 맞게 예측한 것
* AP : PR Curve의 넓이
* mAP : 각 클래스의 AP 평균

#### PR Curve

* 1개의 class에 대해 모든 예측에 대해서 confidence 순서대로 정렬하고 각각의 누적 precision과 recall을 그려 curve를 만듬

![image](https://user-images.githubusercontent.com/63588046/159195103-0b688bba-d887-4491-9e9b-cf434df91b03.png)

![image](https://user-images.githubusercontent.com/63588046/159195127-e79385a2-46ad-4d63-ab60-acaada753d9b.png)
 
 ![image](https://user-images.githubusercontent.com/63588046/159195143-bdc0005d-ba24-4288-9451-3716067d0965.png)
