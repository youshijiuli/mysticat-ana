import pandas as pd
import numpy as np
import xarray as xr

#创建DataArray1
data = np.random.rand(4,3)
locs = ['beijing', 'shanghai', 'guangzhou']
times = pd.date_range('2020-01-01', periods=4)
foo = xr.DataArray(data, coords=[times,locs], dims=['times','city'])
print(foo)
print('-----------------------------------------------------')
'''
<xarray.DataArray (times: 4, city: 3)>
array([[0.85669035, 0.18898483, 0.42078161],
       [0.33922066, 0.69418082, 0.85689543],
       [0.53280417, 0.40773875, 0.32883664],
       [0.30612777, 0.31920479, 0.68427873]])
Coordinates:
  * times     (times) timestime64[ns] 2020-01-01 2020-01-02 2020-01-03 2020-01-04
  * city     (city) <U9 'beijing' 'shanghai' 'guangzhou'
'''

#创建DataArray2—不设定坐标
foo = xr.DataArray(data)
print(foo)
print('-----------------------------------------------------')
'''
<xarray.DataArray (dim_0: 4, dim_1: 3)>
array([[0.54989213, 0.69846077, 0.02484918],
       [0.33194074, 0.34435203, 0.95863462],
       [0.69988189, 0.66363655, 0.25958871],
       [0.53178466, 0.43543301, 0.32999125]])
Dimensions without coordinates: dim_0, dim_1
'''

#创建DataArray3—设定元祖序列作为坐标
data = np.random.rand(4,3)
times=[('2020-01-01'),('2020-01-02'),('2020-01-03'),('2020-01-04')]
locs=[('beijing'),('shanghai'),('guangzhou')]
foo = xr.DataArray(data, coords=[('times', times), ('city', locs)])
print(foo)
print('-----------------------------------------------------')
'''
<xarray.DataArray (times: 4, city: 3)>
array([[0.49757059, 0.72934003, 0.82347596],
       [0.54961109, 0.38952966, 0.24480173],
       [0.40846152, 0.36316063, 0.17120898],
       [0.96056183, 0.15505025, 0.362019  ]])
Coordinates:
  * times     (times) <U10 '2020-01-01' '2020-01-02' '2020-01-03' '2020-01-04'
  * city     (city) <U9 'beijing' 'shanghai' 'guangzhou'
'''

#创建DataArray4—设定字典作为坐标
foo=xr.DataArray(data,coords={'time':times,'space':locs,'const':42,'ranking':('space',[1, 2, 3])},dims=['time','space'])
print(foo)
print('-----------------------------------------------------')
'''
<xarray.DataArray (time: 4, space: 3)>
array([[0.97925202, 0.33437374, 0.17637918],
       [0.34874966, 0.44310298, 0.84050657],
       [0.49291399, 0.76278477, 0.70555877],
       [0.86489609, 0.8290611 , 0.07745245]])
Coordinates:
  * time     (time) <U10 '2020-01-01' '2020-01-02' '2020-01-03' '2020-01-04'
  * space    (space) <U9 'beijing' 'shanghai' 'guangzhou'
    const    int32 42
    ranking  (space) int32 1 2 3
'''

#创建DataArray5—跨多个维度的座标的字典
foo=xr.DataArray(data,coords={'time':times,'space':locs,'const':42,'ranking':(('time','space'),np.arange(12).reshape(4,3))},dims=['time','space'])
print(foo)
print('-----------------------------------------------------')
'''
<xarray.DataArray (time: 4, space: 3)>
array([[0.63124358, 0.67008045, 0.15957764],
       [0.13183074, 0.73271734, 0.50673914],
       [0.33347839, 0.48637254, 0.57481337],
       [0.66615526, 0.36947788, 0.22859004]])
Coordinates:
  * time     (time) <U10 '2020-01-01' '2020-01-02' '2020-01-03' '2020-01-04'
  * space    (space) <U9 'beijing' 'shanghai' 'guangzhou'
    const    int32 42
    # ranking维度本身也是一个4 X 3的矩阵
    ranking  (time, space) int32 0 1 2 3 4 5 6 7 8 9 10 11
'''

