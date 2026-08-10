class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def sell(self, amount):
        
        if amount > self.quantity:
            print("재고가 부족합니다.")
        elif amount <= 0:
            print("올바른 수량을 입력하세요.")
        else:
            self.quantity -= amount

    def restock(self, amount):
        self.quantity += amount

    def show_info(self):
        print(f"상품명: {self.name}, 가격: {self.price}, 재고: {self.quantity}")

product = Product("사과", 1500, 10)

product.sell(3)
product.show_info()

product.sell(20)
product.restock(5)
product.show_info()