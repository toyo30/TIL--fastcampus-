# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
print('\n\n\n1번')

for i in q1:
    if i == "가을":
        print(i)

print(''.join([i for i in q1 if i=="가을"]))

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
print('\n\n\n2번')


if "사과" in q1.values() or "사과" in q1.keys():
    print(True)


##답지 풀이 
for key, value in q2.items():
    if key == "사과" or value =="사과":
        print("사과다!")

##요약
hasapple =[True for key, value in q2.items() if key=="사과" or value=="사과" ]

if len(hasapple)>0:
    print("사과발견")
else:
    print("사과없다.")

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

print('\n\n\n3번')

Score =90

if Score >=81 and Score <=100:
    print("A 학점")
elif Score >=61 and Score <=80:
    print("B학점")
elif Score >=41 and Score <=60:
    print("C학점")
elif Score >=21 and Score <=40:
    print("D학점")
elif Score >=0 and Score <=20:
    print("E학점")
else:
    print("올바른 성적을 입력하세요")


##답지 풀이

score = 100
grade = ''
if 0 < score > 100:
    grade = '나가'
elif score > 80:
    grade = 'A'
elif score > 60:
    grade = 'B'
elif score > 40:
    grade = 'C'
elif score > 20:
    grade = 'D'
elif score >= 0:
    grade = 'E'

print(grade)

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18

print('\n\n\n4번')
a = [12, 6, 18]

###정렬해서 마지막 수 꺼내기 
a.sort()
print(a)

if a[2] in a:
    print(a[2])

### 모든 인덱싱과 비교하기. 
for i in a:
    if i >= a[0] and i >= a[1] and i >= a[2]:
        print(i)


# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
####??? 이 경우 어떻게 선언해주어야 할까요? 

print('\n\n\n5번')

man =[1,3]
girl =[2,4]


if i == man:
    print("남자입니다.")
else:
    print("여자입니다.")

#### 나머지를 이용해서 함. 
s = '891022-2473837'
if int(s[7]) % 2 == 0:
    print('여자')
else:
    print('남자')


# 6 ~ 10 반복문 사용(while 또는 for)  ##while은 언제 사용할까요? 

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]

print('\n\n\n6번')
for i in q3:
    if i == "정":
        continue
    else:
        print(i, end="")

##리스트 컴프리핸션을 사용한 풀이. 

isjung = [i for i in q3 if i != "정"]
print(''.join(isjung))

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.

print('\n\n\n7번')
for i in range(1,101,2):
    print(i, end=' ')


for i in range(1, 101):
    if i % 2 != 0:
        print(i, end=' ')
# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]


print('\n\n\n8번')
for i in q4:
    if len(i) >=5:
        print(i)
    else:
        continue

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]

print('\n\n\n9번')

for i in q5:
    if i.islower():
        print(i)
    else:
        continue

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

print('\n\n\n10번')

for i in q6:
    if i.isupper():
        print("소문자로 변환:", i.lower())
    else:
        print("대문자로 변환:", i.upper())


#리스트 컴프리헨션

number = [i for i in range(1,101)]
print(number)