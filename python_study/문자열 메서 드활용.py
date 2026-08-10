def check_password(password):
    has_letter = False
    has_digit = False
    has_space = False

    for char in password:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_digit = True
        elif char.isspace():
            has_space = True

    if len(password) < 8:
        return "8자 이상이어야 합니다."
    elif not has_letter:
        return "영문자가 포함되어야 합니다."
    elif not has_digit:
        return "숫자가 포함되어야 합니다."
    elif has_space:
        return "공백을 사용할 수 없습니다."
    else:
        return "사용 가능한 비밀번호입니다."


password = input("비밀번호를 입력하세요: ")

result = check_password(password)

print(result)