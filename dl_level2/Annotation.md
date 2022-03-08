## 빅데이터 문제
* 너무 많은 데이터 필요
* 라벨링을 해야함

## Augmenting data
* 존재하는 데이터의 주변에 새로운 데이터 생성
* 
![image](https://user-images.githubusercontent.com/63588046/156956983-8194c1a7-54e9-4e28-b90f-144031b5acea.png)

#### Augment 방법
* brightness
* rotate
* crop

#### Brightness adjustment
* 밝은 데이터와 어두운 데이터 모두 존재 -> 구분해서 augmentation 해야함
``` python
def brightness_augmentation(img):
  img[:,:,0]=img[:,:,0]+100   # R value +100
  img[:,:,1]=img[:,:,1]+100   # G value +100
  img[:,:,2]=img[:,:,2]+100   # B value +100
  
  img[:,:,0][img[:,:,0]>255] = 255  # 255보다 큰 수 255로 맞춤
  img[:,:,1][img[:,:,1]>255] = 255  # 255보다 큰 수 255로 맞춤
  img[:,:,2][img[:,:,2]>255] = 255  # 255보다 큰 수 255로 맞춤
```

#### Rotate
```python
img_rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
img_flipped = cv2.rotate(image, cv2.ROTATE_180)
```

#### Crop
```python
y_start = 500
crop_y_size=400
x_start=300
crop_x_size=800
img_cropped = image[y_start : y_start+crop_y_size, x_start : x_start+crop_x_size, :]
```
![image](https://user-images.githubusercontent.com/63588046/156957812-54d3033b-5aef-49e7-a5ac-55a14c376bba.png)


#### Affine transformation
* 길이와 비율을 유지하고 변형시키는 방법
* 대응 쌍으로 바뀜

![image](https://user-images.githubusercontent.com/63588046/156957941-3c2612b7-da41-4726-ae60-101cdcc38230.png)
```python
rows,cols,ch=image.shape
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv2.getAffineTransform(pts1,pts2)               # 대응 쌍으로 변경
shear_img = cv2.warpAffine(image, M, (cols,rows))   # 일정 크기로 출력
```
![image](https://user-images.githubusercontent.com/63588046/156958554-858edc66-5d3d-4bee-81c0-6a4afbecd1c7.png)


#### CutMix
![image](https://user-images.githubusercontent.com/63588046/156958712-7e1cb06b-ffa2-4b14-8d1d-3337e6c225bc.png)


## Pretrained 
#### Transfer learning
* 미리 학습한 데이터셋으로 우리의 데이터셋 학습
* fully connected layer만 바꾸는 방식

![image](https://user-images.githubusercontent.com/63588046/156959100-1705139d-65c7-456b-ab0d-0188b05e3b72.png)
* convolution layer도 learning rate를 작게 잡아서 학습하는 방식

![image](https://user-images.githubusercontent.com/63588046/156959212-595c7b00-f593-43e0-941c-27611e1243a0.png)

#### Knowledge distillation
* 큰 모델로 학습한 것은 작은 모델에서 학습시키기
* 최근에는 pseudo-labeling(label이 안된 데이터에 label 붙이기)에 사용
* student model이 teacher model이 학습하는 것을 따라가게 만듬 
* student Model만 backward 사용!! -> labeling 안된 student model을 예측 label 생김 (distillation loss, student loss 모두 student model만 변경시킴)

![image](https://user-images.githubusercontent.com/63588046/156959916-fc2aa1bd-312b-499a-94f1-5880534a71a6.png)

![image](https://user-images.githubusercontent.com/63588046/156960226-fbf27d2c-ed0d-4cdd-b739-6267ab1bfa2c.png)

**softmaxt with temperature (T)**

![image](https://user-images.githubusercontent.com/63588046/156960625-ee750c94-eb71-4597-8ad5-b236128b7d30.png)

* 출력값을 smooth하게 만들어줌 (중간값에 많이 분포) (정보를 더 많이 가지고 있음)
* 이 것을 사용해서 soft label을 생성하는데 그 이유가 Teacher Model이 어떤 label을 가지는지 궁금하지X, 어떤 개형으로 학습되는지만 궁금함

#### Distillation Loss
* KL 거리(soft label, soft prediction)
* teacher network inference와 student network inference 비교

#### Student loss
* CrossEntropy(Hard label, Soft pred)
* 실제 label과 student network inference 비교

## Leveraging
#### Semi-supervised learning
* 적은 수의 데이터만 label됨
* label 데이터를 통해 pretrained
* unlabel 데이터 pretrained model로 label
* 이 데이터들로 다시 모델 재학습
* student model이 점점 커짐

![image](https://user-images.githubusercontent.com/63588046/156961514-8894dbfe-0b8b-4b61-81bc-5b7f16ab1e40.png)

![image](https://user-images.githubusercontent.com/63588046/156961963-02859637-4938-4211-83ec-6e5158043aa0.png)






