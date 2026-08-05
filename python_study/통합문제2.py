def price_cal(items):
    total_price = 0

    for item in items:
        total_price += item["가격"]

    return total_price


def discount_cal(total_price):
    if total_price >= 30000:
        return total_price * 0.9
    else:
        return total_price


items = []

for k in range(3):
    name = input(f"{k + 1}번째 상품 이름: ")
    price = int(input(f"{k + 1}번째 상품 가격: "))

    product = {
        "상품": name,
        "가격": price
    }

    items.append(product)


total_price = price_cal(items)
discounted_price = discount_cal(total_price)

print("전체 상품 목록:")
print(items)
print(f"총 가격: {total_price}원")
print(f"할인 적용 후 가격: {discounted_price}원")