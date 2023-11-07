import pandas as pd

'''
编号  参数                        描述
1     display.max_rows            要显示的最大行数
2     display.max_columns         要显示的最大列数
3     display.expand_frame_repr   显示数据帧以拉伸页面
4     display.max_colwidth        显示最大列宽
5     display.precision           显示十进制数的精度
'''

#解释器读取此值并显示此值作为显示上限的行
print("display.max_rows = ",pd.get_option("display.max_rows"))
print('-----------------------------------------------------')
'''
display.max_rows = 60 #默认值
'''

#解释器读取此值并显示此值作为显示上限的列
print("display.max_columns = ", pd.get_option("display.max_columns"))
print('-----------------------------------------------------')
'''
display.max_columns = 0 #默认值
'''

#使用set_option()，可以更改要显示的默认行数
pd.set_option("display.max_rows",80)
print("after set display.max_rows = ",pd.get_option("display.max_rows"))
print('-----------------------------------------------------')
'''
after set display.max_rows =  80
'''

pd.set_option("display.max_columns",32)
print("after set display.max_columns = ",pd.get_option("display.max_columns"))
print('-----------------------------------------------------')
'''
after set display.max_columns =  32
'''

#使用reset_option()，可以将该值更改回显示的默认行数
pd.reset_option("display.max_columns")
print("reset display.max_columns = ",pd.get_option("display.max_columns"))
print('-----------------------------------------------------')
'''
reset display.max_columns =  0
'''

#describe_option打印参数的描述
pd.describe_option("display.max_rows")
print('-----------------------------------------------------')
'''
display.max_rows : int
    If max_rows is exceeded, switch to truncate view. Depending on
    `large_repr`, objects are either centrally truncated or printed as
    a summary view. 'None' value means unlimited.

    In case python/IPython is running in a terminal and `large_repr`
    equals 'truncate' this can be set to 0 and pandas will auto-detect
    the height of the terminal and print a truncated object which fits
    the screen height. The IPython notebook, IPython qtconsole, or
    IDLE do not run in a terminal and hence it is not possible to do
    correct auto-detection.
    [default: 60] [currently: 80]
'''

#option_context上下文管理器用于临时设置语句中的选项。当退出使用块时，选项值将自动恢复
with pd.option_context("display.max_rows",10):
   print(pd.get_option("display.max_rows"))
print(pd.get_option("display.max_rows"))
'''
10
80
'''
