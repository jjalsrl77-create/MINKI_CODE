def remove_duplicates(sentence):
    duplicate = []
    words = sentence.split()

    for word in words:
        if word not in words:
            result.append(word)

    return result

sentence = input("문장을 입력하세요: ")

result = remove_duplicates(sentence)

print(result)