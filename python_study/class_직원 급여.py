class Employee:
    def __init__(self, name, hourly_pay, hours):
        self.name = name
        self.hourly_pay = hourly_pay
        self.hours = hours

    def calculate_salary(self):
        result = self.hourly_pay * self.hours

        return result

    def add_hours(self, hours):
        self.hours += hours
        print(f"{self.name}님의 근무 시간이 {hours}시간 추가되었습니다.")

    def show_info(self):
        salary = self.calculate_salary()

        print(f"이름: {self.name}")
        print(f"근무시간: {self.hours}시간")
        print(f"급여: {salary}")


employee = Employee("민수", 12000, 35)

employee.add_hours(5)
employee.show_info()