import pandas as pd
import numpy as np
import xarray as xr
from matplotlib import pyplot as plt
import matplotlib

'''
np.random.randn从标准正态分布中返回一个或多个样本值
np.random.rand随机样本位于[0, 1)中返回
'''
temp = 15+8*np.random.randn(2,2,3) #温度
print('温度:')
print(temp)
precip = 10*np.random.rand(2,2,3) #降水
print('降水')
print(precip)
lon = [[-99.83, -99.32], [-99.79, -99.23]] #经度
lat = [[42.25, 42.21], [42.63, 42.59]] #纬度
ds = xr.Dataset({'temperature': (['x', 'y', 'time'],  temp),
'precipitation': (['x', 'y', 'time'], precip)},
coords={'lon': (['x', 'y'], lon),
'lat': (['x', 'y'], lat),
'time': pd.date_range('2020-02-06', periods=3),
'reference_time': pd.Timestamp('2020-02-05')})
print(ds)
print('-----------------------------------------------------')
'''
温度:
[[[ 8.24759022 16.60205765 24.94548299]
  [12.94900613 12.63262571 21.77521758]]

 [[14.40984812 11.28388157 26.38437766]
  [10.52786582 15.22821748 14.10640294]]]
降水
[[[3.49546986 2.74409066 0.35352397]
  [5.68390485 9.64621258 0.32173397]]

 [[7.71359293 1.69140942 2.5384702 ]
  [1.91140506 6.13283432 0.64106529]]]
<xarray.Dataset>
Dimensions:         (time: 3, x: 2, y: 2)
Coordinates:
    lon             (x, y) float64 -99.83 -99.32 -99.79 -99.23
    lat             (x, y) float64 42.25 42.21 42.63 42.59
  * time            (time) datetime64[ns] 2020-02-06 2020-02-07 2020-02-08
    reference_time  datetime64[ns] 2020-02-05
Dimensions without coordinates: x, y
Data variables:
    temperature     (x, y, time) float64 8.248 16.6 24.95 ... 10.53 15.23 14.11
    precipitation   (x, y, time) float64 3.495 2.744 0.3535 ... 6.133 0.6411
'''

# Dataset封装DataArray数据
data = np.random.rand(4,3)
locs = ['beijing', 'shanghai', 'guangzhou']
times = pd.date_range('2020-01-01', periods=4)
foo = xr.DataArray(data, coords=[times,locs], dims=['times','city'])
ds=xr.Dataset({'bar': foo})
print(ds)
print('-----------------------------------------------------')
'''
<xarray.Dataset>
Dimensions:  (city: 3, times: 4)
Coordinates:
  * times    (times) datetime64[ns] 2020-01-01 2020-01-02 2020-01-03 2020-01-04
  * city     (city) object 'beijing' 'shanghai' 'guangzhou'
Data variables:
    bar      (times, city) float64 0.5589 0.7528 0.2483 ... 0.5158 0.2416 0.3278
'''

# Dataset封装pandas数据
ds=xr.Dataset({'bar': foo.to_pandas()})
print(ds)
print('-----------------------------------------------------')
# 结果同上

# Dataset实现Phthon的映射接口
# 获取Dataset指定数据内容
temp = 15+8*np.random.randn(2,2,3) #温度
precip = 10*np.random.rand(2,2,3) #降水
lon = [[-99.83, -99.32], [-99.79, -99.23]] #经度
lat = [[42.25, 42.21], [42.63, 42.59]] #纬度
ds = xr.Dataset({'temperature': (['x', 'y', 'time'],  temp),
'precipitation': (['x', 'y', 'time'], precip)},
coords={'lon': (['x', 'y'], lon),
'lat': (['x', 'y'], lat),
'time': pd.date_range('2020-02-06', periods=3),
'reference_time': pd.Timestamp('2020-02-05')})
print('temperature' in ds)
print('temperature'+'*'*50)
print(ds['temperature']) # 等同于ds.temperature
print('data_vars'+'*'*50)
print(ds.data_vars)
print('coords'+'*'*50)
print(ds.coords)
print('-----------------------------------------------------')
'''
True
temperature**************************************************
<xarray.DataArray 'temperature' (x: 2, y: 2, time: 3)>
array([[[20.12808822, 18.62391595, 20.49644511],
        [17.83075942,  7.39596887, 13.61646135]],

       [[26.01945992,  8.66994198, 22.62196108],
        [18.0968054 , 14.09983089,  7.67714084]]])
Coordinates:
    lon             (x, y) float64 -99.83 -99.32 -99.79 -99.23
    lat             (x, y) float64 42.25 42.21 42.63 42.59
  * time            (time) datetime64[ns] 2020-02-06 2020-02-07 2020-02-08
    reference_time  datetime64[ns] 2020-02-05
Dimensions without coordinates: x, y
data_vars**************************************************
Data variables:
    temperature    (x, y, time) float64 20.13 18.62 20.5 ... 18.1 14.1 7.677
    precipitation  (x, y, time) float64 5.523 2.719 1.897 ... 8.429 4.273 7.381
coords**************************************************
Coordinates:
    lon             (x, y) float64 -99.83 -99.32 -99.79 -99.23
    lat             (x, y) float64 42.25 42.21 42.63 42.59
  * time            (time) datetime64[ns] 2020-02-06 2020-02-07 2020-02-08
    reference_time  datetime64[ns] 2020-02-05
'''

