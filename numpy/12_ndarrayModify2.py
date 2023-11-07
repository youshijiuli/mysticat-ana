import numpy as np

'''
numpy.transpose函数用于对换数组的维度
numpy.transpose(arr, axes)
axes：整数列表对应维度，通常所有维度都会对换
'''
a = np.arange(12).reshape(3,4)
print('原数组:')
print(a)
print('对换数组:')
print(np.transpose(a)) #等同于a.T
print('-----------------------------------------------------')

'''
numpy.rollaxis函数向后滚动特定的轴到一个特定位置
numpy.rollaxis(arr, axis, start)
axis：要向后滚动的轴，其它轴的相对位置不会改变
start：默认为零，表示完整的滚动。会滚动到特定位置
'''
a = np.arange(27).reshape(3,3,3)
print('原数组:')
print(a)
#多个二维数组的列数据转为行数据
print('调用rollaxis函数将轴2滚动到轴0宽度到深度:')
print(np.rollaxis(a, 2))
#单个二维数组自身行列数据置换
print('调用rollaxis函数将轴0滚动到轴1宽度到高度:')
print(np.rollaxis(a, 2, 1))
print('-----------------------------------------------------')
'''
原数组:
[[[ 0  1  2]
  [ 3  4  5]
  [ 6  7  8]]

 [[ 9 10 11]
  [12 13 14]
  [15 16 17]]

 [[18 19 20]
  [21 22 23]
  [24 25 26]]]
调用rollaxis函数将轴2滚动到轴0宽度到深度:
[[[ 0  3  6]
  [ 9 12 15]
  [18 21 24]]

 [[ 1  4  7]
  [10 13 16]
  [19 22 25]]

 [[ 2  5  8]
  [11 14 17]
  [20 23 26]]]
调用rollaxis函数将轴0滚动到轴1宽度到高度:
[[[ 0  3  6]
  [ 1  4  7]
  [ 2  5  8]]

 [[ 9 12 15]
  [10 13 16]
  [11 14 17]]

 [[18 21 24]
  [19 22 25]
  [20 23 26]]]
'''

'''
numpy.swapaxes函数用于交换数组的两个轴
numpy.swapaxes(arr, axis1, axis2)
axis1：对应第一个轴的整数
axis2：对应第二个轴的整数
'''
a = np.arange(27).reshape(3,3,3)
print('原数组:')
print(a)
# 现在交换轴 0（深度方向）到轴 2（宽度方向）
print('调用swapaxes函数数组:')
print(np.swapaxes(a, 2, 0))
'''
原数组:
[[[ 0  1  2]
  [ 3  4  5]
  [ 6  7  8]]

 [[ 9 10 11]
  [12 13 14]
  [15 16 17]]

 [[18 19 20]
  [21 22 23]
  [24 25 26]]]

调用swapaxes函数数组:
[[[ 0  9 18]
  [ 3 12 21]
  [ 6 15 24]]

 [[ 1 10 19]
  [ 4 13 22]
  [ 7 16 25]]

 [[ 2 11 20]
  [ 5 14 23]
  [ 8 17 26]]]
'''