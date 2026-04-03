print(range(3))
print(list(range(3)))
# print(list(range(1,46)))
# print(list(range(1,46,5)))
print(list(range(5,1,-1))) # 거꾸로
# 3단 구구단
# 3*1=3
# 3*2=6
# dan=3
# # for i in range(1,10):
    # print(f'{dan}*{i}={dan*i}')

# 구구단
# 2*1=2
# ...
# 3*1=3
# ...
# 9*1=9

# for i in range(2,10):
#     for j in range(1,10):
#          print(f'{i}*{j}={i*j}') # 실제에선 반복할 일이 없음(경우:게임)

i = 0
while i<3: # i가 3보다 작은 동안 반복 실행
    print(f'i={i}')
    i +=1 # 생략하면 무한 반복하게 됨 Crtl=c로 종료
print(f'while end i={i}')
print('end')

i = 0
while i<10: # 0~9
    print(f'i={i}')
    i +=1
    if i == 2: # 2에서 멈추니까 출력X
        break # 쓸 일이 없음 (+반복문인 for문에서도 사용)

ns = [5,15,6,20,7,25]
for n in ns:
    if n<10:
        continue 
    print(n)