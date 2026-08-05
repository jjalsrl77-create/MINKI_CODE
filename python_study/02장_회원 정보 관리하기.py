members = []

for k in range(2):
    name = input(f"{k + 1}번째 회원 이름을 입력하세요: ")
    age = int(input(f"{k + 1}번째 회원 나이를 입력하세요: "))

    hobbies = []

    for i in range(2):
        hobby = input(f"{i + 1}번째 취미를 입력하세요: ")
        hobbies.append(hobby)

    member_info = {
        "이름": name,
        "나이": age,
        "취미": hobbies
    }

    members.append(member_info)

print(members)