##############################
# import
##############################
import wx
import requests

import GUI_Update

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Update.Main):
    def __init__(self, parent):
        # 定义主函数
        GUI_Update.Main.__init__(self, parent)

        self.local_version.SetLabel(local_version)

        url = 'http://tinywebdb.appinventor.space/api'
        data = '{"zk20210":"d0405e87"}'
        #data = {"zk20210":"d0405e87"}
        #res = requests.post(url=url,data=data)
        #print(res)

        
##############################
# 主函数
##############################


def main(version):
    global local_version
    local_version = version
    version = None
    
    app = wx.App(False)
    frame = CalcFrame(None)
    frame.Show(True)
    app.MainLoop()


if __name__ == "__main__":
    version = 'undefined'
    main(version)
