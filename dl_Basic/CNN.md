## Convolution
![image](https://user-images.githubusercontent.com/63588046/152730579-53fc45ed-8f22-4926-ae34-5a1d4d0c1e1e.png)

* 이미지의 channel 수 = filter의 channel 수
* filter의 개수 = output의 channel 수
* 파라미터 개수 =  filter의 channel 수 * w * h * filter 개수

#### fully connecting layer의 수가 줄어들어야함
* 너무 많은 파라미터를 가지게 됨
* 학습하는 모델의 파라미터가 많을수록 학습 hard & generalization bad 

#### Stride
kernel을 얼마나 이동할것인가

#### Padding
output이 얼마나 옆에 붙일것인가

#### 1 * 1 Convolution
* 차원 감소
* layer의 깊이는 늘어나는데 파라미터 수는 감소


#### Relu
* nonlinear
* generalization이 잘됨
* 학습을 계속해도 gradient가 사라지지 않음
* 학습 용이


#### VGGNet
* Receptive field : filter가 한번의 보는 이미지의 면적의 크기\
* 3 * 3 convolution이 2번 사용되면 5 * 5 convolution을 한번 사용하는 것과 receptive field 동일
* 3 * 3 convolution 사용 => 동일한 receptive field, 훨씬 적은 파라미터

#### GoogleNet
* 1 * 1 convolution을 사용해서 파라미터 수를 줄임
![image](https://user-images.githubusercontent.com/63588046/152788156-de0b6405-0103-4b66-846a-e237cbbbac9e.png)
<이러한 현태를 **bottleneck** 구조라고 함>

* Inception blocks : 여러개로 벌려젔다가 다시 합쳐짐

![image](https://user-images.githubusercontent.com/63588046/152765340-a42d33f7-a80e-4538-b5af-d20ab3be91ba.png)

#### ResNet
* 일반적으로 네트워크가 커지면 학습을 더 못시킴
* x + f(x) 를 학습 => residual(차이)만큼만 학습을 함
* shortcut할때 차원을 맞추기 위해서 1 * 1 convolution 사용

#### DenseNet
* Dense Block : 각 layer 들을 계속 concatenation 해서 늘림
![image](https://user-images.githubusercontent.com/63588046/152791795-cc8c66f3-a43b-47b0-b17b-fb16af10a786.png)

* Trasition Block : 1 * 1 Conv를 통해서 차원을 감소시킴



### Segmentation
* Convolutionalization : flatten 하기 대신에 conv 적용 => 파라미터 수는 동일
![image](https://user-images.githubusercontent.com/63588046/152902769-ff4f4726-d002-44c4-a622-4816e153dc76.png)

* input 이미지 크기와 상관없이 작동함
* output 값이 heatmap으로 보여줄 수 있다.

#### Fully Convolutional Network
* segmentation을 할려면 마지막 레이어를 input size로 늘려줘야한다.
* Deconvolution : convolution 역계산과 비슷
![image](https://user-images.githubusercontent.com/63588046/152903364-93a3ded5-f543-4a1d-aaf5-bbd8c61aaa3d.png)


#### RCNN
* 한 이미지에서 2000개 이미지를 추출하고 그 이미지를 CNN에 넣은 후 분류함
* 정확하지 X

#### SPPNet
* 이미지 안에서 bounding box를 뽑고 이미저 전체에 대해서 convolution feature map 만든 다음에 뽑힌 bounding box에 해당하는 tensor만 가져오자 (CNN 1번만 해도 됨)

#### Fast RCNN
* SPPNet에 마지막 layer를 RCNN으로 함(SVM + bbox)

#### Faster RCNN
* bounding box를 뽑는 방법도 학습하자
* RPN : 이 region에 객체가 있는가?
* anchor box : 정해진 box 여러 사이즈


#### Yolo 
* bounding box를 뽑지 않음
* 이미지를 S * S gird로 나눔
* 5개의 bounding box를 찾음 & 이게 쓸모 있는지 결정 & 어떤 클래스인지 찾음

