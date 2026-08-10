import re

text = "100원 200달러 300원 400엔"

result = re.findall(r"\d+(?![\d원])", text)

print(result)