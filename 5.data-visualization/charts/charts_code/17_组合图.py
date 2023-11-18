#%%
from pyecharts.charts import Bar,Line
from pyecharts import options as opts

x = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
bar =Bar()
bar.add_xaxis(x)
bar.add_yaxis('蒸发量',
[2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],
label_opts=opts.LabelOpts(is_show=False))
bar.add_yaxis('降水量',
[2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3],
label_opts=opts.LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=opts.TitleOpts('混合图'),
    tooltip_opts=opts.TooltipOpts(is_show=True,trigger='axis',axis_pointer_type='cross'),
    xaxis_opts= opts.AxisOpts(type_='category',axispointer_opts=opts.AxisPointerOpts(is_show=True,type_='shadow'))
    )

bar.extend_axis(yaxis=opts.AxisOpts(
    name='温度',min_=0,max_= 25,
    interval = 5,
    axislabel_opts = opts.LabelOpts(formatter='{value} °C')
))

line = Line()
line.add_xaxis(x)
line.add_yaxis('平均温度',
[2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2],
yaxis_index=1,
label_opts=opts.LabelOpts(is_show=False)
)

bar.overlap(line) # 合并图
bar.render_notebook()

# %%
