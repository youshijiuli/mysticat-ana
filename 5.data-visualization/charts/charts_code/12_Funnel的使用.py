#%%
from pyecharts.charts import Funnel
from pyecharts.faker import Faker
from pyecharts import options as opts

funnel = Funnel()
funnel.add('',[list(z) for z in zip(Faker.choose(),Faker.values())])
funnel.set_global_opts(title_opts=opts.TitleOpts(title='漏斗图'))
funnel.render_notebook()
# %%
from pyecharts.charts import Funnel
from pyecharts.faker import Faker
from pyecharts import options as opts

funnel = Funnel()
funnel.add('',[list(z) for z in zip(Faker.choose(),Faker.values())],
sort_='ascending',
label_opts=opts.LabelOpts(position='inside'))
funnel.set_global_opts(title_opts=opts.TitleOpts(title='漏斗图'))
funnel.render_notebook()
# %%
