## Multi-modal
* 다양한 데이터 타입 함께 사용 ex. cv+nlp

#### multimodel이 어려운 이유
* 데이터가 너무 다름 (이미지는 3d 데이터, Text는 embedding 데이터)
* 서로 다른 model에서 오는 정보량이 unbalance함


## Visual & Text
#### Text Embedding
* 비슷한 의미를 가진 것을 비슷한 위치해 둠
* 동일한 차이가 나는 것들은 동일한 벡터만큼 차이가 남

#### word2vec -> skip-gram-model
* 단어를 embedding함
* embedding한것을 다시 복구하면 원래 단어 주변에 있는 단어들이 추출됨

#### Joint embedding
* 이미지를 주면 그에 맞는 단어 알려줌
* 단어를 주면 그에 맞는 이미지 알려줌

* 2개의 모델에서 나온 값은 같은 embedding space에 존재한다.
* matching된 데이터는 embedding space에서 2개의 거리가 가깝게 학습시킴
* matching 안된 데이터는 embedding space에서 2개의 거리가 멀게 penalty 줘서 학습시킴


![image](https://user-images.githubusercontent.com/63588046/158132555-299a5b5f-a030-4a38-ae02-6bccf5dd9580.png)

![image](https://user-images.githubusercontent.com/63588046/158133079-a208a821-3612-48ed-87a0-f7c454e7239c.png)


## Cross Modal Translation
#### Image2Sentece
* 이미지는 CNN 사용해서 FC layer 추출
* sentence는 RNN 사용해서 만듬


![image](https://user-images.githubusercontent.com/63588046/158135005-633609a8-0787-4a4c-8593-94f369d7a8fc.png)

#### Show, Attend, and Tell
* 문장을 만들때는 전체적인 것보다 지역적인 것에 관심을 더 가져야함

* 14 * 14 feature map 출력
* Distribution over L location : feature map에서 어느 부분을 attention 할지 찾음
* feature map과 s1으로 z1 출력
* z1과 y1(단어)으로 h1 생성
* h1에서 s2(어디를 attention 할건지)와 d1 생성(생성되는 단어)


![image](https://user-images.githubusercontent.com/63588046/158135196-dfd31dc1-ef34-4974-9283-24178ced52f2.png)

![image](https://user-images.githubusercontent.com/63588046/158136262-6ae760c0-b8f0-4b7e-8bbe-ca772803e4e8.png)

![image](https://user-images.githubusercontent.com/63588046/158136600-28113ea6-e25e-4438-94d9-2b740a857083.png)


#### Text2Image by Gan
* 문장을 주고 이미지 생성 (Generation model)
* 생성된 이미지를 주고 이 문장과 맞는지 파악 (Discriminator model)

![image](https://user-images.githubusercontent.com/63588046/158137268-f05515ce-8d33-4ad9-83f3-d027c2f52734.png)


## Cross modal reasoning
* 다른 모델을 사용해서 결과를 도출해내는 방식
* 
#### Visual question answering
* Image Stream과 Question Stream이 존재
* 각각이 feature dimention vector로 추출
* 2개를 상호 비교함??

## Sound represent
* 소리 변경 - Fourier transform
* STFT : short-time Fourier Transform
* 매우 작은 범위로 푸리에 변경







