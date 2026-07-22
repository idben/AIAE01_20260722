from db import get_conn
from psycopg.rows import dict_row

# python 更新 postgreSQL 資料

sql_str = """
UPDATE products SET price = %s WHERE id = %s
"""
params = (2100, 3)

with get_conn() as conn:
    with conn.cursor(row_factory=dict_row) as cursor:
        cursor.execute(sql_str, params)
        print(f"受影響的筆數: {cursor.rowcount}")
    conn.commit()
