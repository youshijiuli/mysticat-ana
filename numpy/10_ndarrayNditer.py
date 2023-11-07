import numpy as np

a1 = np.arange(6).reshape(2,3)
print('a1数组是:')
print(a1)
print('迭代元素:')
for x in np.nditer(a1):print(x,end=',')
print('\n')
print('-----------------------------------------------------')
'''
a1数组是:
[[0 1 2]
 [3 4 5]]
迭代元素:
0,1,2,3,4,5,
'''

a2 = np.arange(0,60,5)
a2 = a2.reshape(3,4)
print('a2数组:')
print(a2)
a3 = a2.T
print('a2转置:')
print(a3)
print('以C风格顺序排序：')
c = a3.copy(order='C')
print(c)
for x in np.nditer(c):print(x,end=',')
print('\n')
print('以Fortran风格顺序排序：')
c = a3.copy(order='F')
print(c)
for x in np.nditer(c):print (x,end=',')
print('\n')
print('强制nditer对象使用C顺序')
for x in np.nditer(c,order='C'):print(x,end=',')
print('\n')
print('强制nditer对象使用F顺序')
for x in np.nditer(c,order='F'):print(x,end=',')
print('\n')
print('-----------------------------------------------------')

'''
nditer 对象有另一个可选参数 op_flags。 
默认情况下nditer将视待迭代遍历的数组为只读对象(read-only)，
为了在遍历数组的同时，实现对数组元素值得修改，必须指定read-write或者write-only的模式。
'''
print('a2数组:')
print(a2)
a3=a2
for x in np.nditer(a3,op_flags=['readwrite']):
    x[...]=2*x
print('修改后数组:')
print(a3)
print('-----------------------------------------------------')

'''
nditer类的构造器拥有flags参数
参数            描述
c_index         可以跟踪C顺序(横向)的索引 
f_index         可以跟踪Fortran顺序(纵向)的索引 
multi-index     每次迭代可以跟踪一种索引类型 
external_loop   给出的值是具有多个值的一维数组，而不是零维数组 
'''
a4 = np.arange(0,60,5)
a4 = a4.reshape(3,4)
print('a4原始数组:')
print(a4)
print('修改后的多值一维数组:')
for x in np.nditer(a4,flags=['external_loop'],order='F'):print(x,end=',')
print('\n')
print('-----------------------------------------------------')

#如果两个数组是可广播的，nditer组合对象能够同时迭代它们
print('第一个数组:')
print(a4)
print('第二个数组:')
b = np.array([1,2,3,4],dtype=int)
print(b)
print('修改后的数组为：')
for x,y in np.nditer([a4,b]):print("%d-%d"%(x,y),end=',')
'''
第一个数组:
[[ 0  5 10 15]
 [20 25 30 35]
 [40 45 50 55]]
第二个数组:
[1 2 3 4]
修改后的数组为：
0-1,5-2,10-3,15-4,20-1,25-2,30-3,35-4,40-1,45-2,50-3,55-4,
'''