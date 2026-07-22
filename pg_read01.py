from db import get_conn

# python 讀取 postgreSQL 資料
sql_str = """
SELECT id, name, price FROM products 
WHERE stock > %s ORDER BY price ASC
"""
params = (100, )

with get_conn() as conn:
    with conn.cursor() as cursor:
        cursor.execute(sql_str, params)
        rows = cursor.fetchall()

# 處理得到的資料
for row in rows:
    print(row[0], row[1], row[2])