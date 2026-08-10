import re

text = "010-1234-5678"

result = re.sub(r"(\d{3})-(\d{4})-(\d{4})", r"\1.\2.\3", text)

print(result)