def add_transaction(transactions, transaction_type, category, amount):
    transaction = {
        "type": transaction_type,
        "category": category,
        "amount": amount
    }

    transactions.append(transaction)


def calculate_summary(transactions): 
    income = 0
    expense = 0

    for transaction in transactions:
        if transaction["type"] == "수입":
            income += transaction["amount"]
        elif transaction["type"] == "지출":
            expense += transaction["amount"]

    balance = income - expense

    return {
        "income": income,
        "expense": expense,
        "balance": balance
    }


transactions = [
    {"type": "수입", "category": "급여", "amount": 3000000},
    {"type": "지출", "category": "식비", "amount": 120000},
    {"type": "지출", "category": "교통비", "amount": 50000}
]

while True:
    print()
    print("1. 거래 목록")
    print("2. 수입 추가")
    print("3. 지출 추가")
    print("4. 카테고리 검색")
    print("5. 전체 요약")
    print("0. 종료")

    try:
        menu = int(input("메뉴를 선택하세요: "))

        if menu == 1:
            if len(transactions) == 0:
                print("등록된 거래가 없습니다.")
            else:
                for transaction in transactions:
                    print(
                        f"{transaction['type']} | "
                        f"{transaction['category']} | "
                        f"{transaction['amount']}원"
                    )

        elif menu == 2:
            category = input("수입 카테고리: ")

            try:
                amount = int(input("수입 금액: "))

                if amount <= 0:
                    print("금액은 0보다 커야 합니다.")
                else:
                    add_transaction(
                        transactions,
                        "수입",
                        category,
                        amount
                    )

                    print("수입이 추가되었습니다.")

            except ValueError:
                print("금액은 숫자로 입력해주세요.")

        elif menu == 3:
            category = input("지출 카테고리: ")

            try:
                amount = int(input("지출 금액: "))

                if amount <= 0:
                    print("금액은 0보다 커야 합니다.")
                else:
                    add_transaction(
                        transactions,
                        "지출",
                        category,
                        amount
                    )

                    print("지출이 추가되었습니다.")

            except ValueError:
                print("금액은 숫자로 입력해주세요.")

        elif menu == 4:
            category = input("검색할 카테고리: ")

            found = False

            for transaction in transactions:
                if transaction["category"] == category:
                    print(
                        f"{transaction['type']} | "
                        f"{transaction['category']} | "
                        f"{transaction['amount']}원"
                    )

                    found = True

            if not found:
                print("해당 카테고리의 거래가 없습니다.")

        elif menu == 5:
            summary = calculate_summary(transactions)

            print(f"전체 수입: {summary['income']}원")
            print(f"전체 지출: {summary['expense']}원")
            print(f"현재 잔액: {summary['balance']}원")

        elif menu == 0:
            print("가계부 프로그램을 종료합니다.")
            break

        else:
            print("올바른 메뉴를 선택하세요.")

    except ValueError:
        print("메뉴는 숫자로 입력해주세요.")