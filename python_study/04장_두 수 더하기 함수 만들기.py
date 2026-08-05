def add(a, b):
    result = a + b
    return result

num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))

result = add(num1, num2)
print(f"{num1} + {num2} = {result}")