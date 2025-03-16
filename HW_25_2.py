# 2. Напишите программу, которая будет считывать данные о продуктах из файла и
# использовать аннотации типов для аргументов и возвращаемых значений функций.
# Создайте текстовый файл "products.txt", в котором каждая строка будет
# содержать информацию о продукте в формате "название, цена, количество".
# Например:

# Apple, 1.50, 10

# Banana, 0.75, 15

# В программе определите функцию calculate_total_price, которая будет принимать
# список продуктов и возвращать общую стоимость. Продумайте, какая аннотация
# должна быть у аргумента! Считайте данные из файла, разделите строки на
# составляющие и создайте список продуктов. Затем вызовите функцию
# calculate_total_price с этим списком и выведите результат.

# Начиная с этого дз мы потихоньку отказываемся от формата ожидаемого
# ввода-вывода. Потому что в реальных задачах обычно этого нет. Нужно самому
# придумывать даже самые простые тестовые данные, содержимое тестовых файлов и
# т.п. В случае с классами (будут чуть позже) особенно.

from typing import List, Tuple


def compute_total_cost(items: List[Tuple[str, float, int]]) -> float:

    total_cost = 0
    for item in items:
        total_cost += item[1] * item[2]
    return total_cost


try:

    with open("products.txt", "r") as file:
        file_data = [line.strip().split(", ") for line in file.readlines()]

    processed_data = []
    for entry in file_data:
        if len(entry) == 3:
            try:
                name = entry[0]
                price = float(entry[1])
                quantity = int(entry[2])
                processed_data.append((name, price, quantity))
            except ValueError:
                print(f"Ошибка преобразования данных: {entry}")
        else:
            print(f"Некорректная строка: {entry}")

    print(f"Общая стоимость: {compute_total_cost(processed_data):.2f}")

except FileNotFoundError:
    print("Файл products.txt не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
