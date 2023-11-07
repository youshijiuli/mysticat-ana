from matplotlib import pyplot as plt

'''
请根据如下柱形图的数字坐标标记生成该图形，图中柱形上的数字坐标标记无需生成。
'''
x = [7,8,9]
y = [10,11,12]
x2 = [13,14,15]
y2 = [16,17,18]
x3 = [19,20,21]
y3 = [22,23,24]
plt.bar(x,y,color='green',align='center')
plt.bar(x2,y2,color='red',align='center')
plt.bar(x3,y3,color='yellow',align='center')
plt.title('Bar graph')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()