#创建DataArray6—根据pandas的Series和DataFrame创建
df = pd.DataFrame({'x':[0,1],'y':[2,3]},index=['a','b'])
df.index.name = 'abc'
df.columns.name = 'xyz'
print('pandas的DataFrame数据:')
print(df)
print('xarray封装DataFrame数据:')
foo=xr.DataArray(df)
print(foo)
print('-----------------------------------------------------')
'''
pandas的DataFrame数据:
xyz  x  y
abc      
a    0  2
b    1  3
xarray封装DataFrame数据:
<xarray.DataArray (abc: 2, xyz: 2)>
array([[0, 2],
       [1, 3]], dtype=int64)
Coordinates:
  * abc      (abc) object 'a' 'b' # abc索引名称包括a和b索引
  * xyz      (xyz) object 'x' 'y' # xyz列名称包括x和y列
'''

#显示DataArray的特性值
data = np.random.rand(4,3)
locs = ['beijing', 'shanghai', 'guangzhou']
times = pd.date_range('2020-01-01', periods=4)
foo = xr.DataArray(data, coords=[times,locs], dims=['times','city'])
print('values值:')
print(foo.values)
print('dims值:')
print(foo.dims)
print('coords值:')
print(foo.coords)
print('attrs值:')
print(foo.attrs) #其他设置过的元数据字典
print('name值:')
print(foo.name)
print('-----------------------------------------------------')
'''
values值:
[[0.32259074 0.22672477 0.83801168]
 [0.0725351  0.17110382 0.49200772]
 [0.42110477 0.16877604 0.42996814]
 [0.82486979 0.71531442 0.64333906]]
dims值:
('times', 'city')
coords值:
Coordinates:
  * times    (times) datetime64[ns] 2020-01-01 2020-01-02 2020-01-03 2020-01-04
  * city     (city) <U9 'beijing' 'shanghai' 'guangzhou'
attrs值:
{}
name值:
None
'''

# 填充之前丢失的元数据
foo.name = 'foo'
foo.attrs['units'] = 'meters'
print(foo)
print('-----------------------------------------------------')
'''
                  #设置的name
<xarray.DataArray 'foo' (times: 4, city: 3)>
array([[0.38221223, 0.84098074, 0.80021469],
       [0.21717482, 0.86353327, 0.5798719 ],
       [0.04780346, 0.71365008, 0.07320618],
       [0.07013895, 0.55325891, 0.73305981]])
Coordinates:
  * times    (times) datetime64[ns] 2020-01-01 2020-01-02 2020-01-03 2020-01-04
  * city     (city) <U9 'beijing' 'shanghai' 'guangzhou'
Attributes:
    units:    meters #设置的属性units
'''

# 修改name
foo.name='bar' #foo.rename('bar')原先的rename方法已失效，修改后无反应
print(foo)
print('-----------------------------------------------------')

# 查看times坐标
print(foo.coords['times']) #也可简写foo['times']
print('-----------------------------------------------------')
'''
<xarray.DataArray 'times' (times: 4)>
array(['2020-01-01T00:00:00.000000000', '2020-01-02T00:00:00.000000000',
       '2020-01-03T00:00:00.000000000', '2020-01-04T00:00:00.000000000'],
      dtype='datetime64[ns]')
Coordinates:
  * times    (times) datetime64[ns] 2020-01-01 2020-01-02 2020-01-03 2020-01-04
'''

# 修改与删除坐标
foo['times']=pd.date_range('2020-01-05', periods=4)
print(foo.coords)
print('********************************************')
del foo['times']
print(foo.coords)
print('-----------------------------------------------------')