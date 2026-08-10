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


students = [
    {"name": "민수", "score": 85},
    {"name": "지수", "score": 92},
    {"name": "철수", "score": 58},
    {"name": "영희", "score": 76}
]


while True:
    print()
    print("1. 학생 목록")
    print("2. 학생 검색")
    print("3. 학생 추가")
    print("4. 학생 수정")
    print("5. 학생 삭제")
    print("0. 종료")

    try:
        menu = int(input("메뉴를 선택하세요: "))

        if menu == 1:
            print("현재 학생 목록:")

            if len(students) == 0:
                print("등록된 학생이 없습니다.")
            else:
                for student in students:
                    grade = get_grade(student["score"])
                    print(
                        f"{student['name']}: "
                        f"{student['score']}점, {grade}등급"
                    )

        elif menu == 2:
            name = input("검색할 학생 이름: ")
            student = find_student(students, name)

            if student is None:
                print("해당 학생을 찾을 수 없습니다.")
            else:
                grade = get_grade(student["score"])
                print(
                    f"{student['name']}: "
                    f"{student['score']}점, {grade}등급"
                )

        elif menu == 3:
            name = input("새 학생 이름: ")

            if find_student(students, name) is not None:
                print("이미 등록된 학생입니다.")
                continue

            try:
                score = int(input("새 학생 점수: "))

                if score < 0 or score > 100:
                    print("점수는 0점부터 100점 사이여야 합니다.")
                else:
                    new_student = {
                        "name": name,
                        "score": score
                    }

                    students.append(new_student)

                    grade = get_grade(score)

                    print("학생이 추가되었습니다.")
                    print(f"{name}: {score}점, {grade}등급")

            except ValueError:
                print("점수는 숫자로 입력해주세요.")

        elif menu == 4:
            name = input("수정할 학생 이름: ")
            student = find_student(students, name)

            if student is None:
                print("해당 학생을 찾을 수 없습니다.")
            else:
                try:
                    new_score = int(input("새 점수: "))

                    if new_score < 0 or new_score > 100:
                        print("점수는 0점부터 100점 사이여야 합니다.")
                    else:
                        old_score = student["score"]
                        student["score"] = new_score
                        new_grade = get_grade(new_score)

                        print("점수가 수정되었습니다.")
                        print(
                            f"{student['name']}: "
                            f"{old_score}점 → {new_score}점"
                        )
                        print(f"새 등급: {new_grade}")

                except ValueError:
                    print("점수는 숫자로 입력해주세요.")

        elif menu == 5:
            name = input("삭제할 학생 이름: ")
            student = find_student(students, name)

            if student is None:
                print("해당 학생을 찾을 수 없습니다.")
            else:
                students.remove(student)
                print(f"{student['name']} 학생이 삭제되었습니다.")

        elif menu == 0:
            print("프로그램을 종료합니다.")
            break

        else:
            print("올바른 메뉴를 선택하세요.")

    except ValueError:
        print("메뉴는 숫자로 입력해주세요.")