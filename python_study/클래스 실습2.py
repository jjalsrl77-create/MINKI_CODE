class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def add_score(self, amount):
        self.score += amount

    def subtract_score(self, amount):
        self.score -= amount

        if self.score < 0:
            self.score = 0

    def show_info(self):
        print(f"{self.name}: {self.score}점")

    def is_passed(self):
        return self.score >= 60


student = Student("민수", 55)

student.add_score(10)
student.show_info()
print(student.is_passed())

student.subtract_score(100)
student.show_info()
print(student.is_passed())