class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def show_info(self):
        print(f"이름: {self.name}, 점수: {self.score}")


student1 = Student("민수", 85)
student2 = Student("지수", 92)

student1.show_info()
student2.show_info()