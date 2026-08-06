class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        if self.balance >= money:
            self.balance -= money

        else:
            return "올바른 값을 입력해주세요."

    def show_balance(self):
        print(f"예금주: {self.owner}, 현재 잔액: {self.balance}")

result = BankAccount("민수", 100000)

result.deposit(50000)
result.withdraw(70000)

result.show_balance()