# 2. 전제 도서 조회
def show_books(books):
    if not books:
        print("등록된 도서가 없습니다.")

    for title, info in books.items():
        author = info["author"]
        available = info["availavle"]

        print(f"제목: {title}")
        print(f"저자: {author}")
        if available == True:
            print("대여 가능")
        else:
            print("대여 중")
        print()

# 3. 도서 검색
def serch_books(books):
    title = input("검색할 책 제목: ")

    if title in books:
        info = books[title]
        author = info["author"]
        available = info["available"]

        print(f"저자: {author}")

        if available:
            print("대여 상태: 대여 가능")
            print("대여 상태: 대여 중")

    else:
        print("해당 도서가 없습니다.")
    
# 4. 도서 대여 함수
def borrow_book(books):
    title = input("대여할 책 제목: ")

    if title not in books:
        print("해당 도서가 없습니다.")
        return

    info = books[title]
    available = info["available"]

    if available is False:
        print("이미 대여 중인 도서입니다.")
    else:
        info["available"] = False
        print("도서가 대여되었습니다.")

# 5. 도서 반납 함수
def return_book(books):
    title = input("반납할 책 제목: ")

    if title not in books:
        print("해당 도서가 없습니다.")
        return

    info = books[title]

    if info["available"]:
        print("이미 반납된 도서입니다.")
    else:
        info["available"] = True
        print("도서가 반납되었습니다.")

# 6. 대여 가능한 도서만 조회하는 함수
def show_available_books(books):
    available_books = []

    for title, info in books.items():
        if info["available"]:
            available_books.append(title)

    if available_books:
        for title in available_books:
            print(title)
    else:
        print("대여 가능한 도서가 없습니다.")

# 7. 도서 정보를 파일에 저장하는 함수
def save_books(books):
    with open("books.txt", "a") as f:

        for title, info in books.items():
            author = info["author"]
            available = info["available"]
            
            f.write(f"{title}|{author}|{available}\n")
    print("도서 정보가 저장되었습니다.")

# 8. 파일 불러오기 함수
def load_books():
    books = {}

    with open("books.txt", "r") as f:
        for line in f:
            title, author, available = line.strip().split("|")

            books[title] = {
                "author": author,
                "available": available == "True"
                }

    print("도서 정보를 불러왔습니다.")
    return books

books = {
    "파이썬 입문": {
        "author": "홍길동",
        "available": True
    },
    "자료구조 기초": {
        "author": "김철수",
        "available": False
    }
}

while True:
    print("\n1. 도서 추가")
    print("2. 전체 도서 조회")
    print("3. 도서 검색")
    print("4. 도서 대여")
    print("5. 도서 반납")
    print("6. 대여 가능 도서 조회")
    print("7. 파일 저장")
    print("8. 파일 불러오기")
    print("0. 종료")

    menu = input("메뉴를 선택하세요: ")

    if menu == "0":
        print("프로그램을 종료합니다.")
        break

# 1. 도서 추가
def add_book(books):
    author = input("저자를 입력하세요: ")
    title = input("제목을 입력하세요: ")

    books[title] = {
        "author": author,
        "available": True
    }

    print(f"'{title}' 도서가 추가되었습니다.")


books = {
    "파이썬 입문": {
        "author": "홍길동",
        "available": True
    },
    "자료구조 기초": {
        "author": "김철수",
        "available": False
    }
}

add_book(books)
print(books)