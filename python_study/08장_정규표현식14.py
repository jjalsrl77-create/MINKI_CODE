import re

text = "전화번호: 010-1234-5678"

result = re.search(
    r"(?P<first>\d{3})-(?P<middle>\d{4})-(?P<last>\d{4})",
    text
)

first = result.group("first")
middle = result.group("middle")
last = result.group("last")

print(first, middle, last)