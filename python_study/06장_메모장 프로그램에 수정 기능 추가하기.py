def print_menu():
    print("1. 메모 추가")
    print("2. 메모 목록 보기")
    print("3. 메모 삭제")
    print("4. 메모 수정")
    print("5. 종료")

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
        delete_memo = int(input("삭제할 메모의 번호를 입력하세요: "))

        del memo[delete_memo - 1]

    elif menu_num == 4:
        amend_memo = int(input("수정할 메모의 번호를 입력하세요: "))
        new_memo = input("수정할 메모를 입력하세요: ")
        memo[amend_memo - 1] = new_memo

    elif menu_num == 5:
        print("프로그램을 종료합니다.")
        break