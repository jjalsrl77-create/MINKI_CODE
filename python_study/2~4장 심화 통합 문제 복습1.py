def calculate_total(cart):
    total = 0

    for product in cart:
        product_total = product["price"] * product["quantity"]
        total += product_total

        print(f"{product['name']}: {product_total}원")

    if total >= 100000:
        discount = total * 0.1
    elif total >= 50000:
        discount = total * 0.05
    else:
        discount = 0

    payment = total - discount

    result = {
        "total": total,
        "discount": discount,
        "payment": payment
    }

    return result


cart = [
    {"name": "키보드", "price": 50000, "quantity": 1},
    {"name": "마우스", "price": 30000, "quantity": 2},
    {"name": "USB", "price": 10000, "quantity": 3}
]

result = calculate_total(cart)

print(f"총금액: {result['total']}원")
print(f"할인금액: {result['discount']}원")
print(f"결제금액: {result['payment']}원")