number = int(input("숫자를 입력하세요: "))

alist = []

for k in range(1, number + 1):
    if k % 2 == 0:
        alist.append(k)

print(alist)