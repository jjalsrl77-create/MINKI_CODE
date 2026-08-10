def check_id(user_id):
    if len(user_id) < 5:
        return "아이디는 5자 이상이어야 합니다."
    if " " in user_id:
        return "아이디에 공백은 사용할 수 없습니다."
    if user_id == "admin":
        return "사용할 수 없는 아이디입니다."
    return "사용 가능"


while True:
    user_id = input("아이디를 입력하세요: ")

    result = check_id(user_id)

    if result == "사용 가능":
        print("가입이 완료되었습니다.")
        break
    else:
        print(result)