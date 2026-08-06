class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def introduce(self):
        return f"이름: {self.name}, 나이: {self.age}, 학과: {self.major}"

result = Student("민수", 21, "기계공학부")

print(result.introduce())