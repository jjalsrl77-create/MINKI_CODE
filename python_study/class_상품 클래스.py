class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, quantity):
        if quantity > self.stock:
            print("재고가 부족합니다.")
        else:
            self.stock -= quantity
            print(f"{self.name} {quantity}개가 판매되었습니다.")

    def restock(self, quantity):
        self.stock += quantity
        print(f"{self.name} {quantity}개가 입고되었습니다.")

    def show_info(self):
        print(f"상품명: {self.name}")
        print(f"가격: {self.price}원")
        print(f"재고: {self.stock}개")


product = Product("키보드", 50000, 10)

product.sell(3)
product.restock(5)
product.show_info()