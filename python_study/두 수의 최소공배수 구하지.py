def find_lcm(a, b):
    candidate = max(a, b)

    while True:
        if candidate % a == 0 and candidate % b == 0:
            return candidate

        candidate += 1


a = int(input("첫 번째 숫자: "))
b = int(input("두 번째 숫자: "))

result = find_lcm(a, b)

print(f"최소공배수: {result}")