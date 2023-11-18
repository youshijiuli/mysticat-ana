#%% 
from pyecharts.charts import Line
from pyecharts import options as opts
from pyecharts.faker import Faker

line = Line()

line.add_xaxis(xaxis_data=Faker.choose())
line.add_yaxis('商家A',y_axis=Faker.values())
line.add_yaxis('商家B',y_axis=Faker.values())

line.set_global_opts(xaxis_opts=opts.AxisOpts(splitline_opts = opts.SplitLineOpts(is_show=True)))
line.render_notebook()
# %%
from pyecharts.charts import Line
from pyecharts import options as opts
from pyecharts.faker import Faker

line = Line()

line.add_xaxis(xaxis_data=Faker.choose())
line.add_yaxis('商家A',y_axis=Faker.values(),is_smooth = True)
line.add_yaxis('商家B',y_axis=Faker.values(),is_smooth = True)

line.set_global_opts(xaxis_opts=opts.AxisOpts(splitline_opts = opts.SplitLineOpts(is_show=True)))
line.render_notebook()
# %%
from pyecharts.charts import Line
from pyecharts import options as opts
from pyecharts.faker import Faker

line = Line()
x_values = Faker.choose()
y_values = Faker.values()
line.add_xaxis(xaxis_data=x_values)
line.add_yaxis('商家A',y_axis=y_values,is_smooth = True,markpoint_opts = opts.MarkPointOpts(
    data = [opts.MarkPointItem(name='自定义',coord = [x_values[2],y_values[2]],value=y_values[2])]
))
line.set_global_opts(xaxis_opts=opts.AxisOpts(splitline_opts = opts.SplitLineOpts(is_show=True)))

line.render_notebook()
# %%
from pyecharts.charts import Line
from pyecharts import options as opts
from pyecharts.faker import Faker

line = Line()
x_values = Faker.choose()
line.add_xaxis(x_values)
line.add_yaxis(
    series_name=x_values[0],
    y_axis=Faker.values(),
    stack="总量",
    label_opts= opts.LabelOpts(is_show=False)
    )

line.add_yaxis(
    series_name=x_values[1],
    y_axis=Faker.values(),
    stack="总量")


line.add_yaxis(
    series_name=x_values[2],
    y_axis=Faker.values(),
    stack="总量")
line.render_notebook()
# %%
from pyecharts.charts import Line
from pyecharts import options as opts
from pyecharts.faker import Faker

line = Line()
x_values = Faker.choose()
line.add_xaxis(x_values)
line.add_yaxis(
    series_name=x_values[0],
    y_axis=Faker.values(),
    stack="总量",
    label_opts= opts.LabelOpts(is_show=False),
    areastyle_opts = opts.AreaStyleOpts(opacity=0.5)
    )
line.add_yaxis(
    series_name=x_values[1],
    y_axis=Faker.values(),
    stack="总量",
    label_opts= opts.LabelOpts(is_show=False),
    areastyle_opts = opts.AreaStyleOpts(opacity=0.5))
line.add_yaxis(
    series_name=x_values[2],
    y_axis=Faker.values(),
    stack="总量",
    label_opts= opts.LabelOpts(is_show=False),
    areastyle_opts = opts.AreaStyleOpts(opacity=0.5))
line.add_yaxis(
series_name=x_values[3],
y_axis=Faker.values(),
stack="总量",
    label_opts= opts.LabelOpts(is_show=False),
    areastyle_opts = opts.AreaStyleOpts(opacity=0.5))
line.add_yaxis(
    series_name=x_values[4],
    y_axis=Faker.values(),
    stack="总量",
    label_opts= opts.LabelOpts(is_show=False),
    areastyle_opts = opts.AreaStyleOpts(opacity=0.5))
line.set_global_opts(xaxis_opts=opts.AxisOpts(boundary_gap=False))
line.render_notebook()
# %%
