names = [] # 빈 리스트
scores = [] # 빈 리스트
names.append('홍')
scores.append(80)
names.append('김')
scores.append(90)
print(names)
print(scores)
# del names[1] # 김 삭제
# names.pop(1) # 동일
names.remove('김') # 동일
print(names)

scores.clear()
print('scores=',scores)

arr = [30,50,70,60]
# arr.sort() # 오름차순 정렬
arr.sort(reverse=True) # 내림차순 정렬
print(arr)
