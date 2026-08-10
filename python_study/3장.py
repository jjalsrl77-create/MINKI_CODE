# continue는 현재 반복의 남은 코드를 건너뛰고 
# 다음 반복으로 넘어갑니다.
for number in [1, 2, 3, 4]:
    if number == 3:
        continue
    print(number)

# 1번
alist = ["A", "B", "C", "D", "F"]
score = int(input("점수를 입력하세요: "))
if 90 <= score <= 100:
    print(alist[0])
elif 80 <= score < 90:
    print(alist[1])
elif 70 <= score < 80:
    print(alist[2])
elif 60 <= score < 70:
    print(alist[3])
elif 0 <= score < 60:
    print(alist[4])
else:
    print("잘못된 점수입니다.")

# 2번
blist = 0
for k in range(1, 101):
    if k % 5 == 0:
        continue
    elif k % 3 == 0:
        blist += k
print(blist)

# 3번
password = "python123"
while True:
    password1 = input("비밀번호를 입력하세요: ")
    if password1 != password:
        print("비밀번호가 틀렸습니다.")
    else:
        print("로그인 성공!")
        break