# 添加attrs
ds.attrs['title'] = 'example attribute'
print(ds)
print('-----------------------------------------------------')
'''
<xarray.Dataset>
Dimensions:         (time: 3, x: 2, y: 2)
Coordinates:
    lon             (x, y) float64 -99.83 -99.32 -99.79 -99.23
    lat             (x, y) float64 42.25 42.21 42.63 42.59
  * time            (time) datetime64[ns] 2020-02-06 2020-02-07 2020-02-08
    reference_time  datetime64[ns] 2020-02-05
Dimensions without coordinates: x, y
Data variables:
    temperature     (x, y, time) float64 10.52 21.29 4.924 ... 21.27 26.33 17.36
    precipitation   (x, y, time) float64 1.851 9.895 4.412 ... 2.925 5.978 5.497
Attributes:
    title:    example attribute
'''

# 修改dataset
ds['temperature'] = (('x','y','time'), temp)
ds['temperature_double'] = (('x', 'y', 'time'), temp * 2 )
ds['precipitation'] = (('x', 'y', 'time'), precip)
ds.coords['lat'] = (('x', 'y'), lat)
ds.coords['lon'] = (('x', 'y'), lon)
ds.coords['time'] = pd.date_range('2020-05-06', periods=3)
ds.coords['reference_time'] = pd.Timestamp('2015-05-05')
print(ds)
print('-----------------------------------------------------')
'''
<xarray.Dataset>
Dimensions:             (time: 3, x: 2, y: 2)
Coordinates:
    lon                 (x, y) float64 -99.83 -99.32 -99.79 -99.23
    lat                 (x, y) float64 42.25 42.21 42.63 42.59
  * time                (time) datetime64[ns] 2020-05-06 2020-05-07 2020-05-08
    reference_time      datetime64[ns] 2014-05-05
Dimensions without coordinates: x, y
Data variables:
    temperature         (x, y, time) float64 16.76 12.62 15.21 ... 14.42 7.738
    precipitation       (x, y, time) float64 2.503 9.768 1.295 ... 8.562 2.641
    temperature_double  (x, y, time) float64 33.52 25.25 30.43 ... 28.85 15.48
Attributes:
    title:    example attribute
'''

# 获取多个variables
print(ds[['temperature','temperature_double']])
print('-----------------------------------------------------')
'''
<xarray.Dataset>
Dimensions:             (time: 3, x: 2, y: 2)
Coordinates:
  * time                (time) datetime64[ns] 2020-05-06 2020-05-07 2020-05-08
    reference_time      datetime64[ns] 2015-05-05
    lat                 (x, y) float64 42.25 42.21 42.63 42.59
    lon                 (x, y) float64 -99.83 -99.32 -99.79 -99.23
Dimensions without coordinates: x, y
Data variables:
    temperature         (x, y, time) float64 10.87 10.91 16.63 ... 19.82 11.56
    temperature_double  (x, y, time) float64 21.73 21.83 33.26 ... 39.64 23.13
Attributes:
    title:    example attribute
'''

# 删除variables
print(ds.drop_vars('temperature'))
print('-----------------------------------------------------')
'''
<xarray.Dataset>
Dimensions:             (time: 3, x: 2, y: 2)
Coordinates:
    lon                 (x, y) float64 -99.83 -99.32 -99.79 -99.23
    lat                 (x, y) float64 42.25 42.21 42.63 42.59
  * time                (time) datetime64[ns] 2020-05-06 2020-05-07 2020-05-08
    reference_time      datetime64[ns] 2015-05-05
Dimensions without coordinates: x, y
Data variables:
    precipitation       (x, y, time) float64 2.393 0.4089 6.376 ... 3.977 0.3115
    temperature_double  (x, y, time) float64 19.81 45.21 21.19 ... 44.85 41.8
Attributes:
    title:    example attribute
'''

