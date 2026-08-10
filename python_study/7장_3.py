import re

text = "사과 3개, 바나나 12개, 오렌지 5개"

result = re.findall(r"\d+", text)

if result:
    print("숫자를 찾았습니다:", result)