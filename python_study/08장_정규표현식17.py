import re

text = "<html><body>hello</body></html>"
result1 = re.findall(r"<.*>", text)
result2 = re.findall(r"<.*?>", text)

print(result1, result2)