#%%
from pyecharts.charts import Boxplot
from pyecharts import options as opts
from random import randint

box = Boxplot()
box.add_xaxis([f'{i}月' for i in range(1,5)])
box.add_yaxis('A',box.prepare_data([
    [randint(50,80) for i in range(50)],
    [randint(70,100) for i in range(50)],
    [randint(50,90) for i in range(50)],
    [randint(50,120) for i in range(50)],
    ]))
box.set_global_opts(title_opts=opts.TitleOpts(title='箱图的基本案例'))
box.render_notebook()
#%%
from pyecharts.charts import Boxplot
from pyecharts import options as opts
from random import randint

box = Boxplot()
box.add_xaxis([f'{i}月' for i in range(1,5)])
box.add_yaxis('A',box.prepare_data([
    [randint(50,80) for i in range(50)],
    [randint(70,100) for i in range(50)],
    [randint(50,90) for i in range(50)],
    [randint(50,120) for i in range(50)],
    ]))
box.add_yaxis('B',box.prepare_data([
    [randint(50,80) for i in range(50)],
    [randint(70,100) for i in range(50)],
    [randint(50,90) for i in range(50)],
    [randint(50,120) for i in range(50)],
]))
box.set_global_opts(title_opts=opts.TitleOpts(title='多组箱图的基本案例'))
box.render_notebook()
# %%
