# 2. Реализовать класс Email, представляющий электронное письмо. Класс должен
# поддерживать следующие операции:

# - Сравнение писем по дате (операторы <, >, <=, >=, ==, !=)

# - Преобразование письма в строку (метод __str__)

# - Получение длины текста письма (метод __len__)

# - Получение хеш-значения письма (метод __hash__)

# - Проверка наличия текста в письме (метод __bool__)

import datetime
import functools


@functools.total_ordering
class Email:
    def __init__(self, date_str, recipient, subject, body):
        self.date = datetime.date(*map(int, date_str.split("-")))
        self.recipient = recipient
        self.subject = subject
        self.body = body

    def __eq__(self, other):
        return self.date == other.date

    def __lt__(self, other):
        return self.date < other.date

    def __str__(self):
        return (
            f"Date: {self.date}\n"
            f"To: {self.recipient}\n"
            f"Subject: {self.subject}\n"
            f"Body: {self.body}"
        )

    def __len__(self):
        return len(self.body)

    def __hash__(self):
        return hash(self.body) + hash(self.subject) + hash(self.recipient) + hash(self.date)

    def __bool__(self):
        return bool(self.body)
