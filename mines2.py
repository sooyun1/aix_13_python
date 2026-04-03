#지뢰찾기(빨리 터트리기)
# 10x10 영역에 3개의 지뢰를 매설
# 최소의 시도로 모두 터트리기

def read_level():
    msg ='''
#  레벨을 선택하세요
#  1 - 초급(5x5) 지뢰 2개
#  2 - 중급(7x7) 지뢰 4개
#  3 - 고급(10x10) 지뢰 6개
#  선택 레벨>> '''

    while True:
        try:
            ans = input(msg)
            level = int(ans)
        except:
            print("레벨을 선택하세요(1~3)")
        else:
            if not level in [1,2,3]: continue
            break
    return level

level = read_level()

sizes = [0,5,7,10]
size = sizes[level] # 필드크기
mine_counts = [0,2,4,6]
find_mine_count = mine_counts[level] # 지뢰갯수


mines = [] #출력용
for i in range(size): #행 갯수
    mines.append(['+']*size)  #열의갯수
nums = [] #계산용
for i in range(size):
    nums.append([0]*size)

# 임의의 지점에 지뢰 저장(3개)
mine_count = 0
while mine_count < find_mine_count:
    import random
    row = random.randint(0,size-1)
    col = random.randint(0,size-1)

    #폭탄이 같은 자리인 경우 배치취소
    if nums[row][col] >= 9: continue
    mine_count += 1 #배치폭탄 갯수 1 증가
    nums[row][col]=9

    # 이웃한 8개 방의 숫자를 1증가
    if row != 0 and col !=0 : nums[row-1][col-1] += 1
    if row != 0  : nums[row-1][col] += 1
    if row != 0 and col != size-1 : nums[row-1][col+1] += 1
    if col != size-1 : nums[row][col+1] += 1
    if row != size-1 and col != size-1 : nums[row+1][col+1] += 1
    if row != size-1  : nums[row+1][col] += 1
    if row != size-1 and col != 0 : nums[row+1][col-1] += 1
    if col != 0 : nums[row][col-1] += 1
# 확인
# for n in nums:
#     print( n )
remain_mine = mine_count #남은 폭탄갯수
while remain_mine != 0:

    while True:
        try:
            msg=f'지뢰의 좌표를 입력하세요(0~{size-1},0~{size-1})  x,y>> '
            ans = input(msg)
            u_row, u_col = ans.split(',')
            u_row, u_col = int(u_row), int(u_col)
        except:
            print('좌표오류입니다. 다시 입력')
        else:
            # 좌표범위체크
            if u_row not in range(size) : 
                print('잘못된 행 범위입니다. 다시 입력')
                continue
            if u_col not in range(size) : 
                print('잘못된 열 범위입니다. 다시 입력')
                continue
            #  if not (0 <= u_row < size and 0 <= u_col <size):
            #     print("잘못된 입력입니다. 다시 입력해주세요.")
            #     continue
            break

    if nums[u_row][u_col] >= 9: #지뢰 찾으면
        mines[u_row][u_col]="$"
        remain_mine -= 1 #남은 폭탄수 1감소
    else:
        mines[u_row][u_col]=str(nums[u_row][u_col])

    # 남은 지뢰 출력 추가
    print(f"남은 지뢰 개수: {remain_mine}")

    # mines 리스트 출력
    header = 'X '+' '.join([str(i) for i in list(range(size))])
    print(header)
    rcnt = 0 #행번호
    for m in mines:
        print(str(rcnt)+' '+" ".join(m))
        rcnt += 1