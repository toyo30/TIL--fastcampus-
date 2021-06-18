import random
import time

import winsound
import sqlite3
import datetime

# DB생성 

conn =sqlite3.connect()
words =[]



n =1 #게임 시도횟수
cor_cnt = 0 #정답 개수 

with open('/Users/baegmingi/python_basic/파이썬 기초/resource/word.txt', 'r', encoding="UTF-8") as f:
    for c in f:
        words.append(c.strip())


input('Are you ready? Press Enter Key!')

start = time.time()

while n <=5:
    random.shuffle(words)
    q = random.choice(words)

    print()

    print("*Question #{}".format(n))
    print(q) #문제 출력

    x = input() #타이핑 입력

    print()

    if str(q).strip() ==str(x).strip():
        print("pass!")
        cor_cnt +=1
    else:
        print("Wrong!")
    
    n +=1

end = time.time()
et = end - start
et = format(et, ".3f")

if cor_cnt >=3:
    print("합격")
else:
    print("불합격")

print("게입 시간:", et, "초", "정답 개수 : {}".format(cor_cnt))

#시작 지점 코드 'main'에서 실행될 경우에만 
if __name__ =='__main__':
    pass