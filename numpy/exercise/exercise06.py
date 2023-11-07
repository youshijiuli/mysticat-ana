import pandas as pd

'''
请用字典结构生成以下pandas的DataFrame数据结构，打印效果如下:
         one     two
index1  10.0   40
index2  20.0   50
index3  30.0   60
index4   NaN   70
'''
d = {'one':pd.Series([10,20,30],index=['index1','index2','index3']),
     'two':pd.Series([40,50,60,70],index=['index1','index2','index3','index4'])}
df = pd.DataFrame(d)
print(df)