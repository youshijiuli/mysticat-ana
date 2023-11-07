import pandas as pd
import numpy as np

df=pd.read_csv("temp.csv")
print(df)
print('-----------------------------------------------------')
'''
   S.No    Name  Age       City  Salary
0     1     Tom   28    Toronto   20000
1     2     Lee   32   HongKong    3000
2     3  Steven   43   Bay Area    8300
3     4     Ram   38  Hyderabad    3900
'''

#自定义索引
df=pd.read_csv("temp.csv",index_col=['S.No'])
print(df)
print('-----------------------------------------------------')
'''
        Name  Age       City  Salary
S.No                                
1        Tom   28    Toronto   20000
2        Lee   32   HongKong    3000
3     Steven   43   Bay Area    8300
4        Ram   38  Hyderabad    3900
'''

#dtype列作为字典传递
df = pd.read_csv("temp.csv",dtype={'Salary':np.float64}) #将Salary原来int64类型改成float64
print(df.dtypes)
print('-----------------------------------------------------')
'''
S.No        int64
Name       object
Age         int64
City       object
Salary    float64
dtype: object
'''

#使用names参数指定标题的名称
df=pd.read_csv("temp.csv",names=['a','b','c','d','e'])
print(df)
print('-----------------------------------------------------')
'''
标题名称附加了自定义名称，但文件中的标题还没有被消除
      a       b    c          d       e
0  S.No    Name  Age       City  Salary
1     1     Tom   28    Toronto   20000
2     2     Lee   32   HongKong    3000
3     3  Steven   43   Bay Area    8300
4     4     Ram   38  Hyderabad    3900
'''

#如果标题不是第一行，则将行号传递给标题。这将跳过前面的行
df=pd.read_csv("temp.csv",names=['a','b','c','d','e'],header=0)
print(df)
print('-----------------------------------------------------')
'''
   a       b   c          d      e
0  1     Tom  28    Toronto  20000
1  2     Lee  32   HongKong   3000
2  3  Steven  43   Bay Area   8300
3  4     Ram  38  Hyderabad   3900
'''

#skiprows跳到指定行数开始显示
df=pd.read_csv("temp.csv", skiprows=2)
print(df)
'''
   2     Lee  32   HongKong  3000
0  3  Steven  43   Bay Area  8300
1  4     Ram  38  Hyderabad  3900
'''
