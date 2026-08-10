students = {
    "홍길동":85, 
    "김철수":90, 
    "이영희":88, 
    "박민수":92, 
    "최지우":87
}

student = input("학생 이름을 입력하세요: ")
students[student] = int(input("학생의 점수를 입력하세요: "))
print(students)
while True:
    student = input("학생 이름을 입력하세요: ")
    if student == "0":
        break
    elif student in students:
        if students[student] >= 85:
            print("합격")
        else:
            print("불합격")
    else:
        print("해당 학생이 존재하지 않습니다.")


avg = sum(students.values()) / len(students)
print("평균 점수:", avg)

with open("students.txt", "w", encoding="utf-8") as file:
    for name, score in students.items():
        file.write(f"{name}: {score}\n")
print("학생 점수가 students.txt 파일에 저장되었습니다.")