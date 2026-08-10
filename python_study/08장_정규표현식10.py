import re

text = "a\nb"
result = re.findall(r"a.b", text, re.DOTALL)

print(result)