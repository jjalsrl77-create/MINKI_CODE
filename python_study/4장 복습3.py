def cal(a, b, oper):
    if oper == "+":
        return a + b
    elif oper == "-":
        return a - b
    elif oper == "*":
        return a * b
    elif oper == "/":
        return a / b
    else:
        return "지원하지 않는 연산자입니다."
    
print(cal(10, 5, "+"))
print(cal(10, 5, "-"))
print(cal(10, 5, "*"))
print(cal(10, 5, "/"))