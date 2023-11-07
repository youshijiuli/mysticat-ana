import numpy as np

'''
numpy.reshape 函数可以在不改变数据的条件下修改形状，格式numpy.reshape(arr, newshape, order='C') 
arr:要修改形状的数组
newshape:整数或者整数数组，新的形状应当兼容原有形状
order:'C'按行，'F'按列，'A'原顺序，'k'元素在内存中的出现顺序
'''
a = np.arange(8)
print('原始数组:')
print(a)
b = a.reshape(4, 2)
print('修改后数组:')
print(b)
'''
原始数组:
[0 1 2 3 4 5 6 7]
修改后数组:
[[0 1]
 [2 3]
 [4 5]
 [6 7]]
'''
print('-----------------------------------------------------')

#numpy.ndarray.flat数组元素迭代器
a = np.arange(9).reshape(3, 3)
print('原始数组:')
for row in a:print(row)
#对数组中每个元素都进行处理，可以使用flat属性，该属性是一个数组元素迭代器：
print('迭代后的数组：')
for element in a.flat:print(element)
'''
原始数组:
[0 1 2]
[3 4 5]
[6 7 8]
迭代后的数组：
0
1
2
3
4
5
6
7
8
'''
print('-----------------------------------------------------')

'''
numpy.ndarray.flatten返回一份数组拷贝，对拷贝所做的修改不会影响原始数组
ndarray.flatten(order='C')
order:'C'按行，'F'按列，'A'原顺序，'k'元素在内存中的出现顺序
'''
a = np.arange(8).reshape(2,4)
print('原数组:')
print(a)
# 默认按行
print('展开的数组:')
a1=a.flatten()
print(a1)
print('以F风格顺序展开数组:')
a2=a.flatten(order='F')
print(a2)
print('-----------------------------------------------------')

'''
numpy.ravel() 展平的数组元素，顺序通常是"C风格"，返回的是数组视图，修改会影响原始数组
numpy.ravel(a,order='C')
'''
a = np.arange(8).reshape(2,4)
print('原数组：')
print(a)
print('调用 ravel 函数之后：')
a3=a.ravel()
print(a3)
print('以F风格顺序调用ravel函数之后：')
a4=a.ravel(order='F')
print(a4)
