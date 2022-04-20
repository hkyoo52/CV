## Sementation 기반 방식
* 장점 : 다양한 모양의 텍스트를 유연하게 잡아낼 수 있다.
* 단점 : 인접한 개체 구분이 어렵다

![image](https://user-images.githubusercontent.com/63588046/164199163-9e5dffd9-6f7e-4637-8a33-6cec07770248.png)


## Pixel embedding
* 같은 영역의 화소끼리 가깝게 학습
* 다른 영역의 화소는 멀게 학습

![image](https://user-images.githubusercontent.com/63588046/164199393-e27ad85e-aa16-4fd0-9e4f-ba247ab2f9fb.png)

## PSENET
* 텍스트의 중간 부분을 찾음
* 그 부분을 중심으로 확장해나가면서 찾음

![image](https://user-images.githubusercontent.com/63588046/164199731-b52a8737-3524-42eb-a1f1-bcc786e34ac5.png)

## DBNet
* 글자 영역 구분하는 threshold 값을 이미지 별로 모델이 알아서 정함
* 경계선 부분에서는 더 높은 값으로 임계치를 적용하자

![image](https://user-images.githubusercontent.com/63588046/164200178-488a32f0-783d-425f-8060-8b5d0065dc20.png)

![image](https://user-images.githubusercontent.com/63588046/164200226-fe68e0e4-d723-48ef-a735-d420414676ce.png)

![image](https://user-images.githubusercontent.com/63588046/164200298-83e3f423-ddeb-4f77-b293-c1688b9299ba.png)


## TExt Feature Alignment Module
* deformable convolution : pn 변화량을 학습을 통해서 찾음!!
![image](https://user-images.githubusercontent.com/63588046/164201957-7b5fe0b9-4c2e-40eb-954d-b76624229db4.png)



## MOST(Position Aware NMS 사용)
* East에서 고안된 NMS 방법
* MOST는 2개의 bbox를 합칠때 Position-aware Merge 함수 제안
* 종횡비가 클 경우 성능이 좋지 않음
* score 정보가 아닌 position-sensitive-map으로 계산하자

![image](https://user-images.githubusercontent.com/63588046/164203754-d5ad10e7-6dbd-4f4c-b87c-129ad6f19ed6.png)

* p1과 q1 사이 중 p1에 가깝게
* p2와 12 사이 중 q2에 가깝게

![image](https://user-images.githubusercontent.com/63588046/164204001-148c8298-54a0-4599-bf9b-b3d2d6257d97.png)


## TextFuseNet
#### 기존 문제점
* 영역이 끊어지면 합치기 어렵다
![image](https://user-images.githubusercontent.com/63588046/164204637-d5552d04-387e-4a2d-bb8e-8f2810ba99c8.png)

#### 해결법
* 글자 영역 결과만 글자 검출 결과로서 활용
* global/word/char level feature 활용하여 글자 영역 검출과 글자 추출 task 수행

![image](https://user-images.githubusercontent.com/63588046/164205287-5478a1eb-ade3-4258-a4ef-f802e987c459.png)

* global level feature -> 이미지 전체에 대한 segmentation으로 확보한 feature
* word,char level feature -> detect branch에서 학습
* 결과값을 ROI로 합침

![image](https://user-images.githubusercontent.com/63588046/164205969-a5dce5fa-bed5-4ab8-96a0-003a7e20ee8c.png)
