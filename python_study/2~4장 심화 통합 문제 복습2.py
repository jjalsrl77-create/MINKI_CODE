def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def analyze_students(students):
    total = 0
    max_score = 0
    pass_count = 0
    fail_count = 0

    for student in students:
        name = student["name"]
        score = student["score"]

        grade = get_grade(score)

        print(f"{name}: {score}점, {grade}등급")

        total += score

        if score > max_score:
            max_score = score

        if score >= 60:
            pass_count += 1
        else:
            fail_count += 1

    average = total / len(students)

    result = {
        "average": average,
        "max_score": max_score,
        "pass_count": pass_count,
        "fail_count": fail_count
    }

    return result


students = [
    {"name": "민수", "score": 85},
    {"name": "지수", "score": 92},
    {"name": "철수", "score": 58},
    {"name": "영희", "score": 76}
]

result = analyze_students(students)

print()
print(f"평균: {result['average']}")
print(f"최고 점수: {result['max_score']}")
print(f"합격자 수: {result['pass_count']}명")
print(f"불합격자 수: {result['fail_count']}명")