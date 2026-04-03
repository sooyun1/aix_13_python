#회원관리
names = ['홍','김','박']  # 혹은 name_list
print(names[0])
print(names[1:2]) # 김
print(names[1:]) # 김, 박
n = names[1:] # 복사본이 만들어짐
names[1] = '이'
print(names)
print(names[1:][1]) # [이, 박]에서 [1] -> 박 (중첩 조건)
print(n[0]) # '이'로 바뀌기 전 '김'이 나옴

arr = [ [1,2,3],[4,5,6] ]
print(arr[0]) # [1,2,3] (<- 0번째 리스트니까)
print(arr[1]) # [4,5,6]
print(arr[0][0]) # 1

a = [10,20,30]
b = [40,50,60]
print(a+b)
print(a*3)
print(f"  홍길동의 길이={len("홍길동")}  ")
print(len(a+b))
print(len(a*3))