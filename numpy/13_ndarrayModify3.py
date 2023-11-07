import numpy as np

x = np.array([[1],[2],[3]])
y = np.array([4,5,6])
# 对y广播x
b = np.broadcast(x,y)
# 它拥有iterator属性基于自身组件的迭代器元组
print('对y广播x:')
r,c = b.iters
print(next(r),next(c))
print(next(r),next(c))
print(next(r),next(c))
print(next(r),next(c))
print(next(r),next(c))
print(next(r),next(c))
print(next(r),next(c))
print(next(r),next(c))
print(next(r),next(c))
print('-----------------------------------------------------')
'''
对y广播x:
1 4
1 5
1 6
2 4
2 5
2 6
3 4
3 5
3 6
'''

# shape属性返回广播对象形状
print('广播对象形状:')
print(b.shape)
print('-----------------------------------------------------')
'''
广播对象的形状：
(3, 3)
'''

# 手动使用broadcast将x与y相加
b = np.broadcast(x,y)
#empty创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组
c1 = np.empty(b.shape) # 和b一样3X3
print('手动使用broadcast将x与y相加:')
'''
[[4 5 6]                   [[5 6 7]
 [4 5 6]   +  [1],[2],[3] = [6 7 8]
 [4 5 6]]                   [7 8 9]]
'''
c1.flat = [u + v for (u, v) in b]
print('调用 flat 函数：')
print(c1)
#获得和NumPy内建的广播支持相同的结果
#更简化的写法
print('x与y的和:')
c2=x+y
print(c2)
print('-----------------------------------------------------')

#numpy.broadcast_to函数将数组广播到新形状。
a = np.arange(3)
print('原数组:')
print(a)
print('调用 broadcast_to 函数之后:')
#第二个参数必须是原数组的对等长度，从而形成正方形矩阵，否则无效果
print(np.broadcast_to(a,(3,3)))
print('-----------------------------------------------------')
'''
原数组:
[0 1 2]
调用 broadcast_to 函数之后:
[[0 1 2]
 [0 1 2]
 [0 1 2]]
'''

'''
numpy.expand_dims 函数通过在指定位置插入新的轴来扩展数组形状
numpy.expand_dims(arr, axis)
axis：新轴插入的位置
'''
x = np.array(([1,2],[3,4]))
print('数组x:')
print(x)
'''
数组x:
[[1 2]
 [3 4]]
'''
y = np.expand_dims(x, axis=0)
print('数组y:')
print(y)
'''
插入新轴后数组y:
[[[1 2]
  [3 4]]]
'''
print('数组x和y的形状:')
print(x.shape, y.shape)
'''
x.shape (2, 2)
y.shape (1, 2, 2) #多了一个刚插入的轴
'''
# 在位置1插入轴
y = np.expand_dims(x, axis=1)
print('在位置 1 插入轴之后的数组 y：')
print(y)
'''
在位置 1 插入轴之后的数组 y：
[[[1 2]]
            #此空白处就是1插入轴
 [[3 4]]]
'''
print('x.ndim和y.ndim：')
print(x.ndim, y.ndim)
'''
x.ndim 和 y.ndim：
2 3  #x有2个轴，y有3个轴
'''
print('x.shape和y.shape：')
print(x.shape, y.shape)
'''
x.shape和y.shape：
x.shape (2, 2) 
y.shape (2, 1, 2)
'''
print('-----------------------------------------------------')

'''
numpy.squeeze 函数从给定数组的形状中删除一维的条目
numpy.squeeze(arr, axis)
axis：整数或整数元组，用于选择形状中一维条目的子集,维度必须为单维度，否则将会报错
'''
x = np.arange(9).reshape(1,3,3,1)
print('数组x:')
print(x)
'''
数组x:
[[[0 1 2]
  [3 4 5]
  [6 7 8]]]
'''
#第二个参数可以是整数或整数元组，用于选择形状中一维条目的子集,维度必须为单维度，否则将会报错
#y = np.squeeze(x,0)
#y = np.squeeze(x,3)
#y = np.squeeze(x,1) #报错
y = np.squeeze(x,(0,3))
print('数组y:')
print(y)
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
'''
print('数组x和y的形状:')
print(x.shape,y.shape)
'''
数组x和y的形状:
x.shape (1, 3, 3)
y.shape (3, 3)
'''