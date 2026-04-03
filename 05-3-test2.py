'''
숫자맞추기게임(UpDown)
1~100사이 임의의 숫자를 컴퓨터가 정한 것을
스무고개형식으로 맞추는 게임
출력예시)
1~100사이 숫자 입력>> 70
낮춰주세요
1~100사이 숫자 입력>> 60
높여주세요
1~100사이 숫자 입력>> 65
정답입니다
'''
# print("### 숫자맞추기게임 v0.2 ###")
# #1~100사이 임의의 정수를 저장
# import random
# com = random.randint(1,100)
# count = 0
# while True:
#     count += 1
#     user = input(f"{count}번째 시도 - 1~100사이 숫자>> ")
#     user = int(user) 
#     # 판정
#     if com == user:
#         break 
#     if com < user:
#         print("낮춰주세요")
#     else:
#         print("높여주세요")
# print("정답입니다")

# +++++++
# import random

# print("### 숫자맞추기게임 v0.2 ###")
# com = random.randint(1,100)
# count = 0

# while num < 10:
#     num +=  1
#     user = int(input(f"{num}번째 시도 - 1~100사이 숫자>> "))
#     if com == user:
#         break 
#     print("낮춰주세요" if com < user else "높여주세요")
# print(f"정답은{com}입니다. 정답 입력 횟수 {num}")


# print("### 숫자맞추기게임 v0.3 ###")
# import random
# com = random.randint(1,100)
# count = 0

# while True:
#     count +=  1
#     user = int(input(f"{count}번째 시도 - 1~100사이 숫자>> "))

#     if com == user:
#         print("정답입니다")
#         break 
    
#     print("낮춰주세요" if com < user else "높여주세요")
        
#     if count >= 6:
#         print ("당신은 바보입니까? "+f"정답은{com}입니다")
#         break


print("### 숫자맞추기게임 v0.4 ###")
import random
com, count, low, high = random.randint(1,100), 0, 1, 100  #후보숫자 최저/최고값

while True:
    count +=  1
    print(f"후보숫자>> {low} ~ {high}")
    user = int(input(f"{count}번째 시도 - 1~100사이 숫자>> "))

    if com == user:
        print("정답입니다"); break 
    
    print("낮춰주세요" if com < user else "높여주세요")
    low, high = (low, user-1) if com < user else (user+1, high)

    if count >= 6:
        print("당신은 바보입니까? "+f"정답은 {com}입니다")
        break
