# 1번
answer = 37
while True:
    user_answer = int(input("정답을 입력하세요: "))
    count += 1
    if user_answer < answer:
        print("더 큰 수입니다.")
    elif user_answer > answer:
        print("더 작은 수입니다.")
    else:
        print("정답입니다!")
        break
print("시도 횟수: ", count)

# 2번
num = int(input("정수를 입력하세요: "))
for k in range(2, num):
    if num % k ==0:
        print("소수가 아닙니다..")
        break
    else:
        print("소수입니다.")

# 3번
start = int(input("시작 단을 입력하세요: "))
end = int(input("끝 단을 입력하세요: "))

if start > end:
    print("시작 단이 끝 단보다 큽니다.")
elif start < 2 or end > 9:
    print("2~9 사이의 정수를 입력하세요.")
else:
    for dan in range(start, end + 1):
        print(f"\n[{dan}단]")

        for number in range(1, 10):
            print(f"{dan} × {number} = {dan * number}")