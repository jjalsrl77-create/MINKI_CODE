import re

text = "연락처: 010-9876-5432"

result = re.search(r"\d{3}-\d{4}-\d{4}", text)

if result:
    print("연락처를 찾았습니다:", result.group())