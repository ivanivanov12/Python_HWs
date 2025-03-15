# 1. Напишите функцию get_response(url), которая отправляет GET-запрос по
# заданному URL-адресу и возвращает объект ответа. Затем выведите следующую
# информацию об ответе:

# - Код состояния (status code)

# - Текст ответа (response text)

# - Заголовки ответа (response headers)


# Пример использования:


# url = "https://api.example.com"

# response = get_response(url)


# print("Status Code:", response.status_code)

# print("Response Text:", response.text)

# print("Response Headers:", response.headers)

import requests


def fetch_data(link):
    response_data = requests.get("https://" + link)
    print(response_data.status_code)
    print(response_data.text)
    print(response_data.headers)


user_input = input("Введите URL-адрес: ")
fetch_data(user_input)
