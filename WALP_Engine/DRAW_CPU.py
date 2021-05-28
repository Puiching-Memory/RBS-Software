from pyecharts import options as opts
from pyecharts.charts import Gauge, Page


from snapshot_pyppeteer import snapshot
from pyecharts.render import make_snapshot

from pyecharts.charts import Bar

from pyecharts import options as opts

#from ping3 import ping

from PIL import Image

import psutil



def gauge_base() -> Gauge:

    #Line1 = psutil.swap_memory()           
    Line2 = psutil.cpu_times_percent()
    #Line3= psutil.disk_usage('/')

    CPU_text = Line2.user
    #RAM_text = Line1.percent
    #HDD_text = Line3.percent

    
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
        .add("", [("",CPU_text )], max_=100,  detail_label_opts = opts.GaugeDetailOpts( offset_center = [0, "-40%"]), radius="50%", title_label_opts=opts.LabelOpts(font_size=20, color="white", font_family="Microsoft YaHei"), axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color=[(0.3, "#67e0e3"), (0.7, "#37a2da"), (1, "#fd666d")], width=10)))
        #.add("", [("",RAM_text )], max_=100,  detail_label_opts = opts.GaugeDetailOpts( offset_center = [0, "-40%"]), radius="50%", title_label_opts=opts.LabelOpts(font_size=20, color="white", font_family="Microsoft YaHei"), axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color=[(0.3, "#67e0e3"), (0.7, "#37a2da"), (1, "#fd666d")], width=10)))
        
        
        .set_global_opts(title_opts=opts.TitleOpts(title=""))
    )
    make_snapshot(snapshot, c.render(), "./cache_pic/CPU.png")

    img = Image.open('./cache_pic/CPU.png')
    area = (600, 200, 1200, 700)#width在前，height在后
    cropped_img = img.crop(area)
    #cropped_img.show()
    cropped_img.save('./cache_pic/CPU.png')
    #print(CPU)



#if __name__ == "__main__":
#delay = str(delay + 'ms')
gauge_base()
