order = {
    "product": "키보드",
    "price": 50000,
    "quantity": 2
}

order["total"] = order["price"] * order["quantity"]
order["discount"] = 5000

payment = order["total"] - order["discount"]

print(f"상품명: {order['product']}")
print(f"수량: {order['quantity']}개")
print(f"총금액: {order['total']}원")
print(f"할인금액: {order['discount']}원")
print(f"결제금액: {payment}원")