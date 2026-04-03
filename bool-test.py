print( 10 == 100 ) # 둘은 같냐 물어보는 기호
# print ( 10 = 100 ) # 둘은 다름, 오른쪽에 있는 값을 왼쪽 변수에 넣은 =, 근데 변수는 숫자가 되면 안 됨
print( 10 != 100) # !는 not이라는 뜻, 한마디로 다르냐
print(10 <= 100 ) # True
print( 10 >= 100 ) # False 
a = "가방"
b = "하마" 
print ( a == b )
print ( a < b ) # True (단어는 순서를 물어봄, True)
print ( a > b ) # False
c = 35
print( 10 < c < 30 ) # True
print( 10 < c < 20 ) # False

if not c < 30:
    print("c는 30보다 작음") # False가 나오면 실행이 안 됨
    print("c는 30보다 작음")
else:
    print("c는 30보다 큼")
    print("c는 30보다 큼") # 들여쓰기가 다르면 오류
print("END")

score = 68
grade = "" # 비워둠
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"{score}의 학점은 {grade}")

score = 88
if score <= 100 and score >= 90:
    grade = "A"
elif score <= 89 and score >= 80:
    grade = "B"
else:
    grade = "F"
print(f"{score}의 학점은 {grade}")
