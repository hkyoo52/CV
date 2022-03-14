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






