import re

text = "apple 100 banana 200 cherry 300"
numbers = re.findall(r"\d+", text)

words = re.findall(r"[a-z]+", text)

print(numbers)
print(words)