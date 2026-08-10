class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def add_score(self, amount):
        self.score += amount

    def show_info(self):
        print(f"이름: {self.name}, 점수: {self.score}")

    def is_passed(self):
        if self.score >= 60:
            print("True")
        else:
            print("False")