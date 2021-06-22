# Section04-2
# 파이썬 데이터 타입(자료형)
# 문자열, 문자열 연산, 슬라이싱
# 문자열 중요성(가장 많은 분야에서 사용)

# 문자열 생성
str1 = "I am Boy."  #공백도 한글자로 친다. 빈문자열도 한 개다. 
str2 = 'NiceMan'
str3 = """How are you?"""
str4 = '''Thank you!'''
str5 = str()
# 문자열 출력
print(type(str1))
print(type(str2))
print(type(str3))
print(type(str4))
print("문자랑 같이 쓰기.  {} --------------".format(len(str5))) 
print(3 + len(str(5))) #문자 + 문자 가능. 정수 + 정수 가능.
print('안녕', len(str(5)))  #더하지는 못하지만 같이 쓰기 가능. 

# 문자열 길이
print(len(str1))
print(len(str2))
print(len(str3))
print(len(str4))

# 빈 문자열
str_t1 = ''
str_t2 = str()

print(type(str_t1), len(str_t1))
print(type(str_t2), len(str_t2))

# 이스케이프 문자 사용

escape_str1 = "Do you have a \"big collection\"?"
escape_str2 = 'What\'s on TV?'
escape_str3 = "What's on TV?"
escape_str4 = 'This is a "book".'

# 출력1
print(escape_str1)
print(escape_str2)
print(escape_str3)
print(escape_str4)

# 탭, 줄바꿈
t_s1 = "Tab \tClick!"
t_s2 = "New Line\n Start!!"

# 출력2
print(t_s1)
print(t_s2)

# Raw String  ##?????? 있는 그대로 표현해주는 것이다. 소문자 r과 쌍따옴표가 중요. 
raw_s1 = r'C:\Programs\python3\"'
raw_s2 = r"\\a\b\c\d"
raw_s3 = r'\'"'
raw_s4 = r"\"'"

raw_s1 = r"c:\Programs\Test\Bin"


print(raw_s1)
# Raw String 출력
print(raw_s1)
print(raw_s2)
print(raw_s3)
print(raw_s4)

####!!!익스케이프 기호를 써줘야 뛰어쓰기 한대로 출력됨. 안 되면 뛰어쓰기 한채로 에러가 남. 
# 파이썬은 뛰어쓰기 잘해줘야 함 
multi_str1 = \
    """
    문자열
    멀티라인
    테스트
    """
# 멀티라인 출력
print(multi_str1)

#또 멀티라인을 사용해서 밖으로 출력할 수도 있다. 
multi_str2 = \
    '''
    문자열 멀티라인 
    역슬래시(\) \
    테스트
    '''
# 멀티라인(역슬래시) 출력
print(multi_str2)

# 문자열 연산  #문자열을 더하고 뺄 수 있음. 
str_o1 = "Niceman"
str_o2 = "Orange"
str_o3 = "this is string example....wow!!! this is really string"
str_o4 = "Kim Lee Park Joo"

print(3 * str_o1)
print(str_o1 + str_o2)
print(dir(str_o1)) #???? 이건 뭐지??  모듈에서 정의하는 이름들을 확인하기 위해 사용됩니다. 등록되어있는 모든 이름들을 리스트로 반환해주는 파이썬의 
#내장함수라고 할 수 있다. 

#문자열 * int 는 가능하나 문자열 +정수형은 안 됨. 
# print(str_o1 +3)
print('x' in str_o1)  #문자열은 인유테이블이라고 할당해서 입력하면 수정이 불가능하지만 순회불가능함. #한번 할당이되면 수정이 불가능하다. 순회가 가능하다.
print('i' in str_o1) #순회가 가능하다. 문자가 있는지 없는지 확인할 수 있다. 
print('e' not in str_o2)
print('O' not in str_o2)

# 문자열 형 변환
print(str(77))  # type 확인
print(str(10.4))  ##!!!!문자열로 형변환이 됨.
print(str(True))
print(str(complex(12)))
print(str(10.4) + 'a---------') #문자 더하기 문자가능.  

# 문자열 함수   #####문자열을 처리할 수 있는 많은 함수가 있기 때문에 언어활용이 용이하다. 
# 참고 : https://www.w3schools.com/python/python_ref_string.asp
print("Capitalize: ", str_o1.capitalize()) #첫글자가 대문자로바꿔줌. 
# print("Capitalize: ", str_o1.iscapitalize())#대문자입니까? ---> 불린형이니까 문자형이랑 같이 쓸 수 있음.
print(str_o1.isupper()) ###----> 대문자입니까?
print("sominja:", str_o2.lower()) #소문자하기. 
print("sominja:", str_o2.islower())##소문자입니까?
print("endswith?: ", str_o2.endswith("s")) #끝자가 s로 끝나니? 
print("join str: ", str_o1.join(["I'm ", "!"])) #리스트를 문자열로 변환해주는데 앞에 있는 문자열을 사이에 넣어줌. 
print("replace1: ", str_o1.replace('Nice', 'Good'))  ##특정부분을 찾아서 원하는 부분으로 바꿔줌.
print("replace2: ", str_o3.replace("is", "was", 3)) ##특정 부분 3번만 하기. 
print("split: ", str_o4.split(' '))  # Type 확인 뛰어쓰기 단위로 때어서 리스트값으로 변환 
print("sorted:----------- ", sorted(str_o1))  # reverse=True      ###대문자, 소문자 순서대로 출력
##### a.sort()  ----> 리스트를 순서대로 다시 저장하는 함수를 의미한다. 
print("reversed1: ", reversed(str_o2)) #list 형 변환  안되 있음. 함수는 이러한 리스트를 출력해주세요라고 형변환을 해줘야함.
print("reversed2: ", list(reversed(str_o2))) #리스트로 형변환 해버리기. 



####문자열이 한번 할당되면 반환불가능하다고 한 이유 
#niceman 이라는 단어의 위치정보가 0부터시작. 6끝. -1부터 시작. 
###숫자가 정해져있기 때문에 한번 선언하면 수정 불가능하다. 이뮤테이블이라고함. 
###파이썬에서 중요한 문법이다. 수정가능한 자료형 수정 불가능한 자료형. 

# immutable 설명  
im_str = "Good Boy!"

print(dir(im_str))  # __iter__ 확인
# 출력
for i in im_str:
    print(i)

# im_str[0] = "T"  # 수정 불가(immutable)

# 슬라이싱(인덱싱)
# 일부분 추출(정말 중요)
str_sl = 'Niceboy'

# 슬라이싱 연습    ####마지막에 있는 거 이전에 있는 거까지 나온다. 
print(str_sl[0:3])    
print(str_sl[:len(str_sl)])   ###문자가 길어지면 이렇게 쓰는게 낫다. 직접 세지 않아도 쉽게 출력 가능하다. 훨씬.
print(str_sl[:len(str_sl) - 1])
print(str_sl[:])  #처음부터 끝까지임. 
print(str_sl[1:4:2]) ## 1부터 4까지 나오는데, 2개씩 건너뛰는 것. 인덱싱을 가지고 슬라이싱을 한다는 거임.
print(str_sl[-3:6])
print(str_sl[1:-2]) ##1부터 거꾸로  -2 한거까지 나옴
print(str_sl[::-1])##처음주터 끝까지인데 거꾸로 역순으로. 리버스했던 것처럼 출력가능.
print(str_sl[::2])  #처음부터 끝까지인데 2개씩 건너뛰기. 

# immutable 삭제
del str_sl

# 아스키코드
a = 't'

print(ord(a))   ###아스키 코드 번호
print(chr(116))
