import re

text = "apple 100 banana 200 cherry 300"
words = re.findall(r"[a-z]+", text)

print(words)