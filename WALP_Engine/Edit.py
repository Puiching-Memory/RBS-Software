from PIL import Image, ImageFont, ImageDraw
import os
import cv2
from UTC import utc_now, utc_FY2, utc, utc2_FY2, start_utc, final_utc
#from Main_start import delay

from API import now_weater, wind_dire1, wind_dire2, wind_dire3, date1, date2, date3

import Setup

import random
from random import choice#随机数

def redraw_upper_left(path, earth_w, earth_h):
    image1 = Image.new("RGB", (int(230 * earth_w / 1080), int(80 * earth_h / 1080)))

    image2 = Image.open(path)
    image2 = image2.resize((earth_w, earth_h), )

    image2.paste(image1, (0, 0))

    newpath = os.path.dirname(path) + '/upper_left' + os.path.splitext(path)[1]
    image2.save(newpath, "JPEG")
    return newpath

def redraw_bottom_right(path, earth_w, earth_h):
    image1 = Image.new("RGB", (int(80 * earth_w / 1080), int(80 * earth_h / 1080)))

    image2 = Image.open(path)
    image2 = image2.resize((earth_w,earth_h), )

    bw, bh = image1.size
    lw, lh = image2.size

    image2.paste(image1, (lw - bw, lh - bh))

    newpath = os.path.dirname(path) + '/bottom_right' + os.path.splitext(path)[1]
    image2.save(newpath, "JPEG")
    return newpath

def redraw_left_right(path, screen_w, screen_h, earth):
    image1 = Image.new("RGB", (screen_w, screen_h))

    image2 = Image.open(path)
    image2 = image2.resize((earth, earth), )

    bw, bh = image1.size
    lw, lh = image2.size
    image1.paste(image2, (int((bw - lw) / 2), int((bh - lh) / 2)))

    newpath = os.path.dirname(path) + '/Bulid-Ver0' + os.path.splitext(path)[1]
    image1.save(newpath, "PNG")
    return newpath


def Add(path, sizeH, sizeW, earth, Y, X, num):

    im1 = Image.open('./cache_pic/Bulid-Ver' + str(num) + '.jpg')    
    im2 = Image.open(path)
    im2 = im2.resize((sizeH,sizeW))#,Image.ANTIALIAS)

    bw, bh = im1.size
    lw, lh = im2.size
    im1.paste(im2, (1620 - X * num,750 - Y * num))
 
############################

    font = ImageFont.truetype("Astrolab.ttf",13)
    
    draw = ImageDraw.Draw(im1)
    strs = 'FY2_cloud Grayscale'
    draw.text((1630,730),strs,(255,255,255),font=font)
    strs = 'FY2_infrared RGB256'
    draw.text((1630,380),strs,(255,255,255),font=font)
    strs = 'T11-8.50 FY4'
    draw.text((1720,30),strs,(255,255,255),font=font)


    strs = 'Time:' + str(utc_now)
    draw.text((10,10),strs,(255,255,255),font=font)
    strs = '(utc):' + str(utc)
    draw.text((10,30),strs,(255,255,255),font=font)
    strs = 'FY2-Time:' + str(utc2_FY2) + str(utc_FY2)
    draw.text((10,50),strs,(255,255,255),font=font)
    strs = 'Main:' + str(start_utc) + '~' + str(final_utc)
    draw.text((10,70),strs,(255,255,255),font=font)

    font = ImageFont.truetype("FZHTJW.TTF",55)
    strs = now_weater
    draw.text((10,100),strs,(255,255,255),font=font)

    font = ImageFont.truetype("FZHTJW.TTF",25)
    strs = str('过去三天的风向:' + wind_dire1 + '/' + wind_dire2 + '/' + wind_dire3)
    draw.text((10,200),strs,(255,255,255),font=font)

    font = ImageFont.truetype("FZHTJW.TTF",20)
    strs = str(date1 + '       ' + date2 + '       ' + date3)
    draw.text((10,280),strs,(255,255,255),font=font)

    
    num = num + 1

    im1.save('./cache_pic/Bulid-Ver' + str(num) + '.jpg')

