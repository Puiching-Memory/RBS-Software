from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.commons.utils import JsCode

from snapshot_pyppeteer import snapshot
from pyecharts.render import make_snapshot

from API import humidity3, rain3, humidity2, rain2, humidity1, rain1

from PIL import Image

print(humidity3, rain3, humidity2, rain2, humidity1, rain1)

fn = """
    function(params) {
        if(params.name == 'NONE')
            return '\\n\\n\\n' + params.name + ' : ' + params.value + '%';
        return params.name + ' : ' + params.value + '%';
    }
    """

area_color_js = (
    "new echarts.graphic.LinearGradient(0, 0, 0, 1, "
    "[{offset: 0, color: '#eb64fb'}, {offset: 1, color: '#55FFDD'}], false)"
)

def new_label_opts():
    return opts.LabelOpts(formatter=JsCode(fn), position="center")


c = (
    Pie(init_opts=opts.InitOpts(bg_color="black"))
    .set_colors(['white', JsCode(area_color_js)])
    .add(
        "",
        [list(z) for z in zip(["空气湿度", "NONE"], [float(humidity3), 100 - float(humidity3)])],
        center=["10%", "30%"],
        radius=[65, 80],
        label_opts=new_label_opts(),
    )
    .add(
        "",
        [list(z) for z in zip(["空气湿度", "NONE"], [float(humidity2), 100 - float(humidity2)])],
        center=["30%", "30%"],
        radius=[65, 80],
        label_opts=new_label_opts(),
        #color = 'white'
    )
    .add(
        "",
        [list(z) for z in zip(["空气湿度", "NONE"], [float(humidity1), 100 - float(humidity1)])],
        center=["50%", "30%"],
        radius=[65, 80],
        label_opts=new_label_opts(),
    )
    .add(
        "",
        [list(z) for z in zip(["降雨概率", "NONE"], [float(rain1), 100 - float(rain1)])],
        center=["10%", "70%"],
        radius=[65, 80],
        label_opts=new_label_opts(),
    )
    .add(
        "",
        [list(z) for z in zip(["降雨概率", "NONE"], [float(rain2), 100 - float(rain2)])],
        center=["30%", "70%"],
        radius=[65, 80],
        label_opts=new_label_opts(),
    )
    .add(
        "",
        [list(z) for z in zip(["降雨概率", "NONE"], [float(rain3), 100 - float(rain3)])],
        center=["50%", "70%"],
        radius=[65, 80],
        label_opts=new_label_opts(),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title_textstyle_opts=opts.TextStyleOpts(color="#fff"), title=""),
        legend_opts=opts.LegendOpts(
            type_="scroll", pos_top="20%", pos_left="80%", orient="vertical"
        ),
    )
    #.render("mutiple_pie.html")
    #.set_series_opts(label_opts=opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),)
)
make_snapshot(snapshot, c.render(), "./cache_pic/More_weater.png")

img = Image.open('./cache_pic/More_weater.png')
area = (0, 100, 1200, 900)#width在前，height在后
cropped_img = img.crop(area)
#cropped_img.show()
cropped_img.save('./cache_pic/More_weater.png')
