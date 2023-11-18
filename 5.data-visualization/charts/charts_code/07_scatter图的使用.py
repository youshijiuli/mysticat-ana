#%%
from pyecharts.charts import Scatter
from pyecharts import options as opts
from random import random,randint

x = [randint(0,100) for i in range(100)]
y = [randint(0,100) for i in range(100)]

sca = Scatter()
sca.add_xaxis(xaxis_data=x)
sca.add_yaxis('',y_axis=y,label_opts=opts.LabelOpts(is_show=False),symbol_size=10,symbol='rect')
sca.set_global_opts(xaxis_opts=opts.AxisOpts(type_='value'))
sca.render_notebook()

# %%
from pyecharts.charts import Scatter
from pyecharts import options as opts
from random import random,randint

x = [randint(0,100) for i in range(10)]
y = [randint(0,100) for i in range(10)]

sca = Scatter()
sca.add_xaxis(xaxis_data=x)
sca.add_yaxis('',y_axis=y,label_opts=opts.LabelOpts(is_show=True))
sca.set_global_opts(xaxis_opts=opts.AxisOpts(type_='value')
,visualmap_opts=opts.VisualMapOpts(type_='size'))
sca.render_notebook()
# %%
