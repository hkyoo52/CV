# U-Net

### 왜 U-Net이 각광받았는가?
* Deep Learning은 파라미터 수가 많고 네트워크가 깊어서 train data 많이 필요
* 의료계열 같이 데이터가 없는 분야 존재
* 일반인인 labeling 하기 매우 어려움
* 인접해 있는 객체 사이 경계 구분 필요

### U-Net 장점
* Encoder가 확장해서 1024까지 증가시킴 -> 고차원의 정보 매핑
* 각기 다른 계층의 encoder 출력을 decoder와 결합 -> 이전 레이어 정보 효율적 활용

### 아키텍처
* Contracting Path
    * 입력 이미지의 전반적인 특징 추출
    * 차원을 줄이는 Down-Sampling
    * 3 * 3 conv + BN + ReLU
    * padding 사용X -> patch size 감소
    * 2 * 2 Max Pooling(stride=2) -> feature map의 크기 절반으로 감소
    * Max pooling 이후 채널 수 2배 
* Expanding Path
    * Localization을 가능하게 함
    * 차원을 늘리는 Up sampling 작업 & 얕은 layer의 feature 결합

* skip connection에서 이미지 크기가 맞지 않을 경우 crop 사용 -> 가운데로 crop하게 만듬

![image](https://user-images.githubusercontent.com/63588046/165444554-86d5c335-887f-4deb-9bc0-70d7f9ec8af2.png)

### U-Net에 적용된 기술
#### Data Augmentation : Random Elastic deformation
* 객체를 구김 -> 모델을 더 robustic하게 만듬

#### Weight map
* 각은 클래스를 가지는 인접한 셀 분리하기 위해 경계부분에 가중치 제공

![image](https://user-images.githubusercontent.com/63588046/165454283-90787785-9c05-44ba-849b-d253db720e67.png)

### U-Net 한계점
* 깊이가 4로 고정됨
  * 데이터셋마다 최고의 성능 보장 X
  * 최적 깊이 탐색 비용
* 단순한 skip connection
  * 동일한 깊이를 가지는 Encoder Decoder만 연결되는 제한적 구조


# U-Net ++
* Encoder를 공유하는 다양한 깊이의 U-Net 생성
* Dense Skip Connection 사용
   * 같은 층에 있는 모든 conv값과 skip connection
   * conv 한 값과 up-sampling 한것은 concat해서 convolution
* loss 값은 각 층의 있는 모든 node의 loss들을 평균내서 사용
![image](https://user-images.githubusercontent.com/63588046/165660459-d02df8df-fd17-4a55-bb01-e7db7de906ca.png)

### 한계점
* 복잡한 connection -> 파라미터 수가 많음
* 많은 connection -> memory 큼
* Encoder-Decoder 사이에서의 connection이 동일한 크기를 갖는 feature map에서만 진행
      * Full scale에서 충분한 정보 탐지X -> 위치와 경계 명시적 학습X (2칸 이상 떨어진 층에 정보 가져오지 X)

# UNet 3+
* (conventional + inter + intra) skip connection
   * conventional : encoder layer로부터 같은 scale의 feature map 받음
         * 채널수가 맞지 않으므로 conv로 채널 수 맞춤
   * inter : encoder layer로부터 small scale(1개의 픽셀이 가지고 있는 정보가 작다)의 low-level feature map 받음 (경계 정보 강조)
         * 이미지 크기가 맞지 않기 때문에 maxpooling으로 이미지 크기 감소
   * intra : decoder layer로부터 large-scale의 high-level feature map 받음 (위치 정보 구현)

![image](https://user-images.githubusercontent.com/63588046/165661742-47ed99cd-0590-438d-8e72-602c9da8304d.png)


### CGM (classification guided module)
* low-level layer에 남아있는 background noise 때문에 false-positive 문제 발생 
      * 정확도를 높이려고 extra classification task 진행
      * high-level feature map 활용
            * Dropout, 1 * 1 Conv, AdaptiveMaxPool, Sigmoid 통과
            * Argmax를 통해 Organ이 없으면 0, 있으면 1 출력
            * 위에서 얻은 결과와 각 low-layer마다 나온 결과를 곱


