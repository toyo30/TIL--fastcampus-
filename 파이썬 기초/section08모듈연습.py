# Section08
# 파이썬 모듈과 패키지

# 패키지 예제1
# 상대 경로 패키지
# .. : 부모 디렉토리
# .  : 현재 디렉토리

##파일 하나하나가 모듈, 모듈을 모아놓은 것을 패키지라고 할 수 있다. 
## 모듈을 구조적으로 관리하는 것을 패키지라고 한다. 
#모듈 독립적으로 사용할 수 있는 것.


# 사용1(클래스)
from pkg.fibonacci import Fibonacci

Fibonacci.fib(100)
##매서드 가져와서 사용.

print("ex1 : ", Fibonacci.fib2(200))##이메서드를 가져와서 설득하기. 
print("ex1 : ", Fibonacci().title)


# 사용2(클래스)
from pkg.fibonacci import *#매모리를 많이 사용함. 여러개의 클래스를 전부다 불러옴.

Fibonacci.fib(300)

print("ex2 : ", Fibonacci.fib2(400))
print("ex2 : ", Fibonacci().title)


# 사용3(클래스)
from pkg.fibonacci import Fibonacci as fb##fb로 바구겠다. 

fb.fib(500)

print("ex3 : ", fb.fib2(600))
print("ex3 : ", fb().title)


# 사용4(함수) : 파일 Alias
import pkg.calculations as c  ## 모듈이 클래스가 아니라, 전부 함수일 때, 

print("ex4 : ", c.add(10,10))
print("ex4 : ", c.mul(10,4))


# 사용5(함수)
from pkg.calculations import div as d ##필요하는 것만 올려서 사용하기. 

print("ex5 : ", int(d(100,10)))

# 사용6
import pkg.prints as p
import builtins##기본적으로 재공하는 함수. 함수들이 모두 포함되어 있는 것을 알 수 있다. 
## 빌트인 함수 기본 함수. 

p.prt1()
p.prt2()
print(dir(p))
print(dir(builtins))
