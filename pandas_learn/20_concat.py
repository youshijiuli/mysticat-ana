import pandas as pd
import datetime

one = pd.DataFrame({'Name':['Alex','Amy','Allen','Alice','Ayoung'],
                    'subject_id':['sub1','sub2','sub4','sub6','sub5'],
                    'Marks_scored':[98,90,87,69,78]},
                   index=[1,2,3,4,5])
two = pd.DataFrame({'Name': ['Billy','Brian','Bran','Bryce','Betty'],
                    'subject_id':['sub2','sub4','sub3','sub6','sub5'],
                    'Marks_scored':[89,80,79,97,88]},
                   index=[1,2,3,4,5])
rs = pd.concat([one,two])
print(rs)
print('-----------------------------------------------------')
'''
     Name subject_id  Marks_scored
1    Alex       sub1            98
2     Amy       sub2            90
3   Allen       sub4            87
4   Alice       sub6            69
5  Ayoung       sub5            78
1   Billy       sub2            89
2   Brian       sub4            80
3    Bran       sub3            79
4   Bryce       sub6            97
5   Betty       sub5            88
'''

#把特定的键与每个碎片的DataFrame关联起来
rs = pd.concat([one,two],keys=['x','y'])
print(rs)
print('-----------------------------------------------------')
'''
       Name subject_id  Marks_scored
x 1    Alex       sub1            98
  2     Amy       sub2            90
  3   Allen       sub4            87
  4   Alice       sub6            69
  5  Ayoung       sub5            78
y 1   Billy       sub2            89
  2   Brian       sub4            80
  3    Bran       sub3            79
  4   Bryce       sub6            97
  5   Betty       sub5            88
'''

#ignore_index设置为True生成连续索引
rs = pd.concat([one,two],keys=['x','y'],ignore_index=True)
print(rs)
print('-----------------------------------------------------')
'''
     Name subject_id  Marks_scored
0    Alex       sub1            98
1     Amy       sub2            90
2   Allen       sub4            87
3   Alice       sub6            69
4  Ayoung       sub5            78
5   Billy       sub2            89
6   Brian       sub4            80
7    Bran       sub3            79
8   Bryce       sub6            97
9   Betty       sub5            88
'''

#沿axis=1添加两个对象，则会添加新列
rs = pd.concat([one,two],axis=1)
print(rs)
print('-----------------------------------------------------')
'''
     Name subject_id  Marks_scored   Name subject_id  Marks_scored
1    Alex       sub1            98  Billy       sub2            89
2     Amy       sub2            90  Brian       sub4            80
3   Allen       sub4            87   Bran       sub3            79
4   Alice       sub6            69  Bryce       sub6            97
5  Ayoung       sub5            78  Betty       sub5            88
'''

#使用append方法附加连接
rs = one.append(two)
print(rs)
print('-----------------------------------------------------')
'''
     Name subject_id  Marks_scored
1    Alex       sub1            98
2     Amy       sub2            90
3   Allen       sub4            87
4   Alice       sub6            69
5  Ayoung       sub5            78
1   Billy       sub2            89
2   Brian       sub4            80
3    Bran       sub3            79
4   Bryce       sub6            97
5   Betty       sub5            88
'''

rs = one.append([two,one,two])
print(rs)
print('-----------------------------------------------------')
'''
     Name subject_id  Marks_scored
1    Alex       sub1            98
2     Amy       sub2            90
3   Allen       sub4            87
4   Alice       sub6            69
5  Ayoung       sub5            78
1   Billy       sub2            89
2   Brian       sub4            80
3    Bran       sub3            79
4   Bryce       sub6            97
5   Betty       sub5            88
1    Alex       sub1            98
2     Amy       sub2            90
3   Allen       sub4            87
4   Alice       sub6            69
5  Ayoung       sub5            78
1   Billy       sub2            89
2   Brian       sub4            80
3    Bran       sub3            79
4   Bryce       sub6            97
5   Betty       sub5            88
'''

'''
Pandas为时间序列数据的工作时间提供了一个强大的工具，尤其是在金融领域:
生成时间序列
将时间序列转换为不同的频率
'''
#获取当前的日期和时间,pd.datetime将被废除
print(datetime.datetime.now())
print('-----------------------------------------------------')
'''
2020-05-21 17:01:21.932550
'''

#创建时间戳
time = pd.Timestamp('2020-5-01')
print(time)
print('-----------------------------------------------------')

#创建时间范围
time = pd.date_range("12:00","23:59",freq="30min").time
print(time)
print('-----------------------------------------------------')
'''
[datetime.time(12, 0) datetime.time(12, 30) datetime.time(13, 0)
 datetime.time(13, 30) datetime.time(14, 0) datetime.time(14, 30)
 datetime.time(15, 0) datetime.time(15, 30) datetime.time(16, 0)
 datetime.time(16, 30) datetime.time(17, 0) datetime.time(17, 30)
 datetime.time(18, 0) datetime.time(18, 30) datetime.time(19, 0)
 datetime.time(19, 30) datetime.time(20, 0) datetime.time(20, 30)
 datetime.time(21, 0) datetime.time(21, 30) datetime.time(22, 0)
 datetime.time(22, 30) datetime.time(23, 0) datetime.time(23, 30)]
'''

#改变时间的频率
time = pd.date_range("12:00","23:59",freq="H").time
print(time)
print('-----------------------------------------------------')
'''
[datetime.time(12, 0) datetime.time(13, 0) datetime.time(14, 0)
 datetime.time(15, 0) datetime.time(16, 0) datetime.time(17, 0)
 datetime.time(18, 0) datetime.time(19, 0) datetime.time(20, 0)
 datetime.time(21, 0) datetime.time(22, 0) datetime.time(23, 0)]
'''

#使用to_datetime函数转换为时间戳
time = pd.to_datetime(pd.Series(['Jul 31, 2020','2020-05-10', None]))
print(time)
print('-----------------------------------------------------')
'''
0   2020-07-31
1   2020-05-10
2          NaT
dtype: datetime64[ns]
'''

time = pd.to_datetime(['2020/01/23', '2020.4.30', None])
print(time)
'''
DatetimeIndex(['2020-01-23', '2020-04-30', 'NaT'], dtype='datetime64[ns]', freq=None)
'''