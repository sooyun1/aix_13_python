ans = input("나이를 입력하세요> ")
print(f"/{ans}/") # 슬래시: 값의 시작과 끝을 알기 위해서 (빈 공백이라는 뜻)
ans = ans.strip() # 공백 글자 삭제
if ans : # 공백이면 flase
    # print(f"입력값은 {ans}")
    pass
else:
    print("입력안함")