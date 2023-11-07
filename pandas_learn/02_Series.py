import pandas as pd
import numpy as np

#创建一个空的系列
s = pd.Series()
print(s)
print('-----------------------------------------------------')
# Series([], dtype: float64)

#从ndarray创建一个系列
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s)
print('-----------------------------------------------------')
'''
0    a
1    b
2    c
3    d
dtype: object
'''

#从ndarray创建一个系列并修改索引
s = pd.Series(data,index=[100,101,102,103])
print(s)
print('-----------------------------------------------------')
'''
100    a
101    b
102    c
103    d
dtype: object
'''

#从字典创建一个系列
data = {'a':0.,'b':1.,'c':2.}
s = pd.Series(data)
print(s)
print('-----------------------------------------------------')
'''
a    0.0
b    1.0
c    2.0
dtype: float64
'''

#从字典创建一个系列，指定index参数
s = pd.Series(data,index=['b','c','d','a'])
print(s)
print('-----------------------------------------------------')
'''
index致使索引顺序发生变化，未设置的索引项值=NaN
b    1.0
c    2.0
d    NaN
a    0.0
dtype: float64
'''

#从标量固定值创建一个系列
s = pd.Series(5, index=[0, 1, 2, 3])
print(s)
print('-----------------------------------------------------')
'''
如不提供index则只出现第一行索引和标量值
0    5
1    5
2    5
3    5
dtype: int64
'''

#从具有位置的系列中访问数据
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s[2])
print('-----------------------------------------------------')
print(s[:2])
print('-----------------------------------------------------')
print(s[-2:])
print('-----------------------------------------------------')
'''
3
-----------------------------------------------------
a    1
b    2
dtype: int64
-----------------------------------------------------
d    4
e    5
dtype: int64
'''

#使用标签检索数据索引
#s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s['c'])
print('-----------------------------------------------------')
print(s[['a','c']])
print('-----------------------------------------------------')
#print(s['z'])
#print('-----------------------------------------------------')
'''
3
-----------------------------------------------------
a    1
c    3
dtype: int64
-----------------------------------------------------
KeyError: 'z'
'''

#axes返回系列的标签列表
s = pd.Series(np.random.randn(4))
print(s)
print("The axes are:")
print(s.axes)
print('-----------------------------------------------------')
'''
0   -1.343510
1   -0.800768
2    2.486362
3    0.943748
dtype: float64
The axes are:
[RangeIndex(start=0, stop=4, step=1)]
'''

#empty返回布尔值，表示对象是否为空
print("Is the Object empty?")
print(s.empty)
print('-----------------------------------------------------')
'''
Is the Object empty?
False
'''

#ndim返回对象的维数
print("The dimensions of the object:")
print(s.ndim)
print('-----------------------------------------------------')
'''
The dimensions of the object:
1
'''

#size返回系列的大小(长度)
print ("The size of the object:")
print(s.size)
print('-----------------------------------------------------')
'''
The size of the object:
4
'''

#values以数组形式返回系列中的实际数据值
print("The actual data series is:")
print(s.values)
print('-----------------------------------------------------')
'''
The actual data series is:
[-0.06827072 -0.41326551 -0.87833819  0.56251993]
'''

'''
head()和tail()方法
head()返回前n行(观察索引值)。要显示的元素的默认数量为5
tail()返回最后n行(观察索引值)。 要显示的元素的默认数量为5
'''
print("The first two rows of the data series:")
print(s.head(2))
print("The last two rows of the data series:")
print(s.tail(2))
print('-----------------------------------------------------')
'''
The first two rows of the data series:
0   -1.473274
1    1.977214
dtype: float64
The last two rows of the data series:
2    0.294284
3   -0.032361
dtype: float64
'''