def is_positive(number):
    return number > 0

numbers = [-3, 7, 0, -1, 5, 2, -8]

result = sorted(filter(is_positive, numbers))

print(f"양수 목록: {result}")