import re

text = "Python python PYTHON java"
result = re.findall(r"python", text, re.IGNORECASE)

print(result)