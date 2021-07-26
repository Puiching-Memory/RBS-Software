##############################
# import
##############################
from re import S
import wx
import configparser
import os

import GUI_Plug_in

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Plug_in.Main):
    def __init__(self, parent):
        # 定义主函数
        GUI_Plug_in.Main.__init__(self, parent)

        plug_in_list = []
        plug_in_list.append(os.listdir('./plug-in'))
        plug_in_list = plug_in_list[0]
        print(plug_in_list)

        for i in range(0, len(plug_in_list)):
            sigle_str = str(plug_in_list[i])
            if sigle_str.find('.') != -1:
                print('不合规范的文件:' + str(plug_in_list[i]))
                del plug_in_list[i]

        for i in range(0, len(plug_in_list)):
            self.List.Append(plug_in_list[i])


    def Close(self, event):
        self.Destroy()

    def Setup(self, event):
        try:
            path = self.List.GetString(int(self.List.GetSelection()))
            path = './plug-in/' + path + '/Info.cfg' 
            print(path)
            cfg = configparser.ConfigParser()
            cfg.read(path)

            name = cfg.get('main', 'name')
            self.T_Name.SetLabel('插件:' + name)

            author = cfg.get('main', 'author')
            self.T_Author.SetLabel('作者:'+ author)

            PVersion = cfg.get('main', 'PVersion')
            self.T_PVersion.SetLabel('插件版本:' + PVersion)

            SVersion = cfg.get('main', 'SVersion')
            self.T_SVersion.SetLabel('适用版本:' + SVersion + '+')

            Info = cfg.get('main', 'Info')
            self.Info.SetValue(Info)

            self.T_State.SetLabel('状态:' + '可用')
        except:
            self.T_Name.SetLabel('插件:' + 'N/A')
            self.T_Author.SetLabel('作者:'+ 'N/A')
            self.T_PVersion.SetLabel('插件版本:' + 'N/A')
            self.T_SVersion.SetLabel('适用版本:' + 'N/A' + '+')
            self.Info.SetValue('N/A')
            self.T_State.SetLabel('状态:' + '未知错误')
        
        
        
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
