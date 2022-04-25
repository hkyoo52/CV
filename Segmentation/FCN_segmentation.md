## FCN (Fully Convolutional Network for segmentation)
* VGG 네트워크 backbone 사용 -> pretrained weight 사용 가능!!
* VGG 네트워크의 FC layer(nn.Linear)를 Convolution으로 대체
* Transposed Convolution 이용해서 이용해서 Pixel Wise prediction 수행

#### Fully connected layer VS Convolution layer
* Fully connected layer는 마지막에 flatten을 해서 위치 정보를 없앰(위치 관심X, object가 뭔지만 궁금)
* Convolution layer는 위치정보를 해치지 않으면서 정보를 얻음

![image](https://user-images.githubusercontent.com/63588046/165026909-fc9f5e61-f961-42ef-bc1f-b6fff6863941.png)

* nn.Conv는 height, width와 상관이 없기 때문에 크기에 영향을 덜받는다.

#### Transposed Convolution
![image](https://user-images.githubusercontent.com/63588046/165029759-13155d76-0cda-4f3c-8f6a-43cba9d095cd.png)
