def find_second_largest(numbers):
    unique_numbers = list(set(numbers))

    if len(unique_numbers) < 2:
        return None

    unique_numbers.sort(reverse=True)

    return unique_numbers[1]


text = input("숫자를 입력하세요: ")

numbers = list(map(int, text.split()))

result = find_second_largest(numbers)

if result is None:
    print("두 번째로 큰 숫자가 없습니다.")
else:
    print(f"두 번째로 큰 숫자: {result}")