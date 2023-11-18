#%%
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.globals import ThemeType

bar = Bar(init_opts=opts.InitOpts(theme = ThemeType.DARK))
bar.add_xaxis(Faker.choose())
bar.add_yaxis('',Faker.values())
bar.render_notebook()
# %%
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.globals import ThemeType

bar = Bar()
bar.add_xaxis(Faker.choose())
bar.add_yaxis('',Faker.values())
bar.set_series_opts(itemstyle_opts=opts.ItemStyleOpts(color='#99ccff'))
bar.render_notebook()
# %%
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.globals import ThemeType

bar = Bar()
bar.add_xaxis(Faker.choose())
bar.add_yaxis('',Faker.values())
bar.set_series_opts(itemstyle_opts=opts.ItemStyleOpts(color='#99ccff'))
bar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
bar.render_notebook()
# %%
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.globals import ThemeType

bar = Bar()
bar.add_xaxis(Faker.choose())
bar.add_yaxis('',Faker.values())
bar.set_series_opts(markpoint_opts=opts.MarkPointOpts(
    data=[
        opts.MarkPointItem(type_='max',name='最大值'),
        opts.MarkPointItem(type_='min',name='最小值'),
        opts.MarkPointItem(type_='average',name='平均值'),
    ]
))
bar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
bar.render_notebook()
# %%
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.globals import ThemeType

bar = Bar()
bar.add_xaxis(Faker.choose())
bar.add_yaxis('',Faker.values())
bar.set_series_opts(
    markline_opts=opts.MarkLineOpts(
        data=[
            # opts.MarkLineItem(type_='min',name='最小值'),
            # opts.MarkLineItem(type_='max',name='最大值'),
            opts.MarkLineItem(type_='average',name='平均值'),
        ]
    )
)
bar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
bar.render_notebook()
# %%
