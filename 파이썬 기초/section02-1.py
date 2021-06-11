# 기본출력

print("""asdfkjadfsjhklj""")
print('''안녕안녕안녕하세요''')


print()


###separator 옵션사용

print('T', 'E', 's', sep='')
print('2019','02','03', '04', sep='-')
print('niceman', 'google.com', sep='@')

#프린트문 안에서 어떻게 관계되어서 출력될 것인지. 

##end 옵션 사용
print('Welcome To', end=' ')
print('the black parade', end=' ')
print('piano notes')
#print문 끝에 추가하기 원래는 뛰어서 나오는데 붙여지고, end 안에 있는 걸 뒤에 붙여서 출력됨


#format 사용
print('{} and {}'.format('you', 'me'))
print("{0} or {1} and {0}".format('you','me'))
print("{a} are {b}".format(a='you', b='me'))

#%s: 문자, #%d: 정수, %f: 실수  더 정확함 문자와 정수를 정확하게 알려주기 때문에
print("%s's favorite number is %d"%('안녕', 7)) 

# %5d 정수 5자리, %4.2f 정수 4자리, 소수 2자리
print("test1: %5d, price:%4.2f"%(776, 6534.123))#3째자리가 나오고, 2째자리까지만, 나옴
print("Test1:{0:5d}, price:{1:4.2f}".format(776, 6534.123)) #중가로로 묶어놓으면 %를 안 해도 된다.
print("test1:{a:5d}, price: {b:4.2f}".format(a=776, b=6534.123))



#escape code

print("'you'")
print('\'\'')
print('"you"')
