import re

text = "전화번호: 010-1234-5678"

p = re.compile(r"""
\d{3}
-
\d{4}
-
\d{4}
""", re.VERBOSE)

result = p.findall(text)

print(result)