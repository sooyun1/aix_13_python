
for a in [1,3,5]:
    print(a)
print("END")
# 로또번호 생성 및 저장
mylotto = []
import random
for a in [1,2,3,4,5,6,7,8,9,10]:
    r = random.randint(1,45)
    if r not in mylotto: # 생성된 난수가 로또에 없으면 저장
        mylotto.append(r)
    if len(mylotto) == 6: # 중복된 숫자를 제외하면서 6자리를 채우면
        break # 멈춤
mylotto.sort() # 들여쓰기 취소해서 정렬 6번 할 것을 한 번으로 축소, -> 속도가 빠름
print('mylotto=', mylotto)