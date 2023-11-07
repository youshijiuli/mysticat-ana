import pandas as pd
import numpy as np

N=20
df = pd.DataFrame({
    'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
    'x': np.linspace(0,stop=N-1,num=N),
    'y': np.random.rand(N),
    'C': np.random.choice(['Low','Medium','High'],N).tolist(),
    'D': np.random.normal(100, 10, size=(N)).tolist()
    })

#迭代DataFrame提供列名
for col in df:print(col)
print('-----------------------------------------------------')
'''
A
x
y
C
D
'''

'''
要遍历数据帧(DataFrame)中的行，可以使用以下函数:
iteritems() - 迭代(key，value)对
iterrows() - 将行迭代为(索引，系列)对
itertuples() - 以namedtuples的形式迭代行
'''
#iteritems()将每个列作为键，将值与值作为键和列值迭代为Series对象
df = pd.DataFrame(np.random.randn(4,3),columns=['col1','col2','col3'])
print(df)
print('-----------------------------------------------------')
for key,value in df.iteritems():print(key,value)
print('-----------------------------------------------------')
'''
       col1      col2      col3
0 -0.385265  0.527742  0.308916
1 -0.169245  0.416146  1.266482
2 -0.522977 -0.278898 -0.864714
3 -1.612977 -1.309554  0.936490
-----------------------------------------------------
col1 0   -0.385265
1   -0.169245
2   -0.522977
3   -1.612977
Name: col1, dtype: float64
col2 0    0.527742
1    0.416146
2   -0.278898
3   -1.309554
Name: col2, dtype: float64
col3 0    0.308916
1    1.266482
2   -0.864714
3    0.936490
Name: col3, dtype: float64
'''

#iterrows()返回迭代器，产生每个索引值以及包含每行数据的序列
print(df)
print('-----------------------------------------------------')
for row_index,row in df.iterrows():print(row_index,row)
print('-----------------------------------------------------')
'''
       col1      col2      col3
0  1.413707  1.233906 -1.856739
1 -0.629738  0.733525  0.829884
2  0.035927 -1.340493 -0.298163
3  1.683948 -0.651639 -1.722174
-----------------------------------------------------
0 col1    1.413707
col2    1.233906
col3   -1.856739
Name: 0, dtype: float64
1 col1   -0.629738
col2    0.733525
col3    0.829884
Name: 1, dtype: float64
2 col1    0.035927
col2   -1.340493
col3   -0.298163
Name: 2, dtype: float64
3 col1    1.683948
col2   -0.651639
col3   -1.722174
Name: 3, dtype: float64
'''

#itertuples()方法将为DataFrame中的每一行返回一个产生一个命名元组的迭代器。元组的第一个元素将是行的相应索引值，而剩余的值是行值。
print(df)
print('-----------------------------------------------------')
for row in df.itertuples():print(row)
'''
       col1      col2      col3
0 -0.039327  0.216141 -0.931381
1  0.620970 -0.210772  0.777394
2 -0.365603 -0.264538  1.815422
3 -0.200243 -0.098663  0.490763
-----------------------------------------------------
Pandas(Index=0, col1=-0.0393272620194492, col2=0.21614053797036878, col3=-0.9313811785259972)
Pandas(Index=1, col1=0.6209700274291997, col2=-0.2107723308425323, col3=0.7773937221185059)
Pandas(Index=2, col1=-0.3656030641446411, col2=-0.26453841499853203, col3=1.8154219880919322)
Pandas(Index=3, col1=-0.20024343112695797, col2=-0.09866317620487064, col3=0.4907633244414803)
'''