# 1. Реализовать класс Counter, который представляет счетчик. Класс должен
# поддерживать следующие операции:

# - Увеличение значения счетчика на заданное число (оператор +=)

# - Уменьшение значения счетчика на заданное число (оператор -=)

# - Преобразование счетчика в строку (метод __str__)

# - Получение текущего значения счетчика (метод __int__)

class Counter:
    def __init__(self, start_value):
        self.value = start_value

    def __add__(self, step):
        self.value += step
        return Counter(self.value)

    def __sub__(self, step):
        self.value -= step
        return Counter(self.value)

    def __str__(self):
        return f"Counter: {self.value}"

    def __int__(self):
        return self.value
