# def print_n_times(n,*values): # values에 몇개를 쓰든 ok, 하지만 앞으로 오면 안 됨
#     for i in range(n):
#         for value in values:
#             print(value)
#         print()
# print_n_times(3, '안녕','즐거운','파이썬 프로그래밍')

# def print_n_times(*values,n=1): # 기본값을 주면 ok
#     for i in range(n):
#         for value in values:
#             print(value)
#         print()
#     return # 함수의 실행을 막고 호출할 것으로 넘어감
# ans = print_n_times('안녕','즐거운','파이썬 프로그래밍', n=3) # n=n을 부여하면 n만큼 반복 실행
#                                     # n=n은 키워드 매개변수, 제자리(맨 뒤)에만 있어야 함
# print('ans',ans) # 값의 이름을 똑같이 입력하도록 버릇

# greeting(이름) -> 출력: 안녕하세요 이름님 (자료와 함께 리턴하기 286p)
# def greeting(name):
#     return "안녕하세요 "+name+"님"

# ans = greeting("홍길동") # -> 안녕하세요 홍길동님
# print(ans)

# 입력받은 숫자들의 평균을 반환하는 함수
# def calc_avg(*v):
#     tot = 0
#     for i in v:
#         tot += i
#     return tot /len(v)

# ans = calc_avg(10,20,40,50)
# print(ans)

# 점수를 입력받아 학점을 반환하는 함수
# """
# 90 이상 -> A
# 80 이상 -> B
# 70 이상 -> C
# 나머지 -> F
# """
# def get_grade(*v):
#     if v>=90: return"A"
#     if v>=80: return"B"
#     if v>=70: return"C"
#     return

# print(get_grade(70))

#가위바위보 중 하나는 임의로 반환하는 함수
#이름 get_gbb()

    # op = ["가위","바위","보"]
    # return random.choice(op)

def get_gbb():
    import random
    r = random.randint(0,2)
    arr = '가위,바위,보'.split(',')
    return arr[r]

ans = get_gbb()
print(ans)

# 팩토리얼
def fac(n):
    if n==0:
        return 1
    return n * fac(n-1)

ans = fac(4)
print('fac(4)=',ans)