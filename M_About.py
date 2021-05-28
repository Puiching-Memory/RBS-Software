##############################
# import
##############################
import wx
import configparser

import GUI_About

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_About.Main):
    def __init__(self, parent):
        # 定义主函数
        GUI_About.Main.__init__(self, parent)

        # 读取cfg配置文件
        cfg = configparser.ConfigParser()
        cfg.read('./cfg/main.cfg')

        version = cfg.get('main', 'VERSION')

        self.version.SetLabel('CC2021 #' + version)


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
