import pandas as pd
import numpy as np

N=20
'''
date_range函数的freq参数取值参考:
B business day frequency 工作日频率
C custom business day frequency 自定义工作日频率
D calendar day frequency 日历日频率
W weekly frequency 每周频率
M month end frequency 月末频率
SM semi-month end frequency (15th and end of month) 半月结束频率（15日和月末）
BM business month end frequency 营业月结束频率
CBM custom business month end frequency 自定义营业月结束频率
MS month start frequency 月开始频率
SMS semi-month start frequency (1st and 15th) 半月开始频率（第1天和第15天）
BMS business month start frequency 营业月开始频率
CBMS custom business month start frequency 自定义营业月开始频率
Q quarter end frequency 四分之一结束频率
BQ business quarter end frequency 业务季度结束频率
QS quarter start frequency 季度开始频率
BQS business quarter start frequency 业务季开始频率
A, Y year end frequency 年终频率
BA, BY business year end frequency 业务年度结束频率
AS, YS year start frequency 年开始频率
BAS, BYS business year start frequency 营业年度开始频率
BH business hour frequency 营业时间频率
H hourly frequency 每小时频率
T, min minutely frequency 分钟的频率
S secondly frequency 秒钟的频率
L, ms milliseconds 毫秒
U, us microseconds 微妙
N nanoseconds 纳秒
'''
'''
linspace函数:在指定的间隔内返回均匀间隔的数字
random.normal函数参数参考:
参数loc(float)：正态分布的均值，对应着这个分布的中心。loc=0说明这一个以Y轴为对称轴的正态分布，
参数scale(float)：正态分布的标准差，对应分布的宽度，scale越大，正态分布的曲线越矮胖，scale越小，曲线越高瘦。
参数size(int 或者整数元组)：输出的值赋在shape里，默认为None。
'''
df = pd.DataFrame({
   'A': pd.date_range(start='2020-01-01',periods=N,freq='D'),
   'x': np.linspace(0,stop=N-1,num=N),
   'y': np.random.rand(N),
   'C': np.random.choice(['Low','Medium','High'],N).tolist(),
   'D': np.random.normal(100, 10, size=(N)).tolist()
})
print(df)
print('-----------------------------------------------------')
#重建索引
df_reindexed = df.reindex(index=[0,2,5], columns=['A', 'C', 'B'])
print (df_reindexed)
print('-----------------------------------------------------')
'''
            A     x         y       C           D
0  2016-01-01   0.0  0.590036    High  109.093357
1  2016-01-02   1.0  0.980302  Medium  104.344457
2  2016-01-03   2.0  0.369210  Medium  120.060444
3  2016-01-04   3.0  0.739644  Medium  105.712659
4  2016-01-05   4.0  0.721233  Medium   98.717930
5  2016-01-06   5.0  0.172767     Low  108.022031
6  2016-01-07   6.0  0.685071  Medium   87.904471
7  2016-01-08   7.0  0.525201    High   88.027214
8  2016-01-09   8.0  0.293176    High  103.227002
9  2016-01-10   9.0  0.650453  Medium  115.702113
10 2016-01-11  10.0  0.156175  Medium   92.295841
11 2016-01-12  11.0  0.142735  Medium  117.700653
12 2016-01-13  12.0  0.651538     Low   96.144326
13 2016-01-14  13.0  0.992997    High   85.867722
14 2016-01-15  14.0  0.083884     Low   96.181288
15 2016-01-16  15.0  0.774835    High  102.019218
16 2016-01-17  16.0  0.030027  Medium  105.095091
17 2016-01-18  17.0  0.097747     Low   81.228388
18 2016-01-19  18.0  0.913354     Low  106.253851
19 2016-01-20  19.0  0.921869    High  110.600785
-----------------------------------------------------
           A       C   B
0 2016-01-01    High NaN  #原DataFrame数据阵列没有第6列
2 2016-01-03  Medium NaN
5 2016-01-06     Low NaN
'''

