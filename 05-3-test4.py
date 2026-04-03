def power(item):
    return item*item

list1 = [1,2,3]
r1 = map( power, list1 )
# print(type(r1)) # map타입
# print(r1)
list2 = '10,20,30'.split(',')
print(list2) # 문자
list3 = [ int(i) for i in list2 ] # 리스트 내포를 이용하여 문자 -> 숫자로 변환
print(list3) # 숫자

def to_int(c):
    return int(c)
r2 = map(to_int, list2)
print(list(r2))

# 짝수만 추출
list4 = [ i for i in list1 if i%2==0 ]
# =
# list4 = []
# for i in list1:
#     if i%2==0"
#         list4.append(i)
def only_even(i):
    return i%2==0

list4 = filter(only_even, list1) #even=짝, odd=홀
print(type(list4))
print(list(list4))

# 회원이름
names = '홍길동,김길동,박길동'.split(',')
# 김씨만 추출
def only_kim(n):
    return n[0] == '김' #0번째가 '김'일 경우, 참
    # =return '김' in names
kims = filter(only_kim, names)
print(list(kims))

# power = lambda x: x*x
# print(power(3))
print(list(map(lambda x: x*x, [1,3,5])))