def Add_text(num):
    im1 = Image.open('./cache_pic/Bulid-Ver' + str(num) + '.jpg')
    draw = ImageDraw.Draw(im1)
    font = ImageFont.truetype("FZHTJW.TTF",20)
    list1 = ['脚踏实地,仰望星空!','不负初心 不辱使命 不曾背信 万里之外的祖国母亲 可曾听见我的声音 情之所钟 为神州振兴 精忠报国 丹心照汗青','如果你有什么伤心事,请告诉我,让我开心一下','小心二次元!','在你看我这段话时,你的生命已经浪费了3秒钟', '道路千万条,安全第一条,行车不规范,全村老少来吃饭', '你给我听好了,今天也要好好地活着!','口罩滞销!帮帮我们!','1+1=3是宇宙的终极真理','据调查:大部分的家长群都是"相亲相爱一家人"或者"幸福一家人"','熬夜对身体不好,建议直接通宵','世界上没有什么力量比爱情更强大，除了雅克-9T机头NS-37机炮的37×198mm炮弹','你知道吗？樱花下落的速度是秒速五厘米。是发射AP-T穿甲曳光弹时炮口初速的一万七千六百分之一','紧靠在一起的两颗心，会在200米的距离内，被TBG-7V空爆燃烧弹烧成焦炭。','我们不能选择自己的花盆,但我们可以追逐自己的阳光','嘿咻!啊吧啊吧~~~','魂劳梦断,掠浮光,报国路漫漫.临夜长叹,把心藏,言语千万万.','历经残风败雪而今七十有余,纵然暮年壮心仍不已,霜鬓又添几缕,死生无所惧,老骥更当伏枥,浮生能几许？','我们的履带断啦!我们跑得更快啦!','从现在开始这里叫做卢本伟广场!','无论我们遇到什么困难,也不要怕,微笑着面对他!消除恐惧的最好办法就是面对恐惧!坚持,才是胜利!','吼♂吼♂吼♂吼♂','呐，欧尼酱也喜欢二次元吗 (*´ ꒳ `*)','114514','君は君の信じた明日を,歩いていけばいいよ','Союз нерушимый республик свободных!','Нас к торжеству коммунизма ведёт!','要想健康又长寿，抽烟喝酒吃肥肉。一问大爷您高寿，今年刚好二十六。']
    strs = str(random.choice(list1))
    print(strs)
    draw.text((630,970), str('Tips:' + strs),(255,255,255),font=font)
    num = num + 1

    im1.save('./cache_pic/Bulid-Ver' + str(num) + '.jpg')

def changePic():
    path = './cache_pic/cache_wallpaper.jpg'
    size = {'1' : 1, '2' : 0.75, '3' : 0.5}
    #w = int(input("设置壁纸分辨率宽为："))
    w = int(1920)
    h = int(1080)
    #h = int(input("设置壁纸分辨率高为："))
    #flag = input("设置地球大小为（1：大，2：中，3：小）：")
    #print(flag)
    min = h if h < w else w
    max = w + h - min
    earth = int(min * 0.8)
    new_path = redraw_upper_left(path, earth, earth)
    new_path = redraw_bottom_right(new_path, earth, earth)
    new_path = redraw_left_right(new_path, max, min, earth)
    Add('./cache_pic/FY2_cloud.jpg', 300, 300, earth, 0, 0, 0)#1.路径2.X大小3.Y大小4.earth5.X偏移值6.Y偏移值7.导入第次
    Add('./cache_pic/FY2_infrared.jpg', 300, 300, earth, 350, 0, 1)
    Add('./cache_pic/T14-13.5μm.jpg', 300, 300, earth, 350, 0, 2)
    Add('./cache_pic/Himawari-8.png', 250, 250, earth, 240, 105, 3)
    Add('./cache_pic/Ping.png',120, 100, earth, -40, 400, 4  )
    Add('./cache_pic/temperature.png', 500, 300, earth, 30 ,330 ,5)
    Add('./cache_pic/CPU.png',120, 100, earth, -27, 245, 6)
    Add('./cache_pic/RAM.png',120, 100, earth, -23, 190, 7)
    Add('./cache_pic/HDD.png',120, 100, earth, -20, 150, 8)
    Add('./cache_pic/More_weater.png',500, 333, earth, 50, 180, 9)
    Add_text(10)
    
    Setup.setWallPaper()
    return new_path

if __name__ == '__main__':
    changePic()
