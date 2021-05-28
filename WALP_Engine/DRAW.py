from pyecharts import options as opts
from pyecharts.charts import Gauge, Page
#from pyecharts.faker import Collector

from snapshot_pyppeteer import snapshot
from pyecharts.render import make_snapshot

from pyecharts.charts import Bar
#from pyecharts.faker import Faker
from pyecharts import options as opts

from ping3 import ping

from PIL import Image

#from Main_start import delay


def gauge_base() -> Gauge:
    c = (
        Gauge(
            init_opts=opts.InitOpts(
                bg_color={
                    #"type":"gauge",
                    "bg_color":'black',
                    #"repeat":"no-repeat",
                }
            )
        )
        .add("", [("",delay)], max_=460,  detail_label_opts = opts.GaugeDetailOpts( offset_center = [0, "-40%"]), radius="50%", title_label_opts=opts.LabelOpts(font_size=20, color="white", font_family="Microsoft YaHei"), axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color=[(0.3, "#67e0e3"), (0.7, "#37a2da"), (1, "#fd666d")], width=10)))
        .set_global_opts(title_opts=opts.TitleOpts(title=""))
    )
    make_snapshot(snapshot, c.render(), "./cache_pic/Ping.png")

    img = Image.open('./cache_pic/Ping.png')
    area = (600, 200, 1200, 700)#width在前，height在后
    cropped_img = img.crop(area)
    #cropped_img.show()
    cropped_img.save('./cache_pic/Ping.png')



#if __name__ == "__main__":
ip_address = 'www.baidu.com'
response = ping(ip_address)
if response == False:
    print('取消任务-无网络')
else:
    delay = int(response * 1000)
    if delay > 460:
        delay = 460
#delay = str(delay + 'ms')
gauge_base()
