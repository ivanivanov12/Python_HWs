# 1. Напишите программу, которая принимает в качестве аргумента командной строки
# путь к файлу .py и запускает его. При запуске файла программа должна выводить
# сообщение "Файл <имя файла> успешно запущен". Если файл не существует или не
# может быть запущен, программа должна вывести соответствующее сообщение
# об ошибке.

import sys
import os.path


if len(sys.argv) < 2:
    print("Error: No file path provided. Please provide the path to a .py file.")
else:
    file_path = sys.argv[1]

    if os.path.exists(file_path):
        if os.path.isfile(file_path):
            if file_path.endswith(".py"):
                os.system("python " + file_path)
                print(f"File {file_path} is successfully executed.")
            else:
                print("Error: Not a .py file")
        else:
            print("Error: Path does not point to a file")
    else:
        print("Error: File does not exist")
