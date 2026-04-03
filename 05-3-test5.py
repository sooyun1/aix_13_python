# file = open("basic.txt","a")
# # file.write("\n") #줄바꿈
# file.write("헬로 파이썬 프로그래밍 4")
# input('엔터키 누르세요')
# file.close()
# print('end')

with open("basic.txt","a") as file:
    file.write("\n") #줄바꿈
    file.write("헬로 파이썬 프로그래밍 4")
    # file.writelines()
print('end')

