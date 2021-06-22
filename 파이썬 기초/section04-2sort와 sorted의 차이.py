str_1 ="asdflkjhasldkjfhasldkfjahsdfkj"

sorted(str_1) #c= sorted(str_1)  print(c)  같다.   print(sorted(str_1))

## sort와 달리, 저장하라는 명령이 아니라서 따로 저장해줘야함.

print(str_1)        ### 야는 그냥 나왔네. ## 저장하라는 명령이 아니라,  

print(sorted(str_1))  #----> 야는 리스트인데, 


str_2 = [1,4,5,2,7,8,1,5,7,4]

print(str_2.sort())  ### sort의 경우 이렇게 출력이 안 됨. 
                    ### 함수의 경우 순서대로 저장하라는 명령. 출력은 none이 됨. 그러니까, 출력값을 가지고 있지 않고, 저장하는 역할만 한다는 거지.
print("type str_2 :", type(str_2.sort()))  ### 논타입이기 때문에 출력이 안 됨.
print("list str_2", list(sorted(str_2)))  ##이런 식으로 해야 한다.
                    ## str_2.sort()   print(str_2) 이렇게 해야 출력됨
                    ##한번에 출력하려면 리스트로 형변환을 해주어어함.
str_4 = "안녕하세요" #문자열에 sort함수가 쓰이는가? 
# str_3.sort()  #문자열에는 쓰이지 못함.
# print(str_3)

str_2.insert(1, 9)

print(str_2)