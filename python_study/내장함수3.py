def is_even(number):
    return number % 2 == 0

numbers = [7, 2, 9, 4, 1, 8, 3, 6]
result = list(filter(is_even, numbers))

print(sorted(result))