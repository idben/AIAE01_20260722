import pandas as pd
import matplotlib.pyplot as plt
pd.set_option("display.unicode.east_asian_width", True)
plt.rcParams["font.sans-serif"] = ["PingFang HK", "Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False

# 從資料讀取到分析到繪圖
orders_df = pd.read_csv("orders3.csv")
orders_df["總金額"] = orders_df["數量"] * orders_df["單價"]


summary_df = (
    orders_df
    .groupby("商品")["總金額"]
    .sum()
    .reset_index()
    .rename(columns={"總金額": "總銷售額"})
)

print(summary_df["商品"])
print(summary_df["總銷售額"])

# 長條圖
plt.bar(summary_df["商品"], summary_df["總銷售額"])
plt.title("各商品銷售額")
plt.xlabel("商品")
plt.ylabel("\n".join("總銷售額"), rotation=0, labelpad=10, va="center")
plt.grid(axis="y") 
plt.show()
