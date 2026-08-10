class VendingMachine:
    def __init__(self, product_name, price, stock):
        self.product_name = product_name
        self.price = price
        self.stock = stock
        self.money = 0

    def insert_money(self, amount):
        if amount <= 0:
            print("올바른 금액을 넣어주세요.")
        else:
            self.money += amount
            print(f"{amount}원이 투입되었습니다.")

    def buy(self):
        if self.stock == 0:
            print("상품이 품절되었습니다.")
        elif self.money < self.price:
            print("금액이 부족합니다.")
        else:
            self.money -= self.price
            self.stock -= 1
            print(f"{self.product_name} 구매가 완료되었습니다.")

    def restock(self, amount):
        if amount <= 0:
            print("올바른 수량을 입력하세요.")
        else:
            self.stock += amount
            print(f"{self.product_name} {amount}개가 입고되었습니다.")

    def show_info(self):
        print(f"상품명: {self.product_name}")
        print(f"가격: {self.price}원")
        print(f"재고: {self.stock}개")
        print(f"잔액: {self.money}원")


machine = VendingMachine("콜라", 1500, 2)

machine.insert_money(1000)
machine.buy()

machine.insert_money(1000)
machine.buy()

machine.restock(3)
machine.show_info()