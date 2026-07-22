import psycopg

# 共用的連線程式
# 以後 import 這支用 get_conn() 取得連線物件即可
conn_params = {
    "host": "localhost",
    "port": 5432,
    "dbname": "shop",
    "user": "postgres",
    "password": "a123456",
}

def get_conn():
    return psycopg.connect(**conn_params)