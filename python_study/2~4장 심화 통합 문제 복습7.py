def analyze_orders(orders):
    total_count = 0
    total_price = 0

    for order in orders:
        order_price = order["price"] * order["count"]

        print(f"{order['menu']}: {order_price}원")

        total_price += order_price
        total_count += order["count"]

    if total_price >= 20000:
        discount = 2000
    else:
        discount = 0

    payment = total_price - discount

    result = {
        "total_count": total_count,
        "total_price": total_price,
        "discount": discount,
        "payment": payment
    }

    return result


orders = [
    {"menu": "아메리카노", "price": 4000, "count": 2},
    {"menu": "라떼", "price": 5000, "count": 1},
    {"menu": "케이크", "price": 6500, "count": 2}
]

result = analyze_orders(orders)

print()
print(f"전체 수량: {result['total_count']}개")
print(f"총금액: {result['total_price']}원")
print(f"할인금액: {result['discount']}원")
print(f"결제금액: {result['payment']}원")