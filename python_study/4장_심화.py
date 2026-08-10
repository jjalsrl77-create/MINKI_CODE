def get_statistics(*numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    maximum = max(numbers)
    minimum = min(numbers)
    return total, average, maximum, minimum

number = list(map(int, input("정수를 입력하세요: ").split()))
total, average, maximum, minimum = get_statistics(*number)
print(f"합계: {total}, 평균: {average}, 최대값: {maximum}, 최소값: {minimum}")
#리스트를 함수에 하나의 인수로 전달하고 있다. 여러숫자를 받게 하려면 *를 붙여야 한다.
#받은 숫자가 0일 경우도 고려해야한다.
#리스트로 입력받고 튜플로 만들어 출력해야 한다.

def get_statistics(*numbers):
    if len(numbers) == 0:
        return {
            "total": 0,
            "average": 0,
            "maximum": 0,
            "minimum": 0,
            "count": 0
        }
    total = sum(numbers)
    count = len(numbers)

    return {
        "total": total,
        "average": total / count,
        "maximum": max(numbers),
        "minimum": min(numbers),
        "count": count
    }
user_input = input("정수를 입력하세요: ").strip()
if user_input:
    num = list(map(int, user_input.split()))
else:
    num = []
result = get_statistics(*num)

print("합계:", result["total"])
print("평균:", result["average"])
print("최대값:", result["maximum"])
print("최소값:", result["minimum"])
print("개수:", result["count"])

# 2번
def input_score():
    while True:
        try:
            score = int(input("점수를 입력하세요 (0~100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("점수는 0에서 100 사이여야 합니다.")
        except ValueError:
            print("유효한 정수를 입력하세요.")
        
score = input_score()
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# 3번
students = {"홍길동":  85,
            "김철수":  90,
            "이영희":  72
        }
with open("students.txt", "w") as f:
    for name, score in students.items():
        f.write(f"{name}: {score}\n")
print(students)
average = sum(students.values()) / len(students)
print(f"평균 점수: {average}")

maximum = max(students.values())
print(f"최고 점수: {maximum}")

for k in students:
    if students[k] >= 80:
        print(k, students[k])

# items()는 딕셔너리에서 키와 값을 한 쌍으로 함께 꺼내는 method