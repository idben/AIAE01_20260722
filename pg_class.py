from db import get_conn
from psycopg.rows import dict_row
from dataclasses import dataclass

# 物件導向式重構 CRUD

@dataclass
class Product:
    id: int
    name: str
    price: float
    stock: int
    category_id: int

class ProductRepository:
    def __init__(self, get_conn):
        self.get_conn = get_conn

    def add(self, name, price, stock, category_id):
        with self.get_conn() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO products (name, price, stock, category_id) "
                    "VALUES (%s, %s, %s, %s) RETURNING id",
                    (name, price, stock, category_id),
                )
                new_id = cursor.fetchone()[0]
            conn.commit()
        return new_id

repo = ProductRepository(get_conn)
new_id = repo.add("無線滑鼠", 590, 120, 1)
print("新增產品 id：", new_id)
