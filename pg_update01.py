from db import get_conn
from psycopg.rows import dict_row

# python 更新 postgreSQL 資料

sql_str = """
UPDATE products SET price = %s WHERE id = %s
"""
params = (500, 3)

msg = "更新失敗"

with get_conn() as conn:
    with conn.cursor(row_factory=dict_row) as cursor:
        cursor.execute(sql_str, params)
        if cursor.rowcount >= 1:
            msg = "更新成功"
        print(f"受影響的筆數: {cursor.rowcount}")
    conn.commit() # read 為什麼不需要 conn.commit(), 因為 read 不需要寫入

print(msg)