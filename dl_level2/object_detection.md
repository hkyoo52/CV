## Objective detection
* classification + bounding localization
* 1 stage : ROI X, 모든 부분 고려
* 2 stage : ROI O, sampling 된 지점만 rhfugka

![image](https://user-images.githubusercontent.com/63588046/157170808-31313122-1e10-49c5-a524-ab557c76b016.png)

## 1 stage

#### selective search
* Over-segmentation : 색깔이 비슷한 것으로 나눔
* 색이 비슷한 것, 특징이 비슷한 것끼리 합침

#### IOU
* 높을수록 예측력 높음

![image](https://user-images.githubusercontent.com/63588046/157169601-f448947e-e35e-4504-ad49-43c771da8bfd.png)

#### Anchor boxes
* 정답이 있을것 같은 후보 값
* 0.7 이상 => positive
* 0.3 이하 => negative

![image](https://user-images.githubusercontent.com/63588046/157169711-b396e968-ec32-4704-ac87-3c1012824e8c.png)

#### Region proposal network (RPN)
* sliding window로 각 지점을 다 분석
* objectiveness score : 그 지점에 물체가 있는지 없는지 socre 냄 (anchor box 당 2개씩)
* 그 지점에서 x, y, w, h 미세 조정

![image](https://user-images.githubusercontent.com/63588046/157170141-ed6d156d-6c33-4b17-8f8e-d021367d120a.png)

#### Non-Maximum Suppression (NMS)
* objectiveness score 가장 높은 box 선택
* 다른 box와 IOU 비교 -> 50% 이상인것 삭제
* 다음번 가장 높은 objectiveness score 높은 것 찾음


#### R-CNN
* selective search로 2000개 조각 얻음
* wraped region : 224 크기로 resize
* CNN feature
* SVM으로 분류

#### Fast R-CNN
* region proposal -> selective search
* CNN으로 feature map 추출
* ROI projection : 물체의 후보를 결정
* FC layer -> softmax, bbox regressor

#### Faster R-CNN
* 최초의 End to end 
* RPN : selective search도 뉴런으로 진행


![image](https://user-images.githubusercontent.com/63588046/157170423-10583e32-4509-4e35-aa33-dd76162de13c.png)



## 2 stage

#### Yolo
* p 개의 grid로 나눔
* 각 grid마다 박스, object 유무, class가 뭔지 파악 (RPN과 유사)

* 7 * 7의 (5B+C) channel (B는 anchor의 개수, C는 분석할 class 개수)

![image](https://user-images.githubusercontent.com/63588046/157171145-39f40aeb-e031-4639-8a97-cdb7a4c751ce.png)


#### SSD
* grid의 크기에 따라 다른 크기의 anchor box가 나옴 
* 각 레이마다 사용되는 anchor box 개수 다 더해서 마지막에 계산
* 매우 빠르고 높은 성능

![image](https://user-images.githubusercontent.com/63588046/157173592-1d7f186f-f2c8-4d78-ab7e-500824652474.png)

![image](https://user-images.githubusercontent.com/63588046/157173736-b525b880-b06c-47f2-9cb6-a7b226c14126.png)



## 문제점 & 개선점
#### 1 stage 문제점
* 모든 grid를 다 고려함
* 실제로 positive한 grid는 거의 존재X -> imbalance한 문제

#### Focal loss
* cross entropy : 맞으면 작은 loss, 틀리면 큰 loss 
* Focal loss : cross entropy보다 더 심하게 분할시킨다. (잘맞추면 loss는 거의 0)

![image](https://user-images.githubusercontent.com/63588046/157174425-e886efa6-9c58-460f-9792-06195fbac6d4.png)


#### RetinaNet
* Unet과 비슷한 구조
* concat 대신에 더하기 사용
* 각 레이어에 class subset과 box subset 존재

![image](https://user-images.githubusercontent.com/63588046/157175024-595e5514-ced7-434d-a4ca-413cbba5ade2.png)


#### DETR




