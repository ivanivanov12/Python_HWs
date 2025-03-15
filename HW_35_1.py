# 1. Напишите программу, которая запрашивает у пользователя URL-адрес 
# веб-страницы, использует библиотеку Beautiful Soup для парсинга HTML и выводит 
# список всех ссылок на странице.

import requests


def fetch_data(link):
    response_data = requests.get("https://" + link)
    print(response_data.status_code)
    print(response_data.text)
    print(response_data.headers)


user_input = input("Введите URL-адрес: ")
fetch_data(user_input)
