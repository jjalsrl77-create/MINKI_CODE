def print_menu():
    print("1. 메모추가")
    print("2. 메모 목록 보기")
    print("3. 메모 삭제")
    print("4. 종료")

memo = []

while True:
    print_menu()

    menu_num = int(input("메뉴 번호를 입력하세요: "))

    if menu_num == 1:
        write_memo = input("메모를 입력하세요: ")
        memo.append(write_memo)

    elif menu_num == 2:
        print(memo)

    elif menu_num == 3:
        delete_memo = int(input("삭제할 메모 번호를 입력하세요: "))

        memo.remove(memo[delete_memo-1])

    elif menu_num == 4:
        print("프로그램을 종료합니다.")
        break

#OR

def print_menu():
    print("1. 메모 추가")
    print("2. 메모 목록 보기")
    print("3. 메모 삭제")
    print("4. 종료")

memo = []

while True:
    print_menu()

    menu_num = int(input("메뉴 번호를 입력하세요: "))

    if menu_num == 1:
        write_memo = input("메모를 입력하세요: ")
        memo.append(write_memo)

    elif menu_num == 2:
        print("메모 목록")
        for i in range(len(memo)):
            print(f"{i + 1}. {memo[i]}")

    elif menu_num == 3:
        delete_memo = int(input("삭제할 메모 번호를 입력하세요: "))
        del memo[delete_memo - 1]

    elif menu_num == 4:
        print("프로그램을 종료합니다.")
        break