def cal(a, b):
    if b == 0:
        raise ZeroDivisionError("0으로 나눌 수 없습니다.")
    return a / b

try:
    first = float(input("첫 번째 숫자: "))
    second = float(input("두 번째 숫자: "))
    result = cal(first, second)

except ValueError:
    print("숫자를 입력하세요.")

except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")

else:
    print("결과:", result)

finally:
    print("계산을 종료합니다.")