def get_priority_name(priority):
    if priority == 3:
        return "높음"
    elif priority == 2:
        return "보통"
    elif priority == 1:
        return "낮음"
    else:
        return "잘못된 중요도"

tasks = []

for i in range(3):
    title = input("할 일을 입력하세요: ")
    priority = int(input("중요도를 입력하세요(1~3): "))

    task = {
        "title": title,
        "priority": priority
    }

    tasks.append(task)


with open("tasks.txt", "w", encoding="utf-8") as file:
    for task in tasks:
        priority_name = get_priority_name(task["priority"])

        file.write(
            f"{task['title']} - 중요도: {priority_name}\n"
        )


with open("tasks.txt", "r", encoding="utf-8") as file:
    content = file.read()


print("저장된 할 일 목록:")
print(content)