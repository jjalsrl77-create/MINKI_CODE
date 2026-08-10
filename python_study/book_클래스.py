class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False

    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            return f"{self.title}이(가) 대여되었습니다."
        else:
            raise ValueError("이미 대여중입니다.")

    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            return f"{self.title}이(가) 반납되었습니다."
        else:
            raise ValueError("이미 반납된 도서입니다.")

    def is_available(self):
        if self.borrowed:
            return "대여 중"
        else:
            return "대여 가능"

    def __str__(self):
        return f"제목: {self.title}| 저자: {self.author}| 상태: {self.is_available()}"

book = Book("파이썬 입문", "홍길동")

print(book)

book.borrow()
print(book)

book.return_book()
print(book)