from db import get_conn
import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)

# python 讀取 postgreSQL 資料做為 pandas DataFrame
sql_str = """
SELECT * FROM products ORDER BY id
"""

with get_conn() as conn:
    products_df = pd.read_sql_query(sql_str, conn)

products_df = products_df.rename(columns={
    "id": "編號",
    "name": "品名",
    "price": "單價",
    "stock": "庫存",
    "category_id": "分類"
})

print(products_df)