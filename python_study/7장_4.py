import re

text = "비밀번호는 abc123입니다."

result = re.sub(r"\d{3}-\d{4}-\d{4}", "****-****-****", text)

print(result)