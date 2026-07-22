import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)

orders_df = pd.read_csv("orders2.csv")
orders_df["小計"] = orders_df["數量"] * orders_df["單價"]
print(orders_df, "\n")

# 紅茶賣了多少杯? groupby
qty_by_name = orders_df.groupby("飲料")["數量"].sum()
print(qty_by_name, "\n")
sales_by_name = orders_df.groupby("飲料")["小計"].sum()
print(sales_by_name, "\n")
