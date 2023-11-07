import numpy as np
from matplotlib import pyplot as plt
import matplotlib

x = np.arange(2,11)
print('x矩阵:')
print(x)
print('y矩阵:')
y = 2 * x + 5
print(y)
print('生成matplot')
plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x,y)
plt.show()
print('-----------------------------------------------------')
'''
x矩阵:
[ 2  3  4  5  6  7  8  9 10]
y矩阵:
[ 9 11 13 15 17 19 21 23 25]
生成matplot
'''

'''
图形中文显示
Matplotlib 默认情况不支持中文，将simhei.ttf文件放在当前执行的代码文件中
'''
zhfont = matplotlib.font_manager.FontProperties(fname="simhei.ttf")
x = np.arange(2, 11)
y = 2 * x + 5
plt.title("中文标题", fontproperties=zhfont)
# fontproperties 设置中文显示，fontsize 设置字体大小
plt.xlabel("x 轴", fontproperties=zhfont)
plt.ylabel("y 轴", fontproperties=zhfont)
plt.plot(x,y)
plt.show()
print('-----------------------------------------------------')
'''
x矩阵:
[ 2  3  4  5  6  7  8  9 10]
y矩阵:
[ 9 11 13 15 17 19 21 23 25]
生成matplot
'''

# 显示已安装的系统字体
a=sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])
for i in a:print(i)
print('-----------------------------------------------------')

# 点线图
x = np.arange(2,11)
y =  2  * x +  5
plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x,y,"ob")
plt.show()
print('-----------------------------------------------------')

# 正弦波
# 计算正弦曲线上点的 x 和 y 坐标
x = np.arange(0,3*np.pi,0.1)
y = np.sin(x)
plt.title("sine wave form")
plt.plot(x, y)
plt.show()
print('-----------------------------------------------------')

#subplot()绘制正弦和余弦值
# 计算正弦和余弦曲线上的点的 x 和 y 坐标
x = np.arange(0,3* np.pi,0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
# 建立 subplot 网格，高为 2，宽为 1
# 激活第一个 subplot
plt.subplot(2,1,1)
# 绘制第一个图像
plt.plot(x, y_sin)
plt.title('Sin')
# 将第二个 subplot 激活，并绘制第二个图像
plt.subplot(2,1,2)
plt.plot(x, y_cos)
plt.title('Cos')
# 展示图像
plt.show()
print('-----------------------------------------------------')

#pyplot子模块提供bar()函数来生成条形图
x = [5,8,10]
y = [12,16,6]
x2 = [6,9,11]
y2 = [6,15,7]
plt.bar(x,y,align='center')
plt.bar(x2,y2,color='gray',align='center')
plt.title('Bar graph')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()
print('-----------------------------------------------------')

'''
numpy.histogram()函数是数据的频率分布的图形表示。 水平尺寸相等的矩形对应于类间隔，称为bin，变量height对应于频率。
numpy.histogram()函数将输入数组和bin作为两个参数。 bin数组中的连续元素用作每个bin的边界。
'''
#histogram图例1
a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
plt.hist(a,bins=[0,20,40,60,80,100])
plt.title("histogram")
plt.show()
print('-----------------------------------------------------')

#histogram图例2
#生成一些随机数
rng=np.random.RandomState(10) #使用RandomState获得随机数生成器
data1=rng.normal(size=50)
data2=rng.normal(size=100)
binrange=[-1,0,2] # 设置区间, 分别是[-1,0]和[0,2]
hist1,_ = np.histogram(data1, bins=binrange)
hist2,_ = np.histogram(data2, bins=binrange)
# 绘制图像
fig, ax1 = plt.subplots()
fig.set_size_inches(10, 6)
# plt.set_cmap('RdBu') #set_cmap()方法更改现有的绘图对象的色图
x = np.arange(len(binrange)-1)*3
w=0.3
# 绘制多个bar在同一个图中, 这里需要控制width
plt.bar(x-w,hist1,width=2*w,align='center')
plt.bar(x+w,hist2,width=2*w,align='center')
# 设置坐标轴的标签
ax1.yaxis.set_tick_params(labelsize=15) # 设置y轴的字体的大小
ax1.set_xticks(x) # 设置xticks出现的位置
# 设置坐标轴名称
ax1.set_ylabel("Count", fontsize='xx-large')
# 设置标题
ax1.set_title('The Distribution of Normal1 Data and Normal2 Data', fontsize='x-large')
# 设置图例
plt.legend(('Normal1','Nomral2'),fontsize = 'x-large', loc='upper right')
plt.show()
print('-----------------------------------------------------')