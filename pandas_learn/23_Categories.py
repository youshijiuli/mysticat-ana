import pandas as pd
import numpy as np

#通过在pandas对象创建中将dtype指定为“category”
s = pd.Series(["a","b","c","a"], dtype="category")
print(s)
print('-----------------------------------------------------')
'''
0    a
1    b
2    c
3    a
dtype: category
Categories (3, object): [a, b, c]
'''

#使用Categorical标准Pandas分类构造函数
cat = pd.Categorical(['a','b','c','a','b','c'])
print(cat)
print('-----------------------------------------------------')
'''
[a, b, c, a, b, c]
Categories (3, object): [a, b, c]
'''

#第二个参数表示类别。在类别中d不存在将被视为NaN
cat=pd.Categorical(['a','b','c','a','b','c','d'],['c','b','a'])
print(cat)
print('-----------------------------------------------------')
'''
[a, b, c, a, b, c, NaN]
Categories (3, object): [c, b, a]
'''

#排序
cat=pd.Categorical(['a','b','c','a','b','c','d'], ['c', 'b', 'a'],ordered=True)
print(cat)
print('-----------------------------------------------------')
'''
从逻辑上讲，排序(ordered)意味着，a大于b，b大于c
[a, b, c, a, b, c, NaN]
Categories (3, object): [c < b < a]
'''

#describe()得到与类型字符串的Series或DataFrame类似的输出
cat = pd.Categorical(["a","c","c",np.nan], categories=["b","a","c"])
df = pd.DataFrame({"cat":cat,"s":["a","c","c",np.nan]})
print (df.describe())
print('-----------------------------------------------------')
print (df["cat"].describe())
print('-----------------------------------------------------')
'''
       cat  s
count    3  3
unique   2  2
top      c  c
freq     2  2
-----------------------------------------------------
count     3
unique    2
top       c
freq      2
Name: cat, dtype: object
'''

#obj.cat.categories命令用于获取对象的类别
s = pd.Categorical(["a","c","c",np.nan],categories=["b","a","c"])
print(s.categories)
print('-----------------------------------------------------')
'''
Index(['b', 'a', 'c'], dtype='object')
'''

#重命名类别是通过将新值分配给series.cat.categories属性来完成
s = pd.Series(["a","b","c","a"], dtype="category")
s.cat.categories = ["Group %s" % g for g in s.cat.categories]
print(s.cat.categories)
print('-----------------------------------------------------')
'''
Index(['Group a', 'Group b', 'Group c'], dtype='object')
'''

#使用Categorical.add.categories()方法追加新类别
s = pd.Series(["a","b","c","a"],dtype="category")
s = s.cat.add_categories([4])
print(s.cat.categories)
print('-----------------------------------------------------')
'''
Index(['a', 'b', 'c', 4], dtype='object')
'''

#使用Categorical.remove_categories()方法删除不需要类别
s = pd.Series(["a","b","c","a"],dtype="category")
print(s.cat.remove_categories("a"))
print('-----------------------------------------------------')
'''
0    NaN
1      b
2      c
3    NaN
dtype: category
Categories (2, object): [b, c]
'''