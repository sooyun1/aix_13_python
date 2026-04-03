age = 3

def p():
    global age #함수 밖에 있는 age를 불러옵니다
    age = 5
    print('age', age)
p()
print('age2', age)