#%%
from os import name
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts import options as  opts 

bar = Bar()
bar.add_xaxis(Faker.choose())
bar.add_yaxis('商家A',Faker.values())
bar.add_yaxis('商家B',Faker.values())
bar.render_notebook()
# %%
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts import options as  opts 

bar = Bar()
bar.add_xaxis(Faker.choose())
bar.add_yaxis('销售团队A',Faker.values())
bar.add_yaxis('销售团队B',Faker.values())
bar.set_series_opts(markline_opts=opts.MarkLineOpts(
    data=[opts.MarkLineItem(y=80,name='合格指标')]
))
bar.render_notebook()
# %%
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts import options as  opts 

bar = Bar()
bar.add_xaxis(Faker.choose())
bar.add_yaxis('销售团队A',Faker.values())
bar.add_yaxis('销售团队B',Faker.values())
bar.set_series_opts(markline_opts=opts.MarkLineOpts(
    data=[opts.MarkLineItem(type_='max',name='最大值')]
))
bar.render_notebook()
# %%
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts import options as  opts 

bar = Bar()
bar.add_xaxis(Faker.choose())
bar.add_yaxis('频率',Faker.values(),category_gap=0,color=Faker.rand_color())
bar.set_global_opts(title_opts=opts.TitleOpts(title="直方图"))
bar.render_notebook()
# %%
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts import options as  opts 

bar = Bar()
bar.add_xaxis(Faker.choose())
bar.add_yaxis('销售团队A',Faker.values())
bar.add_yaxis('销售团队B',Faker.values())
bar.reversal_axis()
bar.set_series_opts(label_opts=opts.LabelOpts(position="right"))
bar.set_global_opts(title_opts=opts.TitleOpts(title="XY翻转"))
bar.render_notebook()
# %%
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts import options as  opts 

bar = Bar()
bar.add_xaxis(Faker.choose())
bar.add_yaxis('销售团队A',Faker.values(),stack='stack')
bar.add_yaxis('销售团队B',Faker.values(),stack='stack')
bar.set_global_opts(title_opts=opts.TitleOpts(title="堆叠图"))
bar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
bar.render_notebook()
# %%
