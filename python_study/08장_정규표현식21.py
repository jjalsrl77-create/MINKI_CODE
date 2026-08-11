import re

text = "상품코드: ABC-1234"

result = re.search(r"([A-Z]+)-(\d+)", text)

print(result.group(0))
print(result.group(1))
print(result.group(2))