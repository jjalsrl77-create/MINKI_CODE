import re

text = "test@gmail.com admin@naver.com user@daum.net"

ids = re.findall(r"(\w+)@\w+\.\w+", text)

result = [id.upper() for id in ids]

print(result)