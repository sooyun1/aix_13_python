import datetime

now = datetime.datetime.now()
print(now)
print(f"{now.year}년")
print(f"{now.month}월")
print(f"{now.day}일")
print(f"{now.hour}시")
print(f"{now.minute}분")
print(f"{now.second}초")
print(f"{now.weekday()}요일") #0부터 월요일
# f 다음 큰따옴표 다음 중괄호!

if now.hour < 12:
    print(f"현재시간 {now.hour}시로 오전입니다")
else:
    print(f"현재시간 {now.hour}시로 오후입니다")

## 167p 계절구분코드를 if...elif 로 작성
if 3 <= now.month <= 5:
    print(f"이번 달은 {now.month}월로 봄입니다!")
elif 6 <= now.month <= 8:
    print(f"이번 달은 {now.month}월로 여름입니다!")
elif 9 <= now.month <= 11:
    print(f"이번 달은 {now.month}월로 가을입니다!")
elif 12 or 1 <= now.month <= 2:
    print(f"이번 달은 {now.month}월로 겨울입니다!")

# import datetime

now = datetime.datetime.now()
if now.month <= 3:
    print(f"{now.month}월은 겨울입니다")
elif now.month <= 5:
    print(f"{now.month}월은 봄입니다")
elif now.month <= 8:
    print(f"{now.month}월은 여름입니다")
elif now.month <= 11:
    print(f"{now.month}월은 가을입니다")
else:
    print(f"{now.month}월은 겨울입니다")

### 월을 입력받아 계절 출력
month = input("월을 입력(1~12) ")
month = int(month)
if month < 3:
    print(f"{month}월은 겨울입니다")
elif month <= 5:
    print(f"{month}월은 봄입니다")
elif month <= 8:
    print(f"{month}월은 여름입니다")
elif month <= 11:
    print(f"{month}월은 가을입니다")
else:
    print(f"{month}월은 겨울입니다")

number = input("정수 입력> ")
last_character = number[-1]
if last_character in "02468":
    print("짝수입니다")
else:
    print("홀수입니다")