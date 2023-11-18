#%%
from pyecharts.charts import EffectScatter
from pyecharts import options as opts
from pyecharts.faker import Faker

sca = EffectScatter()
sca.add_xaxis(Faker.choose())
sca.add_yaxis('',Faker.values())
sca.set_global_opts(title_opts=opts.TitleOpts(title='涟漪散点图'))
sca.render_notebook()
# %%
from pyecharts.charts import EffectScatter
from pyecharts import options as opts
from pyecharts.faker import Faker
from pyecharts.globals import SymbolType

sca = EffectScatter()
sca.add_xaxis(Faker.choose())
sca.add_yaxis('',Faker.values(),symbol=SymbolType.DIAMOND)
sca.set_global_opts(title_opts=opts.TitleOpts(title='涟漪散点图'))
sca.render_notebook()
# %%
