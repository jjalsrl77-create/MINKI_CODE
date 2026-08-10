class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount}원이 입금되었습니다.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("잔액이 부족합니다.")

        else:
            self.balance -= amount
            print(f"{amount}원이 출금되었습니다.")

    def show_balance(self):
        print(f"{self.owner}님의 잔액은 {self.balance}원입니다.")

account = BankAccount("민수", 10000)

account.deposit(5000)
account.withdraw(3000)
account.show_balance()