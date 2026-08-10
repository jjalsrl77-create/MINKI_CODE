from student import Student

student1 = Student("민수", 55)
student2 = Student("지수", 80)
student3 = Student("철수", 95)

students = [student1, student2, student3]

for student in students:
    student.show_info()
    print("합격 여부:", student.is_passed())
    print()

student1.add_score(10)

print("점수 변경 후")
student1.show_info()
print("합격 여부:", student1.is_passed())