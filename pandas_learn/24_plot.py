import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randn(10,4),index=pd.date_range('2020/1/18',periods=10), columns=list('ABCD'))
df.plot()
plt.show()

#柱形图
df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
df.plot.bar()
plt.show()

#堆积柱形图
df.plot.bar(stacked=True)
plt.show()

#水平柱形图
df.plot.barh(stacked=True)
plt.show()

#直方图
df = pd.DataFrame({'a':np.random.randn(1000)+1,'b':np.random.randn(1000),'c':np.random.randn(1000)-1},columns=['a','b','c'])
df.plot.hist(bins=20)
plt.show()

#分开的直方图
df.hist(bins=20)
plt.show()

#箱形图
df = pd.DataFrame(np.random.rand(10,5),columns=['A','B','C','D','E'])
df.plot.box()
plt.show()

#区域块图形
df = pd.DataFrame(np.random.rand(10, 4), columns=['a','b','c','d'])
df.plot.area()
plt.show()

#散点图形
df = pd.DataFrame(np.random.rand(50,4),columns=['a','b','c','d'])
df.plot.scatter(x='a',y='b')
plt.show()

#饼状图
df = pd.DataFrame(3*np.random.rand(4),index=['a','b','c','d'],columns=['x'])
df.plot.pie(subplots=True)
plt.show()
