def get_average(scores):
    total = sum(scores)
    average = total / len(scores)
    return average

scores = []

for k in range(3):
    score = int(input("점수를 입력하세요: "))
    scores.append(score)

average = get_average(scores)
print(f"평균 점수: {average}")