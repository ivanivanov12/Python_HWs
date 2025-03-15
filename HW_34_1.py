# Напишите функцию extract_emails(text), которая извлекает все адреса
# электронной почты из заданного текста и возвращает их в виде списка.

# Пример использования:

# text = "Contact us at info@example.com or support@example.com for assistance."

# emails = extract_emails(text)

# print(emails)  # Вывод: ['info@example.com', 'support@example.com']

import re


def find_emails(data):
    email_list = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', data)
    return email_list


message = "Contact us at info@example.com or support@example.com for support."

for address in find_emails(message):
    print(address)
