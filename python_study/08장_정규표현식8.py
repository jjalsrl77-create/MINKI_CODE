import re

text1 = "apple 100 banana 200"
text2 = "cherry 300 melon 400"

pattern = re.compile(r"\d+")

result1 = pattern.findall(text1)
result2 = pattern.findall(text2)

print(result1)
print(result2)