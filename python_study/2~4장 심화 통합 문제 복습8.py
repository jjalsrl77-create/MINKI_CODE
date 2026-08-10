def get_level(minutes):
    if minutes >= 40:
        return "고강도"
    elif minutes >= 20:
        return "중강도"
    else:
        return "저강도"


def analyze_records(records):
    total_minutes = 0
    total_calories = 0
    max_calories = 0
    high_count = 0

    for record in records:
        name = record["name"]
        minutes = record["minutes"]
        calories = record["calories"]

        level = get_level(minutes)

        print(f"{name}: {minutes}분, {calories}칼로리, {level}")

        total_minutes += minutes
        total_calories += calories

        if calories > max_calories:
            max_calories = calories

        if level == "고강도":
            high_count += 1

    average_calories = total_calories / len(records)

    result = {
        "total_minutes": total_minutes,
        "total_calories": total_calories,
        "average_calories": average_calories,
        "max_calories": max_calories,
        "high_count": high_count
    }

    return result


records = [
    {"name": "달리기", "minutes": 30, "calories": 250},
    {"name": "자전거", "minutes": 45, "calories": 400},
    {"name": "걷기", "minutes": 20, "calories": 100},
    {"name": "수영", "minutes": 50, "calories": 500}
]

result = analyze_records(records)

print()
print(f"전체 운동 시간: {result['total_minutes']}분")
print(f"전체 소모 칼로리: {result['total_calories']}")
print(f"평균 소모 칼로리: {result['average_calories']}")
print(f"최고 소모 칼로리: {result['max_calories']}")
print(f"고강도 운동 수: {result['high_count']}개")