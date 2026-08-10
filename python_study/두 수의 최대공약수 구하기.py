def find_gcd(a, b):
    result = 1

    for k in range(1, min(a, b) + 1):
        if a % k == 0 and b % k == 0:
            result = k

    return result


a = int(input("첫 번째 숫자: "))
b = int(input("두 번째 숫자: "))

result = find_gcd(a, b)

print(f"최대공약수: {result}")