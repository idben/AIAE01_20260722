from db import get_conn
from psycopg.rows import dict_row

# python 讀取 postgreSQL 資料
# 處理 join 資料表
sql_str = """
SELECT products.name AS product_name, 
categories.name AS category_name, products.price 
FROM products 
JOIN categories ON products.category_id = categories.id 
ORDER BY products.price DESC
"""

with get_conn() as conn:
    with conn.cursor(row_factory=dict_row) as cursor:
        cursor.execute(sql_str)
        rows = cursor.fetchall()

# 處理得到的資料
for row in rows:
    print(row["product_name"], row["category_name"], row["price"])