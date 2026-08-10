def get_book_status(borrowed, days):
    if not borrowed:
        return "대여 가능"
    elif borrowed == True and days > 7:
        return "연체"
    else:
        return "대여 중"

def analyze_books(books):
    borrowed_count = 0
    available_count = 0
    overdue_count = 0
    max_days = 0

    for book in books:
        title = book["title"]
        borrowed = book["borrowed"]
        days = book["days"]

        status = get_book_status(borrowed, days)

        print(f"{title}: {status}")

        if borrowed:
            borrowed_count += 1

        else:
            available_count += 1

        if status == "연체":
            overdue_count += 1

        if days > max_days:
            max_days = days

    result = {
        "borrowed_count": borrowed_count,
        "available_count": available_count,
        "overdue_count": overdue_count,
        "max_days": max_days
    }

    return result

books = [
    {"title": "파이썬 기초", "borrowed": True, "days": 5},
    {"title": "자료구조", "borrowed": False, "days": 0},
    {"title": "알고리즘", "borrowed": True, "days": 12},
    {"title": "웹 개발", "borrowed": True, "days": 3}
]

result = analyze_books(books)

print()
print(f"대여 중인 도서 수: {result['borrowed_count']}권")
print(f"대여 가능한 도서 수: {result['available_count']}권")
print(f"연체 도서 수: {result['overdue_count']}권")
print(f"가장 긴 대여 일수: {result['max_days']}일")