#### 인공지능 용어
* represent = 자료구조
* receptive field : 한개의 pixel이 이전에 얼마나 영역을 참조하였는가 (P+K-1) * (P+K-1)

## CV의 역사
#### KNN
* 가까이에 있는 점의 수를 파악
* 충분한 데이터가 있는 경우 좋은 정확도
* 검색문제가 될 가능성 있음
* 유사도를 평가해야함

#### fully connecting layer (fc layer)
* 내적을 통해서 score를 만들어서 평가를 함
* robust 하지 못함

![image](https://user-images.githubusercontent.com/63588046/156954965-538574a0-9614-413c-bd79-2a9720f7f389.png)


#### Local connected layer
* 대표적으로 CNN 존재
* 부분적으로 판단



#### 네트워크가 깊어질때 문제점
* Gradient vanishing/exploding
* Computationally complex
* Degradation prob (overfitting X)

#### 1 * 1 conv로 차원 변경
* 계산량 감소
* 학습할때 천천히 변함

![image](https://user-images.githubusercontent.com/63588046/156969898-7f160f45-fc06-4414-bff3-b51ef17a873b.png)


#### ResNet
* 학습이 지속하면 degrade 문제가 생긴다.
* 층이 깊어지면 H(x)를 바로 학습하기 어려워짐
* 이전 블록에서 나온 결과값인 F(x)를 대신 학습하고 나서 x만 더해줌으로써 더 쉽게 학습 가능하게 한다.
* backward() 할때는 x로도 흐를 수 있게 한다. (F(x)가 degrade 생겨도 x가 학습함)
* n개 블록이 생기면 2^n 경로가 생김 (한 블록당 경로 2개씩)

![image](https://user-images.githubusercontent.com/63588046/156971208-4bf5ef6a-1645-4be9-894e-d682fa569f75.png)


#### DenseNet
* 바로 이전 정보뿐만 아니라 예전 블록의 정보도 경로로 연결해 준다.
* resnet은 + 를 사용해서 경로를 연결하지만 DenseNet은 concat을 사용한다.
* concat을 사용하면 정보를 그대로 유지한채 학습할 수 있다.

![image](https://user-images.githubusercontent.com/63588046/156971827-e27a3d95-3b9a-4404-8ea6-dd8fb0af20a8.png)

#### SENet
* Depth 늘리지 X
* attention을 사용해서 activation간의 관계를 명확, 중요도 파악
* Squeeze : global avg를 사용해서 공간정보 없앰 (H, W 없앰)
* Excitation에서 fc layer 사용해서 채널간에 연관성 고려 (attention 만듬)
* 나온것을을 가지고 중요한 것만 살리고 중요하지 않은 정보는 없앤다.

![image](https://user-images.githubusercontent.com/63588046/156972260-23b431e7-bed6-4508-bb4a-3f63196e75b7.png)

#### 학습 방법
* width scaling : 채널 수를 늘린다. Ex. googleNet, DenseNet
* depth scaling : 깊이를 늘린다. Ex. Resnet
* resolution scaling : input 크기를 늘린다.
* 최신 => compound scaling : 앞에 3개를 합침

![image](https://user-images.githubusercontent.com/63588046/156976198-380f29c7-03c3-440c-8af3-a9836d4c8744.png)


#### EfficientNet
* compound scaling 방식
* 적은 epoch에도 높은 성능을 보임

#### Deformable convolution
* 물체가 있는 부위만 가지고 만드는 과정 => irregular
* offset을 사용해서 물체가 있는 부위를 찾음

![image](https://user-images.githubusercontent.com/63588046/156976719-0209decb-c706-4210-8645-3aaeabc0f915.png)

