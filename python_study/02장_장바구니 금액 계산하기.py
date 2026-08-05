cart = []

for k in range(3):
    item = input(f"{k + 1}번째 상품 이름: ")
    price = int(input(f"{k + 1}번째 상품 가격: "))

    product = {
        "상품": item,
        "가격": price
    }

    cart.append(product)

total_price = 0

for product in cart:
    total_price += product["가격"]

print("전체 상품 목록:")
print(cart)
print(f"총 금액: {total_price}원")