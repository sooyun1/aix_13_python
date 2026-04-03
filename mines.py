# 지뢰찾기(빨리 터트리기)
# 10x10 영역에 3개의 지뢰를 매설
# 최소의 시도로 모두 터트리기
# 실력대로 해보기 (초급(5x5-2),중급(7x7-4),고급(10x10-6))
# 레벨을 선택하세요
# 1 - 초급(5x5) 지뢰 2개
# 2 - 중급(7x7) 지뢰 4개
# 3 - 고급10x10) 지뢰 6개
# 선택 레벨>> 

import random

# 레벨 선택 추가
print("레벨을 선택하세요(숫자만 입력하시오)")
print("1 - 초급(5x5) 지뢰 2개")
print("2 - 중급(7x7) 지뢰 4개")
print("3 - 고급10x10) 지뢰 6개")

level = int(input("선택 레벨>> "))

if level == 1:
    n = 5
    target_mines = 2
elif level ==2:
    n =7
    target_mines = 4
elif level == 3:
    n = 10
    target_mines = 6
else:
    print("기본값(초급)으로 설정됩니다.")
    n = 5
    target_mines = 2


mines = [] # 출력용

for i in range(n):
    mines.append(['+']*n)

nums = [] # 계산용
for i in range(n):
    nums.append([0]*n)

# 임의의 지점에 지뢰 저장(3개 배치)
mine_count = 0
while mine_count < target_mines:
    # import random
    row = random.randint(0,n-1)
    col = random.randint(0,n-1)
    if nums[row][col] >= 9: continue #폭탄이 같은 자리에 배치될 경우를 배제하기 위해
    mine_count += 1 #배치된 폭탄 갯수 1증가
    nums[row][col] = 9

    # 이웃한 8개 방의 숫자를 1증가
    '''
    r-1 c-1  / r-1 / r-1 c+1
      c-1   /  9  /   c+1
    r+1 c-1/ r+1 / r+1 c+1
    '''
    if row != 0 and col !=0 : nums[row-1][col-1] += 1
    if row != 0 : nums[row-1][col] += 1
    if row != 0 and col != n-1 : nums[row-1][col+1] += 1
    if col != 0 : nums[row][col+1] += 1
    if row != n-1 and col != n-1 : nums[row+1][col+1] += 1
    if row != n-1 : nums[row+1][col] += 1
    if row != n-1 and col != 0 : nums[row+1][col-1] += 1
    if col != 0 : nums[row][col-1] += 1

# 확인
# for n in nums:
#     print(n)
'''
지뢰의 좌표를 입력하세요(0~9,0~9) x,y>> 
...
게임종료.
총 시도 횟수 30회
'''
remain_mine = mine_count #남은 폭탄 갯수
while remain_mine != 0:
    msg = f'지뢰의 좌표를 입력하세요(0~{n-1},0~{n-1}) x,y>> '
    while True:
        ans = input(msg)
        try:
            u_row, u_col = ans.split(',')
            u_row, u_col = int(u_row), int(u_col)

            #범위 체크
            if not (0 <= u_row < n and 0 <= u_col <n):
                print("잘못된 입력입니다. 다시 입력해주세요.")
                continue
            break
        except:
            print("잘못된 입력입니다. 다시 입력해주세요")
    # ans = input(msg)
    # u_row, u_col = ans.split(',')
    # u_row, u_col = int(u_row), int(u_col)
    if nums[u_row][u_col] >= 9: #지뢰를 찾으면
        mines[u_row][u_col]="$"
        remain_mine -= 1 #남은 폭탄 수 1감소
    else:
        mines[u_row][u_col]=str(nums[u_row][u_col])
    
    # 남은 지뢰 출력 추가
    print(f"남은 지뢰 개수: {remain_mine}")

    # mines 리스트 출력
    for m in mines:
        print(" ".join(m))