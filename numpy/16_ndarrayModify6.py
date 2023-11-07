import numpy as np

'''
numpy.resize 函数返回指定大小的新数组
如果新数组大小大于原始大小，则包含原始数组中的元素的副本
numpy.resize(arr, shape)
shape：返回数组的新形状
'''
a = np.array([[1,2,3],[4,5,6]])
print('第一个数组:')
print(a)
print('第一个数组的形状:')
print(a.shape)
b = np.resize(a,(3,2))
print('第二个数组:')
print(b)
print('第二个数组的形状:')
print(b.shape)
# 注意a的第一行在b中重复出现，因为尺寸变大
print('修改第二个数组的大小:')
b = np.resize(a,(3,3))
print(b)
print('-----------------------------------------------------')
'''
第一个数组：
[[1 2 3]
 [4 5 6]]
第一个数组的形状：
(2, 3)
第二个数组：
[[1 2]
 [3 4]
 [5 6]]
第二个数组的形状：
(3, 2)
修改第二个数组的大小：
[[1 2 3]
 [4 5 6]
 [1 2 3]]
'''

'''
numpy.append 函数在数组的末尾添加值。
追加操作会分配整个数组，并把原来的数组复制到新数组中。 此外输入数组的维度必须匹配否则将生成ValueError。
append 函数返回的始终是一个一维数组
numpy.append(arr, values, axis=None)
values：要向arr添加的值，需要和arr形状相同（除了要添加的轴）
axis：默认为 None。当axis无定义时，是横向加成，返回总是为一维数组！
当axis有定义的时候，分别为0和1的时候。当axis有定义的时候，分别为0和1的时候（列数要相同）。当axis为1时，数组是加在右边（行数要相同）。
'''
a = np.array([[1,2,3],[4,5,6]])
print('第一个数组:')
print(a)
print('向数组添加元素:')
print(np.append(a,[7,8,9]))
print('沿轴0添加元素:')
print(np.append(a,[[7,8,9]], axis=0))
print('沿轴1添加元素:')
print(np.append(a,[[5,5,5],[6,6,6]], axis=1))
print('-----------------------------------------------------')
'''
第一个数组:
[[1 2 3]
 [4 5 6]]
向数组添加元素:
[1 2 3 4 5 6 7 8 9]
沿轴0添加元素:
[[1 2 3]
 [4 5 6]
 [7 8 9]]
沿轴1添加元素:
[[1 2 3 5 5 5]
 [4 5 6 6 6 6]]
'''

'''
numpy.insert 函数在给定索引之前，沿给定轴在输入数组中插入值。
numpy.insert(arr, obj, values, axis)
obj：在其之前插入值的索引
values：要插入的值
axis：沿着它插入的轴，如果未提供，则输入数组会被展开
'''
a = np.array([[1,2],[3,4],[5,6]])
print('第一个数组:')
print(a)
print('未传递Axis参数。在插入之前输入数组会被展开。')
print(np.insert(a,3,[11,12]))
print('传递Axis参数。会广播值数组来配输入数组。')
print('沿轴0广播插入第2行:')
print(np.insert(a,1,[11,12],axis=0))
print('沿轴1广播插入第2列:')
print(np.insert(a,1,11,axis=1))
print('-----------------------------------------------------')
'''
第一个数组:
[[1 2]
 [3 4]
 [5 6]]
未传递Axis参数。在插入之前输入数组会被展开。
[ 1  2  3 11 12  4  5  6]
传递Axis参数。会广播值数组来配输入数组。
沿轴0广播插入第2行:
[[ 1  2]
 [11 12]
 [ 3  4]
 [ 5  6]]
沿轴1广播插入第2列:
[[ 1 11 2]
 [ 3 11 4]
 [ 5 11 6]]
'''

'''
numpy.delete 函数返回从输入数组中删除指定子数组的新数组。
与insert()函数的情况一样，如果未提供轴参数，则输入数组将展开。
numpy.delete(arr, obj, axis)
'''
a = np.arange(12).reshape(3, 4)
print('第一个数组:')
print(a)
print('未传递Axis参数。在插入之前输入数组会被展开。')
print(np.delete(a, 5))
print('删除第二列:')
print(np.delete(a, 1, axis=1))
print('包含从数组中删除的替代值的切片:')
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(np.delete(a,np.s_[::3]))
print('-----------------------------------------------------')
'''
第一个数组:
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
未传递Axis参数。在插入之前输入数组会被展开。
[ 0  1  2  3  4  6  7  8  9 10 11]
删除第二列:
[[ 0  2  3]
 [ 4  6  7]
 [ 8 10 11]]
包含从数组中删除的替代值的切片:
[2 3 5 6 8 9]
'''

'''
numpy.unique 函数用于去除数组中的重复元素
numpy.unique(arr, return_index, return_inverse, return_counts)
return_index：如果为true，返回新列表元素在旧列表中的位置（下标）,并以列表形式储
return_inverse：如果为true，返回旧列表元素在新列表中的位置（下标）,并以列表形式储
return_counts：如果为true，返回去重数组中的元素在原数组中的出现次数
'''
a = np.array([5, 2, 6, 2, 7, 5, 6, 8, 2, 9])
print('第一个数组:')
print(a)
print('第一个数组的去重值:')
u = np.unique(a)
print(u)
print('新列表元素在旧列表中的位置下标:')
u,indices = np.unique(a, return_index=True)
print(indices)
print('可以看到每个和原数组下标对应的数值:')
print(a)
print('去重数组的下标:')
u,indices = np.unique(a, return_inverse=True)
print(u)
print('旧列表元素在新列表中的位置下标为:')
print(indices)
print('使用下标重构原数组:')
print(u[indices])
print('返回去重元素的重复数量:')
u,indices = np.unique(a, return_counts=True)
print(u)
print(indices)