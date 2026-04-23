# Автор: Андрей Аксенов
import math
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b

def sqrt(x):
    if x < 0:
        raise ValueError("Квадратный корень из отрицательного числа не определён")
    return math.sqrt(x)

if __name__ == "__main__":
    print("Простой калькулятор запущен.")
    print(f"2 + 2 = {add(2, 2)}")
    # Тесты для новых функций:
    print(f"3 * 4 = {multiply(3, 4)}")
    print(f"sqrt(16) = {sqrt(16)}")