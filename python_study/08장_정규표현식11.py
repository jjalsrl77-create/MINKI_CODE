import re

text = """python one
java two
python three"""

result = re.findall(r"^python", text, re.MULTILINE)

print(result)