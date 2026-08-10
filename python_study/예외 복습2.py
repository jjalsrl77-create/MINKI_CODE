def cal(n1, n2):
    result = n1 / n2
    return result

try:
    num1 = int(input("첫 번째 숫자: "))
    num2 = int(input("두 번째 숫자: "))
    result = cal(num1, num2)

    print(f"결과: {result}")


except ValueError:
    print("숫자만 입력해주세요.")

except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")