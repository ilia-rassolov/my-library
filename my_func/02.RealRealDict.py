"""Функция real_real_dict_cursor(curs, size=max) принимает cursor класса RealDictCursor, возвращает
список записей в виде словарей, где ключи - заголовки полей. Количество необходимых записей - size"""

import psycopg2
from psycopg2.extras import RealDictCursor


def real_real_dict_cursor(curs, size=max):
    if size == max:
        rows = curs.fetchall()
    else:
        rows = curs.fetchmany(size=size)
    result = []
    for row in rows:
        row_dict = {}
        for title in row:
            row_dict[title] = row[title]
        result.append(row_dict)
    return result


conn = psycopg2.connect(dbname='hexlet', user='user')
with conn.cursor(cursor_factory=RealDictCursor) as cursor:
    query = "SELECT * FROM posts;"
    cursor.execute(query)
    result = real_real_dict_cursor(cursor)
print(result)

# [{'id': 1, 'content': 'text', 'created_at': datetime.datetime(2024, ...)}, {'id': 2, 'content': 'It's...}]
