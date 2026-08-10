def is_palindrome(text):
    cleaned_text = text.replace(" ", "").lower()

    if cleaned_text == cleaned_text[::-1]:
        return True
    else:
        return False


text = input("문자열을 입력하세요: ")

result = is_palindrome(text)

if result:
    print("회문입니다.")
else:
    print("회문이 아닙니다.")