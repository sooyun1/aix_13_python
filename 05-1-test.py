# 인삿말 함수
def hello():
    print("안녕하세요")
hello()

# def hello_3times():
#     print("안녕하세요")
#     print("안녕하세요")
#     print("안녕하세요")

# hello_3times()

# def hello_ntimes(msg="안녕하세요", n=1):
#     for i in range(n):
#         print(msg)
# hello_ntimes()

def hello_ntimes(n=1, msg="안녕하세요"):
    for i in range(n):
        print(msg)

hello_ntimes()
# hello_ntimes("방가방가",3) # 안 넘겨지면 n=1

# gugudan(3) -> 3단 구구단 출력
# gugudan() -> 2단 구구단 출력

def dan(n=2, n2=None):
    if n2 == None:
        for i in range(1,10):
            print(f"{n}*{i}={n*i}")
    else:
        for j in range(n,n2+1):
            for i in range(1,10):
                print(f"{j}*{i}={j*i}")
dan(2,5)

# def dan(n=2):
#      for i in range(1,10):
#          print(f"{n}*{i}={n*i}")
# dan()

# def dan(n=2):
#     for i in range(1,10):
#         while n<6:
#             print(f"{n}*{i}={n*i}")
