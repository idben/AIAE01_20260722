import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)

# merge 合併兩份資料
orders_df = pd.read_csv("order_items.csv")
products_df = pd.read_csv("products.csv")

merged_df = orders_df.merge(products_df, on="商品編號", how="inner")
merged_df["小計"] = merged_df["數量"] * merged_df["單價"]

print(merged_df, "\n")

category_summary_df = (
    merged_df
    .groupby("分類")
    .agg(
        總數量=("數量", "sum"),
        總銷售額=("小計", "sum"),
        訂單筆數=("訂單編號", "count"),
    )
    .reset_index()
    .sort_values("總銷售額", ascending=False)
)
print(category_summary_df, "\n")