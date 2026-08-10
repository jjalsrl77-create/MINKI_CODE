def reverse_number(number):
    reversed_number = 0

    while number > 0:
        last_digit = number % 10
        reversed_number = reversed_number * 10 + last_digit
        number = number // 10

    return reversed_number


number = int(input("숫자를 입력하세요: "))

result = reverse_number(number)

print(f"뒤집은 숫자: {result}")