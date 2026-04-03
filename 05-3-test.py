t1 = (1,3,5)
print(t1)
print(t1[1])
# t1[1] = 4 # Error 튜플은 새로운 값으로 저장(변경) 불가능
            #TypeError: 'tuple' object does not support item assignment 아이템 수정 지원X

t2 = [3]
print(type(t2)) # list
t2 = (3,) # 하나만 있는 튜플 객체는 콤마를 찍어줘야 함 (그래서 오류가 발생X)
print(type(t2)) # tuple

# 학생들의 점수를 입력받아 총점과 평균을 계산

def calc_total_avg(*values):
    total = 0
    avg = 0
    total = sum(values)
    avg = total / len(values)
    return total, avg # (total,avg), 소괄호가 자동으로 붙음 => ans

# t, a = calc_total_avg(10,30,50)
# print('total',t) # total
# print('avg',a) # 평균

a, b = 10, 20
print(a,b)
a,b = b,a # 쓸 일 없음
print(a,b)

print(calc_total_avg) # 메모리 위치값(주소)가 나옴

def print_func(fn): # 전달 받음
    fn(); fn(); fn() # 실행 *3
def hello():
    print("HELLO")
print_func(hello) # => fn으로 전달 (FrameWork을 만들 때 활용)