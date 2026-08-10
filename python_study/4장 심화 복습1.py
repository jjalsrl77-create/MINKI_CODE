def cal(s):
    result = {
        "total": sum(s),
        "average": sum(s) / len(s),
        "max": max(s),
        "min": min(s)
    }
    return result

scores = [70, 85, 90, 60, 95]

result = cal(scores)

print(f"총점: {result['total']}")
print(f"평균: {result['average']}")
print(f"최고 점수: {result['max']}")
print(f"최저 점수: {result['min']}")