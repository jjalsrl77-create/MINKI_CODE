student = input("학생 이름: ")

scores = []

for k in range(1, 4):
    score = int(input(f"{k}번째 점수: "))
    scores.append(score)

average = sum(scores) / len(scores)

student_info = {
    "이름": student,
    "점수": scores,
    "평균": average
}

print(student_info)
print(f"{student} 학생의 평균 점수는 {average}점입니다.")