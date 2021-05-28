def checkDir(download_path):
    # 判断路径是否存在
    mkdirlambda = lambda x: os.makedirs(x) if not os.path.exists(x) else True
    mkdirlambda(download_path)


def net():
    if network == 200:
        error = 1
    else:
        error = 2

    print(error)
    print(network)


def crawlWallpaper(download_path="cache_pic"):
    ##############################防止其他程序调用时跳过import环节
    import requests
    import os
    import datetime
    from UTC import start_utc, final_utc, utc_FY2, utc2_FY2

    import Edit

    import DRAW
    import DRAW_HDD
    import DRAW_RAM
    import DRAW_CPU

    import More_weater
    import temperature

    global error
    ##############################
    checkDir(download_path)
    picture_url_1 = "http://img.nsmc.org.cn/CLOUDIMAGE/FY4A/MTCC/FY4A_DISK.JPG"
    res = requests.get(picture_url_1, timeout=3600)
    global network
    network = res.status_code
    net()
    with open("./cache_pic/cache_wallpaper.jpg", "wb") as f:
        f.write(res.content)

    # print(final_utc)
    # print(start_utc)

    picture_url_2 = (
        "http://img.nsmc.org.cn/PORTAL/FY4/IMG/FY4A/AGRI/IMG/DISK/COL/NOM/C011/FY4A-_AGRI--_N_DISK_1047E_L1C_COL-_C011_NOM_"
        + str(start_utc)
        + "_"
        + str(final_utc)
        + "_4000M_V0001.JPG"
    )
    res = requests.get(picture_url_2, timeout=3600)
    network = res.status_code
    net()
    with open("./cache_pic/T11-8.50μm.jpg", "wb") as f:
        f.write(res.content)

    picture_url_3 = (
        "http://img.nsmc.org.cn/CLOUDIMAGE/FY2G/lan/FY2G_LAN_IR3_GRA_"
        + str(utc2_FY2)
        + "_"
        + str(utc_FY2)
        + ".jpg"
    )
    res = requests.get(picture_url_3, timeout=3600)
    network = res.status_code
    net()
    with open("./cache_pic/FY2_cloud.jpg", "wb") as f:
        f.write(res.content)

    picture_url_4 = (
        "http://img.nsmc.org.cn/CLOUDIMAGE/FY2G/lan/FY2G_LAN_IR1_COL_"
        + str(utc2_FY2)
        + "_"
        + str(utc_FY2)
        + ".jpg"
    )
    res = requests.get(picture_url_4, timeout=3600)
    network = res.status_code
    net()
    with open("./cache_pic/FY2_infrared.jpg", "wb") as f:
        f.write(res.content)

    picture_url_5 = (
        "http://img.nsmc.org.cn/PORTAL/FY4/IMG/FY4A/AGRI/IMG/REGI/GRA/GLL/C014/FY4A-_AGRI--_N_REGI_1047E_L1C_GRA-_C014_GLL_"
        + str(start_utc)
        + "_"
        + str(final_utc)
        + "_4000M_V0001.JPG"
    )
    res = requests.get(picture_url_5, timeout=3600)
    network = res.status_code
    net()
    with open("./cache_pic/T14-13.5μm.jpg", "wb") as f:
        f.write(res.content)

    utc_today = datetime.datetime.utcnow() - datetime.timedelta(
        minutes=30
    )  # 获取GMT时间并减去30分钟
    delat_utc_today = utc_today.strftime("%Y/%m/%d/%H%M")
    delat_utc_today_list = list(delat_utc_today)
    delat_utc_today_list[-1] = "0"
    delat_utc_today = "".join(delat_utc_today_list)

    img_url = (
        "https://himawari8-dl.nict.go.jp/himawari8/img/D531106/thumbnail/550/"
        + delat_utc_today
        + "00_0_0.png"
    )
    name = delat_utc_today.replace("/", "_") + "00_0_0.png"  # 获取图片名字

    picture_url_6 = img_url
    res = requests.get(picture_url_6, timeout=3600)
    network = res.status_code
    net()
    with open("./cache_pic/Himawari-8.png", "wb") as f:
        f.write(res.content)

    # DRAW.gauge_base()
    # DRAW_HDD.gauge_base()
    # DRAW_RAM.gauge_base()
    # DRAW_CPU.gauge_base()
    # temperature()

    Edit.changePic()


if __name__ == "__main__":
    crawlWallpaper()
    net()
