# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

## 웹에서  표준통신으로 주고받는데 활용됨. json이라고 하는 것과 같음.


# 딕셔너리 자료형(순서X, 중복X, 수정O, 삭제O)

#key, Value (json) -> MongoDB

# 선언
a = {'name': 'Kim', 'phone': '01012345678', 'birth': '870124'}
b = {0: 'Hello python!'}  ### 숫자로하는 것은 많이 활용되지는 않는다. 
c = {'arr': [1, 2, 3, 4]}

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)

# 출력
print('a - ', a['name'])  # 존재X -> 에러 발생  'name1' 에러 발생
print('a - ', a.get('name'))  # 존재하지 않으면 나오지 않아서 -> None 처리된다. 
print('b - ', b[0])
print('b - ', b.get(0))
print('c - ', c['arr'])
print('c - ', c['arr'][3]) #벨류 값이 리스트이기 때문에 반환됨. 
print('c - ', c.get('arr'))

# 딕셔너리 추가
a['address'] = 'seoul'  ###어드레스라는 키에 서울이라는 벨류를 가짐. 순서가 없어서 마음대로 저장됨
print('a - ', a)
a['rank'] = [1, 2, 3]
a['rank2'] = (1, 2, 3,) ###튜플, 리스트 어떤 형태도 저장 가능하다. 
print('a - ', a)

# dict_keys, dict_values, dict_items : 반복문(iterate) 사용 가능
### item은 한 쌍을 뜻함. 
print('a - ', a.keys())  ## 키만 리스트형태로 가져옴. 생긴거는 리스트처럼 생겼는데, 
### list(a.keys())  -- > 키 값만 가져와서 리스트형식으로 저장해야 사용가능. 
print('b - ', b.keys())
print('c - ', c.keys())

print('a - ', list(a.keys()))
print('b - ', list(b.keys()))
print('c - ', list(c.keys()))

print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())

print('a - ', list(a.values()))
print('b - ', list(b.values()))
print('c - ', list(c.values()))
## values 값을 list 값으로 저장할 수 있음. 
## 딕셔너리 안에 벨류값을 반복하면서 불러올 수도 있다. 

print('a - ', a.items())  #전체를 가지게 되어있음.
print('b - ', b.items())
print('c - ', c.items())

print('a - ', list(a.items()))
print('b - ', list(b.items()))
print('c - ', list(c.items()))
### 리스트 안에 튜플이 있는 형태로 변환 가능. 

print('a - ', 'name' in a)  ### 키가 'name'인게 a에 있니?
print('a - ', 'addr' in a)

 

# 집합(Sets) 자료형(순서X, 중복X) ##추가 삭제 가능한데 함수를 이용해서.

### 수치 계산, 과학 연산. 내부적으로 된 오픈 소스인 경우에 많이 쓰임.

# 선언
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)

# 튜플 변환
t = tuple(b)
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])

# 리스트 변환
l = list(c)
print('l - ', type(l), l)
print('l - ', l[0], l[1:3])

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('l - ', s1 & s2)  ### and기호 교집합
print('l - ', s1.intersection(s2)) ### 교집합. 

print('l - ', s1 | s2)   ##합집합. 
print('l - ', s1.union(s2))

print('l - ', s1 - s2)  ## 차집합. 
print('l - ', s1.difference(s2))

# 추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5)  #### 순서가 없기 때문에 내부적으로 추가됨. 
### 중복이 없기 때문에 추가됨 
print('s1 - ', s1)

s1.remove(2)  ### 값을 지울 수 있음.
print('s1 - ', s1)
