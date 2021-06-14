# Section06
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def function_name(parameter):
#     code

# 함수 호출
# function_name()
# 함수 선언 위치 중요

##함수 입력만/ 출력만 하는 경우도 있다. 
##아규먼트와 크와그스 형태로 받는 것. *args, **Kwargs

##중복되는 형태를 쉽게 하기 위해서. 
##함수를 하나만 구현하고, 하나를 하기 위해서. 
##하나의 기능의 함수를 하나만 만드는 것이 중요하다. 

#문자를 보내는 기능이다.
#선언하는 윗부분에 해야 한다. 
# return이 있는 함수 
# return은 값을 반환해주는 함수
## 함수를 반환할 때는 함수이름만 
## return function
#새롭게 저장됨. 
#return을 통해서 함수를 호출하고 값을 리턴함.

## 파라미터=(매게 변수) 값을 넣는다고 해서 파라미터 값만 나오는 것이 아니라,
## 파라미터와 관련된 다른 변수값을 반환할 때, return이 쓰인다. 


# 예제1
def hello(world):
    print("Hello, ", world)


param1 = "Niceman"

hello(param1)


# 예제2
def hello_return(world):
    value = "Hello, " + str(world)
    return value


str = hello_return("Niceman")

print(str)


# 예제3(다중리턴)

def func_mul1(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return y1, y2, y3


val1, val2, val3 = func_mul1(3)

print(val1, val2, val3)


# 튜플 리턴
def func_mul2(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return (y1, y2, y3)


tup = func_mul2(4)

print(type(tup), tup, list(tup))


# 리스트 리턴
def func_mul2(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return [y1, y2, y3]


lis = func_mul2(6)

print(type(lis), lis, set(lis))


# 딕셔너리 리턴
def func_mul3(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return {'ret1': y1, 'ret2': y2, 'ret3': y3}


dic = func_mul3(8)

print(type(dic), dic, dic.get('ret3'), dic.items(), dic.keys(), dic.values())


## 함수 여러가지로 리턴할 수 있다. 

# 예제4 
# *args, **kwargs 이해

# *args [아규에스]
##########매개변수가 몇 개가 넘어갈지 모를 때, 넘어오는 거에 따라서 함수가 다르게 작동할 때,
#######
def args_func(*args):  # 매개변수명 자유롭게 변경 가능
    for i, v in enumerate(args):
        print('{}'.format(i), v, end=' ')

#### i는 인덱스 v는 값 
#### 튜플 형태니까. 
###enumerate??? 인덱스를 붙여주는 것.튜플의 인덱스를 보여줌. 

args_func('Kim')
args_func('Kim', 'Park')
args_func('Kim', 'Park', 'Lee')

print()


# kwargs [키워드]
# **kwargs 딕셔너리로 받음

def kwargs_func1(**kwargs):
    print(kwargs)

kwargs_func1(name1="kim")


def kwargs_func(**kwargs):  # 매개변수명 자유롭게 변경 가능
    for v in kwargs.keys():
        print('{}'.format(v), kwargs[v], end=' ')
## 키 와 벨류를 하나하나 다 출력함. 
## 이자체가 딕셔너리인 건가? 

kwargs_func(name1='Kim')
kwargs_func(name1='Kim', name2='Park')
kwargs_func(name1='Kim', name2='Park', name3='Lee')

print()

def kwargs_func2(**kwargs):
    for k , v in kwargs.items():
        print(k,v)

#### *args  [아스타아그스] --> 유연하게 튜플로 받음
#### *kwargs  ---> 딕셔너리를 넘길 수 있음


# 전체 혼합
### arg_1, arg_2는 필수적
### *args, **kwargs는 가변적으로 있든 없든 출력 가능. 
def example(arg_1, arg_2, *args, **kwargs):
    print(arg_1, arg_2, args, kwargs)


example(10, 20, 'park', 'kim', 'lee', age1=33, age2=34, age3=44)


# 예제5
# 중첩함수(클로저) ---> 모든 언어에 다 있음.

## 함수 안에 함수가 있는 것이다. 

def nested_func(num):
    def func_in_func(num):
        print(num)

    print("In func")
    func_in_func(num + 100)
###함수 선언과 실행순서를 중첩함수에서 잘 봐야한다. 
###변수의 선언 줄이고, 메모리 관련 효율적으로 가능. 
## 데코레이터. 

nested_func(1)


# 실행불가
# func_in_func(1)


# 예제6
# Hint    힌트를 입력할 수 있다. word는 문자형이고, num은 int인데 -> 결과는 인트형이된다는 것. 
def tot_length1(word: str, num: int) -> int:
    return len(word) * num


print('hint exam1 : ', tot_length1("i love you", 10))


def tot_length2(word: str, num: int) -> None:
    print('hint exam2 : ', len(word) * num)


tot_length2("niceman", 10)


# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화

# 일반 함수. 

# 예제7
# def mul_10(num:int) -> int :
#     return num * 10

# 이 경우 함수는 객체라서 리소스와 메모리를 할당하게 되고, 람다는 즉시 실행해서 메모리, 감소 (heap할당)
# var_func(10)

# def mul_10_one(num): return num * 10
#
# lambda x: x * 10
#게시판 데이터를 데량으로 가져와서 날짜 바꾸기, 형태소분석하면 람다식이 유리할 듯. 

# 일반적 함수 -> 변수 할당
def mul_10(num):
    return num * 10


mul_func = mul_10

print(mul_func(5))
print(mul_func(6))

# 람다 함수 -> 할당
lambda_mul_func = lambda x: x * 10


def func_final(x, y, func):
    print(x * y * func(10))

    ## 함수도 할당 가능. 

func_final(10, 10, lambda_mul_func)

print(func_final(10, 10, lambda x : x *1000))