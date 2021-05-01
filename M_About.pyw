##############################
# import
##############################
import wx

# import bce

import GUI_About

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_About.Main):
    def __init__(self, parent):
        # 定义主函数
        GUI_About.Main.__init__(self, parent)


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
