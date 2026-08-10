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


def find_student(students, name):
    for student in students:
        if student["name"] == name:
            return student

    return None


def analyze_students(students):
    total = 0
    max_score = 0
    min_score = students[0]["score"]
    pass_count = 0
    fail_count = 0

    for student in students:
        score = student["score"]

        total += score

        if score > max_score:
            max_score = score

        if score < min_score:
            min_score = score

        if score >= 60:
            pass_count += 1
        else:
            fail_count += 1

    average = total / len(students)

    return {
        "total": total,
        "average": average,
        "max_score": max_score,
        "min_score": min_score,
        "pass_count": pass_count,
        "fail_count": fail_count
    }


students = [
    {"name": "민수", "score": 85},
    {"name": "지수", "score": 92},
    {"name": "철수", "score": 58},
    {"name": "영희", "score": 76}
]


result = analyze_students(students)

print("전체 분석 결과")
print(f"총점: {result['total']}")
print(f"평균: {result['average']}")
print(f"최고 점수: {result['max_score']}")
print(f"최저 점수: {result['min_score']}")
print(f"합격자 수: {result['pass_count']}명")
print(f"불합격자 수: {result['fail_count']}명")


name = input("검색할 학생 이름을 입력하세요: ")

found_student = find_student(students, name)

if found_student is not None:
    grade = get_grade(found_student["score"])

    print(
        f"검색 결과: {found_student['name']}, "
        f"{found_student['score']}점, {grade}등급"
    )
else:
    print("해당 학생을 찾을 수 없습니다.")

try:
    name = input("새 학생 이름: ")
    score = int(input("새 학생 점수: "))

    if score < 0 or score > 100:
        print("점수는 0점부터 100점 사이여야 합니다.")
    else:
        student = {
            "name": name,
            "score": score
        }

        students.append(student)

        grade = get_grade(score)

        print("학생이 추가되었습니다.")
        print(f"{name}: {score}점, {grade}등급")

except ValueError:
    print("점수는 숫자로 입력해주세요.")