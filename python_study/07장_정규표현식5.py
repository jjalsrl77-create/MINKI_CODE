import re

text = "I like python"
result1 = re.match(r"python", text)
result2 = re.search(r"python", text)

print(result1)
print(result2)