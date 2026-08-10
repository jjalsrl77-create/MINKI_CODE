class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("잔액이 부족합니다.")
        else:
            self.balance -= amount
            print(f"{amount}원이 출금되었습니다.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount}원이 입금되었습니다.")
        else:
            print("입금액은 0보다 커야 합니다.")

    def show_balance(self):
        print(f"{self.owner}님의 잔액: {self.balance}원")


account = BankAccount("민수", 10000)

account.deposit(5000)
account.withdraw(3000)
account.show_balance()