def find_common_divisors(a, b):
    divisors = []
    for k in range(1, min(a, b) + 1):
        if a % k == 0 and b % k == 0:
            divisors.append(k)

    return divisors

a = int(input("첫 번째 숫자: "))
b = int(input("두 번째 숫자: "))

result = find_common_divisors(a, b)

print(f"공약수 목록: {result}")
print(f"공약수 개수: {len(result)}")