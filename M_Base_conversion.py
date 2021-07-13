
##############################
#import
##############################
import wx

import GUI_Base_conversion

import win32api,win32con

##############################
#GUI的函数桥接
##############################


class CalcFrame(GUI_Base_conversion.Main):
        
        def __init__(self,parent):
                        #定义主函数
                GUI_Base_conversion.Main.__init__(self,parent)

        def run(self, event):
            self.M_2.SetValue(str(bin(int(self.M_10.GetValue()))))
            self.M_8.SetValue(str(oct(int(self.M_10.GetValue()))))
            self.M_16.SetValue(str(hex(int(self.M_10.GetValue()))))
                
##############################
#主函数
##############################                

def main():
        app = wx.App(False)
        frame = CalcFrame(None)
        frame.Show(True)
        app.MainLoop()

if __name__ == '__main__':
        main()
