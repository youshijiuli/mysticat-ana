import pandas as pd
import numpy as np

'''
请打印出以下pandas的序列结果：
20    aa
30    bb
40    cc
50    dd
dtype: object
'''
data = np.array(['aa','bb','cc','dd'])
s = pd.Series(data,index=[20,30,40,50])
print(s)

