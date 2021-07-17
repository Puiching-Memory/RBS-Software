##############################
# import
##############################
import wx

import os

from wx.core import version
import GUI_Version

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Version.Main):
    def __init__(self, parent):
        # 定义主函数
        GUI_Version.Main.__init__(self, parent)
        ##global 
        for root, dirs, files in os.walk('./DATA/Version/'):  
            ##print(root) #当前目录路径  
            ##print(dirs) #当前路径下所有子目录  
            print(files) #当前路径下所有非目录子文件  
            self.Place.SetLabel('日志路径: ' + root)

        self.Version_L.SetSelection(-1)

        number = len(files)
        for i in range(0, number):
            file = files[i]
            file = file[0:9]
            ##print(file)
            self.Version_L.Append(file)

    def Start(self, event):
        self.Info.Enable(True)
        place = './DATA/Version/' + self.Version_L.GetString(self.Version_L.GetSelection()) + '.txt'
        info = open(place, 'r', encoding='utf-8')
        Version = str(info.readlines(1))[-15:-6]
        self.Version_T.SetLabel('版本: ' + Version)
        ##print(Version)
        info = open(place, 'r', encoding='utf-8')
        date = str(info.readlines(1))[-32:-22]
        self.Date.SetLabel('日期: ' + date)

        info = open(place, 'r', encoding='utf-8')
        self.Info.SetValue(info.read())

##############################
# 主函数
##############################


def main():
    app = wx.App(False)
    frame = CalcFrame(None)
    frame.Show(True)
    app.MainLoop()


if __name__ == "__main__":
    main()
