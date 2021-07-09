import tkinter
from tkinter import Button
from tkinter import Label
from tkinter import Entry
from tkinter import Scale
from tkinter import Label, PhotoImage
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import Toplevel
from pymediainfo import MediaInfo
import re
from tkinter import Message
import threading
import pygame
import time
import os
import sys
import random
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
from tkinter import StringVar
import requests
import json

top = tkinter.Tk()
top.geometry("800x400")
top.title("嘟嘟的音乐播放器")
top.state("zoomed")


def printsrceen(texts):
    t = int(texts)
    top.attributes("-alpha", t / 100)


screenwidth = top.winfo_screenwidth()
screenheight = top.winfo_screenheight() - 100

pygame.init()
path = StringVar()
paths = StringVar()
patht = StringVar()
v = StringVar()
v1 = StringVar()


def callback():  # 搜索本地文件
    path_ = askopenfilename()
    return path_


def selectPath():  # 随机播放
    folder_path = "D:/音乐"
    folder_list = os.listdir(folder_path)  # 遍历文件夹里面每个文件
    list = []
    count = 0
    for i in folder_list:  # 将文件夹里的文件按顺序传提给变量i  此处区别os.walk()
        if os.path.splitext(i)[1] == '.flac':  # 提取特定后缀文件'.***'
            list.append(i)
            # print(type(list))
            count = count + 1
    # print(count)

    s = random.randint(0, (count - 1))  # 获取随机数
    file = list[s]
    fil = folder_path + "\\" + file

    pygame.mixer.music.load(fil)
    pygame.mixer.music.play(1, 0)
    media_info = MediaInfo.parse(fil)
    data = media_info.to_json()  # medio到json()这两行是获取文件的所有属性
    rst = re.search('other_duration.*?(.*?)min(.*?)s.*?', data)
    t = int(rst.group(0)[19:20])
    r = int(rst.group(0)[-4:-2])
    m = (t * 60 + r) * 1000

    musictime = str(t) + ':' + str(r)
    l2.config(text=file)
    l3.config(text=musictime)
    lbTime = tkinter.Label(top, anchor='w')
    lbTime.place(x=25, y=150)

    def autoclose():
        for i in range(m // 1000):
            lbTime['text'] = '-{} /'.format((m // 1000) - i)
            time.sleep(1)

    t = threading.Thread(target=autoclose)
    t.start()
    loopl = top.after(m, selectPath)


def printScale(text):
    t = int(text)
    pygame.mixer.music.set_volume(t / 100)


def update_timeText():
    # Get the current time, note you can change the format as you wish
    current = time.strftime("%H:%M:%S")  # 获取当前时间

    # Update the timeText Label box with the current time
    timeText.configure(text=current)

    # Call the update_timeText() function after 1 second
    top.after(1000, update_timeText)


def remind():
    top = Toplevel()  # 新建一个tkinter窗口
    top.title('使用提示')
    top.geometry("200x200")
    t = "半分钟后开始播放音乐"
    msg = Message(top, text=t)
    msg.config(font=('times', 18, 'italic'))
    msg.place(x=0, y=0)
    lbTime = tkinter.Label(top, fg="red", anchor='w')
    lbTime.place(x=100, y=45)

    def autoclose():
        for i in range(30):
            lbTime['text'] = '距离窗口关闭还有{}秒'.format(30 - i)
            time.sleep(1)
        top.destroy()

    t = threading.Thread(target=autoclose)
    t.start()
    loopl = top.after(60 * 59500, remind)


def reminds():
    top = Toplevel()
    top.title('使用提示')
    top.geometry("200x200")
    t = "宝贝可以休息一会啦"
    msg = Message(top, text=t)
    msg.config(font=('times', 24, 'italic'))
    msg.place(x=0, y=0)
    folder_path = "D:/音乐"
    folder_list = os.listdir(folder_path)  # 遍历文件夹里面每个文件
    list = []
    count = 0
    for i in folder_list:  # 将文件夹里的文件按顺序传提给变量i  此处区别os.walk()
        if os.path.splitext(i)[1] == '.flac':  # 提取特定后缀文件'.***'
            list.append(i)
            # print(type(list))
            count = count + 1
        # print(count)
    s = random.randint(0, (count - 1))
    file = list[s]
    fil = folder_path + "\\" + file
    pygame.mixer.music.load(fil)
    pygame.mixer.music.play(1, 0)
    lbTime = tkinter.Label(top, fg="red", anchor='w')
    lbTime.place(x=100, y=45)

    def autoclose():
        for i in range(300):
            lbTime['text'] = '距离窗口关闭还有{}秒'.format(300 - i)
            time.sleep(1)
        top.destroy()

    t = threading.Thread(target=autoclose)
    t.start()
    loopl = top.after(60 * 60000, reminds)


def play():  # 播放音乐
    # 拖动音乐文件到程序图标，然后播放音乐
    if len(sys.argv) >= 2:  # 判断是否通过拖动音频文件打开程序
        f = sys.argv[1]  # 如果是，则播放拖动的文件
    else:
        f = callback()  # 若不是，则选择制定文件
    pygame.mixer.music.load(f)
    pygame.mixer.music.play()
    path.set(f)
    media_info = MediaInfo.parse(f)
    data = media_info.to_json()  # medio到json()这两行是获取文件的所有属性
    rst = re.search('other_duration.*?(.*?)min(.*?)s.*?', data)
    t = int(rst.group(0)[19:20])
    r = int(rst.group(0)[-4:-2])
    m = (t * 60 + r) * 1000
    musictime = str(t) + ':' + str(r)
    l2.config(text=f)
    l3.config(text=musictime)
    lbTime = tkinter.Label(top, anchor='w')
    lbTime.place(x=25, y=150)

    def autoclose():
        for i in range(m // 1000):
            lbTime['text'] = '-{} /'.format((m // 1000) - i)
            time.sleep(1)

    t = threading.Thread(target=autoclose)
    t.start()
    loopl = top.after(m, selectPath)


def stop():
    pygame.mixer.music.stop()  # 停止播放
    top.after_cancel(loopl)


def pause():
    pygame.mixer.music.pause()  # 暂停


def unpause():
    pygame.mixer.music.unpause()  # 继续播放


def refleshpic():  # 保存的路径不能有中文，若需要中文则吧/换成\
    global pic_copyright
    bing_api_res = requests.get("https://api.no0a.cn/api/bing/0")
    bing_api_dic = bing_api_res.json()
    print(bing_api_dic)
    pic_url = bing_api_dic['bing']['url']
    pic_copyright = bing_api_dic['bing']['copyright']
    pic_res = requests.get(pic_url)
    pic=pic_res.content
    f = open("./bing_img_cache.png", 'wb')
    f.write(pic)
    f.close()
    path_s = "./bing_img_cache.png"
    paths.set(path_s)
    img_open = Image.open(e1.get())
    img = ImageTk.PhotoImage(img_open)
    l1.config(image=img)
    l1.image = img


def create():
    top = Toplevel()
    top.title('使用提示')
    top.geometry("400x400")
    t = "关于照片，新建一个存放图片的文件，用英文命名，然后存里面的图片也用英文命名。关于音乐: 新建一个名字叫音乐的文件，把歌曲添加到该文件夹。"
    msg = Message(top, text=t)
    msg.config(font=('times', 24, 'italic'))
    msg.place(x=0, y=0)


def copyright():
    top = Toplevel()
    top.title('版权信息')
    top.geometry("500x400")
    t = """软件原作者为 嘟嘟还没长大
由 人工智障 完善
图片来自 必应：每日一图
本图版权信息 %s"""%(pic_copyright)
    msg = Message(top, text=t)
    msg.config(font=('times', 24, 'italic'))
    msg.place(x=0, y=0)


def loop():
    top.after(60 * 60000, reminds)
    top.after(60 * 59500, remind)


def loops():
    selectPath()


def gettime():
    t = time.strftime('%H%M%S')
    s = int(t[0:2])
    d = int(t[2:4])
    f = int(t[4:6])
    g = s * 60 * 60 + d * 60 + f
    return g


errmsg = 'Error!'
# 时间
timeText = Label(top, text="", font=("Helvetica", 15))
timeText.place(x=180, y=370)
update_timeText()
# 选择文件
Button(top, text="选择文件/播放", command=play, width=10, bg="sky blue").place(x=20, y=20)
Entry(top, text=path, width=25, state='readonly').place(x=120, y=20)

# 选择图片
Button(top, text='刷新图片', command=refleshpic, width=10, bg="sky blue").place(x=20, y=55)
e1 = Entry(top, text=paths, state='readonly', width=25)
e1.place(x=120, y=55)
l1 = Label(top)  # 图片放置位置
l1.place(x=320, y=0)

# 随机播放
Button(top, text="随机播放", command=selectPath, width=7, bg="sky blue").place(x=20, y=225)
l2 = Label(top, text='', width=25, font=("Helvetica", 16))  # 音乐名
l2.place(x=0, y=100)
Button(top, text="下一首", command=loops, width=5, bg="sky blue").place(x=100, y=225)
l3 = Label(top, text='', width=15)  # 音乐时长
l3.place(x=24, y=150)
# 暂停，继续播放，结束播放
Button(top, text="暂停", command=pause, width=7, bg="sky blue").place(x=170, y=245)
Button(top, text="继续播放", command=unpause, width=7, bg="sky blue").place(x=170, y=205)
Button(top, text="结束播放", command=stop, width=7, bg="sky blue").place(x=240, y=225)

# 提醒功能
Button(top, text='提醒功能', command=loop, width=10, bg="sky blue").place(x=20, y=325)
# 使用说明
Button(top, text="使用说明", command=create, width=10, bg="sky blue").place(x=20, y=370)
#版权信息
Button(top, text="版权信息", command=copyright, width=10, bg="sky blue").place(x=20, y=415)
# 音量
w1 = Scale(top, from_=0, to=100, orient="horizontal", length=75, variable=v, command=printScale, label="音量")
w1.place(x=240, y=145)

w2 = Scale(top, from_=30, to=100, orient="horizontal", length=100, variable=v1, command=printsrceen, label="透明度")
w2.place(x=150, y=290)

if len(sys.argv) >= 2:  # 初步判断是否通过拖动音频文件打开程序
    play()  # 如果是，则直接运行play()函数

refleshpic()

top.mainloop()

