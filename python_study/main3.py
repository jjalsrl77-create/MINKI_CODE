import temperature as temp

choice = input("변환 방향을 입력하세요 (1: 섭씨→화씨, 2: 화씨→섭씨): ")
temperature = float(input("온도를 입력하세요: "))

if choice == "1":
    result = temp.celsius_to_fahrenheit(temperature)
    print(f"변환 결과: {result}")

elif choice == "2":
    result = temp.fahrenheit_to_celsius(temperature)
    print(f"변환 결과: {result}")

else:
    print("올바른 번호를 입력하세요.")