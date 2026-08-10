import random

dice = random.randint(1,6)

print(f"주사위 결과: {dice}")

if dice >= 4:
    print("승리!")
else:
    print("패배!")