from db import get_conn
from psycopg.rows import dict_row

# python 刪除 postgreSQL 資料

sql_str = """
DELETE FROM products WHERE id = %s
"""
params = (10,)

msg = "刪除失敗"

with get_conn() as conn:
    with conn.cursor(row_factory=dict_row) as cursor:
        cursor.execute(sql_str, params)
        if cursor.rowcount >= 1:
            msg = "刪除成功"
        print(f"刪除的筆數: {cursor.rowcount}")
    conn.commit()

print(msg)