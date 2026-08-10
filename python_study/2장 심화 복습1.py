sen = "Python is fun"

sen1 = sen.strip()
sen2 = len(sen)
sen3 = len(sen1.replace(" ", ""))
sen4 = sen.upper()

print(f"공백 제거 문장: {sen1}")
print(f"전체 글자 수: {sen2}")
print(f"공백을 제외한 글자 수: {sen3}")
print(f"대문자 문장: {sen4}")