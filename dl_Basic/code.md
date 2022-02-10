#### initial 주는법
```` python
    def __init__(self,name='mlp',xdim=784,hdim=256,ydim=10):
        super(MultiLayerPerceptronClass,self).__init__()
        self.name = name
        ~~~
        self.lin_1 = nn.Linear(self.xdim,self.hdim)
        self.lin_2 = nn.Linear(self.hdim,self.ydim)
        self.init_param()                             # 파리미터 초기화!!!! self.init_param()
        
    def init_param(self):                             # init_param()   
        for m in self.modules():
            if isinstance(m,nn.Conv2d):               # 만약 conv2d라면
                nn.init.kaiming_normal_(m.weight)     # kaming_normal로 초기화를 하고 
                nn.init.zeros_(m.bias)                # bias는 0으로 준다
            elif isinstance(m,nn.BatchNorm2d): # init BN
                nn.init.constant_(m.weight,1)
                nn.init.constant_(m.bias,0)
            elif isinstance(m,nn.Linear): # lnit dense
                nn.init.kaiming_normal_(m.weight)
                nn.init.zeros_(m.bias)

    def forward(self,x):
        ~~~~~

````

#### 모델 평가하기
=> train 할때 진행 정도 출력할려고 사용
```` python
def func_eval(model,data_iter,device):
    with torch.no_grad():                                   # 반드시!!! torch.no_grad() 넣기
        model.eval()
        n_total,n_correct = 0,0
        for batch_in,batch_out in data_iter:
            y_trgt = batch_out.to(device)
            model_pred = model(batch_in.view(-1,28*28).to(device))
            _,y_pred = torch.max(model_pred.data,1)
            n_correct += (y_pred==y_trgt).sum().item()      # .item()은 텐서값을 스칼라 값으로 바꿔준다.
            n_total += batch_in.size(0)
        val_accr = (n_correct/n_total)
        model.train() # back to train mode 
    return val_accr
print ("Done")
````

#### train 하는 도중에 그래프 그리기
```` python

    # Plot
    if ((it%PLOT_EVERY)==0) or (it==0) or (it==(MAX_ITER-1)):
        with torch.no_grad():
            y_sgd_numpy = model_sgd.forward(x_torch).cpu().detach().numpy()           # SGD 적용 모델 
            y_momentum_numpy = model_momentum.forward(x_torch).cpu().detach().numpy() # momentum 적용 모델
            y_adam_numpy = model_adam.forward(x_torch).cpu().detach().numpy()         # adam 적용 모델
            
            #그림 그리기
            plt.figure(figsize=(8,4))
            plt.plot(x_numpy,y_numpy,'r.',ms=4,label='GT')
            plt.plot(x_numpy,y_sgd_numpy,'g.',ms=2,label='SGD')                       # SGD 그려라
            plt.plot(x_numpy,y_momentum_numpy,'b.',ms=2,label='Momentum')
            plt.plot(x_numpy,y_adam_numpy,'k.',ms=2,label='ADAM')
            plt.title("[%d/%d]"%(it,MAX_ITER),fontsize=15)
            plt.legend(labelcolor='linecolor',loc='upper right',fontsize=15)
            plt.show()
````

#### Attention code 보자
![image](https://user-images.githubusercontent.com/63588046/153346468-ec0b4c83-eca5-4652-916e-adb008637a54.png)

```` python
class ScaledDotProductAttention(nn.Module):
    def forward(self,Q,K,V,mask=None):
        d_K = K.size()[-1] # key dimension
        scores = Q.matmul(K.transpose(-2,-1))//np.sqrt(d_K)       # batch size, channel 수, w, h 구조임 => 맨 뒤 2개로 행렬곱 할거임
        if mask is not None:
            scores = scores.masked_fill(mask==0, -1e9)
        attention = F.softmax(scores,dim=-1)
        out = attention.matmul(V)
        return out,attention
````








