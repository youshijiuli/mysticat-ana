#%%
# pip install pyecharts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType

bar = Bar()
bar.add_xaxis(['华为','小米','Apple','OPPO','锤子'])
bar.add_yaxis('销售量',[100,70,86,77,50])

# bar.render('render22.html')
bar.render_notebook()
# %%
from pyecharts.charts import Bar

bar =(
    Bar()
.add_xaxis(['华为','小米','Apple','OPPO','锤子'])
.add_yaxis('销售量',[111,70,86,77,50])
)
bar.render_notebook()

# %%
from pyecharts.charts import Bar

bar =Bar().add_xaxis(['华为','小米','Apple','OPPO','锤子']).add_yaxis('销售量',[111,70,86,77,50])

bar.render_notebook()
# %%
from pyecharts.charts import Bar
from pyecharts import options as opts
bar =(
    Bar()
.add_xaxis(['华为','小米','Apple','OPPO','锤子'])
.add_yaxis('销售量',[111,70,86,77,50])
.set_global_opts(title_opts=opts.TitleOpts(title="这是我们的标题",subtitle='2级标题'))
)
bar.render_notebook()
# %%
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType
bar =(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.ROMA))
.add_xaxis(['华为','小米','Apple','OPPO','锤子'])
.add_yaxis('销售量',[111,70,86,77,50])
.set_global_opts(title_opts=opts.TitleOpts(title="这是我们的标题",subtitle='2级标题'))
)
bar.render_notebook()
# %%
