# 머신러닝, 딥러닝에 활용 X
# 구구단 출력 - 3단
# 3 * 1 = 3
# 3 * 2 = 6
dan = 3
print( "{} * {} = {}".format(dan,1,dan*1) ) # 중괄호 안에 들어갈 것들 -> 포맷(순서대로)
print( "{} * {:5d} = {}".format(dan,1,dan*1) )
print( "{} * {:05d} = {}".format(dan,1,dan*1) )

print("헬로 python 프로그래밍".upper()) # 한영이 섞여도 영문만

# strip() - 웹 개발에 많이 씀!!
a = """
     헬로 파이썬 프로그래밍         
"""
print(a.strip()+"/") # (가끔 공백 처리해주는 시스템도 존재)
print("안녕123".isalnum()) # True (공백 들어가면 false)
print("abc abc programming".find("bc")) # 1 (1에 있음)
print("abc abc programming".find("bc",2)) # 5 (5에 있음)
print("abc abc programming".find("bc",6)) # -1 = 없다는 뜻
a = "안녕하세요"
print( "안녕" in a) # T
print( "잘자" in a) # F

b = "홍,김,박,강".split(",")
print(b)
b = "100,200,300,200".split(",") # split은 숫자를 문자로 바꿔줌
print(b)
print(int(b[0]) + int(b[1])) # int를 각각 붙여줘야 숫자로서 계산 가능
print(b[0]+b[1]) # 문자인 형태로 그대로 더하면 합쳐질 뿐
print(int(b[0]+b[1])) # 이것도 마찬가지
# b의 합과 평균
total = 0
mean = 0
total = int(b[0]) + int(b[1]) + int(b[2]) + int(b[3])
# ㄴ위에 문자가 됐기 때문에 int로 숫자로 일일이 바꿔줘야됨
print ("total{}=".format(total))
print("Average={}".format(total/4))
print("total="+str(total))

print(f"total={total}") # 중괄호 안에는 변수 이름을
print(f"평균={total/4}") # 숫자, 문자 상관 없음

# 구구단 3단
dan = 3
print(f"{dan} * {1} = {dan*1}")
print(f"{dan} * {2} = {dan*2}")
print(f"{dan} * {3} = {dan*3}")

# 생년을 입력받아 나이를 계산해서 출력하기
year = input("태어난 해 4자리를 입력하세요")
age = 2026 - int(year)
print(f"당신은 {age}살 입니다")
# = print("당신은 "+str(age)+"살 입니다")
