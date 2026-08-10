class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width + self.height) * 2

    def show_info(self):
        area = self.get_area()
        perimeter = self.get_perimeter()

        print(f"가로: {self.width}")
        print(f"세로: {self.height}")
        print(f"넓이: {area}")
        print(f"둘레: {perimeter}")


rectangle = Rectangle(5, 3)

rectangle.show_info()