def cal(n):
    result = n * 10
    return result

try:
    num = int(input("숫자를 입력하세요: "))
    result = cal(num)
    print(f"결과: {result}")

except ValueError:
    print("숫자만 입력해주세요.")