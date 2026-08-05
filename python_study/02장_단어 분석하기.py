sentence = input("문장을 입력하세요: ")

words = sentence.split(" ")

word_count = len(words)

word_list = []
for word in words:
    word_list.append(word)

first_spell = word_list[0]

last_spell = word_list[-1]

result = {
    "전체 문장": sentence,
    "단어 수": word_count,
    "단어 목록": word_list,
    "첫 번째 단어": first_spell,
    "마지막 단어": last_spell
}

print(result)