def print_menu():
    print("1. 학생 정보 입력")
    print("2. 학생 정보 출력")
    print("3. 프로그램 종료")

print_menu()

num = int(input("메뉴 번호를 입력하세요: "))

print(f"선택한 메뉴 번호: {num}")