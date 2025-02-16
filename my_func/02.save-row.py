"""
Функция save_row принимает соединение с БД (conn), название таблицы (table) и ряд данных для сохранения в
таблицу в виде словаря (row) с идентичными ключами. Сохраняет через плейсхолдер"""

from psycopg2.extras import DictCursor


def save_row(conn, table: str, row: dict):
    placeholders = ', '.join(f'%({k})s' for k in row)
    query = (f"""INSERT INTO {table}
              ({', '.join(row)}) VALUES ({placeholders})""")
    with conn.cursor(cursor_factory=DictCursor) as curs:
        curs.execute(query, row)


# conn = psycopg2.connect(dbname='hexlet', user='user')
# row = {'title': 'My New Post', 'content': 'text', 'author_id': 42}
# posts = 'posts'
# with conn.cursor(cursor_factory=DictCursor) as cursor:
#     query = "SELECT * FROM posts;"
#     cursor.execute(query)
#     print([dict(row) for row in cursor.fetchall()])
# save_row(conn, posts, row)
# with conn.cursor(cursor_factory=DictCursor) as cursor:
#     query = "SELECT * FROM posts;"
#     cursor.execute(query)
#     print([dict(row) for row in cursor.fetchall()])


