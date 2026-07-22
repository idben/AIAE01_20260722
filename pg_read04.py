from db import get_conn
import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)

# python 讀取 postgreSQL 資料做為 pandas DataFrame 的資料夾源
sql_str = """
SELECT * FROM products ORDER BY id
"""

with get_conn() as conn:
    products_df = pd.read_sql_query(sql_str, conn)


print(products_df)