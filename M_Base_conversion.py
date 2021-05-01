
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
                global state
                state = 0

        def calculation( self, event ):
                print('初始化')
                
                if state == 1:
                        print('以1号位开始计算')
                        num = str(self.F2.GetValue())

                        self.F8.SetValue(oct(int(num,2)))
                        
                        self.F10.SetValue(str(int(num,2)))
                        self.F16.SetValue(hex(int(num, 2)))

                elif state == 2:
                        print('以2号位开始计算')
                        num = str(self.F8.GetValue())
                        self.F2.SetValue(bin(int(num, 8)))
                        
                        
                        self.F10.SetValue(str(int(num,8)))

                        self.F16.SetValue(hex(int(num,8)))

                        

                        
                elif state == 3:
                        print('以3号位开始计算')
                        num = int(self.F10.GetValue())
                        
                        self.F2.SetValue(bin(num))
                        self.F16.SetValue(hex(num))

                        self.F8.SetValue(oct(int(num)))
                        
                elif state == 4:
                        print('以4号位开始计算')
                        num = self.F16.GetValue()
                        self.F2.SetValue(bin(int(num, 16)))


                        self.F8.SetValue(oct(int(num,16)))
                        
                        num = str(self.F16.GetValue())
                        self.F10.SetValue(str(int(num, 16)))
                        
                else:
                        print('没有数据!')
                        win32api.MessageBox(0,'输入框不能为空!','请注意',win32con.MB_ICONWARNING)
        
        def F2S( self, event ):
                global state
                state = 1 
        def F8S( self, event ):
                global state
                state = 2
        def F10S( self, event ):
                global state
                state = 3
        def F16S( self, event ):
                global state
                state = 4

        def Clean( self, event ):
                self.F2.SetValue('')
                self.F8.SetValue('')
                self.F10.SetValue('')
                self.F16.SetValue('')

                global state
                state = 0
                
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
