def check_pass(score):
    if score >= 60:
        return "합격"
    else:
        return "불합격"

score = int(input("점수를 입력하세요: "))
result = check_pass(score)
print(f"결과: {result}")