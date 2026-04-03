# try:
#     list1 = [10,20,30]
#     n = list1[3]
#     print(n)
# except:
#     pass
#     # print('!오류발생!')
# print('end')


# num = ["44","22","55","스파이","11"]

# number = []
# for i in num:
#     try:
#         float(i)
#         number.append(i)
#     except:
#         pass

# print("{}내부에 있는 숫자는".format(num))
# print("{}입니다.".format(number))

# try:
#     number = int(input('정수 입력> '))
# except:
#     print('정수를 입력하지 않았습니다.')
# else:
#     print('원의 반지름:', number)
#     print('원의 둘레:',2*3.14*number)
#     print('원의 넓이:',3.14*number*number)
# finally:
#     print('end')

try:
    list1 = [10,20,30]
    n = list1[3]
    print(n)
except Exception as ex:
    print('!오류발생!')
    print('TYPE',type(ex))
    print('ex',ex)

print('end')