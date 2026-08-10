import re

text = "비밀번호는 abc123입니다."

result = re.sub(r"\d", "*", text)

print(result)