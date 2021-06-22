a = list([1,2,3,4])

b= [1,2,3,4]

c = [1,2,3]
c[1:2] = ['a', 'b', 'c']  ###!!! 1부터 2사잉의 구간에 'a', 'b', 'c'가 추가됨.
print('c - ', c)
c[1] = 1
print('c - ', c)

print("a :", a)

print("b :", b)

f =[5,4,3,2,1,8,4]

f.sort()

print(f)


e = [10, 100, ['Pen12312', [1,2,3,4,5], 'Cap', 'Plate']] 
print('e - ', e[-1][1][4])


str_1 ="asdflkjhasldkjfhasldkfjahsdfkj"

sorted(str_1)

print(str_1)        ### 야는 그냥 나왔네. 

print(sorted(str_1))  #----> 야는 리스트인데, 

str_2 = [1,4,5,2,7,8,1,5,7,4,2,2,2]

str_2[:1] = [1234]
print("\"---------------\"", str_2)

str_2.remove(2)

print(str_2)

print(str_2.count(2))  ## 2가 몇 개인지 새기 

str_9 = [1,2,3,3,4,5,2,2,2,2,2]
print(str_9.index(2)) 
