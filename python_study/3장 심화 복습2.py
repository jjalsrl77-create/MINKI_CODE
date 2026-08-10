password = "python123"

for attempt in range(3):
    user_input = input("비밀번호를 입력하세요: ")
    if password == user_input:
        print("로그인 성공")
        break

    else:
        print("비밀번호가 틀렸습니다.")
else:
    print("로그인 기회를 모두 사용했습니다.")