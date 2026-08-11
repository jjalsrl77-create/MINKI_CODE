import re

text = "cat category dog catalog bird"

animal = re.findall(r"\bcat\b", text)

result = [len(animals) for animals in animal]

print(result)