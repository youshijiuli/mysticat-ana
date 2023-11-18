#%%
from pyecharts.charts import Pie
from pyecharts import options as opts
from pyecharts.faker import Faker

pie = Pie()
pie.add('',[list(z) for z in zip(Faker.choose(),Faker.values())])
pie.set_global_opts(title_opts=opts.TitleOpts(title="Pie的基本图表"))
pie.render_notebook()
# %%
from pyecharts.charts import Pie
from pyecharts import options as opts
from pyecharts.faker import Faker

pie = Pie()
pie.add('',[list(z) for z in zip(Faker.choose(),Faker.values())])
pie.set_global_opts(title_opts=opts.TitleOpts(title="Pie的基本图表"))
pie.set_colors(['blue','green','#cc3333','red','orange','purple','#339966'])
pie.render_notebook()
# %%
from pyecharts.charts import Pie
from pyecharts import options as opts
from pyecharts.faker import Faker

pie = Pie()
pie.add('',[list(z) for z in zip(Faker.choose(),Faker.values())])
pie.set_global_opts(title_opts=opts.TitleOpts(title="Pie的基本图表"))
pie.set_colors(['blue','green','#cc3333','red','orange','purple','#339966'])
pie.render_notebook()

#%%
from pyecharts.charts import Pie
from pyecharts import options as opts
from pyecharts.faker import Faker

pie = Pie()
pie.add('',[list(z) for z in zip(Faker.choose(),Faker.values())],radius=['50%','70%'])
pie.set_global_opts(title_opts=opts.TitleOpts(title="Pie的基本图表"))
pie.render_notebook()
# %%

pie = Pie()
pie.add('',[list(z) for z in zip(Faker.choose(),Faker.values())],rosetype='radius')
pie.set_global_opts(title_opts=opts.TitleOpts(title="Pie的基本图表"))
pie.render_notebook()
# %%

pie = Pie()
pie.add('',[list(z) for z in zip(Faker.choose(),Faker.values())])
pie.set_global_opts(title_opts=opts.TitleOpts(title="Pie的基本图表"))
pie.set_series_opts(label_opts=opts.LabelOpts(formatter='{b}:{d}'))
pie.render_notebook()
# %%
