## 기본적인 backward 구조

* 파라미터를 사용할 일 거의 X
* backward와 optimizer 자동 오버라이딩
* forward는 $ hat{y} $ 를 구하는게 목표
* backward는 미분
* optimizer.step은 업데이트

## 기본적인 data 불러오기
* Data : 데이터
* Dataset : 데이터 어떻게 시작할건지, 크기가 얼마인지, 어떤방식으로 반환할건지(map-style)
* transforms : 데이터 전처리 (ToTensor(), CenterCrop())
* DataLoaer : index를 가지고 데이터를 묶어서 전달 (batch, suffle)

              GPU 직전에 데이터 변환을 함



<pre><code>class A:
  def ~~:
    ~~~
  def forward(self,~:
    ~~~
    
model=A(input,output)
if torch.cuda.is_available():
  model.cuda

# 파라미터
  ~~~

criterion = ~~    #loss 함수용
optimizer = ~~

# backward

for epoch in range(epochs):
    if torch.cuda.is_available():
        inputs = Variable(torch.from_numpy(x_train).cuda())
        labels = Variable(torch.from_numpy(y_train).cuda())
    else:
        inputs = Variable(torch.from_numpy(x_train))
        labels = Variable(torch.from_numpy(y_train))
        
  optimizer.zero_grad()
  outputs=model(inputs)
  loss=criterion(output,labels)
  loss.backward()
  optimizer.step()

</code></pre>


## 모델 예측
<pre><code>with torch.no_grad():  # 모델 예측할때는 기울기 업데이트 X
    if torch.cuda.is_available():
        predicted = model(Variable(torch.from_numpy(x_train).cuda())).cpu().data.numpy()
    else:
        predicted = model(Variable(torch.from_numpy(x_train))).data.numpy()
    print(predicted)
</pre></code>

## 결과에서 파라미터 확인
<pre><code>for p in model.parameters():
    if p.requires_grad:
         print(p.name, p.data)
</pre></code>

## Dataset 클래스 => HuggingFace로 표준화된 라이브러리 사용 가능
<pre><code>class A_Dataset(Dataset):
    def __init__(self,labels,~):
      self.labels=labels
      self.~
    def __len__(self):
      return len(self.labels)
    def __getitem(self,idx):
      label=self.labels[idx]
      ~~~
      return ~
</pre></code>

## DataLoader
DataLoader(Dataset, batch_size= ,shuffle=True ~)

sampler : 어떻게 데이터를 뽑을 것인가

collate_fn : [[data,label],[data,label],,,,[data,label]] -> [data,data,data,,,,],[label,label,,,]로 변환
