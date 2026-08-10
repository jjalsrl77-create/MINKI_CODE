class Car:
    def __init__(self, brand, fuel):
        self.brand = brand
        self.fuel = fuel

    def drive(self, distance):
        if distance > self.fuel:
            print("연료가 부족합니다.")
        else:
            self.fuel -= distance
            print(f"{distance}km를 주행했습니다.")

    def refuel(self, amount):
        self.fuel += amount
        print(f"{amount}만큼 주유했습니다.")

    def show_info(self):
        print(f"브랜드: {self.brand}")
        print(f"남은 연료: {self.fuel}")


car = Car("현대", 50)

car.drive(20)
car.drive(40)
car.refuel(30)
car.show_info()