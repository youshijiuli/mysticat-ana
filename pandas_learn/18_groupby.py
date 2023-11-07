import pandas as pd
import numpy as np

ipl_data ={'Team':['Riders','Riders','Devils','Devils','Kings','kings','Kings','Kings','Riders','Royals','Royals','Riders'],
         'Rank':[1,2,2,3,3,4,1,1,2,4,1,2],
         'Year':[2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)
print(df)
print('-----------------------------------------------------')
'''
      Team  Rank  Year  Points
0   Riders     1  2014     876
1   Riders     2  2015     789
2   Devils     2  2014     863
3   Devils     3  2015     673
4    Kings     3  2014     741
5    kings     4  2015     812
6    Kings     1  2016     756
7    Kings     1  2017     788
8   Riders     2  2016     694
9   Royals     4  2014     701
10  Royals     1  2015     804
11  Riders     2  2017     690
'''

'''
将数据拆分成组Pandas对象可以分成任何对象。有多种方式来拆分对象:
obj.groupby('key')
obj.groupby(['key1','key2'])
obj.groupby(key,axis=1)
'''
print(df.groupby('Team'))
print('-----------------------------------------------------')
'''
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000029DA5439580>
'''

#查看分组
print(df.groupby('Team').groups)
print('-----------------------------------------------------')
'''
{'Devils': Int64Index([2, 3], dtype='int64'), 
'Kings': Int64Index([4, 6, 7], dtype='int64'), 
'Riders': Int64Index([0, 1, 8, 11], dtype='int64'), 
'Royals': Int64Index([9, 10], dtype='int64'), 
'kings': Int64Index([5], dtype='int64')}
'''

#按多列分组
print(df.groupby(['Team','Year']).groups)
print('-----------------------------------------------------')
'''
{('Devils', 2014): Int64Index([2], dtype='int64'), 
('Devils', 2015): Int64Index([3], dtype='int64'), 
('Kings', 2014): Int64Index([4], dtype='int64'), 
('Kings', 2016): Int64Index([6], dtype='int64'), 
('Kings', 2017): Int64Index([7], dtype='int64'), 
('Riders', 2014): Int64Index([0], dtype='int64'), 
('Riders', 2015): Int64Index([1], dtype='int64'), 
('Riders', 2016): Int64Index([8], dtype='int64'), 
('Riders', 2017): Int64Index([11], dtype='int64'), 
('Royals', 2014): Int64Index([9], dtype='int64'), 
('Royals', 2015): Int64Index([10], dtype='int64'), 
('kings', 2015): Int64Index([5], dtype='int64')}
'''

#迭代遍历分组使用groupby对象，可以遍历类似itertools.obj的对象
grouped = df.groupby('Year')
for name,group in grouped:
    print(name)
    print(group)
print('-----------------------------------------------------')
'''
2014
     Team  Rank  Year  Points
0  Riders     1  2014     876
2  Devils     2  2014     863
4   Kings     3  2014     741
9  Royals     4  2014     701
2015
      Team  Rank  Year  Points
1   Riders     2  2015     789
3   Devils     3  2015     673
5    kings     4  2015     812
10  Royals     1  2015     804
2016
     Team  Rank  Year  Points
6   Kings     1  2016     756
8  Riders     2  2016     694
2017
      Team  Rank  Year  Points
7    Kings     1  2017     788
11  Riders     2  2017     690
'''

#使用get_group()方法，可以选择一个组
grouped = df.groupby('Year')
print(grouped.get_group(2014))
print('-----------------------------------------------------')
'''
     Team  Rank  Year  Points
0  Riders     1  2014     876
2  Devils     2  2014     863
4   Kings     3  2014     741
9  Royals     4  2014     701
'''

#聚合函数为每个组返回单个聚合值。当创建了分组(group by)对象，就可以对分组数据执行多个聚合操作。一个比较常用的是通过聚合或等效的agg方法聚合
grouped = df.groupby('Year')
print(grouped['Points'].agg(np.mean))
print('-----------------------------------------------------')
'''
Year
2014    795.25
2015    769.50
2016    725.00
2017    739.00
Name: Points, dtype: float64
'''

#size()函数查看每个分组的大小的方法
grouped = df.groupby('Team')
print(grouped.agg(np.size))
print('-----------------------------------------------------')
'''
        Rank  Year  Points
Team                      
Devils     2     2       2
Kings      3     3       3
Riders     4     4       4
Royals     2     2       2
kings      1     1       1
'''

#一次应用多个聚合函数
grouped = df.groupby('Team')
agg = grouped['Points'].agg([np.sum,np.mean,np.std])
print(agg)
print('-----------------------------------------------------')
'''
         sum        mean         std
Team                                
Devils  1536  768.000000  134.350288
Kings   2285  761.666667   24.006943
Riders  3049  762.250000   88.567771
Royals  1505  752.500000   72.831998
kings    812  812.000000         NaN
'''

#分组或列上的转换返回索引大小与被分组的索引相同的对象。因此转换应该返回与组块大小相同的结果
grouped = df.groupby('Team')
print(grouped.groups)
print('-----------------------------------------------------')
score = lambda x:(x-x.mean())/x.std()*10
print(grouped.transform(score))
print('-----------------------------------------------------')
'''
{'Devils': Int64Index([2, 3], dtype='int64'), 
'Kings': Int64Index([4, 6, 7], dtype='int64'), 
'Riders': Int64Index([0, 1, 8, 11], dtype='int64'),
'Royals': Int64Index([9, 10], dtype='int64'), 
'kings': Int64Index([5], dtype='int64')}
-----------------------------------------------------
         Rank       Year     Points
0  -15.000000 -11.618950  12.843272
1    5.000000  -3.872983   3.020286
2   -7.071068  -7.071068   7.071068
3    7.071068   7.071068  -7.071068
4   11.547005 -10.910895  -8.608621
5         NaN        NaN        NaN
6   -5.773503   2.182179  -2.360428
7   -5.773503   8.728716  10.969049
8    5.000000   3.872983  -7.705963
9    7.071068  -7.071068  -7.071068
10  -7.071068   7.071068   7.071068
11   5.000000  11.618950  -8.157595
'''

#过滤根据定义的标准过滤数据并返回数据的子集。filter()函数用于过滤数据
grouped = df.groupby('Team')
print(grouped.groups)
print('-----------------------------------------------------')
filter = df.groupby('Team').filter(lambda x:len(x)>=3) #返回三次以上参加的队伍
print(filter)
print('-----------------------------------------------------')
'''
{'Devils': Int64Index([2, 3], dtype='int64'), 
'Kings': Int64Index([4, 6, 7], dtype='int64'),  #三次以上参加的队伍
'Riders': Int64Index([0, 1, 8, 11], dtype='int64'),  #三次以上参加的队伍
'Royals': Int64Index([9, 10], dtype='int64'), 
'kings': Int64Index([5], dtype='int64')}
-----------------------------------------------------
      Team  Rank  Year  Points
0   Riders     1  2014     876
1   Riders     2  2015     789
4    Kings     3  2014     741
6    Kings     1  2016     756
7    Kings     1  2017     788
8   Riders     2  2016     694
11  Riders     2  2017     690
'''