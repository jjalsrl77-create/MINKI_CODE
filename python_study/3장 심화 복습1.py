number = int(input("숫자를 입력하세요: "))

if number > 100:
    print("큰 수입니다.")

elif 1 <= number <= 100:
    print("범위 안의 수입니다.")

elif number == 0:
    print("0입니다.")

else:
    print("음수입니다.")