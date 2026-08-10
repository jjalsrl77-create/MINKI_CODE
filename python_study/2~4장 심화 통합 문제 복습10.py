def get_reservation_status(reserved, days_left):
    if not reserved:
        return "예약 없음"
    elif reserved and days_left < 0:
        return "예약 만료"
    else:
        return "예약 예정"

def analyze_appointments(appointments):
    reserved_count = 0
    no_reservation_count = 0
    expired_count = 0
    max_days_left = 0

    for appointment in appointments:
        name = appointment["name"]
        reserved = appointment["reserved"]
        days_left = appointment["days_left"]

        status = get_reservation_status(reserved, days_left)

        print(f"{name}: {status}")

        if reserved:
            reserved_count += 1

        else:
            no_reservation_count += 1

        if reserved and days_left < 0:
            expired_count += 1

        if days_left > max_days_left:
            max_days_left = days_left

    return {
        "reserved_count": reserved_count,
        "no_reservation_count": no_reservation_count,
        "expired_count": expired_count,
        "max_days_left": max_days_left
    }

appointments = [
    {"name": "민수", "reserved": True, "days_left": 2},
    {"name": "지수", "reserved": False, "days_left": 0},
    {"name": "철수", "reserved": True, "days_left": -1},
    {"name": "영희", "reserved": True, "days_left": 5}
]

appointment = analyze_appointments(appointments)

print()
print(f"예약된 인원: {appointment['reserved_count']}")
print(f"예약 없는 인원: {appointment['no_reservation_count']}")
print(f"예약 만료 인원: {appointment['expired_count']}")
print(f"가장 많이 남은 일수: {appointment['max_days_left']}")