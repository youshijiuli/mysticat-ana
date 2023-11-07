import pandas as pd
import numpy as np

unsorted_df=pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns=['col2','col1'])
print (unsorted_df)
print('-----------------------------------------------------')

#使用sort_index()方法，通过传递axis参数和排序顺序，可以对DataFrame进行排序。 默认情况下，按照升序对行标签进行排序。
asc_sorted_df=unsorted_df.sort_index()
print (asc_sorted_df)
print('-----------------------------------------------------')
desc_sorted_df=unsorted_df.sort_index(ascending=False)
print (desc_sorted_df)
print('-----------------------------------------------------')
'''
       col2      col1
0  1.877154 -0.083941
1 -1.326036  0.179948
2 -0.399063 -0.465008
3  0.304482 -0.612925
4  0.748230  0.601547
5 -0.770469 -1.066199
6  1.594197 -0.838231
7  0.945457  0.285526
8 -0.427039  1.936231
9  0.528863 -0.340283
-----------------------------------------------------
       col2      col1
9  0.528863 -0.340283
8 -0.427039  1.936231
7  0.945457  0.285526
6  1.594197 -0.838231
5 -0.770469 -1.066199
4  0.748230  0.601547
3  0.304482 -0.612925
2 -0.399063 -0.465008
1 -1.326036  0.179948
0  1.877154 -0.083941
'''

#列排序
col_sorted_df=unsorted_df.sort_index(axis=1)
print(col_sorted_df)
print('-----------------------------------------------------')
'''
       col1      col2
1 -0.143246  0.644528
4  1.080042 -0.416753
6  2.438776 -0.593799
2 -1.212113 -1.235193
3 -0.865098 -0.827953
5 -0.058463 -0.966069
9 -0.670185  1.137415
8  0.307156 -0.837121
0  1.397314 -2.216309
7  0.065886 -0.158305
'''

#sort_values()是按值排序的方法。它接受一个by参数，它将使用要与其排序值的DataFrame的列名称
unsorted_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
print(unsorted_df)
print('-----------------------------------------------------')
col1_sorted_df = unsorted_df.sort_values(by='col1')
print(col1_sorted_df)
print('-----------------------------------------------------')
col1_col2_sorted_df = unsorted_df.sort_values(by=['col1','col2'])
print(col1_col2_sorted_df)
print('-----------------------------------------------------')
'''
   col1  col2
0     2     1
1     1     3
2     1     2
3     1     4
-----------------------------------------------------
   col1  col2
1     1     3
2     1     2
3     1     4
0     2     1
-----------------------------------------------------
   col1  col2
2     1     2
1     1     3
3     1     4
0     2     1
'''

#sort_values()提供了从mergeesort，heapsort和quicksort中选择算法的一个配置。Mergesort是唯一稳定的算法。
sorted_df = unsorted_df.sort_values(by='col1',kind='mergesort')
print(sorted_df)
'''
   col1  col2
1     1     3
2     1     2
3     1     4
0     2     1
'''