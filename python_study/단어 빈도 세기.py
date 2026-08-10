def count_words(sentence):
    counts = {}
    words = sentence.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


sentence = input("문장을 입력하세요: ")

result = count_words(sentence)

print(result)