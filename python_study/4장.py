# 1번
def calculate(a, b, operator):
    if operator == "+":
        return a+b
    elif operator == "-":
        return a-b 
    elif operator == "*":
        return a*b
    elif operator == "/" :
        if b == 0:
            return "0으로 나눌 수 없습니다."
        return a/b
    else:
        return "지원하지 않는 연산입니다."
operator = input("연산자를 입력하세요: ")
a = int(input("첫 번째 숫자를 입력하세요: "))
b = int(input("두 번째 숫자를 입력하세요: "))
cal = calculate(a, b, operator)
print(cal)

# 2번
def get_average(scores):
    avg = sum(scores) / len(scores)
    return avg
scores = list(map(int, input("점수를 입력하세요(쉼표로 구분): ").split(",")))
average = get_average(scores)
print(average)

# 3번
diary = input("오늘의 일기를 입력하세요: ")

with open("diary.txt", "a", encoding="utf-8") as file:
    file.write(diary + "\n")
    file.close
with open("diary.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
