import re

text = "book 120 pen 30 bag 450"
result = re.finditer(r"\d+", text)

for match in result:
    print(f"값: {match.group()}, 시작 위치: {match.start()}, 끝 위치: {match.end()}")