def analyze_text(text):
    letter_count = 0
    digit_count = 0
    space_count = 0
    other_count = 0

    for char in text:
        if char.isalpha():
            letter_count += 1

        elif char.isdigit():
            digit_count += 1

        elif char.isspace():
            space_count += 1

        else:
            other_count += 1

    return {
        "letter": letter_count,
        "digit": digit_count,
        "space": space_count,
        "other": other_count
    }

text = input("문자열을 입력하세요: ")

result = analyze_text(text)

print(f"영문자 개수: {result['letter']}")
print(f"숫자 개수: {result['digit']}")
print(f"공백 개수: {result['space']}")
print(f"기타 문자 개수: {result['other']}")