def fru(index):
    if index < 0 or index >= len(fruits):
        raise IndexError("해당 인덱스의 과일이 없습니다.")

    return fruits[index]


try:
    fruits = ["사과", "바나나", "오렌지"]
    index = int(input("인덱스를 입력하세요: "))

    result = fru(index)

except ValueError:
    print("정수를 입력하세요.")

except IndexError as error:
    print(error)

else:
    print(f"선택한 과일: {result}")