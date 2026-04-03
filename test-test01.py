# a = input("> 1번째 숫자: ")
# b = input("> 2번째 숫자: ")
# print("{} + {} = {}".format(a,b,int(a)+int(b)))

# string = "hello"
# string.upper()
# print("A 지점:", string)

# print("B 지점:", string.upper())


# 1) 3
# 2) 1-c, 2-b, 3-a, 4-c
# 3) a,b,int(a)+int(b)
# 4) A 지점: hello B 지점: HELLO


#도전문제1
r = input("> 구의 반지름을 입력해주세요: ")
v = 4*(3.141592)*(int(r)**3)/3
print(f"구의 부피는 {v}입니다.")
s = 4*(3.141592)*(int(r)**2)
print(f"구의 겉넓이는 {s}입니다.")

#도전문제2
a = float(input("밑변의 길이를 입력해주세요: "))
b = float(input("높이의 길이를 입력해주세요: "))
c = (a**2+b**2)**(1/2)
print(f"빗변의 길이는 {c}입니다.")