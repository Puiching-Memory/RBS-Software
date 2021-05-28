##############################
# import
##############################
import wx
import random

import GUI_Roll

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Roll.Main):
    def __init__(self, parent):
        # 定义主函数
        GUI_Roll.Main.__init__(self, parent)

    def Run(self, event):
        num = random.randint(1, 48)
        self.Main_text.SetLabel(str(num))


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
