# import Download
# import Edit
# import Setup

import threading
import win32api
from ping3 import ping


def hello(name):
    ip_address = "www.baidu.com"
    response = ping(ip_address)
    print(response)
    print("Restart")

    if response == False:
        print("取消任务-无网络")
    else:
        win32api.ShellExecute(0, "open", "Wallpaper-Engine.exe", "", "", 1)
        # Main_start.Start()
        # Start()
        # Download.crawlWallpaper()
        # Edit.changePic()
        # Setup.setWallPaper()

        delay = int(response * 1000)
        print(delay, "延迟")
    global timer
    timer = threading.Timer(600.0, hello, ["Hawk"])
    timer.start()


if __name__ == "__main__":
    timer = threading.Timer(60.0, hello, ["Hawk"])  ##每隔两秒调用函数hello
    timer.start()
