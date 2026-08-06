class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

result = Student("민수", 21, "기계공학부")

print(f"이름: {result.name}")
print(f"나이: {result.age}")
print(f"학과: {result.major}")