import numpy as np

a=np.array([1,2,3])
print(a)
# [1, 2, 3]
print('-----------------------------------------------------')
# 多维数组
b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''
print('-----------------------------------------------------')
# 生成3层嵌套数组
c=np.array([1,2,3,4,5],ndmin=3)
print(c)
# [[[1 2 3 4 5]]]
print('-----------------------------------------------------')
# 设置dtype数组元素的数据类型
d=np.array([[1,2,3],[1.23,2.34,4.56]],dtype=np.float)
print(d)
'''
[[1.   2.   3.  ]
 [1.23 2.34 4.56]]
'''