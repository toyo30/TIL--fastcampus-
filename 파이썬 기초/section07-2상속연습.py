# Section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

##부모가 주는 것. 
## 파이썬은 다중 상속 가능. 

# 예제1
# 상속 기본
# 슈퍼클래스(부모클래스) 및 서브클래스(자식클래스) -> 모든 속성, 메소드 사용 가능

#상속을 통해서 코딩을 하면, 코드를 재사용할 수 있고, 중복되는 코드를 최소화할 수 있다. 

# 라면 -> 속성(종류, 회사, 맛, 면 종류, 이름) : 부모 클래스 생성가능. 

# 공통으로 쓸 수 있는 것들 물려받아서 사용. 

# 부모 클래스에서 상속받아서 사용하면, 서브클래스에서 코드를 재사용할 수 있다. 

class Car:
    """Parent Class"""
    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        return 'Car class method!'

##자동차 클래스를 상속받는 것 -> Car의 속성과 메서드를 사용할 수 있다.
class BmwCar(Car):
    "Sub class"
    def __init__(self, car_name, tp, color):
        super().__init__(tp,color)##부모한테 자식속성넘겨주기.
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name :; %s" %self.car_name


class BenzCar(Car):
    "Sub class"
    def __init__(self, car_name, tp, color):
        super().__init__(tp,color)##부모한테 자식속성넘겨주기.
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name :; %s" %self.car_name

    def show(self):
        print(super().show())
        return 'Car Info %s %s %s'%(self.car_name, self.type, self.color)

##일반 사용

model1 = BmwCar("520d", 'sedan', 'red')

print(model1.color) #super에서 가져온 것이다. 
print(model1.type) #부모클래스에서 가져온 것.
print(model1.car_name)

print("------", model1.show()) ##super 클래스에 구현이 되어있는 메서드임. 

##여러 클래스들이 한 매서드를 공유하여 코드의 중복을 피하고, Car클래스를 상속받아서 사용할 수 있다. 

print(model1.show_model()) #자식 클래스에서 구현 한 것. 

##부모와 자식 모든 매서드와 속성에 접근가능하다. 

print(model1.__dict__) ##자식과 부모에서 다 가져왔음.

# Method Oveerriding(오버라이딩)

#올라타다. 자식의 새로운 기능으로 덮어쓰는 것을 의미함. 

model2= BenzCar("220d", "suv", "black")

print(model2.show()) ##부모 클래스에 있는 걸 사용하되, 내 입맛에 맛게 사용. 

#parent Method Call
#super().show 
#를 통해서 부모클래스의 것에서도 접근 가능. 
model3 =BenzCar("356s", "sedan", 'sliver')
print(model3.show())

# Inheritance info 
#상속관계를 보여주는 매서드

print(BmwCar.mro())##object 모든 클래스의 부모
print(BenzCar.mro()) ##상속 정보를 리스트 형식으로 출력해주는 것 

#예제2
#다중 상속

class X(object):#모든 클래스는 오브젝트를 상속받는다. 
    pass
class Y():
    pass
class Z:
    pass
class A(X,Y):
    pass
class B(Y,Z):
    pass
class M(B,A,Z):
    pass
print(M.mro())

print(A.mro())
#너무 복잡한 다중 상속은 코드를 복잡하게 할 수도 있다. 2-3개 정도 중요. 
