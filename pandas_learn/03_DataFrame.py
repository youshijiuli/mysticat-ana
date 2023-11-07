import pandas as pd

#创建一个空的DataFrame
df = pd.DataFrame()
print(df)
print('-----------------------------------------------------')
'''
Empty DataFrame
Columns: []
Index: []
'''

#从列表创建DataFrame1
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)
print('-----------------------------------------------------')
'''
   0
0  1
1  2
2  3
3  4
4  5
'''

#从列表创建DataFrame2
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)
print('-----------------------------------------------------')
'''
     Name  Age
0    Alex   10
1     Bob   12
2  Clarke   13
'''

#从列表创建DataFrame3
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print(df)
print('-----------------------------------------------------')
'''
     Name   Age
0    Alex  10.0
1     Bob  12.0
2  Clarke  13.0
'''

#从ndarrays/Lists的字典来创建DataFrame
data = {'Name':['Tom','Jack','Steve','Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print(df)
print('-----------------------------------------------------')
''''
    Name  Age
0    Tom   28
1   Jack   34
2  Steve   29
3  Ricky   42
'''

#使用数组创建一个索引的DataFrame
df = pd.DataFrame(data,index=['rank1','rank2','rank3','rank4'])
print(df)
print('-----------------------------------------------------')
'''
        Name  Age
rank1    Tom   28
rank2   Jack   34
rank3  Steve   29
rank4  Ricky   42
'''

#通过传递字典列表来创建DataFrame
data = [{'a':1,'b':2},{'a':5,'b':10,'c':20}]
df = pd.DataFrame(data)
print(df)
print('-----------------------------------------------------')
'''
   a   b     c
0  1   2   NaN
1  5  10  20.0
'''

#通过传递字典列表和行索引来创建DataFrame
df = pd.DataFrame(data,index=['first','second'])
print(df)
print('-----------------------------------------------------')
'''
        a   b     c
first   1   2   NaN
second  5  10  20.0
'''

#使用字典、行索引和列索引列表创建DataFrame
data = [{'a':1,'b':2},{'a':5,'b':10,'c':20}]
df1 = pd.DataFrame(data,index=['first','second'], columns=['a','b'])
df2 = pd.DataFrame(data,index=['first','second'], columns=['a','b1'])
print(df1)
print(df2)
print('-----------------------------------------------------')
'''
        a   b
first   1   2
second  5  10
        a  b1
first   1 NaN
second  5 NaN
'''

#从系列的字典来创建DataFrame
d = {'one':pd.Series([1, 2, 3],index=['a','b','c']),
    'two':pd.Series([1, 2, 3, 4],index=['a','b','c','d'])}
df = pd.DataFrame(d)
print(df)
print('-----------------------------------------------------')
'''
   one  two
a  1.0    1
b  2.0    2
c  3.0    3
d  NaN    4
'''

#通过从DataFrame中选择一列
print(df['two'])
print('-----------------------------------------------------')
'''
a    1
b    2
c    3
d    4
Name: two, dtype: int64
'''

#列添加
print("根据series添加新列:")
df['three']=pd.Series([10,20,30],index=['a','b','c'])
print(df)
print("根据已有列添加新列:")
df['four']=df['one']+df['three']
print(df)
print('-----------------------------------------------------')
'''
根据series添加新列:
   one  two  three
a  1.0    1   10.0
b  2.0    2   20.0
c  3.0    3   30.0
d  NaN    4    NaN
根据已有列添加新列:
   one  two  three  four
a  1.0    1   10.0  11.0
b  2.0    2   20.0  22.0
c  3.0    3   30.0  33.0
d  NaN    4    NaN   NaN
'''

#列删除
print('原有DataFrame:')
print(df)
del df['one']
df.pop('two')
print('删除后DataFrame:')
print(df)
print('-----------------------------------------------------')
'''
原有DataFrame:
   one  two  three  four
a  1.0    1   10.0  11.0
b  2.0    2   20.0  22.0
c  3.0    3   30.0  33.0
d  NaN    4    NaN   NaN
删除后DataFrame:
   three  four
a   10.0  11.0
b   20.0  22.0
c   30.0  33.0
d    NaN   NaN
'''

#通过将行标签传递给loc()函数来选择行
d = {'one':pd.Series([1,2,3],index=['a','b','c']),
     'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
df = pd.DataFrame(d)
print(df.loc['b'])
print('-----------------------------------------------------')
'''
one    2.0
two    2.0
Name: b, dtype: float64
'''

#通过将整数位置传递给iloc()函数来选择行
print(df.iloc[2])
print('-----------------------------------------------------')
'''
one    3.0
two    3.0
Name: c, dtype: float64
'''

#行切片运算符选择多行
print('原有DataFrame:')
print(df)
print('-----------------------------------------------------')
print(df[2:4])
print('-----------------------------------------------------')
'''
原有DataFrame:
   one  two
a  1.0    1
b  2.0    2
c  3.0    3
d  NaN    4
-----------------------------------------------------
   one  two
c  3.0    3
d  NaN    4
'''

#使用append()函数将新行添加到DataFrame
df = pd.DataFrame([[1,2], [3,4]],columns=['a','b'])
df2 = pd.DataFrame([[5,6], [7,8]],columns=['a','b'])
df = df.append(df2) # 追加的索引不会连续
print(df)
print('-----------------------------------------------------')
'''
   a  b
0  1  2
1  3  4
0  5  6
1  7  8
'''

#删除行，如果索引标签重复，则会删除多行
print('原有DataFrame:')
print(df)
print('-----------------------------------------------------')
df = df.drop(0) # 索引0重复被一并删除
df.to_xarray()
print(df)
print('-----------------------------------------------------')
'''
   a  b
0  1  2
1  3  4
0  5  6
1  7  8
-----------------------------------------------------
   a  b
1  3  4
1  7  8
'''

d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
df = pd.DataFrame(d)
print("Our data series is:")
print(df)
print('-----------------------------------------------------')
'''
Our data series is:
    Name  Age  Rating
0    Tom   25    4.23
1  James   26    3.24
2  Ricky   25    3.98
3    Vin   23    2.56
4  Steve   30    3.20
5  Minsu   29    4.60
6   Jack   23    3.80
'''

#T返回DataFrame的转置
print("The transpose of the data series is:")
print(df.T)
print('-----------------------------------------------------')
'''
The transpose of the data series is:
           0      1      2     3      4      5     6
Name     Tom  James  Ricky   Vin  Steve  Minsu  Jack
Age       25     26     25    23     30     29    23
Rating  4.23   3.24   3.98  2.56    3.2    4.6   3.8
'''

#axes返回行轴标签和列轴标签列表
print("Row axis labels and column axis labels are:")
print(df.axes)
print('-----------------------------------------------------')
'''
Row axis labels and column axis labels are:
[RangeIndex(start=0, stop=7, step=1), Index(['Name', 'Age', 'Rating'], dtype='object')]
'''

#dtypes返回每列的数据类型
print("The data types of each column are:")
print(df.dtypes)
print('-----------------------------------------------------')
'''
The data types of each column are:
Name       object
Age         int64
Rating    float64
dtype: object
'''

#empty返回布尔值，表示对象是否为空
print("Is the object empty?")
print(df.empty)
print('-----------------------------------------------------')
'''
Is the object empty?
False
'''

#ndim返回对象的维数
print("The dimension of the object is:")
print(df.ndim)
print('-----------------------------------------------------')
'''
The dimension of the object is:
2
'''

#shape返回表示DataFrame的维度的元组。 元组(a，b)，其中a表示行数，b表示列数
print("The shape of the object is:")
print(df.shape)
print('-----------------------------------------------------')
'''
The shape of the object is:
(7, 3)
'''

#size返回DataFrame中的元素数
print("The total number of elements in our object is:")
print(df.size)
print('-----------------------------------------------------')
'''
The total number of elements in our object is:
21
'''

#values将DataFrame中的实际数据作为NDarray返回
print("The actual data in our data frame is:")
print(df.values)
print('-----------------------------------------------------')
'''
The actual data in our data frame is:
[['Tom' 25 4.23]
 ['James' 26 3.24]
 ['Ricky' 25 3.98]
 ['Vin' 23 2.56]
 ['Steve' 30 3.2]
 ['Minsu' 29 4.6]
 ['Jack' 23 3.8]]
'''

'''
head()返回前n行(观察索引值)。显示元素的默认数量为5
tail()返回最后n行(观察索引值)。显示元素的默认数量为5
'''
print("The first two rows of the data frame is:")
print(df.head(2))
print("The last two rows of the data frame is:")
print(df.tail(2))
print('-----------------------------------------------------')
'''
The first two rows of the data frame is:
    Name  Age  Rating
0    Tom   25    4.23
1  James   26    3.24
The last two rows of the data frame is:
    Name  Age  Rating
5  Minsu   29     4.6
6   Jack   23     3.8
'''