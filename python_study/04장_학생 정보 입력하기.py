def print_student(student):
    print(f"이름: {student['이름']}")
    print(f"나이: {student['나이']}")
    print(f"학과: {student['학과']}")

name = input("이름을 입력하세요: ")
age = int(input("나이를 입력하세요: "))
major = input("학과를 입력하세요: ")

student = {
    "이름": name,
    "나이": age,
    "학과": major
}

print_student(student)