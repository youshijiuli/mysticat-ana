import numpy as np

'''
numpy.sort()函数返回输入数组的排序副本
numpy.sort(a, axis, kind, order)
axis: 沿着它排序数组的轴，如果没有数组会被展开，沿着最后的轴排序， axis=0 按列排序，axis=1 按行排序
kind: 默认为'quicksort'（快速排序）
order: 如果数组包含字段，则是要排序的字段
'''
a = np.array([[3,7],[9,1]])
print('原数组:')
print(a)
print('调用sort() 函数:')
print(np.sort(a))
print('按列排序:')
print(np.sort(a,axis=0))
#在sort函数中排序字段
dt = np.dtype([('name','S10'),('age',int)])
a = np.array([("raju",21), ("anil",25), ("ravi",17), ("amar",27)], dtype=dt)
print('原姓名、年龄数组:')
print(a)
print('按age排序:')
print(np.sort(a,order='age'))
print('-----------------------------------------------------')
'''
原数组:
[[3 7]
 [9 1]]
调用sort() 函数:
[[3 7]
 [1 9]]
按列排序:
[[3 1]
 [9 7]]
姓名、年龄数组:
[(b'raju', 21) (b'anil', 25) (b'ravi', 17) (b'amar', 27)]
按age排序:
[(b'ravi', 17) (b'raju', 21) (b'anil', 25) (b'amar', 27)]
'''

#numpy.argsort()函数返回的是数组值从小到大的索引值
x = np.array([3,1,2])
print('原数组:')
print(x)
print ('对x调用argsort()函数:')
y = np.argsort(x)
print (y)
print ('以排序后的顺序重构原数组:')
print (x[y])
print ('使用循环重构原数组:')
for i in y:print(x[i], end=' ')
print('\n-----------------------------------------------------')
'''
原数组:
[3 1 2]
对 x 调用 argsort() 函数:
[1 2 0] # 排序后的索引值
以排序后的顺序重构原数组:
[1 2 3]
使用循环重构原数组:
1 2 3 
'''

'''
numpy.lexsort() 用于对多个序列进行排序,每一列代表一个序列，排序时优先照顾靠后的列
如重点班录取学生按照总成绩录取。
在总成绩相同时，数学成绩高的优先录取，
在总成绩和数学成绩都相同时，按照英语成绩录取…… 
这里，总成绩排在电子表格的最后一列，数学成绩在倒数第二列，英语成绩在倒数第三列。 
'''
nm = ('raju','anil','ravi','amar')
dv = ('80','90','60','70')
dv1 = ('88','99','66','77')
ind = np.lexsort((dv1,dv,nm))
print('调用lexsort()函数:')
print(ind)
print ('使用这个索引来获取排序后的数据:')
print ([nm[i]+", "+dv[i]+", "+dv1[i] for i in ind])
print('-----------------------------------------------------')
'''
调用 lexsort()函数:
[3 1 0 2]
使用这个索引来获取排序后的数据:
['amar, 70, 77', 'anil, 90, 99', 'raju, 80, 88', 'ravi, 60, 66']
'''

'''
msort(a)数组按第一个轴排序，返回排序后的数组副本。np.msort(a) 相等于 np.sort(a, axis=0)。 
sort_complex(a)对复数按照先实部后虚部的顺序进行排序 
partition(a, kth[, axis, kind, order])指定一个数，对数组进行分区 
argpartition(a, kth[, axis, kind, order])可以通过关键字 kind 指定算法沿着指定轴对数组进行分区 
'''
print('对复数按照先实部后虚部的顺序进行排序')
print(np.sort_complex([5, 3, 6, 2, 1]))
print(np.sort_complex([1 + 2j, 2 - 1j, 3 - 2j, 3 - 3j, 3 + 5j]))
# [1.+0.j 2.+0.j 3.+0.j 5.+0.j 6.+0.j]
# [1.+2.j 2.-1.j 3.-3.j 3.-2.j 3.+5.j]
print('-----------------------------------------------------')

a = np.array([30, 40, 20, 10])
'''
partition() 分区排序
1.先对数组排序（升序）
2.以排序后的索引是i的元素为基准，将元素分成两部分
3.大于该元素的放在其后面但不排序，小于该元素的放在其前面也不排序
'''
print(np.partition(a,0)) # 以排序后的第1个值10划分 [10 40 20 30]
print(np.partition(a,1)) # 以排序后的第2个值20划分 [10 20 40 30]
print(np.partition(a,2)) # 以排序后的第3个值30划分[10 20 30 40]
print(np.partition(a,3)) # 以排序后的第4个值40划分[20 10 30 40]
print('-----------------------------------------------------')

