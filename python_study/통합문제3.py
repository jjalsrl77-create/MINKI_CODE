def get_grade(price):
    if price >= 100000:
        return "VIP"
    elif price >= 50000:
        return "Gold"
    else:
        return "Silver"


members = []

for k in range(3):
    name = input(f"{k + 1}번째 회원 이름: ")
    price = int(input(f"{k + 1}번째 회원 구매 금액: "))

    grade = get_grade(price)

    member_info = {
        "이름": name,
        "구매 금액": price,
        "등급": grade
    }

    members.append(member_info)

print("전체 회원 정보:")
print(members)
