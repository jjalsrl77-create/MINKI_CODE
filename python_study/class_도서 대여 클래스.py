class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False

    def borrow(self):
        if self.borrowed:
            print("이미 대여 중입니다.")
        else:
            self.borrowed = True
            print("대여가 완료되었습니다.")

    def return_book(self):
        if not self.borrowed:
            print("대여 중인 책이 아닙니다.")
        else:
            self.borrowed = False
            print("반납이 완료되었습니다.")

    def show_info(self):
        if self.borrowed:
            status = "대여 중"
        else:
            status = "대여 가능"

        print(f"제목: {self.title}")
        print(f"저자: {self.author}")
        print(f"상태: {status}")


book = Book("파이썬 기초", "홍길동")

book.show_info()
book.borrow()
book.borrow()
book.return_book()
book.show_info()