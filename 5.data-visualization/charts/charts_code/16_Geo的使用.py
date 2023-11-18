#%%
from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.faker import Faker
from pyecharts.globals import GeoType
from pyecharts.types import VisualMap

geo = Geo()
geo.add_schema()
geo.add('',
[list(z) for z in zip(Faker.provinces,Faker.values())],
label_opts=opts.LabelOpts(is_show=False),
type_=GeoType.EFFECT_SCATTER
)
geo.set_global_opts(
    title_opts=opts.TitleOpts('坐标地图'),
    visualmap_opts= opts.VisualMapOpts()
)
geo.render_notebook()
# %%
from pyecharts.globals import GeoType,SymbolType
from pyecharts.types import VisualMap


geo = Geo()
geo.add_schema()
geo.add('',
[['北京','上海'],['北京','深圳'],['西藏','贵州']],
type_=GeoType.LINES,
label_opts=opts.LabelOpts(is_show=False),
effect_opts = opts.EffectOpts(symbol=SymbolType.ARROW,symbol_size=8,color='red'),
linestyle_opts = opts.LineStyleOpts(curve=0.3),
color='blue'
)

geo.set_global_opts(
    title_opts=opts.TitleOpts('坐标地图'),
    visualmap_opts= opts.VisualMapOpts()
)
geo.render_notebook()

# %%
