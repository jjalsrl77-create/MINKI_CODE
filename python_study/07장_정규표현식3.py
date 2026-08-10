import re

text = "문의: test@gmail.com, 관리자: admin@naver.com"
emails = re.findall(r"[a-z]+@[a-z]+\.[a-z]+", text)

print(emails)