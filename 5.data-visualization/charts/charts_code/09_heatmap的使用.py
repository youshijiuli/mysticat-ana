#%%
from pyecharts.charts import HeatMap
from pyecharts import options as opts
from pyecharts.faker import Faker
from random import randint

from pyecharts.types import VisualMap
value = [[i,j, randint(0,40)] for i in range(24) for j in range(7)]

hm = HeatMap()
hm.add_xaxis(Faker.clock)
hm.add_yaxis('',Faker.week,value)
hm.set_global_opts(title_opts=opts.TitleOpts(title='热力图'),
visualmap_opts= opts.VisualMapOpts()
)
hm.render_notebook()
# %%
from pyecharts.charts import HeatMap
from pyecharts import options as opts
from pyecharts.faker import Faker
from random import randint

from pyecharts.types import VisualMap
value = [[i,j, randint(0,40)] for i in range(24) for j in range(7)]

hm = HeatMap()
hm.add_xaxis(Faker.clock)
hm.add_yaxis('',Faker.week,value,label_opts=opts.LabelOpts(is_show=True,position='inside'))
hm.set_global_opts(title_opts=opts.TitleOpts(title='热力图'),
visualmap_opts= opts.VisualMapOpts()
)
hm.render_notebook()
# %%
