def is_perfect(number):
    divisor_sum = 0

    for k in range(1, number):
        if number % k == 0:
            divisor_sum += k

    return divisor_sum == number


number = int(input("숫자를 입력하세요: "))

result = is_perfect(number)

if result:
    print("완전수입니다.")
else:
    print("완전수가 아닙니다.")