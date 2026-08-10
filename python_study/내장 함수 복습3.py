names = ["민수", "지수", "철수"]
scores = [90, 85, 78]

for number, data in enumerate(zip(names, scores), start = 1):
    name, score = data
    print(f"{number}번 {name}: {score}점")