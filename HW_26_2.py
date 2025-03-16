# 2. Напишите программу, которая принимает в качестве аргумента командной строки
# путь к директории и выводит список всех файлов и поддиректорий внутри этой
# директории. Для этой задачи используйте модуль os и его функцию walk. Программа
# должна выводить полный путь к каждому файлу и директории.

import os
import sys

if len(sys.argv) < 2:
    print("Error: No target directory provided.")
    print("Usage: python script.py <target_directory>")
else:
    target_directory = sys.argv[1]

    if not os.path.exists(target_directory):
        print(f"Error: The directory '{target_directory}' does not exist.")
    else:
        os.chdir(target_directory)
        current_directory = os.getcwd()

        for folder_path, subfolders, files in os.walk(current_directory):
            for file_name in files:
                print(os.path.join(folder_path, file_name))
