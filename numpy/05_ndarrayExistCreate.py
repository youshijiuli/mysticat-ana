import numpy as np

#列表转换为ndarray
x = [1,2,3]
a1 = np.asarray(x)
print('a1数组:')
print(a1)
'''
a1数组:
[1 2 3]
'''
print('-----------------------------------------------------')
#元组转换为ndarray
x = (1,2,3)
a2 = np.asarray(x)
print('a2数组:')
print(a2)
'''
a2数组:
[1 2 3]
'''
print('-----------------------------------------------------')
#元组列表转换为ndarray
x = [(1,2,3),(4,5)]
a3 = np.asarray(x)
print('a3数组:')
print(a3)
'''
a3数组:
[(1, 2, 3) (4, 5)]
'''
print('-----------------------------------------------------')
#设置dtype参数
x = [1,2,3]
a4 = np.asarray(x,dtype=float)
print('a4数组:')
print(a4)
'''
a4数组:
[1. 2. 3.]
'''
print('-----------------------------------------------------')
#numpy.frombuffer实现动态数组
#buffer是字符串的时候，Python3默认str是Unicode 类型，所以要转成 bytestring 在原str前加上b
x = b'Hello World'
a5 = np.frombuffer(x, dtype='S1')
print('a5数组:')
print(a5)
'''
a5数组:
[b'H' b'e' b'l' b'l' b'o' b' ' b'W' b'o' b'r' b'l' b'd']
'''
print('-----------------------------------------------------')
#numpy.fromiter从迭代对象中建立ndarray对象，返回一维数组
# 使用 range 函数创建列表对象
list = range(5)
it = iter(list)
a6 = np.fromiter(it, dtype=float)
print('a6数组:')
print(a6)
'''
a6数组:
[0. 1. 2. 3. 4.]
'''