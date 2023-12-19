# Вариант 9
# Задание 2
class Calculator:
    def __init__(self):
        pass
    def add(self, x, y):
        return x + y
    def subtract(self, x, y):
        return x - y
    def multiply(self, x, y):
        return x * y
    def divide(self, x, y):
        if y == 0:
            return "Ошибка деления на ноль!"
        else:
            return x / y

def input_data():
    x = float(input("Введите первое число: "))
    y = float(input("Введите второе число: "))
    return x, y

# Example usage
calc = Calculator()
x, y = input_data()
print("Сумма: ", calc.add(x, y))
print("Разница: ", calc.subtract(x, y))
print("Произведение: ", calc.multiply(x, y))
print("Деление: ", calc.divide(x, y))