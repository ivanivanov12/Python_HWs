# 1. Напишите декоратор validate_args, который будет проверять типы аргументов
# функции и выводить сообщение об ошибке, если переданы аргументы неправильного
# типа. Декоратор должен принимать ожидаемые типы аргументов в качестве
# параметров

def validate_types(*expected_types):
    def decorator(function_to_wrap):
        def wrapped_function(*arguments):
            for index in range(len(expected_types)):
                if not isinstance(arguments[index], expected_types[index]):
                    raise TypeError("Неверные типы данных")
            function_to_wrap(*arguments)
        return wrapped_function
    return decorator
