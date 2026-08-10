def get_delivery_status(delivered, minutes):
    if not delivered:
        return "배달 준비"
    elif delivered and minutes > 40:
        return "배달 지연"
    else:
        return "배달 완료"

def analyze_orders(orders):
    delivered_count = 0
    preparing_count = 0
    delayed_count = 0
    total_price = 0
    max_minutes = 0

    for order in orders:
        menu = order["menu"]
        delivered = order["delivered"]
        minutes = order["minutes"]
        price = order["price"]

        status = get_delivery_status(delivered, minutes)

        print(f"{menu}: {status}")

        delivered_count += delivered

        if not delivered:
            preparing_count += 1

        if delivered and minutes > 40:
            delayed_count += 1

        total_price += price

        if minutes > max_minutes:
            max_minutes = minutes 

    return {
        "delivered_count": delivered_count,
        "preparing_count": preparing_count,
        "delayed_count": delayed_count,
        "total_price": total_price,
        "max_minutes": max_minutes
    }

orders = [
    {"menu": "치킨", "delivered": True, "minutes": 35, "price": 22000},
    {"menu": "피자", "delivered": False, "minutes": 0, "price": 18000},
    {"menu": "햄버거", "delivered": True, "minutes": 55, "price": 12000},
    {"menu": "떡볶이", "delivered": True, "minutes": 25, "price": 15000}
]

result = analyze_orders(orders)

print()
print(f"배달 완료 주문 수: {orders['delivered_count']}")
print(f"배달 준비 주문 수: {orders['preparing_count']}")
print(f"배달 지연 주문 수: {orders['delayed_count']}")
print(f"전체 주문 금액: {orders['total_price']}")
print(f"가장 긴 배달 시간: {orders['max_minutes']}")