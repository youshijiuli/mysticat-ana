import pandas as pd
import datetime

#创建日期范围
datelist = pd.date_range('2020/5/21',periods=5)
print(datelist)
print('-----------------------------------------------------')
'''
DatetimeIndex(['2020-05-21','2020-05-22','2020-05-23','2020-05-24','2020-05-25'],dtype='datetime64[ns]', freq='D')
'''

#更改日期频率
datelist = pd.date_range('2020/5/21',periods=5,freq='M')
print(datelist)
print('-----------------------------------------------------')
'''
DatetimeIndex(['2020-05-31','2020-06-30','2020-07-31','2020-08-31','2020-09-30'],dtype='datetime64[ns]',freq='M')
'''

#bdate_range()用来表示商业日期范围，不同于date_range()，它不包括星期六和星期天
start = datetime.datetime(2020,1,1)
end = datetime.datetime(2020,1,8)
dates = pd.bdate_range(start, end)
print(dates)
print('-----------------------------------------------------')
'''
DatetimeIndex(['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-06','2020-01-07', '2020-01-08'],dtype='datetime64[ns]', freq='B')
'''

#如果偏移设为分钟会包括周六和周日
df = pd.bdate_range('20200101 9:30','20200106 16:00',freq='1min')
print(df)
print('-----------------------------------------------------')

#进一步加工
x = df[df.indexer_between_time('9:30','16:00')] #限制要的时间段
x = x[x.dayofweek<5] #限制周一至周五
print(x)
print('-----------------------------------------------------')
'''
DatetimeIndex(['2020-01-01 09:30:00', '2020-01-01 09:31:00',
               '2020-01-01 09:32:00', '2020-01-01 09:33:00',
               '2020-01-01 09:34:00', '2020-01-01 09:35:00',
               '2020-01-01 09:36:00', '2020-01-01 09:37:00',
               '2020-01-01 09:38:00', '2020-01-01 09:39:00',
               ...
               '2020-01-03 15:51:00', '2020-01-03 15:52:00',
               '2020-01-03 15:53:00', '2020-01-03 15:54:00',
               '2020-01-03 15:55:00', '2020-01-03 15:56:00',
               '2020-01-03 15:57:00', '2020-01-03 15:58:00',
               '2020-01-03 15:59:00', '2020-01-03 16:00:00'],
              dtype='datetime64[ns]', length=1173, freq=None)
'''