class InsufficientBalanceError(Exception):
    pass


def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("출금액은 0보다 커야 합니다.")

    if amount > balance:
        raise InsufficientBalanceError("잔액이 부족합니다.")

    return balance - amount


balance = 10000

try:
    amount = int(input("출금액: "))
    remaining_balance = withdraw(balance, amount)

except ValueError as error:
    print(error)

except InsufficientBalanceError as error:
    print(error)

else:
    print(f"출금액: {amount}원")
    print(f"남은 잔액: {remaining_balance}원")