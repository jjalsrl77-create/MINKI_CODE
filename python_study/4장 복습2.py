def get_average(num):
    result = sum(num) / len(num)
    return result

numbers = [70, 80, 90, 100]

result = get_average(numbers)
print(result)