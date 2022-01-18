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
