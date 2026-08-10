class LibraryMember:
    def __init__(self, name):
        self.name = name
        self.borrow = []

    def borrow_book(self, title):
        if title in self.borrow:
            print("이미 대여 중인 책입니다.")
        elif len(self.borrow) >= 3:
            print("더 이상 대여할 수 없습니다.")
        else:
            self.borrow.append(title)
            print(f"{title} 대여가 완료되었습니다.")

    def return_book(self, title):
        if title not in self.borrow:
            print("대여 중인 책이 아닙니다.")
        else:
            self.borrow.remove(title)
            print(f"{title} 반납이 완료되었습니다.")

    def show_books(self):
        if len(self.borrow) == 0:
            print("대여 중인 책이 없습니다.")
        else:
            print(f"{self.name}님의 대여 목록:")

            for title in self.borrow:
                print(title)


member = LibraryMember("민수")

member.borrow_book("파이썬 기초")
member.borrow_book("자료구조")
member.borrow_book("알고리즘")
member.borrow_book("웹 개발")

member.return_book("자료구조")
member.show_books()