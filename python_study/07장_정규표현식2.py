import re

text = "민수 010-1234-5678, 영희 010-9876-5432"
phone_numbers = re.findall(r"\d{3}-\d{4}-\d{4}", text)

print(phone_numbers)