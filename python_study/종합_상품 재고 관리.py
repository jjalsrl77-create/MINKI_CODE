import json

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def add_stock(self, quantity):
        if quantity <= 0:
            raise ValueError("입고 수량은 0보다 커야 합니다.")

        self.stock += quantity

    def sell(self, quantity):
        if quantity <= 0:
            raise ValueError("판매 수량은 0보다 커야 합니다.")

        if quantity > self.stock:
            raise ValueError("재고가 부족합니다.")

        self.stock -= quantity

    def get_value(self):
        return self.price * self.stock

    def __str__(self):
        return f"{self.name} | {self.price}원 | 재고 {self.stock}개"

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if self.find_product(product.name) is not None:
            raise ValueError("이미 존재하는 상품입니다.")

        self.products.append(product)

    def find_product(self, name):
        for product in self.products:
            if product.name == name:
                return product

        return None

    def add_stock(self, name, quantity):
        product = self.find_product(name)

        if product is None:
            raise ValueError("해당 상품이 없습니다.")

        product.add_stock(quantity)


def sell_product(self, name, quantity):
    product = self.find_product(name)

    if product is None:
        raise ValueError("해당 상품이 없습니다.")

    product.sell(quantity)

    def sell_product(self, name, quantity):
        product = self.find_product(name)

        if product is None:
            raise ValueError("해당 상품이 없습니다.")

        product.sell(quantity)

    def get_total_stock(self):
        return sum(product.stock for product in self.products)

    def get_total_value(self):
        return sum(product.get_value() for product in self.products)

def save_products_json(products, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump([product.to_dict() for product in products], file, ensure_ascii=False, indent=4)

def load_products_json(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        print("저장된 상품 파일이 없습니다. 새로 시작합니다.")
        return []

    except json.JSONDecodeError:
        print("상품 파일이 손상되었습니다. 새로 시작합니다.")
        return []

def load_products_json(filename):
    valid_products = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            products = json.load(file)

        if not isinstance(products, list):
            print("전체 데이터가 리스트 형식이 아닙니다.")
            return []

        for product in products:
            if (
                isinstance(product, dict)
                and "name" in product
                and "price" in product
                and "stock" in product
                and isinstance(product["name"], str)
                and isinstance(product["price"], int)
                and isinstance(product["stock"], int)
                and product["name"].strip() != ""
                and product["price"] > 0
                and product["stock"] >= 0
            ):
                valid_products.append(product)
            else:
                print(f"잘못된 데이터입니다: {product}")

    except FileNotFoundError:
        print("저장된 상품 파일이 없습니다. 새로 시작합니다.")

    except json.JSONDecodeError:
        print("상품 파일이 손상되었습니다. 새로 시작합니다.")

    return valid_products

def find_product(products, name):
    for product in products:
        if product["name"] == name:

            return product

    return None


def calculate_inventory(products):
    total_stock = 0
    total_value = 0
    max_stock = -1
    max_stock_product = None

    for product in products:
        stock = product["stock"]
        price = product["price"]

        total_stock += stock
        total_value += stock * price

        if stock > max_stock:
            max_stock = stock
            max_stock_product = product["name"]

    return {
        "total_stock": total_stock,
        "total_value": total_value,
        "max_stock_product": max_stock_product
    }

def save_products(products, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for product in products:
            line = (
                f"{product['name']},"
                f"{product['price']},"
                f"{product['stock']}\n"
            )
            file.write(line)

    print("저장되었습니다.")

def load_products(filename):
    products = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                original_line = line.strip()

                if not original_line:
                    continue

                try:
                    name, price, stock = original_line.split(",")

                    name = name.strip()
                    price = price.strip()
                    stock = stock.strip()

                    if not name or not price or not stock:
                        raise ValueError

                    price = int(price)
                    stock = int(stock)

                    products.append({
                        "name": name,
                        "price": price,
                        "stock": stock
                    })

                except ValueError:
                    print(f"잘못된 데이터입니다: {original_line}")

    except FileNotFoundError:
        print("저장된 상품 파일이 없습니다. 새로 시작합니다.")

    return products


products = load_products("products.txt")

while True:
    print()
    print("1. 상품 목록")
    print("2. 상품 검색")
    print("3. 상품 추가")
    print("4. 재고 입고")
    print("5. 상품 판매")
    print("6. 재고 요약")
    print("0. 종료")

    try:
        menu = int(input("메뉴를 선택하세요: "))

        if menu == 1:
            if len(products) == 0:
                print("등록된 상품이 없습니다.")
            else:
                for product in products:
                    print(
                        f"{product['name']} | "
                        f"{product['price']}원 | "
                        f"재고 {product['stock']}개"
                    )

        elif menu == 2:
            name = input("검색할 상품 이름: ")

            product = find_product(products, name)

            if product is None:
                print("해당 상품이 없습니다.")

            else:
                print(f"상품명: {product['name']}")
                print(f"가격: {product['price']}원")
                print(f"재고: {product['stock']}개")

        elif menu == 3:
            name = input("상품명: ")

            if find_product(products, name) is not None:
                print("이미 존재하는 상품입니다.")
            else:
                try:
                    price = int(input("가격: "))
                    stock = int(input("재고 수량: "))

                    if price <= 0 or stock < 0:
                        print("가격은 0보다 커야 하고, 재고는 0 이상이어야 합니다.")
                    else:
                        products.append({
                            "name": name,
                            "price": price,
                            "stock": stock
                        })

                        print("상품이 추가되었습니다.")
                        print(f"{name} | {price}원 | 재고 {stock}개")

                except ValueError:
                    print("가격과 재고는 숫자로 입력해주세요.")

        elif menu == 4:
            name = input("재고 입고할 상품 이름: ")

            product = find_product(products, name)

            if product is None:
                print("해당 상품이 없습니다.")
            else:
                try:
                    stock_increase = int(input("입고 수량: "))

                    if stock_increase <= 0:
                        print("입고 수량은 0보다 커야 합니다.")
                    else:
                        product["stock"] += stock_increase
                        print(f"{name}의 재고가 {stock_increase}개 입고되었습니다.")
                        print(f"현재 재고: {product['stock']}개")

                except ValueError:
                    print("입고 수량은 숫자로 입력해주세요.")

        elif menu == 5:
            name = input("판매할 상품 이름: ")

            product = find_product(products, name)

            if product is None:
                print("해당 상품이 없습니다.")
            else:
                try:
                    stock_decrease = int(input("판매 수량: "))

                    if stock_decrease <= 0:
                        print("판매 수량은 0보다 커야 합니다.")
                    elif stock_decrease > product["stock"]:
                        print("재고가 부족합니다.")
                    else:
                        product["stock"] -= stock_decrease
                        print(f"{name}의 재고가 {stock_decrease}개 판매되었습니다.")
                        print(f"현재 재고: {product['stock']}개")

                except ValueError:
                    print("판매 수량은 숫자로 입력해주세요.")

        elif menu == 6:
            summary = calculate_inventory(products)

            print(f"총 재고 수량: {summary['total_stock']}개")
            print(f"총 재고 가치: {summary['total_value']}원")

            if summary['max_stock_product'] is None:
                print(f"재고가 가장 많은 상품: 없음")

            else:
                print(f"재고가 가장 많은 상품: {summary['max_stock_product']}")

        elif menu == 0:
            print("재고 관리 프로그램을 종료합니다.")
            break

        else:
            print("올바른 메뉴를 선택하세요.")

    except ValueError:
        print("메뉴는 숫자로 입력해주세요.")