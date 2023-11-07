import numpy as np

'''
使用arange函数生成一个1到9数字的3 X 3数组a1和一个1到3数字的一维数组a2，通过numpy的broadcast生成数组c2,c2的数组打印结果如下:
[[ 2  4  6]
 [ 5  7  9]
 [ 8 10 12]]
'''
a2 = np.arange(1,10).reshape(3, 3)
b2 = np.arange(1,4)
c2 = a2+b2
print('广播c2数组:')
print(c2)