import numpy as np

'''
numpy.amin()用于计算数组中的元素沿指定轴的最小值。
numpy.amax()用于计算数组中的元素沿指定轴的最大值。
'''
a = np.array([[3,7,5],[8,4,3],[2,4,9]])
print('原数组:')
print(a)
print('调用amin()函数横向最小值:')
print(np.amin(a,1))
print('再次调用amin()函数纵向最小值:')
print(np.amin(a,0))
print('调用amax()函数:')
print(np.amax(a))
print('调用amax()函数纵向最大值:')
print(np.amax(a,axis=0))
print('-----------------------------------------------------')
'''
原数组:
[[3 7 5]
 [8 4 3]
 [2 4 9]]
调用amin()函数横向最小值:
[3 3 2]
再次调用amin()函数纵向最小值:
[2 4 3]
调用amax()函数:
9
调用amax()函数纵向最大值:
[8 7 9]
'''

#numpy.ptp()函数计算数组中元素最大值与最小值的差（最大值-最小值）
a = np.array([[3,7,5],[8,4,3],[2,4,9]])
print('原数组:')
print(a)
print('调用ptp()函数:')
print(np.ptp(a))
print('沿轴1调用ptp()函数:')
print(np.ptp(a,axis=1))
print('沿轴0调用ptp()函数:')
print(np.ptp(a,axis=0))
print('-----------------------------------------------------')
'''
原数组:
[[3 7 5]
 [8 4 3]
 [2 4 9]]
调用ptp()函数:
7  (9-2)
沿轴1调用ptp()函数:
[4 5 7]  (7-3) (8-3) (9-2)
沿轴0调用ptp()函数:
[6 3 6]  (8-2) (7-4) (9-3)
'''

'''
numpy.percentile()百分位数是统计中使用的度量，表示小于这个值的观察值的百分比
numpy.percentile(a, q, axis)
q: 要计算的百分位数，在 0 ~ 100 之间
axis: 沿着它计算百分位数的轴
例如：
高等院校的入学考试成绩经常以百分位数的形式报告。
假设某个考生在入学考试中的语文部分的原始分数为65分。
相对于参加同一考试的其他学生来说，他的成绩如何并不容易知道。
但是如果原始分数65分恰好对应的是第70百分位数，
我们就能知道大约70%的学生的考分比他低，而约30%的学生考分比他高
'''
a = np.array([[10,7,4],[3,9,1]])
print('原数组:')
print(a)
print('调用percentile()函数:')
print('50%的分位数，就是a里排序之后的中位数:')
print(np.percentile(a, 50))
print('axis为0，在纵列上求:')
print(np.percentile(a, 50, axis=0))
print('axis为1，在横行上求:')
print(np.percentile(a, 50, axis=1))
print('保持维度不变:')
print(np.percentile(a, 50, axis=1, keepdims=True))
print('-----------------------------------------------------')
'''
原数组:
[[10  7  4]
 [ 3  9  1]]
调用percentile()函数:
50%的分位数，就是a里排序之后的中位数:
5.5
axis为0，在纵列上求:
[6.5 8. 2.5]
axis为1，在横行上求:
[7. 3.]
保持维度不变:
[[7.]
 [3.]]
'''

#numpy.median()函数用于计算数组a中元素的中位数（中值）
a = np.array([[30,65,70],[80,95,10],[50,90,60]])
print('原数组:')
print(a)
print('调用median()函数:')
print(np.median(a))
print('沿轴0纵轴调用median()函数:')
print(np.median(a,axis=0))
print('沿轴1横轴调用median()函数:')
print(np.median(a,axis=1))
print('-----------------------------------------------------')
'''
原数组:
[[30 65 70]
 [80 95 10]
 [50 90 60]]
调用median()函数:
65.0
沿轴0纵轴调用median()函数:
[50. 90. 60.]
沿轴1横轴调用median()函数:
[65. 80. 60.]
'''

'''
numpy.mean()函数返回数组中元素的算术平均值。如果提供了轴，则沿其计算。
算术平均值是沿轴的元素的总和除以元素的数量。
'''
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print('原数组:')
print(a)
print('调用mean()函数:')
print(np.mean(a))
print('沿轴0纵轴调用mean()函数:')
print(np.mean(a,axis=0))
print('沿轴1横轴调用mean()函数:')
print(np.mean(a,axis=1))
print('-----------------------------------------------------')
'''
原数组:
[[1 2 3]
 [3 4 5]
 [4 5 6]]
调用mean()函数:
3.6666666666666665
沿轴0纵轴调用mean()函数:
[2.66666667 3.66666667 4.66666667]
沿轴1横轴调用mean()函数:
[2. 4. 5.]
'''

'''
numpy.average()函数根据在另一个数组中给出的各自的权重计算数组中元素的加权平均值。
该函数可以接受一个轴参数。如果没有指定轴，则数组会被展开。
加权平均值即将各数值乘以相应的权数，然后加总求和得到总体值，再除以总的单位数。
'''
a = np.array([1,2,3,4])
print('原数组:')
print(a)
print('调用average()函数:')
print(np.average(a))
# 不指定权重时相当于 mean 函数
wts = np.array([4,3,2,1])
print('再次调用average()函数:')
#将相应元素的乘积相加，并将和除以权重的和，来计算加权平均值
print(np.average(a,weights = wts))
# 如果returned参数设为true,则返回权重的和
print('权重的和:')
print(np.average([1,2,3,4],weights=[4,3,2,1],returned=True))
print('-----------------------------------------------------')
'''
原数组:
[1 2 3 4]
调用average()函数:
2.5
再次调用average()函数:
2.0  (1x4+2x3+3x2+4x1)/(4+3+2+1)
权重的和:
(2.0, 10.0)
'''

#多维数组中指定计算轴
a = np.arange(6).reshape(3,2)
print('原数组:')
print(a)
print('修改后数组:')
wt = np.array([3,5])
print(np.average(a,axis=1,weights=wt))
print('修改后数组：')
print(np.average(a,axis=1,weights=wt,returned=True))
print('-----------------------------------------------------')

'''
标准差是一组数据平均值分散程度的一种度量。
标准差是方差的算术平方根。
std = sqrt(mean((x - x.mean())**2))
如果数组是[1,2,3,4]，则其平均值为2.5。 
因此差的平方是 [2.25,0.25,0.25,2.25]，sqrt((2.25+0.25+0.25+2.25)/4),结果为 1.1180339887498949。
'''
print("[1,2,3,4]标准差")
print(np.std([1,2,3,4]))
# 1.118033988749895

'''
统计中的方差（样本方差）是每个样本值与全体样本值的平均数之差的平方值的平均数，即 mean((x - x.mean())** 2)。 
标准差是方差的平方根。
'''
print("[1,2,3,4]方差")
print(np.var([1,2,3,4]))