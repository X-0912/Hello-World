from pandas import read_csv
import matplotlib.pyplot as plt
filename =r"D:\PC\数据可视化\实验2\flowingdata_subscribers.csv"
data = read_csv(filename)
print(data)

x = data['Date']
y = data['Subscribers']

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']


# 绘制散点图
plt.scatter(x, y, s=60, c='g', marker='o', alpha=0.6, label='Data')

plt.xlabel('Date')
plt.ylabel('Subscribers')
plt.title('FlowingData网站于2010年1月份的订阅者量')
plt.legend()
plt.grid(True)
plt.xticks(rotation=90)
plt.xticks(fontsize=6)  # 设置标签字体大小为8号
plt.show()
