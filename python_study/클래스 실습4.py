class Employee:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def calculate_pay(self):
        return self.pay
    
    def show_info(self):
        print(f"이름: {self.name}, 급여: {self.calculate_pay()}")

class Manager(Employee):
    def __init__(self, name, pay, bonus):
        self.name = name
        self.pay = pay
        self.bonus = bonus

    def calculate_pay(self):
        return self.pay + self.bonus
    
    def show_info(self):
        print(f"이름: {self.name}, 기본 급여: {self.pay}, 보너스: {self.bonus}, 총 급여: {self.calculate_pay()}")

employee = Employee("민수", 3000000)
manager = Manager("지수", 4000000, 1000000)

employee.show_info()
manager.show_info()