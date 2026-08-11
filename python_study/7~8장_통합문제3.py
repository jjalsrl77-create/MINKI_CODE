import re

text = "민수 010-1234-5678 영희 010-9876-5432 철수 010-1111-2222"

numbers = re.findall(r"\d{3}-\d{4}-(\d{4})", text)

result = [int(number) for number in numbers]

print(result)