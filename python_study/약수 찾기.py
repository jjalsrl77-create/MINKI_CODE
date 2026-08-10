def find_divisors(number):
    divisors = []

    for k in range(1, number+1):
        if number % k == 0:
            divisors.append(k)

    return divisors

number = int(input("숫자를 입력하세요: "))

result = find_divisors(number)

print(f"약수 목록: {result}")
print(f"약수 개수: {len(result)}")