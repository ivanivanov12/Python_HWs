# В базе данных ich_edit три таблицы. Users с полями (id, name, age),
# Products с полями (pid, prod, quantity) и Sales с полями (sid, id, pid).

# Программа должна вывести все имена из таблицы users, дать пользователю
# выбрать одно из них и вывести все покупки этого пользователя.
import mysql.connector

db_config = {
    'host': 'ich-edit.edu.itcareerhub.de',
    'user': 'ich1',
    'password': 'ich1_password_ilovedbs',
    'database': 'ich_edit'
}

table_info = {
    "Users": ["id", "name", "age"],
    "Products": ["pid", "prod", "quantity"],
    "Sales": ["sid", "pid", "id"]
}
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()
cursor.execute("SELECT DISTINCT name FROM Users")
result = cursor.fetchall()
names = [res[0] for res in result]
print("В таблице users есть пользователи: ")
print(*names, sep=", ")
name = input("Выберите одного из них: ")
if name not in names:
    print("Такого пользователя нет")
else:
    cursor.execute("""
        SELECT Users.name,
        Users.age, Products.prod FROM Users JOIN
        Sales ON Users.id=Sales.id JOIN Products ON
        Products.pid=Sales.pid WHERE Users.name=%s
""", (name,))
result = cursor.fetchall()
if len(result) == 0:
    print(f"У пользователя {name} нет покупок")
else:
    print("ИМЯ\t\tВОЗРАСТ\t\tТОВАР ")
for row in result:
    print(*row, sep="\t\t")
cursor.close()
connection.close()
