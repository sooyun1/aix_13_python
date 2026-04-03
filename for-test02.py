# 로또번호 생성 방법 2
nums = list(range(1,46)) # 1~45 ///range는 46 포함X
# print('nums',nums)
mylotto = [] #로또 번호 저장용
for a in [1,2,3,4,5,6]:
    import random
    r = random.randint(0,len(nums)-1) # ///randint는 마지막 숫자까지 포함을 하기 때문에 -1을 해줘야 함
    mylotto.append(nums[r]) # 지워질 녀석 (내 로또번호가 될 녀석)
    nums.pop(r) # 저장한 번호를 리스트에서 삭제 (-> 중복선택 불가)
mylotto.sort() # 들여쓰기 하게 되면 정렬을 ㅈㄴ 많이 함 -> 시간이 많이 듦
print('mylotto', mylotto)
