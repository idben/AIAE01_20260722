import matplotlib.pyplot as plt
# 設定中文字型
plt.rcParams["font.sans-serif"] = ["PingFang HK", "Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False

days = ["週一", "週二", "週三", "週四", "週五", "週六", "週日"]
sales = [3200, 3500, 3300, 4100, 4800, 5200, 5000]
# 折線圖
plt.figure(figsize=(6, 4))  # 設定圖片尺寸, 數字 x 100 就是像素
plt.plot(days, sales, marker="o", label="每日銷售金額")       # 提供數據，畫什麼圖的依據
plt.title("一週的飲料銷售數據")   # 圖例的文字
plt.xlabel("星期")              # X方向代表的文字
# plt.ylabel("金額", rotation=0, labelpad=10)     # Y方向代表的文字 
# rotation: 旋轉角度  labelpad: 往左平移距離  va: 對齊方式
plt.ylabel("\n".join("金額"), rotation=0, labelpad=10, va="center") # 直書
plt.grid(True)                  # 開啟格線
plt.legend()                    # 左上角顯示圖例
plt.show()                      # 顯示圖片
