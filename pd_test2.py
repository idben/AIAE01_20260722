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

# groupby 的統計資料型別是 Series
sales_by_name_df = (
    orders_df
    .groupby("飲料")["小計"]
    .sum()
    .reset_index()
)

sales_by_name_df = sales_by_name_df.rename(columns={"小計": "總銷售額"})
print(sales_by_name_df, "\n")

avg_qty_df = (
    orders_df
    .groupby("飲料")["數量"]
    .mean()
    .reset_index()
)
print(avg_qty_df, "\n")

order_count_df = (
    orders_df
    .groupby("飲料")["訂單編號"]
    .count()
    .reset_index()
)
order_count_df = order_count_df.rename(columns={"訂單編號": "訂單筆數"})
print(order_count_df, "\n")

# 一次看多種統計方法
summary_df = (
    orders_df
    .groupby("飲料")
    .agg(
        總數量=("數量", "sum"),
        平均數量=("數量", "mean"),
        訂單筆數=("訂單編號", "count"),
        總銷售額=("小計", "sum"),
    )
    .reset_index()
)
print(summary_df, "\n")

# 練習 1