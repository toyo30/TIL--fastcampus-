# Section09
# 파일 읽기, 쓰기

# 읽기 모드 r, 쓰기 모드(기존 파일 삭제) w, 추가 모드(파일 생성 또는 추가) a
# 기타 : https://docs.python.org/3.7/library/functions.html#open
# 상대 경로('../', './'), 절대 경로 확인('C:\...')

# 파일 읽기
# 예제1
f = open('./resource')
contents = f.read()
print(contents)
# print(dir(f))
# 반드시 close 리소스 반환
f.close()

print()

# 예제2
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(iter(c))
    print(list(c))
    print(c)

print()

# read : 전체 내용 읽기, read(10) : 10글자 읽기

# 예제3
with open('./resource/review.txt', 'r') as f:
    for c in f:
        # print(c)
        print(c.strip())

print()

# 예제4
with open('./resource/review.txt', 'r') as f:
    contents = f.read()
    print('>', contents)
    contents = f.read()
    print('>', contents)  # 내용 없음 다 읽어났기 때문에 
    f.seek(0, 0)
    contents = f.read()
    print('>', contents)

# readline : 한 줄씩 읽기, readline(문자수) : 문자수 읽기

print()

# 예제5
with open('./resource/review.txt', 'r') as f:
    line = f.readline()  ## 한줄 한줄 읽기 
    while line:
        print(line, end='')
        line = f.readline()

# readlines : 전체 읽은 후 라인 단위 리스트 저장

print()
print()

# 예제6
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()
    print(contents)
    print()
    for c in contents:
        print(c, end='')

print()
print()

# 예제7
score = []
with open('./resource/score.txt', 'r') as f:
    
    for line in f:##라인별로 가져오기. 
        score.append(int(line))##라인을 가져와서 
    print(score)##리스트 형식으로 저장되어있는지를 확인. 
    print('Average : {:6.3f}'.format(sum(score) / len(score)))

## sum 리스트에 있는 거 더하기. 
# 파일 쓰기

# 예제1
with open('./resource/test.txt', 'w') as f:
    f.write('niceman!')

# 예제2
with open('./resource/test.txt', 'a') as f:
    f.write('niceman!!')

# 예제3
from random import randint

with open('./resource/score2.txt', 'w') as f:
    for cnt in range(6):##다섯자리 쓰기. 
        f.write(str(randint(50, 100)))##렌덤으로 정수 생산하기. 
        f.write('\n')

# 예제4
# writelines : 리스트 -> 파일로 저장
with open('./resource/test2.txt', 'w') as f:
    list = ['Kim\n', 'Park\n', 'Lee\n']
    f.writelines(list)

# 예제5
with open('./resource/test3.txt', 'w') as f:
    print('Test Contents!', file=f)
    print('Test Contents!!', file=f)
