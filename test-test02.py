#1-1
import datetime

now = datetime.datetime.now()

talk = input("입력: ")
if "안녕" in talk:
    print("안녕하세요.")
elif "안녕" in talk:
    print("안녕하세요")
elif "시" in talk:
    print(f"지금은 {now.hour}시입니다.")
else:
    print(f"{talk}")

#1-2
num = int(input("점수를 입력해주세요: "))

for a in [2,3,4,5]:
    if num % a == 0:
        print(f"{a}로 나누어 떨어니는 숫자입니다.")
    else:
        print(f"{a}로 나누어 떨어지는 숫자가 아닙니다.")

#2-1
#1) [0,1,2,3,4,5,6,7,0,1,2,3,4,5,6,7], [0,1,2,3,4,5,6,7,10],
#   [0,1,2,0,3,4,5,6,7], [0,1,2,4,5,6,7], [0,1,2,4,5,6,7], []
# 2) number > 100:
# 3)
for num in numbers:
    if num % 2 == 0:
        print(f"{num}는 짝수입니다.")
    else:
        print(f"{num}는 홀수입니다.")

for num in numbers:
    if num // 1 >= 100:
        print(f"{num}는 3 자릿수입니다.")
    elif num // 1 >- 10:
        print(f"{num}는 2 자릿수입니다.")
    else:
        print(f"{num}는 1 자릿수입니다.")

# 4) (number + 2) % 3
# 5) (i*2)+1

numbers = [1,2,3,4,5,6,7,8,9]

for i in range(0, len(numbers) // 2):
    j = (i*2)+1
    print(f"i = {i}, j = {j}")
    numbers[i] = numbers[j] ** 2

print(numbers)