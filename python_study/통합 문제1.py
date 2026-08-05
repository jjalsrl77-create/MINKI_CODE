def average_score(scores):
    total = sum(scores)
    average = total / len(scores)
    return average

def score_info(average):
    if average >= 60:
        return "합격"
    else:
        return "불합격"

students = []

for k in range(3):
    name = input("학생 이름: ")

    scores = []

    for i in range(3):
        score = int(input(f"{name} 학생의 {i + 1}번째 점수: "))
        scores.append(score)

    average = average_score(scores)
    result = score_info(average)

    student_info = {
        "이름": name,
        "점수": scores,
        "평균": average,
        "결과": result
    }

    students.append(student_info)

for student in students:
    print(f"{student['이름']} 학생")
    print(f"점수: {student['점수']}")
    print(f"평균: {student['평균']}")
    print(f"결과: {student['결과']}")