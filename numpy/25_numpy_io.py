import numpy as np

'''
numpy.save()函数将数组保存到以.npy为扩展名的文件中
numpy.save(file, arr, allow_pickle=True, fix_imports=True)
file：要保存的文件，扩展名为 .npy，如果文件路径末尾没有扩展名 .npy，该扩展名会被自动加上。
arr: 要保存的数组
allow_pickle: 可选布尔值，允许使用 Python pickles 保存对象数组，
Python 中的pickle用于在保存到磁盘文件或从磁盘文件读取之前，对对象进行序列化和反序列化。
fix_imports: 可选为了方便Pyhton2中读取 Python3保存的数据。
'''
a = np.array([1,2,3,4,5])
# 保存到 outfile.npy 文件上
np.save('outfile.npy', a)
# 保存到 outfile2.npy 文件上，如果文件路径末尾没有扩展名 .npy，该扩展名会被自动加上
np.save('outfile2', a)
b = np.load('outfile.npy')
print(b)
print('-----------------------------------------------------')
'''
[1 2 3 4 5]
直接查看文件是乱码，是Numpy专用的二进制格式后的数据:
�NUMPY v {'descr': '<i4', 'fortran_order': False, 'shape': (5,), }
'''

'''
numpy.savez()函数将多个数组保存到以npz为扩展名的文件中。
numpy.savez(file, *args, **kwds)
file：要保存的文件，扩展名为 .npz，如果文件路径末尾没有扩展名 .npz，该扩展名会被自动加上。
args: 要保存的数组，可以使用关键字参数为数组起一个名字，非关键字参数传递的数组会自动起名为 arr_0, arr_1, …　。
kwds: 要保存的数组使用关键字名称。
'''
a = np.array([[1,2,3],[4,5,6]])
b = np.arange(0, 1.0, 0.1)
c = np.sin(b)
# c使用了自定义数组名称
np.savez("mynpz.npz", a, b, c_title=c)
r = np.load("mynpz.npz")
print(r.files) # 查看各个数组名称
print(r["arr_0"]) # 数组a
print(r["arr_1"]) # 数组b
print(r["c_title"]) # 数组c
print('-----------------------------------------------------')
'''
['c_title', 'arr_0', 'arr_1']
[[1 2 3]
 [4 5 6]]
[0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]
[0.         0.09983342 0.19866933 0.29552021 0.38941834 0.47942554
 0.56464247 0.64421769 0.71735609 0.78332691]
'''

'''
savetxt()函数是以简单的文本文件格式存储数据，对应的使用loadtxt()函数来获取数据。
np.loadtxt(FILENAME, dtype=int, delimiter=' ')
np.savetxt(FILENAME, a, fmt="%d", delimiter=",")
参数delimiter可以指定各种分隔符、针对特定列的转换器函数、需要跳过的行数等。
'''
a = np.array([1,2,3,4,5])
np.savetxt('out.txt',a)
b = np.loadtxt('out.txt')
print(b)
print('-----------------------------------------------------')
#[1. 2. 3. 4. 5.]

#使用delimiter参数
#reshape某个维度等于-1的话，那么Numpy会根据剩下的维度计算出数组的另外一个shape属性值
a=np.arange(0,10,0.5).reshape(4,-1)
print("a原数组:")
print(a)
np.savetxt("out.txt",a,fmt="%d",delimiter=",") # 改为保存为整数，以逗号分隔
b = np.loadtxt("out.txt",delimiter=",") # load 时也要指定为逗号分隔
print(b)
'''
a原数组:
[[0.  0.5 1.  1.5 2. ]
 [2.5 3.  3.5 4.  4.5]
 [5.  5.5 6.  6.5 7. ]
 [7.5 8.  8.5 9.  9.5]]
[[0. 0. 1. 1. 2.]
 [2. 3. 3. 4. 4.]
 [5. 5. 6. 6. 7.]
 [7. 8. 8. 9. 9.]]

out.txt文件:
0,0,1,1,2
2,3,3,4,4
5,5,6,6,7
7,8,8,9,9
'''