#删除dims
print(ds.drop_dims('time'))
print('-----------------------------------------------------')
'''
<xarray.Dataset>
Dimensions:         (x: 2, y: 2)
Coordinates:
    lon             (x, y) float64 -99.83 -99.32 -99.79 -99.23
    lat             (x, y) float64 42.25 42.21 42.63 42.59
    reference_time  datetime64[ns] 2015-05-05
Dimensions without coordinates: x, y
Data variables:
    *empty*
Attributes:
    title:    example attribute
'''

# 根据已有变量生成新变量
print(ds.assign(temperature2 = 2 * ds.temperature))
print('-----------------------------------------------------')
'''
<xarray.Dataset>
Dimensions:             (time: 3, x: 2, y: 2)
Coordinates:
    lon                 (x, y) float64 -99.83 -99.32 -99.79 -99.23
    lat                 (x, y) float64 42.25 42.21 42.63 42.59
  * time                (time) datetime64[ns] 2020-05-06 2020-05-07 2020-05-08
    reference_time      datetime64[ns] 2015-05-05
Dimensions without coordinates: x, y
Data variables:
    temperature         (x, y, time) float64 20.04 14.95 6.867 ... 10.67 28.37
    precipitation       (x, y, time) float64 8.867 5.471 7.526 ... 1.067 6.337
    temperature_double  (x, y, time) float64 40.08 29.9 13.73 ... 21.34 56.74
    temperature2        (x, y, time) float64 40.08 29.9 13.73 ... 21.34 56.74
Attributes:
    title:    example attribute
'''

#变量重命名
print(ds.rename({'temperature': 'temp', 'precipitation': 'precip'}))
print('-----------------------------------------------------')
'''
<xarray.Dataset>
Dimensions:             (time: 3, x: 2, y: 2)
Coordinates:
    lon                 (x, y) float64 -99.83 -99.32 -99.79 -99.23
    lat                 (x, y) float64 42.25 42.21 42.63 42.59
  * time                (time) datetime64[ns] 2020-05-06 2020-05-07 2020-05-08
    reference_time      datetime64[ns] 2015-05-05
Dimensions without coordinates: x, y
Data variables:
    temp                (x, y, time) float64 22.92 5.283 22.03 ... 19.75 -5.534
    precip              (x, y, time) float64 6.067 5.609 6.942 ... 4.708 4.717
    temperature_double  (x, y, time) float64 45.83 10.57 44.07 ... 39.5 -11.07
Attributes:
    title:    example attribute
'''

ds.coords['day'] = ('time', [6, 7, 8])
print(ds.swap_dims({'time': 'day'})) # 将维度坐标从time切换到自定义的非维度坐标day
print('-----------------------------------------------------')
'''
<xarray.Dataset>
Dimensions:             (day: 3, x: 2, y: 2)
Coordinates:
    lon                 (x, y) float64 -99.83 -99.32 -99.79 -99.23
    lat                 (x, y) float64 42.25 42.21 42.63 42.59
    time                (day) datetime64[ns] 2020-05-06 2020-05-07 2020-05-08
    reference_time      datetime64[ns] 2015-05-05
  * day                 (day) int32 6 7 8
Dimensions without coordinates: x, y
Data variables:
    temperature         (x, y, day) float64 21.82 8.389 18.3 ... 7.322 13.11
    precipitation       (x, y, day) float64 4.517 9.47 7.255 ... 3.973 4.279
    temperature_double  (x, y, day) float64 43.63 16.78 36.6 ... 14.64 26.21
Attributes:
    title:    example attribute
'''

