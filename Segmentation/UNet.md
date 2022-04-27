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