#reindex_like重建索引与其他对象对齐
df1 = pd.DataFrame(np.random.randn(10,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(7,3),columns=['col1','col2','col3'])
print('df1:')
print(df1)
print('********************************************')
print('df2:')
print(df2)
print('********************************************')
df1 = df1.reindex_like(df2) # 必须确保df1和df2列明相同
print('df1_reindex_like:')
print(df1)
print('-----------------------------------------------------')
'''
df1:
       col1      col2      col3
0  1.120884 -0.722240 -0.035394
1  0.567509 -0.383762  1.828184
2 -0.522544 -0.240184 -0.919806
3  0.149930 -1.641542  0.854048
4 -1.112209  1.459420  1.412488
5 -0.180803 -0.182349 -1.539578
6  1.493674  1.143905 -0.371386
7 -0.741226 -0.763347 -1.243734
8 -0.782101 -0.567510 -0.481966
9  1.229414  1.183105  1.282665
********************************************
df2:
       col1      col2      col3
0  0.176301  1.271658  2.233986
1  0.024532  1.476283 -2.297913
2 -0.268861 -0.861881  0.386327
3 -1.322043  0.805677 -0.692940
4  1.750905 -0.531995 -1.136702
5  1.304911 -1.437062 -0.014875
6 -0.455027  0.743176 -0.708046
********************************************
df1_reindex_like: #对齐df2，也只有6行数据
       col1      col2      col3
0  1.120884 -0.722240 -0.035394
1  0.567509 -0.383762  1.828184
2 -0.522544 -0.240184 -0.919806
3  0.149930 -1.641542  0.854048
4 -1.112209  1.459420  1.412488
5 -0.180803 -0.182349 -1.539578
6  1.493674  1.143905 -0.371386
'''

'''
reindex()填充
pad/ffill - 向前填充值(向下复制填充最近的非NaN数据)
bfill/backfill - 向后填充值(向上复制填充最近的非NaN数据)
nearest  - 从最近的索引值填充(NaN的数据由最近的非NaN数据复制填充)
'''
df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])
print('原df1:')
print(df1)
print('原df2:')
print(df2)
# Padding NAN's
print('df2_reindex_like:')
print(df2.reindex_like(df1))
# Now Fill the NAN's with preceding Values
print("向前填充值:")
print(df2.reindex_like(df1,method='ffill'))
print('-----------------------------------------------------')
'''
原df1:
       col1      col2      col3
0  1.099247 -0.994045 -0.694985
1 -0.961867 -0.626915  0.279980
2  1.542600 -0.563582  1.234232
3 -0.431756  1.694917  1.559258
4 -2.124758  0.139736 -0.804344
5  0.422229 -0.525990  1.305312
原df2:
       col1      col2      col3
0 -0.098905 -1.440083 -0.406245
1  0.762296  0.629481 -0.257523
df2_reindex_like:
       col1      col2      col3
0 -0.098905 -1.440083 -0.406245
1  0.762296  0.629481 -0.257523
2       NaN       NaN       NaN
3       NaN       NaN       NaN
4       NaN       NaN       NaN
5       NaN       NaN       NaN
向前填充值:# 原先的NaN值根据索引1行向前复制填充
       col1      col2      col3
0 -0.098905 -1.440083 -0.406245
1  0.762296  0.629481 -0.257523
2  0.762296  0.629481 -0.257523
3  0.762296  0.629481 -0.257523
4  0.762296  0.629481 -0.257523
5  0.762296  0.629481 -0.257523
'''

#设置填充限制
df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])
print(df2.reindex_like(df1))
print("向前填充值1行数据:")
print(df2.reindex_like(df1,method='ffill',limit=1))
print('-----------------------------------------------------')
'''
       col1      col2      col3
0  1.283185 -0.888355 -0.233402
1  0.219788 -0.896609  0.836132
2       NaN       NaN       NaN
3       NaN       NaN       NaN
4       NaN       NaN       NaN
5       NaN       NaN       NaN
向前填充值1行数据:
       col1      col2      col3
0  1.283185 -0.888355 -0.233402
1  0.219788 -0.896609  0.836132
2  0.219788 -0.896609  0.836132 # 只填充1行
3       NaN       NaN       NaN
4       NaN       NaN       NaN
5       NaN       NaN       NaN
'''

#重命名,rename()方法允许基于一些映射(字典或者系列)或任意函数来重新标记一个轴
df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
print(df1)
print ("重命名行列:")
print(df1.rename(columns={'col1':'c1','col2':'c2'},index ={0 :'apple',1 :'banana',2 :'durian'}))
'''
       col1      col2      col3
0 -1.825568  0.033222  1.078255
1  0.254910  0.343282  0.488169
2  0.065620  0.795595  0.817078
3  2.096562 -0.725959 -1.851755
4  0.005908 -1.881947 -0.570932
5  0.223082  0.630078 -0.440466
重命名行列:
              c1        c2      col3
apple  -1.825568  0.033222  1.078255
banana  0.254910  0.343282  0.488169
durian  0.065620  0.795595  0.817078
3       2.096562 -0.725959 -1.851755
4       0.005908 -1.881947 -0.570932
5       0.223082  0.630078 -0.440466
'''