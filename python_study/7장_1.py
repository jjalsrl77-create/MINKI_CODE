import re

text = "주문번호는 AB-12345입니다."

result = re.search(r"[A-Z]{2}-\d{5}", text)

if result:
    print("주문번호를 찾았습니다:", result.group())