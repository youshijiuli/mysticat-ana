#%%
from pyecharts.charts import Bar,Timeline
from pyecharts import options as opts
from pyecharts.faker import Faker

x = Faker.choose()
tl = Timeline() 
for i in range(2000,2006):
    bar = Bar()
    bar.add_xaxis(x)
    bar.add_yaxis('A',Faker.values())
    bar.add_yaxis('B',Faker.values())
    bar.set_global_opts(title_opts=opts.TitleOpts(f'{i}年的数据表'))
    tl.add(bar,f'{i}年')
tl.render_notebook()
# %%
