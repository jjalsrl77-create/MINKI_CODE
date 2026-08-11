import re

text = "apple 3 banana 5 cherry 10"

numbers = re.findall(r"\d+", text)

result = [int(number) ** 2 for number in numbers]

print(result)