def get_shipping_status(shipped, days):
    if not shipped:
        return "배송 준비"
    elif days > 7:
        return "배송 지연"
    else:
        return "배송 중"


def analyze_orders(orders):
    shipped_count = 0
    preparing_count = 0
    delayed_count = 0
    max_days = 0

    for order in orders:
        product = order["product"]
        shipped = order["shipped"]
        days = order["days"]

        status = get_shipping_status(shipped, days)

        print(f"{product}: {status}")

        if shipped:
            shipped_count += 1
        else:
            preparing_count += 1

        if status == "배송 지연":
            delayed_count += 1

        if days > max_days:
            max_days = days

    return {
        "shipped_count": shipped_count,
        "preparing_count": preparing_count,
        "delayed_count": delayed_count,
        "max_days": max_days
    }


orders = [
    {"product": "노트북", "shipped": True, "days": 2},
    {"product": "마우스", "shipped": False, "days": 0},
    {"product": "키보드", "shipped": True, "days": 8},
    {"product": "모니터", "shipped": True, "days": 4}
]

result = analyze_orders(orders)

print()
print(f"배송된 주문 수: {result['shipped_count']}개")
print(f"배송 준비 주문 수: {result['preparing_count']}개")
print(f"배송 지연 주문 수: {result['delayed_count']}개")
print(f"가장 긴 배송 일수: {result['max_days']}일")