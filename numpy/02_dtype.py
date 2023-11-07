import numpy as np

# 使用标量类型
dt0 = np.dtype(np.int32)
print(dt0)
# int32
print('-----------------------------------------------------')
# int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替
dt1 = np.dtype('i8')
print(dt1)
# int64
print('-----------------------------------------------------')
# 小端法存储数据
dt2 = np.dtype('<i4')
print(dt2)
# int32
print('-----------------------------------------------------')
# 将数据类型应用于 ndarray 对象
# S10为10个长度的字符串，也可以写成a10
dt3 = np.dtype([('name','S10'),('考试合格',np.bool_),('成绩',np.int8)])
print(dt3)
a1 = np.array([('jack',True,80),('rose',False,56),('sandra',True,95)], dtype = dt3)
print(a1)
print('-----------------------------------------------------')
'''
[('name', 'S20'), ('考试合格', '?'), ('成绩', 'i1')]
[(b'jack',  True, 80) (b'rose', False, 56) (b'sandra',  True, 95)] # b代表以byte存入
'''
'''
每个内建类型都有一个唯一定义它的字符代码
字符    对应类型
b       布尔型 
i       (有符号) 整型 
u       无符号整型 integer 
f       浮点型 
c       复数浮点型 
m       timedelta（时间间隔） 
M       datetime（日期时间） 
O       (Python) 对象 
S,a    (byte-)字符串 
U       Unicode 
V       原始数据 (void) 
'''

#大小端内存存储演示
A = np.array([1, 2, 3])
print('小端法存储:')
print(A.view(np.uint8))
A.newbyteorder().byteswap(inplace=True) #转大端法
print('大端法存储:')
print(A.view(np.uint8))