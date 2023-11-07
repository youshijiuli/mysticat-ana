import pandas as pd

#字符串
timediff = pd.Timedelta('2 days 2 hours 15 minutes 30 seconds')
print(timediff)
print('-----------------------------------------------------')
'''
2 days 02:15:30
'''

#整数
timediff = pd.Timedelta(6,unit='h')
print(timediff)
print('-----------------------------------------------------')
'''
0 days 06:00:00
'''

#数据偏移
timediff = pd.Timedelta(days=2)
print(timediff)
print('-----------------------------------------------------')
'''
2 days 00:00:00
'''

#运算操作
s = pd.Series(pd.date_range('2020-1-1',periods=3,freq='D'))
td = pd.Series([pd.Timedelta(days=i) for i in range(3)])
df = pd.DataFrame(dict(A =s,B =td))
print(df)
print('-----------------------------------------------------')
'''
           A      B
0 2020-01-01 0 days
1 2020-01-02 1 days
2 2020-01-03 2 days
'''

#相加操作
df = pd.DataFrame(dict(A =s,B =td))
df['C']=df['A']+df['B']
print(df)
print('-----------------------------------------------------')
'''
           A      B          C
0 2020-01-01 0 days 2020-01-01
1 2020-01-02 1 days 2020-01-03
2 2020-01-03 2 days 2020-01-05
'''

#相减操作
df = pd.DataFrame(dict(A=s, B=td))
df['C']=df['A']+df['B']
df['D']=df['C']-df['B']
print(df)
'''
           A      B          C          D
0 2020-01-01 0 days 2020-01-01 2020-01-01
1 2020-01-02 1 days 2020-01-03 2020-01-02
2 2020-01-03 2 days 2020-01-05 2020-01-03
'''