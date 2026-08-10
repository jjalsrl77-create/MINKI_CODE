def find_longest_word(sentence):
    words = sentence.split()

    longest_word = ""

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word


sentence = input("문장을 입력하세요: ")

result = find_longest_word(sentence)

print(f"가장 긴 단어: {result}")
print(f"글자 수: {len(result)}")