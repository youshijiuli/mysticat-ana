#%%
from pyecharts.charts import Bar
from pyecharts.faker import Faker

bar = Bar()
bar.add_xaxis(Faker.choose())
bar.add_yaxis("",Faker.values())
bar.render_notebook()
# %%
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts import options as opts

bar = Bar()
bar.add_xaxis(Faker.choose())
bar.add_yaxis("",Faker.values())
bar.set_global_opts(title_opts=opts.TitleOpts(title="1级标题",subtitle='2级标题',title_link='http://www.itbaizhan.cn/'))
bar.render_notebook()
# bar.render()
# %%
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts import options as opts

bar = Bar()
bar.add_xaxis(Faker.choose())
bar.add_yaxis("",Faker.values())
bar.set_global_opts(title_opts=opts.TitleOpts(title="1级标题",subtitle='2级标题',title_link='http://www.itbaizhan.cn/'))
bar.set_global_opts(xaxis_opts=opts.AxisOpts(is_show=True,min_=-1,max_=7))
bar.set_global_opts(yaxis_opts=opts.AxisOpts(max_=50))
bar.render_notebook()
