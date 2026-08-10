def get_status(progress, quiz):
    if progress >= 80 and quiz >= 60:
        return "수료"
    else:
        return "미수료"


def analyze_course(students):
    total_quiz = 0
    max_quiz = 0
    complete_count = 0
    incomplete_count = 0

    for student in students:
        name = student["name"]
        progress = student["progress"]
        quiz = student["quiz"]

        status = get_status(progress, quiz)

        print(f"{name}: 진도율 {progress}%, 퀴즈 {quiz}점, {status}")

        total_quiz += quiz

        if quiz > max_quiz:
            max_quiz = quiz

        if status == "수료":
            complete_count += 1
        else:
            incomplete_count += 1

    average_quiz = total_quiz / len(students)

    result = {
        "average_quiz": average_quiz,
        "max_quiz": max_quiz,
        "complete_count": complete_count,
        "incomplete_count": incomplete_count
    }

    return result


students = [
    {"name": "민수", "progress": 85, "quiz": 90},
    {"name": "지수", "progress": 100, "quiz": 95},
    {"name": "철수", "progress": 60, "quiz": 55},
    {"name": "영희", "progress": 75, "quiz": 80}
]

result = analyze_course(students)

print()
print(f"평균 퀴즈 점수: {result['average_quiz']}")
print(f"최고 퀴즈 점수: {result['max_quiz']}")
print(f"수료자 수: {result['complete_count']}명")
print(f"미수료자 수: {result['incomplete_count']}명")