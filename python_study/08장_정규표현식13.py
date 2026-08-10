import re

text = "전화번호: 010-1234-5678"

result = re.search(r"(\d{3})-(\d{4})-(\d{4})", text)

print(result.group(0))
print(result.group(1))
print(result.group(2))
print(result.group(3))