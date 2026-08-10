import calculator

num1 = int(input("첫 번째 숫자 입력: "))
num2 = int(input("두 번째 숫자 입력: "))
operator = input("연산자 입력 (+, -, *, /): ")

if operator == "+":
    result = calculator.add(num1, num2)
elif operator == "-":
    result = calculator.subtract(num1, num2)
elif operator == "*":
    result = calculator.multiply(num1, num2)
elif operator == "/":
    result = calculator.divide(num1, num2)
else:
    result = "지원하지 않는 연산자입니다."

print("결과:", result)