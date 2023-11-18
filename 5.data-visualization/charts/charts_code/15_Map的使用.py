#%%
from pyecharts.charts import Map
from pyecharts import options as opts

map = Map()
map.add('',[['河北',10],['四川',20]],is_map_symbol_show=False)
map.set_global_opts(
    title_opts=opts.TitleOpts('地图'),
    visualmap_opts=opts.VisualMapOpts()
)
map.render_notebook()
#%%
from pyecharts.charts import Map
from pyecharts import options as opts

map = Map()
map.add('',
[['河北',10],['四川',20]],
maptype='河北',
is_map_symbol_show=False,
label_opts=opts.LabelOpts(is_show=False))
map.set_global_opts(
    title_opts=opts.TitleOpts('地图'),
    visualmap_opts=opts.VisualMapOpts()
)
map.render_notebook()
# %%
