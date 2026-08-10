def calculate_ticket_price(tickets):
    ticket_count = 0
    total = 0

    for ticket in tickets:
        ticket_total = ticket["price"] * ticket["count"]

        total += ticket_total
        ticket_count += ticket["count"]

        print(f"{ticket['type']}: {ticket_total}원")

    if ticket_count >= 5:
        discount = total * 0.1
    else:
        discount = 0

    payment = total - discount

    result = {
        "ticket_count": ticket_count,
        "total": total,
        "discount": discount,
        "payment": payment
    }

    return result


tickets = [
    {"type": "성인", "price": 14000, "count": 2},
    {"type": "청소년", "price": 10000, "count": 1},
    {"type": "어린이", "price": 7000, "count": 2}
]

result = calculate_ticket_price(tickets)

print()
print(f"전체 표 수: {result['ticket_count']}장")
print(f"총금액: {result['total']}원")
print(f"할인금액: {result['discount']}원")
print(f"결제금액: {result['payment']}원")