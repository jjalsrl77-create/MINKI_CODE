foods = []

for k in range(5):
    food = input("좋아하는 음식을 입력하세요: ")
    foods.append(food)

foods_list = {
    "음식 목록": foods,
    "첫번째 음식": foods[0],
    "마지막 음식": foods[-1],
    "음식 개수": len(foods)
}

print(foods_list)