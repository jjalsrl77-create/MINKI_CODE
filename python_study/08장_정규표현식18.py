import re

text = "apple 100 banana 200 cherry 300"
result = re.sub(r"\d+", "NUMBER", text)

print(result)