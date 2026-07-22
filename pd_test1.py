import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)

# 排序，多個欄位的排序
orders_df = pd.read_csv("orders.csv")
print(orders_df, "\n")

# 單一欄位排序
sorted_df = orders_df.sort_values("數量", ascending=False)
print(sorted_df, "\n")

# 複數欄位排序
sorted2_df = orders_df.sort_values(["數量", "單價"], ascending=[True, False])
print(sorted2_df, "\n")

# 找出缺失值
clubs_df = pd.read_csv("clubs.csv")
print(clubs_df, "\n")
print(clubs_df.isna(), "\n")
print(clubs_df.isna().sum(), "\n")

# 缺失值處理1: 刪除該筆資料
clean1_df = clubs_df.dropna(subset=["社團", "是否繳費"])
print(clean1_df, "\n")