#将坐标转换为变量
print(ds.reset_coords())
print('-----------------------------------------------------')
'''
<xarray.Dataset>
Dimensions:             (time: 3, x: 2, y: 2)
Coordinates:
#由于time参与了
{'temperature': (['x', 'y', 'time'],  temp),
'precipitation': (['x', 'y', 'time'], precip)}
数据构建，所以time坐标不会被转换成变量，否则就不能支撑坐标了
  * time                (time) datetime64[ns] 2020-05-06 2020-05-07 2020-05-08
Dimensions without coordinates: x, y
Data variables:
    temperature         (x, y, time) float64 16.37 -8.224 4.644 ... 20.7 -11.01
    precipitation       (x, y, time) float64 1.631 1.102 7.86 ... 4.002 0.01919
    lon                 (x, y) float64 -99.83 -99.32 -99.79 -99.23
    lat                 (x, y) float64 42.25 42.21 42.63 42.59
    reference_time      datetime64[ns] 2015-05-05
    temperature_double  (x, y, time) float64 32.73 -16.45 9.289 ... 41.4 -22.02
    day                 (time) int32 6 7 8
Attributes:
    title:    example attribute
'''

#指定变量转坐标
print(ds.set_coords(['temperature','precipitation']))
print('-----------------------------------------------------')
'''
<xarray.Dataset>
Dimensions:             (time: 3, x: 2, y: 2)
Coordinates:
#与temperature和precipitation相关的变量也被自动转换为坐标
    temperature         (x, y, time) float64 23.81 20.76 15.88 ... 11.95 11.83
    precipitation       (x, y, time) float64 3.743 4.88 1.779 ... 5.481 6.479
    lon                 (x, y) float64 -99.83 -99.32 -99.79 -99.23
    lat                 (x, y) float64 42.25 42.21 42.63 42.59
  * time                (time) datetime64[ns] 2020-05-06 2020-05-07 2020-05-08
    reference_time      datetime64[ns] 2015-05-05
    day                 (time) int32 6 7 8
Dimensions without coordinates: x, y
Data variables:
    temperature_double  (x, y, time) float64 47.63 41.52 31.77 ... 23.9 23.66
Attributes:
    title:    example attribute
'''

#将坐标转换为dataset
ds1=ds.coords.to_dataset()
print(ds1)
print('-----------------------------------------------------')
'''
<xarray.Dataset>
Dimensions:         (time: 3, x: 2, y: 2)
Coordinates:
    day             (time) int32 6 7 8
    reference_time  datetime64[ns] 2015-05-05
  * time            (time) datetime64[ns] 2020-05-06 2020-05-07 2020-05-08
    lon             (x, y) float64 -99.83 -99.32 -99.79 -99.23
    lat             (x, y) float64 42.25 42.21 42.63 42.59
Dimensions without coordinates: x, y
Data variables:
    *empty*
Attributes:
    title:    example attribute
'''

#合并坐标
alt = xr.Dataset(coords={'z': [10,9,8], 'lat': 0, 'lon': 0})
print(ds.coords.merge(alt.coords))
print('-----------------------------------------------------')
'''
Dimensions:         (time: 3, z: 3)
Coordinates:
  * time            (time) datetime64[ns] 2020-05-06 2020-05-07 2020-05-08
    reference_time  datetime64[ns] 2015-05-05
    day             (time) int32 6 7 8
  * z               (z) int32 10 9 8
Data variables:
    *empty*
'''

#将指定的维度坐标或非维度坐标或DataArray转换为pandas.Index
print(ds['day'].to_index())
print('-----------------------------------------------------')
'''
DatetimeIndex(['2020-05-06', '2020-05-07', '2020-05-08'], dtype='datetime64[ns]', name='time', freq='D')
'''

#将所有的维度坐标转换为pandas.Index
print(ds.indexes)
print('-----------------------------------------------------')
'''
time: DatetimeIndex(['2020-05-06', '2020-05-07', '2020-05-08'], dtype='datetime64[ns]', name='time', freq='D')
'''

#使用pandas.MultiIndex标记坐标值
midx = pd.MultiIndex.from_arrays([['R', 'R', 'V', 'V'], [0.1, 0.2, 0.7, 0.9]],names=('band', 'wn'))
mda = xr.DataArray(np.random.rand(4), coords={'spec': midx}, dims='spec')
print(mda)
print('-----------------------------------------------------')
'''
<xarray.DataArray (spec: 4)>
array([0.0669567 , 0.25446109, 0.39444313, 0.41830347])
Coordinates:
  * spec     (spec) MultiIndex
  # "-" 代表spec的虚拟或派生坐标
  - band     (spec) object 'R' 'R' 'V' 'V'
  - wn       (spec) float64 0.1 0.2 0.7 0.9
'''

# 检索虚拟派生坐标
print(mda['band']) # 等同于mda.band
print('-----------------------------------------------------')