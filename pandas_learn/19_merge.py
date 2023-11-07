import pandas as pd

left = pd.DataFrame({'id':[1,2,3,4,5],'Name':['Alex','Amy','Allen','Alice','Ayoung'],'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame({'id':[1,2,3,4,5],'Name':['Billy','Brian','Bran','Bryce','Betty'],'subject_id':['sub2','sub4','sub3','sub6','sub5']})
print (left)
print('-----------------------------------------------------')
print (right)
print('-----------------------------------------------------')
'''
   id    Name subject_id
0   1    Alex       sub1
1   2     Amy       sub2
2   3   Allen       sub4
3   4   Alice       sub6
4   5  Ayoung       sub5
-----------------------------------------------------
   id   Name subject_id
0   1  Billy       sub2
1   2  Brian       sub4
2   3   Bran       sub3
3   4  Bryce       sub6
4   5  Betty       sub5
'''

#在一个键上合并两个数据帧
rs = pd.merge(left,right,on='id')
print(rs)
print('-----------------------------------------------------')
'''
   id  Name_x subject_id_x Name_y subject_id_y
0   1    Alex         sub1  Billy         sub2
1   2     Amy         sub2  Brian         sub4
2   3   Allen         sub4   Bran         sub3
3   4   Alice         sub6  Bryce         sub6
4   5  Ayoung         sub5  Betty         sub5
'''

#合并多个键上的两个数据框
rs = pd.merge(left,right,on=['id','subject_id']) # 满足id和subject_id都相同
print(rs)
print('-----------------------------------------------------')
'''
   id  Name_x subject_id Name_y
0   4   Alice       sub6  Bryce
1   5  Ayoung       sub5  Betty
'''

'''
合并使用“how”的参数
如何合并参数指定如何确定哪些键将被包含在结果表中。如果组合键没有出现在左侧或右侧表中，则连接表中的值将为NA。
这里是how选项和SQL等效名称的总结:
合并方法   SQL等效               描述
left       LEFT OUTER JOIN       使用左侧对象的键
right      RIGHT OUTER JOIN      使用右侧对象的键
outer      FULL OUTER JOIN       使用键的联合
inner      INNER JOIN            使用键的交集
'''
rs = pd.merge(left,right,on='subject_id',how='left')
print(rs)
print('-----------------------------------------------------')
'''
   id_x  Name_x subject_id  id_y Name_y
0     1    Alex       sub1   NaN    NaN
1     2     Amy       sub2   1.0  Billy
2     3   Allen       sub4   2.0  Brian
3     4   Alice       sub6   4.0  Bryce
4     5  Ayoung       sub5   5.0  Betty
'''

rs = pd.merge(left,right,on='subject_id',how='right')
print(rs)
print('-----------------------------------------------------')
'''
   id_x  Name_x subject_id  id_y Name_y
0   2.0     Amy       sub2     1  Billy
1   3.0   Allen       sub4     2  Brian
2   4.0   Alice       sub6     4  Bryce
3   5.0  Ayoung       sub5     5  Betty
4   NaN     NaN       sub3     3   Bran
'''

rs = pd.merge(left,right,on='subject_id',how='outer')
print(rs)
print('-----------------------------------------------------')
'''
   id_x  Name_x subject_id  id_y Name_y
0   1.0    Alex       sub1   NaN    NaN
1   2.0     Amy       sub2   1.0  Billy
2   3.0   Allen       sub4   2.0  Brian
3   4.0   Alice       sub6   4.0  Bryce
4   5.0  Ayoung       sub5   5.0  Betty
5   NaN     NaN       sub3   3.0   Bran
'''

rs = pd.merge(left,right,on='subject_id',how='inner')
print(rs)
'''
   id_x  Name_x subject_id  id_y Name_y
0     2     Amy       sub2     1  Billy
1     3   Allen       sub4     2  Brian
2     4   Alice       sub6     4  Bryce
3     5  Ayoung       sub5     5  Betty
'''