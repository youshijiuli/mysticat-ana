import pandas as pd
import numpy as np

s = pd.Series(['Tom','William Rick','John','Alber@t',np.nan,'1234','SteveMinsu'])
print (s)
print('-----------------------------------------------------')
'''
0             Tom
1    William Rick
2            John
3         Alber@t
4             NaN
5            1234
6      SteveMinsu
dtype: object
'''

#将Series/Index中的字符串转换为小写
print(s.str.lower())
print('-----------------------------------------------------')
#将Series/Index中的字符串转换为大写
print (s.str.upper())
print('-----------------------------------------------------')
'''
0                 tom
1    william rickjohn
2             alber@t
3                 NaN
4                1234
5          steveminsu
dtype: object
-----------------------------------------------------
0                 TOM
1    WILLIAM RICKJOHN
2             ALBER@T
3                 NaN
4                1234
5          STEVEMINSU
dtype: object
'''

#len()计算字符串长度
print(s.str.len())
print('-----------------------------------------------------')
'''
0     3.0
1    16.0
2     7.0
3     NaN
4     4.0
5    10.0
dtype: float64
'''

#strip()从两侧的系列/索引中的每个字符串中删除空格(包括换行符)
s = pd.Series(['  Tom   ',' William Rick','John', 'Alber@t'])
print (s)
print('-----------------------------------------------------')
print (s.str.strip())
print('-----------------------------------------------------')
'''
0           Tom   
1     William Rick
2             John
3          Alber@t
dtype: object
-----------------------------------------------------
0             Tom
1    William Rick
2            John
3         Alber@t
dtype: object
'''

#split(' ')用给定的模式拆分每个字符串
s = pd.Series(['Tom ','William Rick','John','Alber@t'])
print(s)
print('-----------------------------------------------------')
print(s.str.split(' '))
print('-----------------------------------------------------')
'''
0            Tom 
1    William Rick
2            John
3         Alber@t
dtype: object
-----------------------------------------------------
0            [Tom, ]
1    [William, Rick]
2             [John]
3          [Alber@t]
dtype: object
'''

#cat(sep=' ')使用给定的分隔符连接系列/索引元素
print(s.str.cat(sep=' <=> '))
print('-----------------------------------------------------')
'''
Tom  <=> William Rick <=> John <=> Alber@t
'''

#get_dummies()返回具有单热编码值的数据帧(DataFrame)
print(s.str.get_dummies())
print('-----------------------------------------------------')
'''
   Alber@t  John  Tom   William Rick
0        0     0     1             0
1        0     0     0             1
2        0     1     0             0
3        1     0     0             0
'''

#contains(pattern)如果元素中包含子字符串，则返回每个元素的布尔值True，否则为False
s = pd.Series(['Tom','William Rick','John','Alber@t'])
print (s.str.contains('o'))
print('-----------------------------------------------------')
'''
0     True
1    False
2     True
3    False
dtype: bool
'''

#replace(a,b)将值a替换为值b
print(s.str.replace('@','$'))
print('-----------------------------------------------------')
'''
0             Tom
1    William Rick
2            John
3         Alber$t
dtype: object
'''

#repeat(value)重复每个元素指定的次数
print(s.str.repeat(2))
print('-----------------------------------------------------')
'''
0                      TomTom
1    William RickWilliam Rick
2                    JohnJohn
3              Alber@tAlber@t
dtype: object
'''

#count(pattern)返回模式中每个元素的出现总数
print(s.str.count('m'))
print('-----------------------------------------------------')
'''
0    1
1    1
2    0
3    0
dtype: int64
'''

#startswith(pattern)如果系列/索引中的元素以模式开始，则返回true
print(s.str.startswith('T'))
print('-----------------------------------------------------')
'''
0     True
1    False
2    False
3    False
dtype: bool
'''

#endswith(pattern)如果系列/索引中的元素以模式结束，则返回true
print(s.str.endswith('t'))
print('-----------------------------------------------------')
'''
0    False
1    False
2    False
3     True
dtype: bool
'''

#find(pattern)返回模式第一次出现的位置
print(s.str.find('e'))
print('-----------------------------------------------------')
'''
0   -1
1   -1
2   -1
3    3
dtype: int64
'''

#findall(pattern)返回模式的所有出现的列表
print (s.str.findall('o'))
print('-----------------------------------------------------')
'''
0    [o]
1     []
2    [o]
3     []
dtype: object
'''

#swapcase变换字母大小写
print(s.str.swapcase())
print('-----------------------------------------------------')
'''
0             tOM
1    wILLIAM rICK
2            jOHN
3         aLBER@T
dtype: object
'''

#islower()检查系列/索引中每个字符串中的所有字符是否小写，返回布尔值
print (s.str.islower())
print('-----------------------------------------------------')
'''
0    False
1    False
2    False
3    False
dtype: bool
'''

#isupper()检查系列/索引中每个字符串中的所有字符是否大写，返回布尔值
s = pd.Series(['TOM','William Rick','John','Alber@t'])
print(s.str.isupper())
print('-----------------------------------------------------')
'''
0     True
1    False
2    False
3    False
dtype: bool
'''

#isnumeric()检查系列/索引中每个字符串中的所有字符是否为数字，返回布尔值
s = pd.Series(['Tom','1199','William Rick','John','Alber@t'])
print(s.str.isnumeric())
'''
0    False
1     True
2    False
3    False
4    False
dtype: bool
'''