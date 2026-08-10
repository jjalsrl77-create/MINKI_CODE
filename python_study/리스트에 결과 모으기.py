def extract_numbers(text):
    numbers = []

    for char in text:
        if char.isdigit():
            numbers.append(int(char))
            
    return numbers


text = input("문자열을 입력하세요: ")

result = extract_numbers(text)

print(f"숫자 목록: {result}")
print(f"숫자 합계: {sum(result)}")