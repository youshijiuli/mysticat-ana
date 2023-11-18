#%%
from pyecharts.charts import Radar
from pyecharts import options as opts

radar = Radar()

data1 = [[8,7,8,8,9,7]]
data2 = [[9,5,7,8,6,7]]

radar.add_schema(
    schema=[
        opts.RadarIndicatorItem(name='拍照',max_=10),
        opts.RadarIndicatorItem(name='外观',max_=10),
        opts.RadarIndicatorItem(name='性能',max_=10),
        opts.RadarIndicatorItem(name='屏幕',max_=10),
        opts.RadarIndicatorItem(name='内存',max_=10),
        opts.RadarIndicatorItem(name='系统',max_=10)]
)
radar.add('OPPO',data1)
radar.add('华为',data2)
radar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
radar.set_global_opts(title_opts=opts.TitleOpts('雷达图'))
radar.render_notebook()
# %%
