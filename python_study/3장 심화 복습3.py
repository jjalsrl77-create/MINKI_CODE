answer = 7

while True:
    num = int(input("숫자를 입력하세요: "))

    if num == answer:
        print("정답입니다!")
        break

    elif num > answer:
        print("더 작은 수를 입력하세요")

    else:
        print("더 큰 수를 입력하세요.")