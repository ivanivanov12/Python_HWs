# 2. Напишите функцию, которая принимает на вход список чисел и возвращает сумму
# квадратов только четных чисел из списка, используя функциональные подходы
# (например, map, filter и reduce).

# Пример вывода:

# Введите числа: 4, 6, 3, 4, 2, 3, 9, 0, 7

# Результат: 72

from functools import reduce


def square_sum(s):
    filtr = filter(lambda x: x % 2 == 0, s)
    square_map = map(lambda x: x * x, filtr)
    return reduce(lambda x, y: x + y, square_map, 0)


result = list(map(int, input("Введите список чисел: ").split(",")))

print("Результат:", square_sum(result))
