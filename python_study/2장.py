sentence = "python is easy and python is fun"
print(len(sentence))
print(sentence.count("python"))
print(sentence.upper())

#split()은 공백을 기준으로 문자열을 나눠 리스트를 만들고
#set()은 그 리스트에서 중복을 제거합니다.
sentence = "python is easy and python is fun"

print(len(sentence))
print(sentence.count("python"))
print(sentence.upper())

words = sentence.split()
print(words)

unique_words = set(words)
print(unique_words)

#3번
scores = {
    "민수": 80,
    "지수": 95,
    "철수": 70
}
print(scores["지수"])
scores["철수"] = 75
scores["영희"] = 88
print(scores.keys())
print(scores.values())
scores1 = sum(scores.values())
print(scores1)