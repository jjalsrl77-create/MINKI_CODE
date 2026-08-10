class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        item = {
            "name": name,
            "price": price
        }

        self.items.append(item)
        print(f"{name}가 추가되었습니다.")

    def remove_item(self, name):
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                print(f"{name}가 삭제되었습니다.")
                return

        print("상품을 찾을 수 없습니다.")

    def get_total(self):
        total = 0

        for item in self.items:
            total += item["price"]

        return total

    def show_items(self):
        for item in self.items:
            print(f"{item['name']}: {item['price']}원")


cart = ShoppingCart()

cart.add_item("키보드", 50000)
cart.add_item("마우스", 30000)
cart.add_item("USB", 10000)

cart.remove_item("마우스")
cart.show_items()

print(f"총금액: {cart.get_total()}원")