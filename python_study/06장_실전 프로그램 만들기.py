memo = []

while True:
        menu_num = int(input("메뉴 번호를 입력하세요: "))

        if menu_num == 1:
            write_memo = input("메모를 입력하세요.")
            memo.append(write_memo)

        elif menu_num == 2:
            print(f"메모 목록: {memo}")

        elif menu_num == 3:
            print(f"프로그램을 종료합니다.")
            break


#OR

memo = []

def print_menu():
    print("1. 메모 추가")
    print("2. 메모 목록 보기")
    print("3. 종료")

while True:
    print_menu()

    menu_num = int(input("메뉴 번호를 입력하세요: "))

    if menu_num == 1:
        write_memo = input("메모를 입력하세요: ")
        memo.append(write_memo)

    elif menu_num == 2:
        print(f"메모 목록: {memo}")

    elif menu_num == 3:
        print("프로그램을 종료합니다.")
        break