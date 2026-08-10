# 1번
sentence = "Python is Easy and PYTHON is Fun"

print("전체 문자 수:", len(sentence))
print("공백 제외 문자 수:", len(sentence.replace(" ", "")))

words = sentence.split()
print("단어 수:", len(words))

lower_words = [word.lower() for word in words]
unique_words = set(lower_words)

print("중복 제거 단어 수:", len(unique_words))
print("첫 번째 단어:", words[0])
print("마지막 단어:", words[-1])
print("소문자 단어 리스트:", lower_words)

# 2번
inventory = {
    "사과": 10,
    "바나나": 5,
    "오렌지": 8
}
name = input("과일 이름을 입력하세요: ")
num = int(input("수량을 입력하세요: "))

if name not in inventory:
    print("해당 과일이 재고에 없습니다.")
elif inventory[name] < num:
    print("재고가 부족합니다.")
elif inventory[name] == num:
    del inventory[name]
    print(f"{name} {num}개가 판매되었습니다. 재고가 모두 소진되었습니다.")
else:
    inventory[name] -= num
    print(f"{name} {num}개가 판매되었습니다. 남은 재고: {inventory[name]}개")

# 3번
class_a = {"민수", "지수", "철수", "영희"}
class_b = {"영희", "민수", "준호", "서연"}
common_stu = class_a.intersection(class_b)
print("두 반에 모두 속한 학생:", common_stu)
print(class_a)
print(class_b)
print(class_a.union(class_b))
only_stu = class_a.symmetric_difference(class_b) 
# symmetric_difference == ^(연산자)
print("하나의 반에만 속한 학생:", only_stu)