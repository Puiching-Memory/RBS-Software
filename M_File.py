##############################
# import
##############################
import wx

import GUI_File
import configparser

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_File.Main):
    def __init__(self, parent):
        # 定义主函数
        GUI_File.Main.__init__(self, parent)

        cfg = configparser.ConfigParser()
        cfg.read('./cfg/File.cfg')
        File_Tpye = cfg.get('File', 'type')
        print(File_Tpye)

        self.File_Type.SetLabel('文件类型:' + File_Tpye)

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
