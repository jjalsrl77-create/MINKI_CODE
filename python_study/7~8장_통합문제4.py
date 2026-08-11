import re

text = "score: 70, 85, 90, 100"

grade = re.findall(r"\d+", text)

result = list(map(lambda x: int(x) + 10, grade))

print(result)