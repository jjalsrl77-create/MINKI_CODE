def print_menu():
    print("1. 메모 추가")
    print("2. 메모 목록 보기")
    print("3. 메모 삭제")
    print("4. 메모 수정")
    print("5. 메모 검색")
    print("6. 종료")

memo = []

def add_memo():
    write_memo = input("추가할 메모를 입력하세요.")
    memo.append(write_memo)
    print(memo)

def show_memo():
    for k in range(len(memo)):
        print(f"{k + 1} : {memo[k]}")

def delete_memo():
    delete = int(input("삭제할 메모의 번호를 입력하세요: "))

    del memo[delete - 1]

    print(memo)

def update_memo():
    amend_memo = int(input("수정할 메모의 번호를 입력하세요: "))
    rewrite_memo = input("수정할 메모를 입력하세요: ")

    memo[amend_memo - 1] = rewrite_memo

def search_memo():
    search_memo = input("검색할 메모를 입력하세요: ")

    found = False

    for k in range(len(memo)):
        if search_memo in memo[k]:
            print(f"{k+1} : {memo[k]}")
            found = True

    if found == False:
        print("검색어가 포함된 메모가 없습니다.")

def end_memo():
    print("프로그램을 종료합니다.")

while True:
    print_menu()

    menu_num = int(input("선택할 메뉴 번호를 입력하세요: "))

    if menu_num == 1:
        add_memo()

    elif menu_num == 2:
        show_memo()

    elif menu_num == 3: 
        delete_memo()

    elif menu_num == 4:
        update_memo()

    elif menu_num == 5:
        search_memo()

    elif menu_num == 6:
        end_memo()
        break