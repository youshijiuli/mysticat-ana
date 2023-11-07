import numpy as np

'''
numpy.concatenate 函数用于沿指定轴连接相同形状的两个或多个数组
numpy.concatenate((a1, a2, ...), axis)
a1, a2, ...：相同类型的数组
axis：沿着它连接数组的轴，默认为 0
'''
a = np.array([[1,2],[3,4]])
print('第一个数组:')
print(a)
b = np.array([[5,6],[7,8]])
print('第二个数组:')
print(b)
# 两个数组的维度相同
print('沿轴0横向连接两个数组:')
print(np.concatenate((a,b)))
print('沿轴1纵向连接两个数组:')
print(np.concatenate((a,b),axis=1))
print('-----------------------------------------------------')
'''
第一个数组:
[[1 2]
 [3 4]]
第二个数组:
[[5 6]
 [7 8]]
沿轴0横向连接两个数组:
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
沿轴1纵向连接两个数组:
[[1 2 5 6]
 [3 4 7 8]]
'''

'''
numpy.stack函数用于沿新轴连接数组序列
numpy.stack(arrays, axis)
arrays相同形状的数组序列
axis：返回数组中的轴，输入数组沿着它来堆叠
'''
a = np.array([[1,2],[3,4]])
print('第一个数组:')
print(a)
b = np.array([[5,6],[7,8]])
print('第二个数组:')
print(b)
print('沿轴0堆叠两个数组:')
print(np.stack((a,b),0))
print('沿轴1堆叠两个数组:')
print(np.stack((a,b),1))
print('-----------------------------------------------------')
'''
第一个数组:
[[1 2]
 [3 4]]
第二个数组:
[[5 6]
 [7 8]]
沿轴0堆叠两个数组:
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
沿轴1堆叠两个数组:
[[[1 2]
  [5 6]]

 [[3 4]
  [7 8]]]
'''

#numpy.hstack是numpy.stack函数的变体通过水平堆叠来生成数组
#numpy.vstack是numpy.stack 函数的变体通过垂直堆叠来生成数组
a = np.array([[1,2],[3,4]])
print('第一个数组:')
print(a)
b = np.array([[5,6],[7,8]])
print('第二个数组:')
print(b)
print('水平列堆叠:')
c = np.hstack((a, b))
print(c)
print('竖直行堆叠:')
d = np.vstack((a,b))
print(d)
'''
第一个数组:
[[1 2]
 [3 4]]
第二个数组:
[[5 6]
 [7 8]]
水平列堆叠:
[[1 2 5 6]
 [3 4 7 8]]
竖直行堆叠:
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
'''