fruits = ["사과", "바나나", "포도"]

def choice(i):
    if i < 0 or i >= len(fruits):
        raise IndexError

    return fruits[i]

try:
    index = int(input("인덱스를 입력하세요: "))
    result = choice(index)

    print(f"선택한 과일: {result}")

except ValueError:
    print("인덱스는 숫자로 입력해주세요.")

except IndexError:
    print("존재하지 않는 위치입니다.")