#argpartition与partition()类似，不过返回的不是分区排序好的元素数组，而是排序完成的元素索引数组
arr = np.array([46, 57, 23, 39, 1, 10, 0, 120])
print('排序后以2为索引基准的前后索引顺序:')
print(np.argpartition(arr,2)) # [6 4 5 3 1 2 0 7]
print(arr[np.argpartition(arr,2)[3]])
print('-----------------------------------------------------')
'''
排序后以2为索引基准的前后索引顺序:
[6 4 5 3 1 2 0 7]
39
*************************************************************
arr[np.argpartition(arr,2)处理过程:
1.[46, 57, 23, 39,  1, 10, 0, 120]的对应索引为
  [0,   1,  2,  3,  4,  5, 6,  7]

2.排序
[0,  1,  10,  23,  39,  46,  57,  120]的对应索引为
[0,  1,   2,   3,   4,   5,   6,   7]

3.通过argpartition对索引2即值10进行小堆前放和大堆后放处理
[0, 1, 10, 39, 57, 23, 46, 120]
[6  4   5   3   1   2   0   7]

4.arr[np.argpartition(arr,2)[3]取出对应索引下标的值
39
*************************************************************
'''
# 同理基准值也可以是多个，如10和23所对应的坐标2,3进行小堆前放和大堆后放处理
print(arr[np.argpartition(arr,[2,3])[2]]) #10
print(arr[np.argpartition(arr,[2,3])[3]]) #23
print('-----------------------------------------------------')

#numpy.argmax()和numpy.argmin()函数分别沿给定轴返回最大和最小元素的索引
a = np.array([[30,40,70],[80,20,10],[50,90,60]])
print('原数组是:')
print(a)
print('调用argmax()函数:')
print(np.argmax(a))
print('展开数组:')
print(a.flatten())
print('沿轴0纵轴的最大值索引:')
maxindex = np.argmax(a,axis=0)
print(maxindex)
print('沿轴1横轴的最大值索引:')
maxindex = np.argmax(a,axis=1)
print(maxindex)
print('调用argmin()函数:')
minindex = np.argmin(a)
print(minindex)
print('展开数组中的最小值:')
print(a.flatten()[minindex])
print('沿轴0纵轴的最小值索引:')
minindex = np.argmin(a,axis=0)
print(minindex)
print('沿轴1横轴的最小值索引:')
minindex = np.argmin(a,axis=1)
print(minindex)
print('-----------------------------------------------------')
'''
原数组是:
[[30 40 70]
 [80 20 10]
 [50 90 60]]
调用argmax()函数:
7  # 90
展开数组:
[30 40 70 80 20 10 50 90 60]
沿轴0纵轴的最大值索引:
[1 2 0]   #80,90,70
沿轴1横轴的最大值索引:
[2 0 1]   #70,80,90
调用argmin()函数:
5 # 10
展开数组中的最小值:
10
沿轴0纵轴的最小值索引:
[0 1 1]   #30,20,10
沿轴1横轴的最小值索引:
[0 2 0]   #30,10,50
'''

#numpy.nonzero()函数返回输入数组中非零元素的索引
a = np.array([[30,40,0],[0,20,10],[50,0,60]])
print('原数组:')
print(a)
print('调用nonzero()函数:')
print(np.nonzero(a))
print('-----------------------------------------------------')
'''
原数组:
[[30 40  0]
 [ 0 20 10]
 [50  0 60]]
调用nonzero()函数:
(array([0, 0, 1, 1, 2, 2], dtype=int64), 
 array([0, 1, 1, 2, 0, 2], dtype=int64))
'''

#numpy.where()函数返回输入数组中满足给定条件的元素的索引
x = np.arange(9).reshape(3,3)
print('原数组:')
print(x)
print('大于3的元素的索引:')
y = np.where(x>3)
print(y)
print('使用这些索引来获取满足条件的元素:')
print(x[y])
print('-----------------------------------------------------')
'''
原数组:
[[0 1 2]
 [3 4 5]
 [6 7 8]]
大于3的元素的索引:
(array([1, 1, 2, 2, 2], dtype=int64), 
 array([1, 2, 0, 1, 2], dtype=int64))
使用这些索引来获取满足条件的元素:
[4 5 6 7 8]
'''

#numpy.extract()函数根据某个条件从数组中抽取元素，返回满条件的元素
x = np.arange(9).reshape(3,3)
print('原数组:')
print(x)
# 定义条件选择偶数元素
condition = np.mod(x,2)==0
print('按元素的条件值:')
print(condition)
print('使用条件提取元素:')
print(np.extract(condition,x))
'''
原数组:
[[0 1 2]
 [3 4 5]
 [6 7 8]]
按元素的条件值:
[[ True False  True]
 [False  True False]
 [ True False  True]]
使用条件提取元素:
[0 2 4 6 8]
'''











