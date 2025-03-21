# В базе данных ich_edit три таблицы. Users с полями (id, name, age), Products
# с полями (pid, prod, quantity) и Sales с полями (sid, id, pid).

# Программа должна запросить у пользователя название таблицы и вывести все ее
# строки или сообщение, что такой таблицы нет.
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

table_name = input("Введите название таблицы: ")

if table_name not in table_info.keys():
    print("Такой таблицы нет в БД")
else:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    sql_query = f"SELECT * FROM {table_name}"
    cursor.execute(sql_query)
    query_result = cursor.fetchall()
    print(*table_info[table_name], sep="\t\t")

    for record in query_result:
        print(*record, sep="\t\t")
    cursor.close()
    connection.close()
