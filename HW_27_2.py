# 2. Напишите функцию, которая принимает на вход список функций и значение, а затем
# применяет композицию этих функций к значению, возвращая конечный результат.

# Пример использования:

# add_one = lambda x: x + 1

# double = lambda x: x * 2

# subtract_three = lambda x: x - 3

# functions = [add_one, double, subtract_three]
# compose_functions(functions, 5) должно вывести 9

def apply_operations(ops, value):
    result = value
    for operation in ops:
        result = operation(result)
    return result


def increment(x): return x + 1
def multiply_by_two(x): return x * 2
def decrease_by_three(x): return x - 3


operations = [increment, multiply_by_two, decrease_by_three]

print(apply_operations(operations, 5))
