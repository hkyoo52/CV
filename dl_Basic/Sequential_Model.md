## Sequential Model
* 입력이 여러개 들어와도 작동되어야 한다.
* 이전 데이터들로 다음 데이터를 예측한다.
* Autoregressive model : 이후 정보는 바로 전 과거 정보 1개로 결정
* Markov model : 나의 현재는 바로 전 과거에만 의존한다.

![image](https://user-images.githubusercontent.com/63588046/152907275-ac2c2cc8-0f0c-4372-b37e-bb14e0aa820f.png)

* Latent autoregressive model : hidden state가 존재하고 이 정보가 이전의 정보를 가지고 있음


#### RNN
* 나의 hidden state는 x 데이터와 이전에 얻어진 정보의 의존한다.


![image](https://user-images.githubusercontent.com/63588046/152907554-bb0935ba-0e4d-4737-b965-e349fa89414e.png)

* 문제점 : 한참 전에 정보들이 거의 고려되지 않는다
* 네트워크가 너무 커지면 기울기가 폭발하거나 없어짐


![image](https://user-images.githubusercontent.com/63588046/152907914-4b7fef36-d6a1-4b2b-8534-69a8a128ccfa.png)

#### LSTM

* previous cell state : 지금까지 나온 정보를 summary, 밖으로 나가지 X
* previous hidden state : 이전 hidden state


![image](https://user-images.githubusercontent.com/63588046/152908654-299da717-3bcc-407b-a97b-f726202a39ae.png)

* Forget gate : 어떤 정보를 잃어버릴 것인지
* Input gate : 입력 값을 어떤 정보를 넣을 것인지


![image](https://user-images.githubusercontent.com/63588046/152908429-b534bca1-0720-46b1-bb6a-7dc667960ec6.png)

* Update cell : 어느 값을 더하고 없앨것인지 합침
* Output Gate : 어떤 값을 밖으로 낼 것인지 결정


![image](https://user-images.githubusercontent.com/63588046/152908552-48ca1eca-4e50-4826-81e0-64c4d012247d.png)

#### GRU
* output gate가 없음
* cell gate가 없음
* 적은 파라미터로 비슷한 역활을 함 -> general하게 됨


![image](https://user-images.githubusercontent.com/63588046/152908979-5945d089-fc65-4001-b0c5-4ac0f7a65a71.png)


## Transformer
* 재귀적 X, 한번의 모든 단어를 처리함
* Attention 사용
* sequence 데이터를 encoding하는 방식

![image](https://user-images.githubusercontent.com/63588046/152920957-17ee561d-d332-4683-ba46-8698d2ea01e7.png)


### encoder
#### self-attention
* n개의 단어가 주어지면 n개의 벡터로 바꿈, 한 벡터를 바꿀때 같이 있는 다른 n-1개의 벡터도 같이 고민
* 어떤 단어와 어떤 단어가 관계가 있는지 파악 Ex. animal didn't cross the street because it was to tired => animal=it
* Queries, Keys Values 벡터를 만듬 => Score 벡터 생성
* Score 벡터 : encoding 하고자 하는 단어(queries 벡터)와 나머지 n개와의 key 벡터와 내적(이 단어가 나머지 단어와 얼마나 유사한지 파악)
* attention weight : score 벡터 normalization 한 것을 softmax에 넣은 값
* 최종 벡터(encoding vector) : attention weight * value 벡터 의 총합   
* 입력에 따라 출력이 고정되는 것이 아니라 입력 주변의 값에 의해 값이 바뀜(flexible)  => 더 많은 것을 표현 가능


![image](https://user-images.githubusercontent.com/63588046/152923993-a1e1693d-fe5e-49ea-a4b6-0fa60cef7114.png)

#### fead-forwafd : 1개의 벡터로 전달
![image](https://user-images.githubusercontent.com/63588046/152921268-80da2936-97e4-44f8-b45d-11041ddc6c18.png)


#### Multi-headed attention
* attention으로 embedded된 값 n개 만듬


#### 이후
* 차원을 원래처럼 줄임
* positional encoding : 특정한 값을 더함
* decoder를 가지고 단어를 생성, masking 사용
* masking : 이전 데이터에만 depending하게 만듬(미래 정보 사용 안하도록)
* 
