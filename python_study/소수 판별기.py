def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True


number = int(input("숫자를 입력하세요: "))

result = is_prime(number)

if result:
    print("소수입니다.")
else:
    print("소수가 아닙니다.")