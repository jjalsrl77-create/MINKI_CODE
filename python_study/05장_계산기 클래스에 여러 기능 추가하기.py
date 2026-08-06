class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


cal = Calculator()

print(f"더하기: {cal.add(10, 5)}")
print(f"빼기: {cal.sub(10, 5)}")
print(f"곱하기: {cal.mul(10, 5)}")
print(f"나누기: {cal.div(10, 5)}")