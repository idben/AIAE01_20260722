from db import get_conn
from psycopg.rows import dict_row

# python 讀取 postgreSQL 資料
# 以 dict 的格式呈現得到的資料
sql_str = """
SELECT id, name, price FROM products 
WHERE stock > %s ORDER BY price ASC
"""
params = (100, )

with get_conn() as conn:
    with conn.cursor(row_factory=dict_row) as cursor:
        cursor.execute(sql_str, params)
        rows = cursor.fetchall()

# 處理得到的資料
for row in rows:
    print(row["id"], row["name"], row["price"])