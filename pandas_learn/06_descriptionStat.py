import pandas as pd
import numpy as np

d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
df = pd.DataFrame(d)
print(df)
print('-----------------------------------------------------')
'''
      Name  Age  Rating
0      Tom   25    4.23
1    James   26    3.24
2    Ricky   25    3.98
3      Vin   23    2.56
4    Steve   30    3.20
5    Minsu   29    4.60
6     Jack   23    3.80
7      Lee   34    3.78
8    David   40    2.98
9   Gasper   30    4.80
10  Betina   51    4.10
11  Andres   46    3.65
'''

#sum()方法返回所请求轴的值的总和。默认情况下，轴为索引(axis=0)纵向
print('show sum():')
print(df.sum()) #等价于df.sum(0)
print('-----------------------------------------------------')
'''
show sum():
Name      TomJamesRickyVinSteveMinsuJackLeeDavidGasperBe...
Age                                                     382
Rating                                                44.92
dtype: object
'''

#除字符串列，数字列横向叠加
print('show sum(1):')
print(df.sum(1))
print('-----------------------------------------------------')
'''
show sum(1):
      age+rating
0     29.23
1     29.24
2     28.98
3     25.56
4     33.20
5     33.60
6     26.80
7     37.78
8     42.98
9     34.80
10    55.10
11    49.65
dtype: float64
'''

#mean()返回平均值
print('show mean():')
print(df.mean())
print('-----------------------------------------------------')
'''
Age       31.833333
Rating     3.743333
dtype: float64
'''

#std()返回数字列的Bressel标准偏差
'''
标准偏差(Std Dev,Standard Deviation) -统计学名词。
一种度量数据分布的分散程度之标准，用以衡量数据值偏离算术平均值的程度。
标准偏差越小，这些值偏离平均值就越少

例如，A、B两组各有6位学生参加同一次语文测验，A组的分数为95、85、75、65、55、45，
B组的分数为73、72、71、69、68、67。这两组的平均数都是70，
但A组的标准差应该是17.078分,B组的标准差应该是2.160分，
说明A组学生之间的差距要比B组学生之间的差距大得多。

例：有一组数字分别是200、50、100、200，求它们的样本标准偏差。
X=(200+50+100+200)/4 = 550/4 = 137.5
S^2=[(200-137.5)^2+(50-137.5)^2+(100-137.5)^2+(200-137.5)^2]/(4-1)
样本标准偏差 S = Sqrt(S^2)=75， 
'''
print('show std():')
print(df.std())
print('-----------------------------------------------------')
'''
show std():
Age       9.232682
Rating    0.661628
dtype: float64
'''

#describe()函数是用来计算有关DataFrame列的统计信息的摘要
print(df.describe())
print('-----------------------------------------------------')
'''
             Age     Rating
count  12.000000  12.000000  (数量)
mean   31.833333   3.743333  (平均值)
std     9.232682   0.661628  (标准差)
min    23.000000   2.560000  (最小值)
25%    25.000000   3.230000  (排序后第25%的数字)
50%    29.500000   3.790000  (排序后第50%的数字)
75%    35.500000   4.132500  (排序后第75%的数字)
max    51.000000   4.800000  (最大值)
'''

#有3个Ricky信息
d = {'Name':pd.Series(['Tom','James','Ricky','Ricky','Ricky','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
df = pd.DataFrame(d)
print(df)
print('-----------------------------------------------------')

#include用于传递列总结的必要信息的参数
print(df.describe(include=['object'])) #显示freq最高的对象
print('-----------------------------------------------------')
'''
         Name
count      12
unique     10
top     Ricky
freq        3
'''

#统计信息的摘要追加freq最高的对象信息统计
print(df.describe(include='all'))
print('-----------------------------------------------------')
'''
         Name        Age     Rating
count      12  12.000000  12.000000
unique     10        NaN        NaN
top     Ricky        NaN        NaN
freq        3        NaN        NaN
mean      NaN  31.833333   3.743333
std       NaN   9.232682   0.661628
min       NaN  23.000000   2.560000
25%       NaN  25.000000   3.230000
50%       NaN  29.500000   3.790000
75%       NaN  35.500000   4.132500
max       NaN  51.000000   4.800000
'''
