import re

text = "apple 100 banana 200 cherry 300"
result = re.finditer(r"\d+", text)

for k in result:
    print("값:", k.group())
    print("시작 위치:", k.start())
    print("끝 위치:", k.end())
    print("범위:", k.span())
    print()