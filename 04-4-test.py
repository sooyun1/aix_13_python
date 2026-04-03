a = [5,1,3]
# print(min(a))
# print(max(a))
# print(sum(a))
# print('avg=',sum(a)/len(a)) # 평균값
# a.sort() # 정렬
# print('sorted',a)
# # a.reverse()
# r = reversed(a) #Iter(반복)ator 반환
# for v in r: # r안에는 next()가 들어있음
#     print(list(str(v)))

# a = [1,3,5]
# b = [i*10 for i in a]
# print(b)


# 짝수만 추출
a = [i for i in range(10) if i%2==0]
print(a)

a = list("12345") #[]
print("-".join(a)) # 유용하게 사용

# a = ['1','2','3']
# a = [1,2,3] # 타입이 달라서 오류 발생 TypeError
# a = [ str(n) for n in a ] # str = string = 문자, 숫자열을 문자열로 변환
# print("-".join(a))

# 짝수 홀수 변환
# a = range(5)
# # [ 참일때값 if 조건식 else 거짓일때값 for 변수 in 자료구조 ]
# b = [ '짝' if n%2==0 else '홀' 
#             for n in a ]
# print(b)