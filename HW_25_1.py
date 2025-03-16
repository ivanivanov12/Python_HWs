# 1. Напишите функцию find_longest_word, которая будет принимать список слов и
# возвращать самое длинное слово из списка. Аннотируйте типы аргументов и
# возвращаемого значения функции.


# Пример вызова функции и ожидаемого вывода:


# words = ["apple", "banana", "cherry", "dragonfruit"]

# result = find_longest_word(words)

# print(result)  # Ожидаемый вывод: "dragonfruit"

from typing import List


def longest_word_in_list(word_list: List[str]) -> str:
    return max(word_list, key=len)


fruits = ["apple", "banana", "cherry", "dragonfruit"]
longest_fruit = longest_word_in_list(fruits)
print(longest_fruit)
