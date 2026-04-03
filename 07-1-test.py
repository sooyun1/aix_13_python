# # 수학 연산 모듈
# from math import pi
# print(pi)

# # 모듈 이름이 너무 길어서 다른 걸로 바꾸는 게 as
# import math as m
# print(m.pi)


# import random
# # print(random.choice([1,2,3,4,5])) #랜덤하게 선택
# print(random.shuffle([1,2,3,4,5])) #섞어줌
# a = [1,2,3,4,5]
# random.shuffle(a)
# print(a)

# # 랜덤하게 2개 선택
# print(random.sample([1,2,3,4,5], k=2)) 

# # 시스템 모듈
# import sys
# print(sys.getwindowsversion())

# # 운영체체
# import os
# print(os.name)
# dir = os.listdir() #존재하는 모듈 이름들
# for d in dir:
#     print(d)

# # 시간
# import time
# print('지금부터 3초 정지합니다')
# time.sleep(3)
# print('END')

# # 웹주소
from urllib import request
target = request.urlopen("https://www.naver.com/")
output = target.read()
print(output)

# 날씨 정보 가져오기
