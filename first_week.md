## <파이썬 코드>
-------------

* 테스트 해 볼때

<pre><code>def function(값):
  ...
   return 정답 

import unittest
class Test(unittest.TestCase):
   def do_test(self):
     random_number_list = [테스트 해볼 숫자들]
     pred = function(random_number_list)
     self.assertEqual(pred, 정답)
        
tbm = Test()
tbm.do_test()       <= 만약 테스트 해볼 숫자와 정답이 다르면 오류가 뜸

</code></pre>

* CMD 사용법

파일 만들기 : mkdir 파일명
경로 변경   : cd 경로
현재 위치 파일 : dir

dir ..\이전폴더에 있는 파일 -> 이전 폴더에 있는 파일로 이동 가능
(..은 현재 바로 직전에 있는 폴더를 의미)




* 행렬 코드
<pre><code>np.inner(A,B) : 행렬의 내적
np.linalg.inv(X) : 역행렬
np.linalg.pinv(X) : psedo-inverse
</code></pre>

* 미분 코드
<pre><code>import sympy as sym
from sympy.abc import x,y   -> x,y는 변수로 입력됨
sym.diff(sym.poly(x**2+2*x*y+3),x)   ->  다변수 함수를 x로 편미분함
</code></pre>

* 경사하강법 코드
<pre><code>input :norm(norm값 구하는 코드), gradient(기울기 구하는 함수), init(초기 위치), lr, eps 
Output : var

var=init
grad=gradient(var)
while(norm(grad)>eps):
  var=var-lr*grad
  grad=gradient(var)
</code></pre>  

* 선형회귀 경사하강법 
<pre><code>for t in range(T):
  error=y-X@beta
  grad=-transpose(X)@error
  beta=beta-lr*grad
</code></pre>

SoftMax 코드
<pre><code>def softmax(vec):
  denumerator = np.exp(vec-np.max(vec,axis=-1,keepdims=True)  --> 실제 식과 다르게 max(vec)을 빼는 이유는 너무 큰 값이 나오면 학습이 overflow가 발생할 수 있어서
  numerator=np.sum(ducumerator, axis=-1, keepdims=True)
  return denmerator/numerator
</code></pre>

## <수학>
-------------
* 행렬

![image](https://user-images.githubusercontent.com/63588046/149851781-065a0ca0-c514-4afb-b4e6-4f8d6412b95d.png)

![image](https://user-images.githubusercontent.com/63588046/149852171-8e835976-649c-4663-8ad1-71bab87114c7.png)

위 식을 사용하면 증명 가능 (기억하자!!)


* 확률적 경사하강법 (SGD)

![image](https://user-images.githubusercontent.com/63588046/149854382-425bd18d-ed58-4aed-a523-e6523e73d483.png)

일부 데이터의 t+1번째 상태는 loss함수의 grad 값을 뺀다.  일부 데이터들의 grad의 평균은 전체 데이터의 grad와 거의 수렴한다.
데이터 중에서 한개 또는 일부 활용하여업데이트
여러개의 지점에서 경사하강법을 사용하므로 local minimum에 빠지지 않을 확률이 높음
^ : hat 으로 벡터라는 의미를 가짐

L2 norm 표시 : ||y-XB||~2~

softmax(o) = (exp(o1)/시그마(exp(o_i),exp(o2)/시그마(exp(o_i),,,,)
softmax는 모델을 분류할 때 사용한다.
