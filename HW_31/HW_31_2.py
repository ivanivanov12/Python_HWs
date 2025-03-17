# 2. Напишите декоратор log_args, который будет записывать аргументы и
# результаты вызовов функции в лог-файл. Каждый вызов функции должен быть
# записан на новой строке в формате "Аргументы: <аргументы>, Результат:
# <результат>". Используйте модуль logging для записи в лог-файл.

# Убедитесь, что перед запуском кода у вас создан файл log.txt в той же
# директории, где находится скрипт Python.

import logging

log_level = logging.INFO
log_handlers = [logging.FileHandler('mylog.log')]
logging.basicConfig(level=log_level, handlers=log_handlers)


def log_decorator(target_function):
    def decorated_function(*parameters):
        result = target_function(*parameters)
        logging.info(f'Аргументы {parameters}, результат {result}')
        return result
    return decorated_function
