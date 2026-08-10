class Member:
    def __init__(self, name, points):
        self.name = name
        self.points = points

    def earn_points(self, amount):
        self.points += amount
        print(f"{amount}포인트가 적립되었습니다.")

    def use_points(self, amount):
        if self.points >= amount:
            self.points -= amount
            print(f"{self.points}포인트가 사용되었습니다.")

        else:
            print("포인트가 부족합니다.")

    def show_info(self):
        print(f"회원 이름: {self.name}")
        print(f"보유 포인트: {self.points}")


member = Member("민수", 1000)

member.earn_points(500)
member.use_points(300)
member.use_points(2000)
member.show_info()