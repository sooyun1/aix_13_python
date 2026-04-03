# ans = input("이름은? ")
# print(ans)
year = input("태어난해를 4자리로 입력")
age = 2026 - int(year) # 숫자 - 문자이기 때문에 타입을 바꿔줌 (+int) 소수점은 float
print("당신은 "+year+"년에 태어났습니다")
print("당신의 나이는 "+str(age))