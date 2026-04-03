import random

# 스트라이크 / 볼 계산
def check_guess(secret, guess):
    strike = sum(secret[i] == guess[i] for i in range(4))
    ball = sum((g in secret) and (g != secret[i]) for i, g in enumerate(guess))
    return strike, ball

# 사용자 입력 처리
def get_user_guess():
    while True:
        user_input = input("4자리 숫자 입력(중복 없이)>> ")
        if len(user_input) != 4 or not user_input.isdigit():
            print("⚠ 4자리 숫자를 입력하세요.")
            continue
        guess = [int(x) for x in user_input]
        if len(set(guess)) != 4:
            print("⚠ 중복된 숫자는 안됩니다.")
            continue
        return guess

# 컴퓨터 숫자 생성
def generate_number():
    return random.sample(range(10), 4)

# 게임 시작
def play_game():
    secret_number = generate_number()
    turn = 1
    print("🎮 숫자야구 게임 시작! 4자리 숫자를 맞춰보세요.")

    while True:
        print(f"\n--- {turn} 턴 ---")
        user_guess = get_user_guess()
        s, b = check_guess(secret_number, user_guess)
        print(f"👉 결과: {s}S {b}B")
        if s == 4:
            print("🎉 정답입니다! 승리!")
            print(f"컴퓨터 숫자: {''.join(map(str, secret_number))}")
            break
        turn += 1

play_game()